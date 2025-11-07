"""Agent resolution and management utilities."""

from devkit_cli.config import AGENT_CONFIG
from devkit_cli.models import Agent, AgentType


def get_agent_by_flag(claude: bool, cursor: bool) -> tuple[Agent | None, str | None]:
    """
    Resolve agent from command-line flags.

    Args:
        claude: --claude flag value
        cursor: --cursor flag value

    Returns:
        Tuple of (Agent instance or None, error message or None)

        - (None, None): No flags set, will prompt user
        - (Agent, None): Valid agent selected
        - (None, "error"): Invalid flag combination

    Examples:
        >>> get_agent_by_flag(True, False)
        (Agent(CLAUDE_CODE), None)

        >>> get_agent_by_flag(False, False)
        (None, None)  # Will prompt

        >>> get_agent_by_flag(True, True)
        (None, "Cannot specify multiple agent flags")
    """
    flags_set = sum([claude, cursor])

    if flags_set > 1:
        return None, "Cannot specify multiple agent flags (--claude, --cursor)"

    if flags_set == 0:
        return None, None  # No flags - will prompt user

    # Exactly one flag is set
    if claude:
        agent = AGENT_CONFIG[AgentType.CLAUDE_CODE]
        if not agent.supported:
            return None, f"{agent.display_name} is not supported yet"
        return agent, None

    if cursor:
        agent = AGENT_CONFIG[AgentType.CURSOR]
        if not agent.supported:
            return None, f"{agent.display_name} is not supported yet"
        return agent, None

    # Should never reach here
    return None, "Unknown agent flag"


def get_supported_agents() -> list[Agent]:
    """
    Get list of supported agents only.

    Returns:
        List of Agent instances where supported=True
    """
    return [agent for agent in AGENT_CONFIG.values() if agent.supported]


def get_all_agents() -> list[Agent]:
    """
    Get all agents regardless of support status.

    Returns:
        List of all Agent instances
    """
    return list(AGENT_CONFIG.values())
