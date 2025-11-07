"""UI components for DevKit CLI."""

import sys
from typing import Sequence
from rich.console import Console
from rich.text import Text
from devkit_cli.models import Agent, InstallResult

try:
    import readchar
    READCHAR_AVAILABLE = True
except ImportError:
    READCHAR_AVAILABLE = False


console = Console()


def show_error(message: str, prefix: str = "Error") -> None:
    """
    Display a styled error message.

    Args:
        message: Error message to display
        prefix: Prefix text (default: "Error")
    """
    error_text = Text()
    error_text.append(f"{prefix}: ", style="red bold")
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

    while True:
        # Clear screen and show options
        console.clear()
        console.print("\n[bold]Select a coding agent:[/bold]\n")

        for idx, agent in enumerate(agents):
            prefix = "→" if idx == selected_idx else " "

            status = "" if agent.supported else " [dim](not supported yet)[/dim]"

            if idx == selected_idx:
                console.print(f"  {prefix} [bold cyan]{agent.display_name}[/bold cyan]{status}")
            else:
                console.print(f"  {prefix} {agent.display_name}{status}")

        console.print("\n[dim]Use ↑↓ arrows to navigate, Enter to select, Ctrl+C to cancel[/dim]")

        # Read key
        key = readchar.readkey()

        if key == readchar.key.UP:
            selected_idx = (selected_idx - 1) % len(agents)
        elif key == readchar.key.DOWN:
            selected_idx = (selected_idx + 1) % len(agents)
        elif key in (readchar.key.ENTER, readchar.key.CR, readchar.key.LF):
            selected_agent = agents[selected_idx]
            if not selected_agent.supported:
                console.print(f"\n[yellow]⚠ {selected_agent.display_name} is not supported yet.[/yellow]")
                console.print("[dim]Press any key to continue...[/dim]")
                readchar.readkey()
                continue
            return selected_agent
        elif key == readchar.key.CTRL_C:
            console.print("\n[yellow]Cancelled[/yellow]")
            return None


def _select_agent_fallback(agents: Sequence[Agent]) -> Agent | None:
    """Fallback agent selection using numbers (when readchar unavailable)."""
    console.print("\n[bold]Select a coding agent:[/bold]\n")

    for idx, agent in enumerate(agents, 1):
        status = "" if agent.supported else " [dim](not supported yet)[/dim]"
        console.print(f"  {idx}. {agent.display_name}{status}")

    console.print()

    while True:
        try:
            choice = console.input("[bold cyan]Enter number (or 'q' to quit):[/bold cyan] ")
            if choice.lower() == 'q':
                return None

            idx = int(choice) - 1
            if 0 <= idx < len(agents):
                selected_agent = agents[idx]
                if not selected_agent.supported:
                    console.print(f"[yellow]⚠ {selected_agent.display_name} is not supported yet.[/yellow]\n")
                    continue
                return selected_agent
            else:
                console.print("[red]Invalid choice. Please try again.[/red]\n")
        except (ValueError, KeyError):
            console.print("[red]Invalid input. Please enter a number.[/red]\n")
        except KeyboardInterrupt:
            console.print("\n[yellow]Cancelled[/yellow]")
            return None


def show_result(result: InstallResult) -> None:
    """
    Display installation result to user.

    Args:
        result: Installation result to display
    """
    if result.success:
        console.print(f"\n[green]✓ Successfully installed templates for {result.agent.display_name}[/green]\n")
    else:
        console.print(f"\n[red]✗ Failed to install templates[/red]\n")
        console.print(f"[red]{result.message}[/red]\n")
        return

    # Show details
    details = []

    if result.conflicts:
        details.append(f"[yellow]• Found {len(result.conflicts)} existing file(s)[/yellow]")

    if result.backup_path:
        details.append(f"[blue]• Created backup: {result.backup_path.name}[/blue]")

    details.append(f"[green]• Copied {len(result.files_copied)} file(s) to {result.agent.folder}/[/green]")

    for detail in details:
        console.print(detail)

    # Show file list
    if result.files_copied:
        console.print(f"\n[bold]Files installed:[/bold]")
        for file_path in sorted(result.files_copied):
            console.print(f"  • {result.agent.folder}/{file_path}")

    console.print()


def prompt_project_path() -> str:
    """
    Interactively prompt for project path.

    Returns:
        Project path string entered by user
    """
    console.print("\n[bold]Project path:[/bold]")
    console.print("[dim]Enter path (or '.' for current directory, Ctrl+C to cancel)[/dim]\n")

    try:
        path = console.input("[cyan]Path:[/cyan] ").strip()
        if not path:
            console.print("[yellow]Path cannot be empty. Please try again.[/yellow]")
            return prompt_project_path()
        return path
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled[/yellow]")
        sys.exit(0)


def show_main_menu() -> None:
    """Display interactive main menu and route to selected action."""
    if not READCHAR_AVAILABLE:
        _show_main_menu_fallback()
        return

    options = [
        ("Initialize Project", "init"),
        ("Show Version", "version"),
        ("Exit", "exit"),
    ]

    selected_idx = 0

    while True:
        console.clear()
        console.print("\n[bold cyan]DevKit CLI[/bold cyan]\n")
        console.print("[bold]Main Menu:[/bold]\n")

        for idx, (label, _) in enumerate(options):
            prefix = "→" if idx == selected_idx else " "
            if idx == selected_idx:
                console.print(f"  {prefix} [bold cyan]{label}[/bold cyan]")
            else:
                console.print(f"  {prefix} {label}")

        console.print("\n[dim]Use ↑↓ arrows to navigate, Enter to select, Ctrl+C to exit[/dim]")

        key = readchar.readkey()

        if key == readchar.key.UP:
            selected_idx = (selected_idx - 1) % len(options)
        elif key == readchar.key.DOWN:
            selected_idx = (selected_idx + 1) % len(options)
        elif key in (readchar.key.ENTER, readchar.key.CR, readchar.key.LF):
            _, action = options[selected_idx]
            console.clear()

            if action == "init":
                # Call init without any arguments (will prompt for everything)
                from devkit_cli.cli import init
                init(project_name=None, here=False, claude=False, cursor=False)
                return
            elif action == "version":
                from devkit_cli import __version__
                show_version(__version__)
                console.input("\n[dim]Press Enter to continue...[/dim]")
                continue
            elif action == "exit":
                console.print("[dim]Goodbye![/dim]\n")
                sys.exit(0)
        elif key == readchar.key.CTRL_C:
            console.print("\n[dim]Goodbye![/dim]\n")
            sys.exit(0)


def _show_main_menu_fallback() -> None:
    """Fallback main menu using numbered selection."""
    console.print("\n[bold cyan]DevKit CLI[/bold cyan]\n")
    console.print("[bold]Main Menu:[/bold]\n")

    options = [
        ("Initialize Project", "init"),
        ("Show Version", "version"),
        ("Exit", "exit"),
    ]

    for idx, (label, _) in enumerate(options, 1):
        console.print(f"  {idx}. {label}")

    console.print()

    while True:
        try:
            choice = console.input("[bold cyan]Enter number (or 'q' to quit):[/bold cyan] ")
            if choice.lower() == 'q':
                console.print("[dim]Goodbye![/dim]\n")
                sys.exit(0)

            idx = int(choice) - 1
            if 0 <= idx < len(options):
                _, action = options[idx]

                if action == "init":
                    from devkit_cli.cli import init
                    init(project_name=None, here=False, claude=False, cursor=False)
                    return
                elif action == "version":
                    from devkit_cli import __version__
                    show_version(__version__)
                    console.input("\n[dim]Press Enter to continue...[/dim]")
                    continue
                elif action == "exit":
                    console.print("[dim]Goodbye![/dim]\n")
                    sys.exit(0)
            else:
                console.print("[red]Invalid choice. Please try again.[/red]\n")
        except (ValueError, KeyError):
            console.print("[red]Invalid input. Please enter a number.[/red]\n")
        except KeyboardInterrupt:
            console.print("\n[dim]Goodbye![/dim]\n")
            sys.exit(0)


def show_version(version: str) -> None:
    """
    Display version information.

    Args:
        version: Version string
    """
    console.print(f"\n[bold cyan]DevKit CLI[/bold cyan] version [green]{version}[/green]\n")
