# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Project Overview

DevKit-AI is a lightweight CLI tool that bootstraps AI coding agent templates for development projects. It provides pre-configured agents (code-explorer, code-architect, code-reviewer) and commands (feature-dev) to accelerate development workflows.

## Architecture

DevKit follows a layered architecture with clear dependency flow:

```
cli.py (entry point)
  ↓
ui.py (user interaction) + agent_utils.py (agent resolution)
  ↓
core.py (business logic)
  ↓
utils.py (pure functions) + config.py (constants) + models.py (data)
```

**Principle**: Dependencies flow downward. No circular imports. Each layer has a clear responsibility.

## Development Patterns

### Code Organization

- **Separation of concerns**: Each module has a single, clear responsibility
- **Type hints**: Use type hints throughout for better IDE support and type safety
- **Path handling**: Always use `pathlib.Path`, never string concatenation
- **Error handling**: Use custom exceptions with clear, actionable error messages

### Module Responsibilities

- **cli.py**: Command definitions, argument parsing, orchestration
- **ui.py**: Interactive prompts, menus, result display
- **core.py**: Template installation, conflict detection, backup logic
- **agent_utils.py**: Agent resolution from flags
- **config.py**: Agent configurations, constants, template paths
- **models.py**: Data structures (Agent, InstallResult, AgentType)
- **utils.py**: Path resolution, file operations, custom exceptions

### Dependencies

- **uv**: Dependency management (use `uv add` for dependencies)
- **typer**: CLI framework with type hints
- **rich**: Terminal UI and formatting
- **readchar**: Interactive keyboard input (with fallback)
- **Python**: >=3.11 required

### Running the Project

**IMPORTANT**: Always use `uv` to run the project:
- Run CLI: `uv run devkit` or `uv run python -m devkit_cli.cli`
- Run tests: `uv run pytest`
- Never use plain `python` command - always prefix with `uv run`

### Coding Standards

1. **Type safety**: Use dataclasses and type hints everywhere
2. **Immutability**: Prefer immutable data structures where possible
3. **Clear names**: Function and variable names should be self-documenting
4. **Small functions**: Keep functions focused and small
5. **No magic**: Explicit is better than implicit

### Error Handling

- Custom exceptions inherit from `DevKitError`
- Always provide actionable error messages
- Handle errors at appropriate abstraction levels
- Use Rich console for user-facing error messages

### Testing

- Test each component after implementation (manual for v1, automated for v2)
- Verify edge cases: conflicts, missing directories, invalid paths
- Clean up test artifacts immediately after testing
- Use real terminal for interactive UI testing (mocking has limitations)

### UI Patterns

- Interactive selection with arrow keys, fallback to numbered input
- Rich console for all output (no raw print statements)
- Clear error messages with Text objects (avoids Rich markup conflicts)
- Visual hierarchy: bold for headers, dim for hints, colored for status
- Always provide next steps after operations

## Development Workflow

### Use Feature-Dev to Build Features

When implementing new features:
1. Use `/feature-dev` workflow on this project (dog-fooding)
2. Follow all 7 phases - they prevent premature implementation
3. Document pain points discovered - each becomes an improvement

### Key Practices from DevKit Development

- **Ask clarifying questions early**: Resolve ambiguities before designing (Phase 3)
- **Launch multiple explorers**: Different focuses reveal different insights (Phase 2)
- **Test incrementally**: Build and test each module before moving to next (Phase 5)
- **Multi-agent review**: Different reviewers catch different issues (Phase 6)

## Quality Assurance Strategy

### Multi-Agent Review (Critical)

Before completing any significant feature:

1. **Launch 3-4 review agents in parallel** with different focuses:
   - Functional correctness (bugs, logic errors, edge cases)
   - Code quality (simplicity, DRY, elegance)
   - Project conventions (adherence to this CLAUDE.md)
   - Architecture (structure, extensibility, complexity)

2. **Critical evaluation of agent feedback**:
   - Agents are not always correct - think critically
   - If agents contradict, investigate which is right
   - Prioritize issues by impact (security > bugs > quality > style)
   - Ask yourself: "Does this fix actually improve the code?"

3. **Fix high-priority issues immediately**:
   - P0 (security, crashes, data loss): Must fix
   - P1 (bugs, major quality): Should fix
   - P2 (code smells, minor): Can defer

### Clarification Protocol

When requirements are unclear:
- **Don't assume** - ask the user specific questions
- **Group questions** by priority: blocking vs design vs polish
- **Suggest defaults** but get explicit confirmation
- **Document decisions** for future reference

### Code Review After Each Step

- Run code-reviewer agent on changed files
- Check confidence scores (only address ≥80)
- Validate that fixes don't introduce new issues
- Re-review after fixes if changes are substantial
