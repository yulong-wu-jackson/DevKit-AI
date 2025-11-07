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
TEMPLATE_SUBDIRS = ["agents", "commands", "hooks"]

# UI Theme - Nordic Literary: Low-saturation ice blue with sophisticated greyscale
# Design philosophy: Calm, professional, easy on eyes, literary elegance
UI_THEME = {
    # Greyscale Hierarchy (brightest to dimmest)
    "text_primary": "bright_white",     # Clearest text, main content
    "text_secondary": "white",          # Regular text
    "text_tertiary": "#a8a8a8",        # Grey, de-emphasized content
    "text_hint": "#808080",             # Subtle grey, hints
    "text_dim": "dim",                  # Dimmest, least important

    # Ice Blue Palette (low saturation, calming)
    "primary": "#7ba4d9",               # Soft steel blue - main interactive
    "primary_muted": "#5d8cb8",         # Muted blue-grey - secondary
    "accent": "#96bfe6",                # Light ice blue - subtle highlights
    "border": "#556677",                # Charcoal blue-grey - borders
    "border_subtle": "#3a4454",         # Darker border for trees/guides

    # Status Colors (muted, not bright)
    "success": "#7ba888",               # Sage green - success states
    "success_dim": "#5a8566",           # Darker sage - completed items
    "warning": "#c9b875",               # Muted gold - warnings
    "error": "#c98989",                 # Dusty rose - errors
    "info": "#7ba4d9",                  # Same as primary - info messages

    # Banner Gradient (cool blue-grey cascade)
    "banner_gradient": [
        "#96bfe6",  # Light ice blue (top)
        "#7ba4d9",  # Steel blue
        "#5d8cb8",  # Muted blue-grey
        "#556677",  # Charcoal blue-grey (bottom)
    ],
}

# Banner ASCII art
BANNER = """   ██████████                        █████   ████  ███   █████
  ░░███░░░░███                      ░░███   ███░  ░░░   ░░███
   ░███   ░░███  ██████  █████ █████ ░███  ███    ████  ███████
   ░███    ░███ ███░░███░░███ ░░███  ░███████    ░░███ ░░░███░
   ░███    ░███░███████  ░███  ░███  ░███░░███    ░███   ░███
   ░███    ███ ░███░░░   ░░███ ███   ░███ ░░███   ░███   ░███ ███
   ██████████  ░░██████   ░░█████    █████ ░░████ █████  ░░█████
  ░░░░░░░░░░    ░░░░░░     ░░░░░    ░░░░░   ░░░░ ░░░░░    ░░░░░  """
