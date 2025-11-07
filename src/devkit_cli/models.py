"""Data models for DevKit CLI."""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class AgentType(str, Enum):
    """Supported coding agents."""
    CLAUDE_CODE = "claude-code"
    CURSOR = "cursor"


@dataclass
class Agent:
    """Represents a coding agent configuration."""
    name: str
    display_name: str
    folder: str
    supported: bool
    description: str


@dataclass
class InstallResult:
    """Result of template installation."""
    success: bool
    project_path: Path
    agent: Agent
    files_copied: list[Path]
    backup_path: Path | None
    conflicts: list[Path]
    message: str
