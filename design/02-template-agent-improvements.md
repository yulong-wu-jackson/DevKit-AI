# Template & Agent Improvements

Strategic improvements for the agents and commands that DevKit installs.

## Context

Having just used the feature-dev workflow to build DevKit itself, I can provide unique insights into what makes agents effective and what's missing.

## Agent-Specific Improvements

### Code-Explorer Agent

**What Works Well**:
- Clear mission: "trace implementation from entry points to data storage"
- Good structured approach (Discovery → Flow → Architecture → Details)
- File:line reference requirement helps with navigation

**What Could Be Better**:

#### 1. Add Language-Specific Guidance (Priority: MEDIUM)

**Problem**: Explorer treats all codebases the same.

**Solution**: Add language-specific prompts in the template:

```markdown
## Language-Specific Patterns

When exploring codebases, adapt your approach to the language:

**Python**:
- Entry points: Look for __main__.py, cli.py, Flask/FastAPI routes
- Patterns: Decorators, metaclasses, dependency injection
- Import chains: Follow 'from X import Y' to understand dependencies

**TypeScript/JavaScript**:
- Entry points: index.ts, main.ts, Express routes, React components
- Patterns: Async/await, promises, middleware, HOCs
- Module system: Check import and export statements

**Go**:
- Entry points: main.go, cmd/ directory, HTTP handlers
- Patterns: Interfaces, goroutines, channels, middleware
- Package organization: Internal vs external packages

**Rust**:
- Entry points: main.rs, lib.rs, binary crates
- Patterns: Traits, ownership, lifetimes, macros
- Module system: mod declarations and use statements
```

**Impact**: Explorers give more accurate, language-appropriate analysis.

---

#### 2. Add Output Templates for Consistency (Priority: MEDIUM)

**Problem**: Explorer output format is described but not templated.

**Solution**: Add structured output template to agent instructions:

```markdown
## Output Template

Use this structure for your exploration results:

### Entry Points
- File: path/to/file.ext:123
- Description: What this entry point does
- Triggered By: How it's invoked (HTTP route, CLI command, etc.)

### Execution Flow
1. Entry: file.ext:123 -> function_name()
2. Step 1: [Description of what happens]
   - Data transformation: Input -> Output
   - Key function: other_file.ext:456 -> helper_function()
3. Step 2: ...
4. Output: Final result or side effect

### Key Components
| Component | File:Line | Responsibility | Dependencies |
|-----------|-----------|----------------|--------------|
| ComponentName | path:123 | Does X | Uses Y, Z |

### Architecture Insights
- Pattern: [e.g., Repository Pattern, MVC, etc.]
- Layer: [e.g., Presentation -> Service -> Data]
- Design Decision: [Why it's structured this way]

### Essential Files to Read
1. path/to/file1.ext - Core business logic
2. path/to/file2.ext - Data layer
...
```

**Impact**: Consistent, parseable output that's easier to consume and reference later.

---

### Code-Architect Agent

**What Works Well**:
- Decisive approach: "make confident choices rather than presenting multiple options"
- Comprehensive blueprint with file paths and responsibilities
- Build sequence as checklist is actionable

**What Could Be Better**:

#### 3. Add Risk Assessment Section (Priority: HIGH)

**Problem**: Architect proposes designs but doesn't highlight risks.

**During DevKit development**:
- Architect suggested patterns but didn't warn about circular imports
- Didn't identify that ui.py would grow too large
- Didn't flag potential test coverage gaps

**Solution**: Add to agent template:

```markdown
## Risk Assessment (Required Section)

For each architectural decision, identify:

### Technical Risks
- Performance: Will this scale? Any bottlenecks?
- Complexity: Is this too complex for the team? Maintenance burden?
- Dependencies: Are we adding heavy dependencies?
- Testing: How hard is this to test?

### Implementation Risks
- Scope Creep: Are we building more than needed?
- Breaking Changes: Will this break existing code?
- Time: Realistic timeline for implementation?
- Unknowns: What don't we know yet?

### Mitigation Strategies
For each high risk:
- How to validate early (proof-of-concept, spike)
- Fallback options if it doesn't work
- When to stop and reconsider

### Example Risk Assessment

Decision: Use Typer for CLI framework

Risks:
- Dependency: Adds typer + rich + click to deps
- Testing: Typer apps are harder to unit test
- Migration: If we need to switch CLI frameworks later

Mitigations:
- Spike: Build prototype in 1 hour to validate
- Testing: Use Typer's test utilities, isolate business logic
- Migration: Keep CLI layer thin, core logic independent
```

**Impact**: Fewer architectural regrets, better risk awareness, earlier course correction.

---

#### 4. Add Complexity Budget (Priority: MEDIUM)

**Problem**: No guidance on when a design is "too complex."

**Real Example from DevKit**:
- ui.py grew to 287 lines
- Should have been split into 3 modules
- Architect didn't flag this

**Solution**: Add complexity guidelines:

```markdown
## Complexity Budget

Keep your design within these guidelines:

### Module Size
- Python module: Aim for <300 lines, max 500 lines
- TypeScript module: Aim for <400 lines, max 600 lines
- Class: Aim for <200 lines, max 300 lines
- Function: Aim for <50 lines, max 100 lines

**If exceeding**: Explain why or refactor into smaller pieces.

### Dependency Count
- Direct dependencies: <10 for small features, <20 for large
- Circular dependencies: ZERO (red flag)
- Depth of dependency graph: <5 levels

**If exceeding**: Simplify or justify the complexity.

### Abstraction Layers
- Layers: 3-5 is ideal (e.g., CLI -> Service -> Data)
- Too few (<2): Everything is coupled
- Too many (>6): Over-engineered

**If exceeding**: Flatten or explain each layer's necessity.

### Cognitive Load
Ask yourself: Can a new developer understand this in <30 minutes?
- If no: Simplify or add extensive documentation
```

---

### Code-Reviewer Agent

**What Works Well**:
- Confidence scoring (0-100) with ≥80 threshold prevents noise
- Three review focuses cover key areas
- References specific lines and files

**What Could Be Better**:

#### 5. Add Automated Fix Suggestions (Priority: HIGH)

**Problem**: Reviewer suggests fixes in prose, but not in code.

**Current Output**:
```
Issue: Missing exception handling in copy_file
Fix: Add try-except block around shutil.copy2()
```

**Better Output**:
```
Issue: Missing exception handling in copy_file (utils.py:91)

Current Code:
    def copy_file(source: Path, dest: Path) -> None:
        ensure_directory(dest.parent)
        shutil.copy2(source, dest)

Suggested Fix:
    def copy_file(source: Path, dest: Path) -> None:
        ensure_directory(dest.parent)
        try:
            shutil.copy2(source, dest)
        except (OSError, IOError) as e:
            raise DevKitError(f"Failed to copy {source.name}: {e}") from e

Confidence: 90%
Priority: P0 (Must fix - could crash on permission errors)
```

**Impact**: Users can copy-paste fixes directly, faster iteration.

---

#### 6. Add Context About "Why This Matters" (Priority: MEDIUM)

**Problem**: Issues listed but not explained why they're important.

**Current**:
```
Issue: files_backed_up should be Optional[Path]
Confidence: 82
```

**Better**:
```
Issue: files_backed_up should be Optional[Path]

Why This Matters:
- Using list[Path] suggests 0-N backups
- In reality, there's always 0 or 1 backup
- Type system should reflect reality
- Optional[Path] is clearer intent: "may or may not have backup"
- Simplifies code: No list indexing, direct None check

Example Impact:
# Current (confusing)
if result.files_backed_up:
    backup = result.files_backed_up[0]  # Why [0]? Could there be more?

# With Optional[Path] (clear)
if result.backup_path:
    backup = result.backup_path  # Obvious: single backup or None

Confidence: 82%
Priority: P2 (Should fix - improves code clarity)
```

**Impact**: Users understand the "why" and make informed decisions.

---

## Workflow Enhancements

### Feature-Dev Command Improvements

#### 7. Add "Light Mode" for Small Changes (Priority: HIGH)

**Problem**: 7-phase workflow is overkill for bug fixes or minor tweaks.

**Use Case**: Fix a typo, adjust a constant, add a log statement.

**Solution**: Add fast-track option:

```markdown
## Usage Modes

Feature-dev supports two modes:

### Full Mode (Default)
For new features or significant changes:
- All 7 phases
- Multiple agents
- Architecture design
- Comprehensive review

Usage: /feature-dev [description]

### Light Mode (Fast Track)
For bug fixes, minor tweaks, or simple changes:
- Skip Phase 2 (exploration)
- Skip Phase 4 (architecture)
- Streamlined review (single agent)

Usage: /feature-dev --light [description]

**When to use Light Mode**:
- Fixing a bug in existing code
- Adjusting configuration values
- Adding logging or error messages
- Refactoring single function
- Updating documentation

**When to use Full Mode**:
- Adding new features
- Modifying core architecture
- Integrating new libraries
- Complex refactoring
```

---

#### 8. Add File Context Tracking (Priority: HIGH)

**Problem**: Phase 2 finds important files, but Phase 5 must re-discover them.

**Real Issue I Experienced**:
- Explorer agents returned "list of 5-10 key files"
- I had to manually track those files
- By Phase 5, I forgot some of them
- Had to re-read agent outputs to find the files

**Solution**: Add context management:

```markdown
## Phase 2: Codebase Exploration (Enhanced)

**Actions**:
1. Launch 2-3 code-explorer agents in parallel
2. **After agents return**:
   - Collect all file paths mentioned
   - Create context file: .claude/context/feature-{name}-files.md
   - Save for reference in later phases

### Context File Format

    # Context: Feature {name}
    Generated: 2025-01-07

    ## Essential Files (From Exploration)

    ### Core Business Logic
    - src/core.py:78-136 - TemplateManager.install_templates()
    - src/utils.py:23-49 - get_project_path()

    ### UI Components
    - src/ui.py:33-69 - select_agent() interactive selection

    ### Configuration
    - src/config.py:8-23 - AGENT_CONFIG

    ## Architecture Insights
    - Pattern: Facade (TemplateManager hides complexity)
    - Layer: CLI -> Core -> Utils
    - Design: Dependency injection for Agent config

3. **Reference context in Phase 5**:
   - Read .claude/context/feature-{name}-files.md
   - Ensure all relevant files are still considered
   - Update context if new files discovered
```

**Impact**: No lost context between phases, more reliable implementation.

---

## Cross-Cutting Improvements

### 9. Add Examples to Every Agent (Priority: HIGH)

**Problem**: Agents have abstract instructions but no concrete examples.

**Better**: Add real examples from actual feature implementations:

```markdown
## Example Exploration: Authentication Feature

Suppose you're asked to explore authentication in a web app:

### Entry Points Found
- API Route: src/routes/auth.ts:23 - POST /api/login
- Middleware: src/middleware/auth.ts:45 - authenticateRequest()
- UI Component: src/components/LoginForm.tsx:12 - LoginForm component

### Execution Flow Traced
1. User submits login form (LoginForm.tsx:45)
2. POST request to /api/login (auth.ts:23)
3. loginHandler() validates credentials (auth.ts:67)
4. Calls AuthService.authenticate() (services/auth.ts:89)
5. Queries database (db/users.ts:34)
6. Generates JWT token (utils/jwt.ts:12)
7. Returns token to client

### Key Components
| Component | File | Responsibility |
|-----------|------|----------------|
| AuthService | services/auth.ts:23 | Business logic for auth |
| JWTUtil | utils/jwt.ts:8 | Token generation/validation |
| UserRepository | db/users.ts:15 | Database access |

### Architecture: Layered + Repository Pattern
- Presentation: Routes and controllers
- Business Logic: AuthService
- Data Access: UserRepository
- Utilities: JWT handling

### Files to Read
1. src/routes/auth.ts - API endpoints
2. src/services/auth.ts - Core auth logic
3. src/db/users.ts - User data access
4. src/utils/jwt.ts - Token handling
5. src/middleware/auth.ts - Request authentication
```

**Impact**: Agents produce higher-quality, more consistent output.

---

### 10. Add Self-Check Checklists (Priority: MEDIUM)

**Problem**: Agents don't validate their own work before returning.

**Solution**: Add validation checklist to each agent:

```markdown
## Self-Check Before Submitting

Before returning your analysis, verify:

### Code-Explorer Checklist
- [ ] Listed at least one clear entry point with file:line
- [ ] Traced execution flow through at least 3 steps
- [ ] Identified at least 2 key components
- [ ] Described at least one architectural pattern
- [ ] Provided 5-10 essential files to read
- [ ] All file paths are absolute and accurate
- [ ] All line numbers are correct (not approximate)

### Code-Architect Checklist
- [ ] Analyzed existing patterns from the codebase
- [ ] Made confident architectural choice (not just options)
- [ ] Specified exact files to create/modify
- [ ] Included component responsibilities
- [ ] Described data flow end-to-end
- [ ] Provided build sequence as checklist
- [ ] Addressed error handling strategy
- [ ] Considered testing approach
- [ ] Assessed risks and mitigations

### Code-Reviewer Checklist
- [ ] Only reported issues with confidence ≥80
- [ ] Provided file paths and line numbers for each issue
- [ ] Grouped issues by severity (P0, P1, P2, P3)
- [ ] Suggested concrete fixes (not just descriptions)
- [ ] Checked against CLAUDE.md if it exists
- [ ] Differentiated between bugs and style issues
- [ ] Provided "why this matters" context
```

**Impact**: Higher quality agent output, fewer mistakes.

---

## Template Organization Improvements

### 11. Add Template Categories (Priority: MEDIUM)

**Current**: All templates in flat structure.

**Better**: Organize by purpose:

```
templates/claude-code/
├── agents/
│   ├── analysis/
│   │   └── code-explorer.md
│   ├── design/
│   │   └── code-architect.md
│   └── quality/
│       └── code-reviewer.md
├── commands/
│   ├── workflows/
│   │   └── feature-dev.md
│   └── utilities/
│       └── quick-fix.md  (future)
└── README.md  (explains organization)
```

**Benefits**:
- Easier to find relevant agents
- Clear categorization
- Room for growth

---

### 12. Add Agent Capabilities Manifest (Priority: LOW)

**Problem**: No machine-readable way to know what agents can do.

**Solution**: Add manifest.json:

```json
{
  "version": "1.0.0",
  "agents": {
    "code-explorer": {
      "category": "analysis",
      "capabilities": ["trace-execution", "map-architecture", "find-patterns"],
      "best_for": ["understanding existing features", "finding similar code"],
      "not_for": ["designing new features", "reviewing code"],
      "model": "sonnet",
      "avg_duration_seconds": 120
    },
    "code-architect": {
      "category": "design",
      "capabilities": ["architecture-design", "pattern-matching", "blueprint-creation"],
      "best_for": ["designing features", "refactoring plans"],
      "not_for": ["quick fixes", "bug hunting"],
      "model": "sonnet",
      "avg_duration_seconds": 180
    },
    "code-reviewer": {
      "category": "quality",
      "capabilities": ["bug-detection", "code-quality", "convention-checking"],
      "best_for": ["pre-merge review", "finding bugs"],
      "not_for": ["architectural decisions", "feature design"],
      "model": "sonnet",
      "avg_duration_seconds": 90
    }
  },
  "commands": {
    "feature-dev": {
      "workflow_type": "comprehensive",
      "phases": 7,
      "agents_used": ["code-explorer", "code-architect", "code-reviewer"],
      "best_for": ["new features", "significant changes"],
      "estimated_duration": "30-120 minutes"
    }
  }
}
```

**Use Cases**:
- CLI could show capabilities: `devkit show-agents`
- Agents could self-coordinate better
- Documentation could be auto-generated

---

## Workflow-Specific Improvements

### 13. Feature-Dev: Add Progress Checkpoints (Priority: MEDIUM)

**Problem**: 7 phases can take hours, no way to pause/resume.

**Solution**:

```markdown
## Phase Checkpointing

At the end of each phase, save progress:

### After Phase 2 (Exploration)
Save to: .claude/sessions/feature-{name}/phase2-exploration.md
Contains:
- Exploration findings
- Files identified
- Patterns discovered

### After Phase 4 (Architecture)
Save to: .claude/sessions/feature-{name}/phase4-architecture.md
Contains:
- Chosen approach
- Architecture blueprint
- User's decision rationale

### Resume Feature Development
If session interrupted:
- /feature-dev --resume feature-{name}
- Reads saved progress
- Continues from last checkpoint
```

**Impact**: Users can pause long implementations, resume later.

---

### 14. Feature-Dev: Add Pre-Flight Checks (Priority: LOW)

**Problem**: No validation before starting Phase 5.

**Solution**:

```markdown
## Phase 5: Implementation

**Goal**: Build the feature

**DO NOT START WITHOUT USER APPROVAL**

### Pre-Flight Checklist

Before writing any code, verify:

- [ ] All questions from Phase 3 are answered
- [ ] User approved chosen architecture from Phase 4
- [ ] All essential files from Phase 2 are accessible
- [ ] Development environment is ready (tests passing, no uncommitted changes)
- [ ] You understand the build sequence from Phase 4

If any item is unchecked, stop and resolve before proceeding.

**Actions**:
1. Wait for explicit user approval
2. Run pre-flight checks
3. Read all relevant files identified in previous phases
4. Implement following chosen architecture
5. Update todos as you progress
```

---

## Summary: Template Improvement Priorities

### Must-Have for v1.1 (Next Release)

1. **Risk Assessment** in code-architect (prevents architectural regrets)
2. **Priority Framework** in code-reviewer (guides fix decisions)
3. **Output Templates** for consistency across agents
4. **Self-Check Checklists** to improve agent reliability

### Should-Have for v1.2

5. **Language-Specific Guidance** in code-explorer
6. **Automated Fix Suggestions** in code-reviewer
7. **Context Tracking** in feature-dev
8. **Light Mode** for quick changes

### Nice-to-Have for v2.0

9. **Template Metadata** with versioning
10. **Complexity Budgets** in architecture
11. **Progress Checkpointing** in feature-dev
12. **Agent Capabilities Manifest**

---

## Key Insight from Building DevKit

**The 7-phase workflow is excellent, but it assumes perfect execution.** In reality:
- Agents sometimes miss important files
- Architecture designs have blind spots
- Reviews find issues requiring redesign

**Missing**: Feedback loops, rollback strategies, and recovery paths.

The templates should be **defensive** - assume things will go wrong and provide clear guidance for recovery. This matches how real software development works: iterate, fail, learn, retry.
