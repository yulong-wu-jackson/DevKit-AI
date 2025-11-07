"""Utility functions for DevKit CLI."""

import shutil
from datetime import datetime
from pathlib import Path


class DevKitError(Exception):
    """Base exception for DevKit CLI errors."""
    pass


class ProjectPathError(DevKitError):
    """Error related to project path resolution."""
    pass


class TemplateNotFoundError(DevKitError):
    """Error when template files are not found."""
    pass


def get_project_path(project_name: str | None, here: bool) -> Path:
    """
    Resolve project path from arguments.

    Args:
        project_name: Name of the project (can be None if --here is used)
        here: Whether to use current directory

    Returns:
        Resolved absolute Path to project

    Raises:
        ProjectPathError: If arguments are invalid
    """
    if here:
        if project_name:
            raise ProjectPathError("Cannot specify both project name and --here flag")
        return Path.cwd()

    if not project_name:
        raise ProjectPathError("Must specify project name or use --here flag")

    # Handle special case: "." means current directory
    if project_name == ".":
        return Path.cwd()

    return Path(project_name).resolve()


def ensure_directory(path: Path) -> None:
    """
    Create directory if it doesn't exist.

    Args:
        path: Directory path to create
    """
    path.mkdir(parents=True, exist_ok=True)


def create_backup(source: Path) -> Path:
    """
    Create a timestamped backup of a directory.

    Args:
        source: Directory to backup

    Returns:
        Path to backup directory
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = source.parent / f"{source.name}.backup-{timestamp}"
    shutil.copytree(source, backup_path)
    return backup_path


def copy_file(source: Path, dest: Path) -> None:
    """
    Copy a file, creating parent directories if needed.

    Args:
        source: Source file path
        dest: Destination file path

    Raises:
        DevKitError: If file copy fails
    """
    ensure_directory(dest.parent)
    try:
        shutil.copy2(source, dest)
    except (OSError, IOError) as e:
        raise DevKitError(f"Failed to copy {source.name} to {dest}: {e}") from e
