"""CLI commands for DevKit."""

import sys
from pathlib import Path
from typing import Optional
import typer
from devkit_cli import __version__
from devkit_cli.config import AGENT_CONFIG
from devkit_cli.core import TemplateManager
from devkit_cli.ui import select_agent, show_result, show_version, show_error, show_main_menu, prompt_project_path, show_banner, console
from devkit_cli.config import UI_THEME
from rich.panel import Panel
from devkit_cli.utils import get_project_path, ensure_directory, ProjectPathError
from devkit_cli.agent_utils import get_agent_by_flag


app = typer.Typer(
    name="devkit",
    help="Lightweight CLI tool to bootstrap AI coding agent templates",
    add_completion=False,
)


@app.callback(invoke_without_command=True)
def main_callback(ctx: typer.Context) -> None:
    """
    Main callback - shows interactive menu when no command is specified.

    Args:
        ctx: Typer context
    """
    if ctx.invoked_subcommand is None:
        while True:
            action = show_main_menu()

            if action == "init":
                init(project_name=None, here=False, claude=False, cursor=False)
            elif action == "version":
                show_version(__version__)
                console.input(f"\n[{UI_THEME['text_hint']}]Press Enter to continue...[/{UI_THEME['text_hint']}]")
                # Loop continues to show main menu again
            elif action == "exit":
                console.print(f"[{UI_THEME['text_hint']}]Goodbye![/{UI_THEME['text_hint']}]\n")
                sys.exit(0)
            elif action is None:
                # User cancelled
                sys.exit(0)


@app.command()
def init(
    project_name: Optional[str] = typer.Argument(
        None,
        help="Name of the project directory to initialize (or use --here)"
    ),
    here: bool = typer.Option(
        False,
        "--here",
        help="Initialize templates in the current directory"
    ),
    claude: bool = typer.Option(
        False,
        "--claude",
        help="Use Claude Code agent (skip interactive selection)"
    ),
    cursor: bool = typer.Option(
        False,
        "--cursor",
        help="Use Cursor agent (skip interactive selection)"
    ),
) -> None:
    """
    Initialize a project with AI coding agent templates.

    Examples:
        devkit init my-project --claude    # Direct execution, no prompts
        devkit init --here --claude        # Install in current dir
        devkit init my-project             # Prompt for agent selection
        devkit init --claude               # Prompt for project path
        devkit init                        # Prompt for both
    """
    # Show banner at command start
    show_banner()

    try:
        # Step 1: Resolve agent from flags (or prompt if missing)
        agent, error = get_agent_by_flag(claude, cursor)

        if error:
            # Conflicting flags or unsupported agent
            show_error(error)
            sys.exit(1)

        if agent is None:
            # No flags provided - prompt user
            agents = list(AGENT_CONFIG.values())
            agent = select_agent(agents)

            if not agent:
                console.print(f"[{UI_THEME['warning']}]No agent selected. Exiting.[/{UI_THEME['warning']}]")
                sys.exit(0)

        # Step 2: Resolve project path (prompt if missing)
        try:
            project_path = get_project_path(project_name, here)
        except ProjectPathError:
            # Path info missing - prompt user
            path_input = prompt_project_path()
            # Re-parse with the user input
            if path_input == ".":
                project_path = Path.cwd()
            else:
                project_path = Path(path_input).resolve()

        # Create project directory if it doesn't exist
        if not project_path.exists():
            ensure_directory(project_path)
            console.print(f"[{UI_THEME['text_hint']}]Created directory: {project_path}[/{UI_THEME['text_hint']}]\n")

        # Step 3: Install templates
        template_manager = TemplateManager(agent)
        result = template_manager.install_templates(project_path)

        # Step 4: Show result
        show_result(result)

        # Step 5: Show next steps
        if result.success:
            next_steps_text = (
                f"[{UI_THEME['text_secondary']}]1. Navigate to your project:[/{UI_THEME['text_secondary']}] [{UI_THEME['primary']}]cd {project_path.name if not here else '.'}[/{UI_THEME['primary']}]\n"
                f"[{UI_THEME['text_secondary']}]2. Use the installed templates in your coding agent[/{UI_THEME['text_secondary']}]"
            )
            next_steps_panel = Panel(
                next_steps_text,
                title=f"[bold {UI_THEME['text_primary']}]Next Steps[/bold {UI_THEME['text_primary']}]",
                border_style=UI_THEME["border"],
                padding=(1, 2)
            )
            console.print(next_steps_panel)

    except ProjectPathError as e:
        show_error(str(e))
        sys.exit(1)
    except KeyboardInterrupt:
        console.print(f"\n[{UI_THEME['warning']}]Operation cancelled by user.[/{UI_THEME['warning']}]")
        sys.exit(0)
    except Exception as e:
        show_error(str(e), prefix="Unexpected error")
        sys.exit(1)


@app.command()
def version() -> None:
    """Show version information."""
    show_version(__version__)


def main() -> None:
    """Main entry point for CLI."""
    app()


if __name__ == "__main__":
    main()
