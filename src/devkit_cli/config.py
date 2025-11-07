"""Configuration for DevKit CLI."""

from pathlib import Path
from devkit_cli.models import Agent, AgentType


# Agent configurations
AGENT_CONFIG: dict[AgentType, Agent] = {
    AgentType.CLAUDE_CODE: Agent(
        name=AgentType.CLAUDE_CODE,
        display_name="Claude Code",
        folder=".claude",
        supported=True,
        description="AI coding assistant by Anthropic"
    ),
    AgentType.CURSOR: Agent(
        name=AgentType.CURSOR,
        display_name="Cursor",
        folder=".cursor",
        supported=False,
        description="AI-powered code editor (not supported yet)"
    ),
}

# Path to bundled templates
TEMPLATES_DIR = Path(__file__).parent / "templates"

# Template structure
TEMPLATE_SUBDIRS = ["agents", "commands"]
