"""UI components for DevKit CLI."""

import sys
from typing import Sequence
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.tree import Tree
from devkit_cli.models import Agent, InstallResult
from devkit_cli.config import BANNER, UI_THEME

try:
    import readchar
    READCHAR_AVAILABLE = True
except ImportError:
    READCHAR_AVAILABLE = False


console = Console()


def show_banner() -> None:
    """Display the DevKit ASCII art banner with ice blue gradient."""
    # Clear both screen and scrollback buffer for completely clean display
    # ANSI escape sequences: \033[3J clears scrollback, \033[2J clears screen, \033[H moves cursor to home
    sys.stdout.write("\033[3J\033[2J\033[H")
    sys.stdout.flush()

    lines = BANNER.split('\n')
    gradient = UI_THEME["banner_gradient"]

    # Apply gradient: each line gets progressively darker shade
    for i, line in enumerate(lines):
        # Calculate which gradient color to use
        color_index = int((i / max(len(lines) - 1, 1)) * (len(gradient) - 1))
        color = gradient[color_index]
        console.print(line, style=color, highlight=False)

    console.print()


def show_error(message: str, prefix: str = "Error") -> None:
    """
    Display a styled error message.

    Args:
        message: Error message to display
        prefix: Prefix text (default: "Error")
    """
    error_text = Text()
    error_text.append(f"{prefix}: ", style=f"{UI_THEME['error']} bold")
    error_text.append(message)
    console.print(error_text)


def select_agent(agents: Sequence[Agent]) -> Agent | None:
    """
    Interactive agent selection with arrow keys.

    Args:
        agents: List of available agents

    Returns:
        Selected agent, or None if cancelled
    """
    if not READCHAR_AVAILABLE:
        # Fallback: simple numbered selection
        return _select_agent_fallback(agents)

    selected_idx = 0
    first_iteration = True

    while True:
        # Clear screen and show options
        if first_iteration:
            # On first iteration, clear scrollback buffer too
            sys.stdout.write("\033[3J\033[2J\033[H")
            sys.stdout.flush()
            first_iteration = False
        else:
            console.clear()

        console.print(f"\n[bold {UI_THEME['text_primary']}]Select a coding agent:[/bold {UI_THEME['text_primary']}]\n")

        for idx, agent in enumerate(agents):
            prefix = "❯" if idx == selected_idx else " "

            status = "" if agent.supported else f" [{UI_THEME['text_hint']}](not supported yet)[/{UI_THEME['text_hint']}]"

            if idx == selected_idx:
                console.print(f"  {prefix} [bold {UI_THEME['primary']}]{agent.display_name}[/bold {UI_THEME['primary']}]{status}")
            else:
                console.print(f"  {prefix} [{UI_THEME['text_secondary']}]{agent.display_name}[/{UI_THEME['text_secondary']}]{status}")

        console.print(f"\n[{UI_THEME['text_hint']}]Use ↑↓ arrows to navigate, Enter to select, ESC/Ctrl+C to cancel[/{UI_THEME['text_hint']}]")

        # Read key
        key = readchar.readkey()

        if key == readchar.key.UP:
            selected_idx = (selected_idx - 1) % len(agents)
        elif key == readchar.key.DOWN:
            selected_idx = (selected_idx + 1) % len(agents)
        elif key in (readchar.key.ENTER, readchar.key.CR, readchar.key.LF):
            selected_agent = agents[selected_idx]
            if not selected_agent.supported:
                console.print(f"\n[{UI_THEME['warning']}]⚠ {selected_agent.display_name} is not supported yet.[/{UI_THEME['warning']}]")
                console.print(f"[{UI_THEME['text_hint']}]Press any key to continue...[/{UI_THEME['text_hint']}]")
                readchar.readkey()
                continue
            return selected_agent
        elif key in (readchar.key.CTRL_C, readchar.key.ESC):
            console.print(f"\n[{UI_THEME['warning']}]Cancelled[/{UI_THEME['warning']}]")
            return None


def _select_agent_fallback(agents: Sequence[Agent]) -> Agent | None:
    """Fallback agent selection using numbers (when readchar unavailable)."""
    console.print(f"\n[bold {UI_THEME['text_primary']}]Select a coding agent:[/bold {UI_THEME['text_primary']}]\n")

    for idx, agent in enumerate(agents, 1):
        status = "" if agent.supported else f" [{UI_THEME['text_hint']}](not supported yet)[/{UI_THEME['text_hint']}]"
        console.print(f"  {idx}. [{UI_THEME['text_secondary']}]{agent.display_name}[/{UI_THEME['text_secondary']}]{status}")

    console.print()

    while True:
        try:
            choice = console.input(f"[bold {UI_THEME['primary']}]Enter number (or 'q' to quit):[/bold {UI_THEME['primary']}] ")
            if choice.lower() == 'q':
                return None

            idx = int(choice) - 1
            if 0 <= idx < len(agents):
                selected_agent = agents[idx]
                if not selected_agent.supported:
                    console.print(f"[{UI_THEME['warning']}]⚠ {selected_agent.display_name} is not supported yet.[/{UI_THEME['warning']}]\n")
                    continue
                return selected_agent
            else:
                console.print(f"[{UI_THEME['error']}]Invalid choice. Please try again.[/{UI_THEME['error']}]\n")
        except (ValueError, KeyError):
            console.print(f"[{UI_THEME['error']}]Invalid input. Please enter a number.[/{UI_THEME['error']}]\n")
        except KeyboardInterrupt:
            console.print(f"\n[{UI_THEME['warning']}]Cancelled[/{UI_THEME['warning']}]")
            return None


def show_result(result: InstallResult) -> None:
    """
    Display installation result to user.

    Args:
        result: Installation result to display
    """
    console.print()

    if not result.success:
        error_panel = Panel(
            f"[{UI_THEME['error']}]{result.message}[/{UI_THEME['error']}]",
            title=f"[{UI_THEME['error']}]✗ Installation Failed[/{UI_THEME['error']}]",
            border_style=UI_THEME["error"],
            padding=(1, 2)
        )
        console.print(error_panel)
        console.print()
        return

    # Build details content
    details_lines = []

    if result.conflicts:
        details_lines.append(f"[{UI_THEME['warning']}]Found {len(result.conflicts)} existing file(s)[/{UI_THEME['warning']}]")

    if result.backup_path:
        details_lines.append(f"[{UI_THEME['info']}]Created backup: {result.backup_path.name}[/{UI_THEME['info']}]")

    details_lines.append(f"[{UI_THEME['success']}]Copied {len(result.files_copied)} file(s) to {result.agent.folder}/[/{UI_THEME['success']}]")

    # Create success panel with details
    details_text = "\n".join(details_lines)
    success_panel = Panel(
        details_text,
        title=f"[{UI_THEME['success']}]✓ Successfully installed templates for {result.agent.display_name}[/{UI_THEME['success']}]",
        border_style=UI_THEME["success"],
        padding=(1, 2)
    )
    console.print(success_panel)

    # Show file tree
    if result.files_copied:
        console.print()
        tree = Tree(
            f"[bold {UI_THEME['primary']}]{result.agent.folder}/[/bold {UI_THEME['primary']}]",
            guide_style=UI_THEME["border_subtle"]
        )

        # Organize files by subdirectory
        files_by_dir = {}
        for file_path in sorted(result.files_copied):
            parts = file_path.parts
            if len(parts) > 1:
                subdir = parts[0]
                filename = "/".join(parts[1:])
                if subdir not in files_by_dir:
                    files_by_dir[subdir] = []
                files_by_dir[subdir].append(filename)
            else:
                # File at root
                if "." not in files_by_dir:
                    files_by_dir["."] = []
                files_by_dir["."].append(str(file_path))

        # Build tree structure
        for subdir in sorted(files_by_dir.keys()):
            if subdir == ".":
                # Root files
                for filename in files_by_dir[subdir]:
                    tree.add(f"[{UI_THEME['text_tertiary']}]{filename}[/{UI_THEME['text_tertiary']}]")
            else:
                # Subdirectory
                branch = tree.add(f"[bold {UI_THEME['text_secondary']}]{subdir}/[/bold {UI_THEME['text_secondary']}]")
                for filename in files_by_dir[subdir]:
                    branch.add(f"[{UI_THEME['text_tertiary']}]{filename}[/{UI_THEME['text_tertiary']}]")

        console.print(tree)

    console.print()


def prompt_project_path() -> str:
    """
    Interactively prompt for project path.

    Returns:
        Project path string entered by user
    """
    console.print(f"\n[bold {UI_THEME['text_primary']}]Project path:[/bold {UI_THEME['text_primary']}]")
    console.print(f"[{UI_THEME['text_hint']}]Enter path (or '.' for current directory, Ctrl+C to cancel)[/{UI_THEME['text_hint']}]\n")

    while True:
        try:
            path = console.input(f"[{UI_THEME['primary']}]Path:[/{UI_THEME['primary']}] ").strip()
            if path:
                return path
            console.print(f"[{UI_THEME['warning']}]Path cannot be empty. Please try again.[/{UI_THEME['warning']}]")
        except KeyboardInterrupt:
            console.print(f"\n[{UI_THEME['warning']}]Cancelled[/{UI_THEME['warning']}]")
            sys.exit(0)


def show_main_menu() -> str | None:
    """Display interactive main menu and return selected action.

    Returns:
        Action string: "init", "version", "exit", or None if cancelled
    """
    if not READCHAR_AVAILABLE:
        return _show_main_menu_fallback()

    options = [
        ("Initialize Project", "init"),
        ("Show Version", "version"),
        ("Exit", "exit"),
    ]

    selected_idx = 0

    while True:
        show_banner()
        console.print(f"[bold {UI_THEME['text_primary']}]Main Menu:[/bold {UI_THEME['text_primary']}]\n")

        for idx, (label, _) in enumerate(options):
            prefix = "❯" if idx == selected_idx else " "
            if idx == selected_idx:
                console.print(f"  {prefix} [bold {UI_THEME['primary']}]{label}[/bold {UI_THEME['primary']}]")
            else:
                console.print(f"  {prefix} [{UI_THEME['text_secondary']}]{label}[/{UI_THEME['text_secondary']}]")

        console.print(f"\n[{UI_THEME['text_hint']}]Use ↑↓ arrows to navigate, Enter to select, ESC to exit[/{UI_THEME['text_hint']}]")

        key = readchar.readkey()

        if key == readchar.key.UP:
            selected_idx = (selected_idx - 1) % len(options)
        elif key == readchar.key.DOWN:
            selected_idx = (selected_idx + 1) % len(options)
        elif key in (readchar.key.ENTER, readchar.key.CR, readchar.key.LF):
            _, action = options[selected_idx]
            console.clear()
            return action
        elif key in (readchar.key.CTRL_C, readchar.key.ESC):
            console.print(f"\n[{UI_THEME['text_hint']}]Goodbye![/{UI_THEME['text_hint']}]\n")
            return None


def _show_main_menu_fallback() -> str | None:
    """Fallback main menu using numbered selection.

    Returns:
        Action string: "init", "version", "exit", or None if cancelled
    """
    show_banner()
    console.print(f"[bold {UI_THEME['text_primary']}]Main Menu:[/bold {UI_THEME['text_primary']}]\n")

    options = [
        ("Initialize Project", "init"),
        ("Show Version", "version"),
        ("Exit", "exit"),
    ]

    for idx, (label, _) in enumerate(options, 1):
        console.print(f"  {idx}. [{UI_THEME['text_secondary']}]{label}[/{UI_THEME['text_secondary']}]")

    console.print()

    while True:
        try:
            choice = console.input(f"[bold {UI_THEME['primary']}]Enter number (or 'q' to quit):[/bold {UI_THEME['primary']}] ")
            if choice.lower() == 'q':
                console.print(f"[{UI_THEME['text_hint']}]Goodbye![/{UI_THEME['text_hint']}]\n")
                return None

            idx = int(choice) - 1
            if 0 <= idx < len(options):
                _, action = options[idx]
                return action
            else:
                console.print(f"[{UI_THEME['error']}]Invalid choice. Please try again.[/{UI_THEME['error']}]\n")
        except (ValueError, KeyError):
            console.print(f"[{UI_THEME['error']}]Invalid input. Please enter a number.[/{UI_THEME['error']}]\n")
        except KeyboardInterrupt:
            console.print(f"\n[{UI_THEME['text_hint']}]Goodbye![/{UI_THEME['text_hint']}]\n")
            return None


def show_version(version: str) -> None:
    """
    Display version information.

    Args:
        version: Version string
    """
    show_banner()
    version_panel = Panel(
        f"[{UI_THEME['text_secondary']}]Version[/{UI_THEME['text_secondary']}] [bold {UI_THEME['accent']}]{version}[/bold {UI_THEME['accent']}]",
        title=f"[bold {UI_THEME['text_primary']}]DevKit CLI[/bold {UI_THEME['text_primary']}]",
        border_style=UI_THEME["border"],
        padding=(1, 2)
    )
    console.print(version_panel)
    console.print()
