"""Core template management logic for DevKit CLI."""

import json
from pathlib import Path
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from devkit_cli.config import TEMPLATES_DIR, TEMPLATE_SUBDIRS, UI_THEME
from devkit_cli.models import Agent, InstallResult
from devkit_cli.utils import (
    ensure_directory,
    copy_file,
    create_backup,
    TemplateNotFoundError,
)


class TemplateManager:
    """Manages template operations for DevKit CLI."""

    def __init__(self, agent: Agent):
        """
        Initialize template manager.

        Args:
            agent: Agent configuration to use
        """
        self.agent = agent
        self.template_path = TEMPLATES_DIR / agent.name

    def get_template_files(self) -> list[Path]:
        """
        Get list of all template files for the agent.

        Returns:
            List of template file paths relative to template root

        Raises:
            TemplateNotFoundError: If template directory doesn't exist
        """
        if not self.template_path.exists():
            raise TemplateNotFoundError(
                f"Template directory not found: {self.template_path}"
            )

        template_files = []
        for subdir in TEMPLATE_SUBDIRS:
            subdir_path = self.template_path / subdir
            if subdir_path.exists():
                for file_path in subdir_path.rglob("*"):
                    if file_path.is_file():
                        # Store path relative to template root
                        rel_path = file_path.relative_to(self.template_path)
                        template_files.append(rel_path)

        return template_files

    def detect_conflicts(self, project_path: Path) -> list[Path]:
        """
        Detect files that would be overwritten.

        Args:
            project_path: Target project directory

        Returns:
            List of files that already exist in project
        """
        agent_folder = project_path / self.agent.folder
        if not agent_folder.exists():
            return []

        conflicts = []
        template_files = self.get_template_files()

        for rel_path in template_files:
            dest_file = agent_folder / rel_path
            if dest_file.exists():
                conflicts.append(rel_path)

        return conflicts

    def install_templates(self, project_path: Path) -> InstallResult:
        """
        Install templates to project directory.

        Automatically creates backup if conflicts are detected.

        Args:
            project_path: Target project directory

        Returns:
            InstallResult with details of the operation
        """
        agent_folder = project_path / self.agent.folder
        template_files = self.get_template_files()

        # Check if template directory is empty
        if not template_files:
            return InstallResult(
                success=False,
                project_path=project_path,
                agent=self.agent,
                files_copied=[],
                backup_path=None,
                conflicts=[],
                message=f"No template files found for {self.agent.display_name}"
            )

        conflicts = self.detect_conflicts(project_path)
        backup_path = None

        # Create backup if conflicts exist
        if conflicts and agent_folder.exists():
            backup_path = create_backup(agent_folder)

        # Ensure agent folder exists
        ensure_directory(agent_folder)

        # Copy all template files with progress indicator
        files_copied = []

        with Progress(
            SpinnerColumn(style=UI_THEME["primary"]),
            TextColumn("[bold {color}]{{task.description}}[/bold {color}]".format(color=UI_THEME["primary"])),
            BarColumn(complete_style=UI_THEME["success"], finished_style=UI_THEME["success"]),
            TaskProgressColumn(),
            transient=True  # Remove progress bar when done
        ) as progress:
            task = progress.add_task("Installing templates", total=len(template_files))

            for rel_path in template_files:
                source_file = self.template_path / rel_path
                dest_file = agent_folder / rel_path
                copy_file(source_file, dest_file)
                files_copied.append(rel_path)
                progress.update(task, advance=1)

        # Configure hooks in settings.local.json
        self._configure_hooks(agent_folder)

        # Build result message
        message = self._build_result_message(
            project_path, files_copied, conflicts, backup_path
        )

        return InstallResult(
            success=True,
            project_path=project_path,
            agent=self.agent,
            files_copied=files_copied,
            backup_path=backup_path,
            conflicts=conflicts,
            message=message,
        )

    def _configure_hooks(self, agent_folder: Path) -> None:
        """
        Configure hooks in settings.local.json.
        
        Creates or merges hooks configuration into the settings file.
        
        Args:
            agent_folder: Path to the agent folder (e.g., .claude/)
        """
        settings_file = agent_folder / "settings.local.json"
        
        # Define the hooks configuration
        hooks_config = {
            "hooks": {
                "SessionStart": [
                    {
                        "hooks": [
                            {
                                "type": "command",
                                "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/welcome-banner.sh",
                                "timeout": 5
                            }
                        ]
                    }
                ]
            }
        }
        
        # Load existing settings if file exists
        if settings_file.exists():
            try:
                with open(settings_file, 'r', encoding='utf-8') as f:
                    existing_settings = json.load(f)
            except (json.JSONDecodeError, IOError):
                # If file is corrupted or empty, start fresh
                existing_settings = {}
        else:
            existing_settings = {}
        
        # Merge hooks configuration
        if "hooks" not in existing_settings:
            existing_settings["hooks"] = {}
        
        # Merge SessionStart hooks
        if "SessionStart" not in existing_settings["hooks"]:
            existing_settings["hooks"]["SessionStart"] = hooks_config["hooks"]["SessionStart"]
        else:
            # Append to existing SessionStart hooks if not already present
            existing_hooks = existing_settings["hooks"]["SessionStart"]
            new_hook = hooks_config["hooks"]["SessionStart"][0]
            
            # Check if this exact hook already exists
            hook_exists = any(
                h.get("hooks", [{}])[0].get("command") == new_hook["hooks"][0]["command"]
                for h in existing_hooks
                if isinstance(h, dict) and "hooks" in h
            )
            
            if not hook_exists:
                existing_hooks.append(new_hook)
        
        # Write back to file
        with open(settings_file, 'w', encoding='utf-8') as f:
            json.dump(existing_settings, f, indent=2, ensure_ascii=False)
            f.write('\n')  # Add trailing newline

    def _build_result_message(
        self,
        project_path: Path,
        files_copied: list[Path],
        conflicts: list[Path],
        backup_path: Path | None,
    ) -> str:
        """Build human-readable result message."""
        parts = []

        if conflicts:
            parts.append(
                f"Found {len(conflicts)} existing file(s) that would be overwritten."
            )
            if backup_path:
                parts.append(f"Created backup at: {backup_path.name}")

        parts.append(f"Copied {len(files_copied)} template file(s) to {self.agent.folder}/")

        return " ".join(parts)
