---
description: Write a conventional commit message for staged changes
---

# Write Commit Message

Analyze the staged changes and write a conventional commit message.

## Instructions

### 1. Analyze the Changes

Run `git diff --staged` and categorize changes by type:
- **Code changes**: *.py, *.js, *.ts, *.go, etc.
- **Documentation**: README, *.md, docs/
- **Configuration**: *.json, *.yaml, *.toml, pyproject.toml
- **Tests**: test_*.py, *.test.js, etc.

### 2. Identify Primary Changes

For commits with multiple change types, determine the PRIMARY change:
- **Code changes take priority** over documentation
- **Features/fixes take priority** over refactoring/chores
- **Breaking changes take highest priority**

If you're unsure, ask yourself: "What would a developer looking at this commit be most interested in?"

### 3. Handle Large Diffs

If `git diff --staged` is very large (>10K lines):
1. Focus on **file names and structure** first
2. Read key changed files directly (Read tool) to understand intent
3. Don't get lost in documentation changes - identify code changes first

### 4. Write the Commit Message

Format: `<type>(<scope>): <subject>`

**Types** (in priority order):
- `feat`: New feature or significant enhancement
- `fix`: Bug fix
- `refactor`: Code restructuring without behavior change
- `docs`: Documentation only
- `style`: Formatting, UI/UX improvements
- `test`: Adding or updating tests
- `chore`: Maintenance, dependencies, config

**Guidelines:**
- Subject line: Under 80 characters, imperative mood
- Optional body: Explain WHAT changed and WHY (not HOW)
- For multi-faceted commits: Mention primary change in subject, others in body
- Focus on **user/developer impact**, not implementation details

## Output

Provide the commit message ready to commit:
- First line: type and subject (concise)
- Optional: blank line + bullet points for details
- Be specific enough to understand the change, but concise enough to scan, should not be cumbersome