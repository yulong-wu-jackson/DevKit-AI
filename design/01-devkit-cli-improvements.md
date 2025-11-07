# DevKit CLI Improvements

This document outlines improvements to make the DevKit CLI tool more robust, user-friendly, and maintainable.

## Context

As an AI agent who just built DevKit using the feature-dev workflow, I experienced firsthand what works well and what could be better. This document captures those insights.

## Critical Issues to Address

### 1. Missing Test Coverage (Priority: HIGH)

**Problem**: Zero automated tests means regressions go undetected.

**Impact**:
- Breaking changes can slip through
- Refactoring is risky
- Hard to validate edge cases

**Solution**:
```python
# tests/test_agent_utils.py
def test_get_agent_by_flag_single_claude():
    agent, error = get_agent_by_flag(claude=True, cursor=False)
    assert agent is not None
    assert agent.name == AgentType.CLAUDE_CODE
    assert error is None

def test_get_agent_by_flag_conflicting():
    agent, error = get_agent_by_flag(claude=True, cursor=True)
    assert agent is None
    assert "multiple" in error.lower()

def test_get_agent_by_flag_unsupported():
    agent, error = get_agent_by_flag(claude=False, cursor=True)
    assert agent is None
    assert "not supported" in error.lower()
```

**Estimated Effort**: 4-6 hours for basic test suite (20-30 tests)

---

### 2. Circular Import Between cli.py and ui.py (Priority: HIGH) ✅ COMPLETED

**Status**: Fixed on 2025-11-07
- Implemented Solution 2 (Event-Based)
- `show_main_menu()` now returns action string instead of executing
- `cli.py` handles routing based on returned action
- No more circular imports

**Problem**:
- `cli.py` imports from `ui.py`
- `ui.py` imports `cli.init()` inside functions (lines 216, 260)
- Creates tight coupling, makes testing hard

**Current Code (ui.py:216)**:
```python
if action == "init":
    from devkit_cli.cli import init
    init(project_name=None, here=False, claude=False, cursor=False)
```

**Solution 1: Callback Pattern**
```python
# ui.py - accept callback function
def show_main_menu(on_init: Callable, on_version: Callable) -> None:
    if action == "init":
        on_init()
    elif action == "version":
        on_version()

# cli.py - pass functions
def main_callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        show_main_menu(
            on_init=lambda: init(None, False, False, False),
            on_version=lambda: show_version(__version__)
        )
```

**Solution 2: Event-Based (Better)**
```python
# ui.py returns selected action instead of executing
def show_main_menu() -> str:
    # ... menu logic ...
    return action  # "init", "version", "exit"

# cli.py handles routing
def main_callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        action = show_main_menu()
        if action == "init":
            init(None, False, False, False)
        elif action == "version":
            show_version(__version__)
```

**Estimated Effort**: 2 hours

---

### 2.1. UI Color Scheme - Nordic Literary Design ✅ COMPLETED

**Status**: Implemented on 2025-11-07
- Designed sophisticated "Nordic Literary" color palette
- Low-saturation ice blue with greyscale hierarchy
- Banner gradient from light ice blue to charcoal blue-grey
- All UI components updated to use theme constants
- Calm, professional, easy on eyes

**Design Philosophy**:
- **Literary elegance**: Inspired by classic literature and Scandinavian design
- **Low saturation**: Muted colors, not bright, comfortable for long viewing
- **Greyscale foundation**: 5-level hierarchy (bright_white → white → grey → subtle grey → dim)
- **Ice blue accents**: Cool blue-grey palette (#96bfe6 → #7ba4d9 → #5d8cb8 → #556677)
- **Artistic status colors**: Sage green, muted gold, dusty rose

**Color Palette** (`config.py`):
```python
UI_THEME = {
    # Greyscale Hierarchy
    "text_primary": "bright_white",     # Clearest text
    "text_secondary": "white",          # Regular text
    "text_tertiary": "#a8a8a8",        # De-emphasized
    "text_hint": "#808080",             # Hints
    "text_dim": "dim",                  # Least important

    # Ice Blue Palette
    "primary": "#7ba4d9",               # Soft steel blue
    "primary_muted": "#5d8cb8",         # Muted blue-grey
    "accent": "#96bfe6",                # Light ice blue
    "border": "#556677",                # Charcoal blue-grey
    "border_subtle": "#3a4454",         # Darker borders

    # Status Colors (muted)
    "success": "#7ba888",               # Sage green
    "warning": "#c9b875",               # Muted gold
    "error": "#c98989",                 # Dusty rose

    # Banner Gradient
    "banner_gradient": ["#96bfe6", "#7ba4d9", "#5d8cb8", "#556677"],
}
```

**Implementation**:
- Banner displays with 4-color gradient (top to bottom)
- All hardcoded colors replaced with theme constants
- Consistent color usage across all UI components
- Typography hierarchy using greyscale levels

**Estimated Effort**: 2-3 hours (completed)

---

### 3. Large UI Module Needs Refactoring (Priority: MEDIUM)

**Problem**: `ui.py` is 287 lines doing 5 different things:
- Menu display
- Agent selection
- Path prompting
- Result display
- Version display

**Solution**: Split into focused modules:

```
src/devkit_cli/ui/
├── __init__.py         # Re-exports everything
├── display.py          # show_result, show_version, show_error
├── prompts.py          # select_agent, prompt_project_path
└── menu.py             # show_main_menu
```

**Benefits**:
- Easier to test individual components
- Clearer responsibilities
- Easier to find code
- Better code organization

**Estimated Effort**: 3-4 hours

---

## User Experience Improvements

### 4. Add Confirmation for Destructive Operations (Priority: MEDIUM)

**Problem**: DevKit overwrites existing `.claude/` without asking permission (only backs up).

**Current Behavior**:
```bash
$ devkit init --here --claude
# Silently backs up and overwrites .claude/
```

**Improved Behavior**:
```bash
$ devkit init --here --claude

⚠ Found existing .claude/ folder with 4 files
  This will create a backup and overwrite with new templates.

Continue? [Y/n]: _
```

**Implementation**:
```python
# In cli.py
conflicts = template_manager.detect_conflicts(project_path)
if conflicts and not force:
    console.print(f"\n[yellow]⚠ Found existing {agent.folder}/ folder with {len(conflicts)} files[/yellow]")
    console.print("  This will create a backup and overwrite with new templates.\n")

    if not confirm_action("Continue?", default=True):
        console.print("[yellow]Operation cancelled.[/yellow]")
        sys.exit(0)
```

**Add Force Flag**:
```python
force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation prompts")
```

**Estimated Effort**: 1 hour

---

### 5. Improve Path Display in Next Steps (Priority: LOW)

**Problem**: Next steps show `cd {project_path.name}` which is wrong for absolute paths.

**Current (line 113)**:
```python
console.print(f"  1. Navigate to your project: cd {project_path.name if not here else '.'}")
```

**For input**: `devkit init /tmp/myproject --claude`
**Says**: `cd myproject` (but user isn't in /tmp!)

**Fixed**:
```python
# Calculate relative path from current directory
try:
    rel_path = project_path.relative_to(Path.cwd())
    cd_path = str(rel_path)
except ValueError:
    # Not relative to cwd, show absolute
    cd_path = str(project_path)

if here:
    cd_path = "."

console.print(f"  1. Navigate to your project: cd {cd_path}")
```

**Estimated Effort**: 30 minutes

---

### 6. Add Help Command (Priority: MEDIUM)

**Problem**: No built-in help beyond `--help` flags.

**Solution**:
```python
@app.command()
def help() -> None:
    """Show detailed help and usage examples."""
    console.print("\n[bold cyan]DevKit CLI Help[/bold cyan]\n")

    console.print("[bold]Quick Start:[/bold]")
    console.print("  devkit                     # Interactive menu")
    console.print("  devkit init proj --claude  # Direct execution")
    console.print("  devkit version             # Show version\n")

    console.print("[bold]Common Workflows:[/bold]")
    console.print("  1. New project:     devkit init my-project --claude")
    console.print("  2. Existing project: cd my-project && devkit init --here --claude")
    console.print("  3. Update templates: devkit init --here --claude --force\n")

    console.print("[bold]Learn More:[/bold]")
    console.print("  README:  https://github.com/yulong-wu-jackson/DevKit-AI")
    console.print("  Issues:  https://github.com/yulong-wu-jackson/DevKit-AI/issues\n")
```

**Estimated Effort**: 1 hour

---

## Robustness Improvements

### 7. Validate Templates at Startup (Priority: HIGH)

**Problem**: No check that templates exist until installation fails.

**Solution**:
```python
# In __init__.py or config.py
def validate_templates() -> None:
    """Validate all configured templates exist."""
    for agent in AGENT_CONFIG.values():
        if not agent.supported:
            continue

        template_path = TEMPLATES_DIR / agent.name
        if not template_path.exists():
            raise TemplateNotFoundError(
                f"Template directory missing: {template_path}\n"
                f"Expected agents/ and commands/ subdirectories"
            )

        # Check required subdirectories
        for subdir in TEMPLATE_SUBDIRS:
            subdir_path = template_path / subdir
            if not subdir_path.exists():
                raise TemplateNotFoundError(
                    f"Required subdirectory missing: {subdir_path}"
                )

# Call on module import
validate_templates()
```

**Better Error Messages**:
```
Error: Template directory missing: /path/to/devkit_cli/templates/claude-code
Expected agents/ and commands/ subdirectories

This usually means:
  1. DevKit was not installed correctly
  2. Template files are missing from the package

To fix:
  uv tool uninstall devkit-cli
  uv tool install devkit-cli --from git+https://github.com/...
```

**Estimated Effort**: 1-2 hours

---

### 8. Use Typer Mutually Exclusive Groups (Priority: MEDIUM)

**Problem**: `--here` and `project_name` conflict is checked in code, not at argument level.

**Current** (validated in utils.py):
```python
if here and project_name:
    raise ProjectPathError("Cannot specify both project name and --here flag")
```

**Better** (Typer enforces):
```python
# Define mutually exclusive options
# Note: Typer doesn't directly support this, but we can use Context
# Or we can validate early in the command

@app.command()
def init(
    ctx: typer.Context,
    project_name: Optional[str] = typer.Argument(None),
    here: bool = typer.Option(False, "--here"),
    ...
) -> None:
    # Validate early
    if here and project_name and project_name != ".":
        raise typer.BadParameter("Cannot use both project name and --here")
```

**Estimated Effort**: 1 hour

---

## Performance and Scalability

### 9. Template Caching (Priority: LOW)

**Current**: Templates loaded every time.
**For v1.0**: Not an issue (4 files, instant)
**For v2.0**: If templates grow to 50+ files, could be slow

**Future Solution**:
```python
class TemplateManager:
    _template_cache: dict[str, list[Path]] = {}

    def get_template_files(self) -> list[Path]:
        cache_key = str(self.template_path)
        if cache_key in self._template_cache:
            return self._template_cache[cache_key]

        # ... existing logic ...
        self._template_cache[cache_key] = template_files
        return template_files
```

---

## Configuration Extensibility

### 10. Support Configuration File (Priority: MEDIUM)

**Problem**: All settings are hardcoded.

**Use Cases**:
- Company wants custom template path
- User wants to change default agent
- Project wants specific template version

**Solution**: Add `.devkit.toml` support

```toml
# .devkit.toml (project-level)
[devkit]
default_agent = "claude-code"
template_source = "git+https://custom/templates"
auto_backup = true
backup_prefix = ".backup"

[agents.custom]
name = "my-agent"
folder = ".myagent"
templates = "./local/templates"
```

**Implementation**:
```python
# config.py
from pathlib import Path
import tomllib  # Python 3.11+

def load_config() -> dict:
    """Load config from .devkit.toml if it exists."""
    config_path = Path.cwd() / ".devkit.toml"
    if config_path.exists():
        with open(config_path, "rb") as f:
            return tomllib.load(f)
    return {}

# Override defaults with config file
user_config = load_config()
DEFAULT_AGENT = user_config.get("default_agent", "claude-code")
```

**Estimated Effort**: 4-6 hours

---

## Summary of Recommendations

**Must-Fix Before v1.0**:
1. Add test suite (20+ tests)
2. Fix circular imports
3. Validate templates at startup
4. Better error messages

**Should-Fix for v1.1**:
1. Split ui.py into modules
2. Add help command
3. Add confirmation prompts
4. Fix path display
5. Use Typer validation

**Nice-to-Have for v2.0**:
1. Configuration file support
2. Plugin system for agents
3. Template versioning
4. Performance optimizations

**Total Estimated Effort to v1.0**: 10-15 hours
**Total Estimated Effort to v2.0**: 30-40 hours
