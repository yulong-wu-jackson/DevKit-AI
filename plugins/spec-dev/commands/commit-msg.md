---
description: Write a conventional commit message for staged changes
allowed-tools: Bash(git diff:*), Bash(git status:*), Bash(git log:*), Bash(git branch:*), Read
---

## Context

Staged changes summary:
!`git diff --staged --stat`

Files changed:
!`git diff --staged --name-only`

Recent commit style reference:
!`git log --oneline -5`

Current git diff (staged and unstaged changes):
!`git diff HEAD`

Current branch:
!`git branch --show-current`

---

## Instructions

Analyze the staged changes above and write a conventional commit message.

### 1. Categorize Changes

Group the changed files by type:
- **Code**: *.py, *.js, *.ts, *.go, *.rs, *.java, etc.
- **Documentation**: README*, *.md, docs/
- **Configuration**: *.json, *.yaml, *.toml, pyproject.toml, package.json
- **Tests**: test_*.py, *_test.go, *.test.js, *.spec.ts

### 2. Handle Large Diffs

If the staged diff is very large (many files or >10K lines):
1. Focus on **file names and structure** to understand scope
2. Use the Read tool on key changed files to understand intent
3. Prioritize understanding code changes over documentation changes

### 3. Write the Commit Message

**Format:** `<type>(<scope>): <subject>`

Appends a ! after the type/scope if introducing a breaking change

**Types** (priority order):
- `feat`: New feature or significant enhancement
- `fix`: Bug fix
- `refactor`: Code restructuring without behavior change
- `docs`: Documentation only
- `style`: Formatting, UI/UX improvements
- `test`: Adding or updating tests
- `chore`: Maintenance, dependencies, config

**Guidelines:**
- Subject line: Under 80 characters, imperative mood ("add" not "added")
- Ask: "What would a developer looking at this commit be most interested in?"
- Optional body: Explain WHAT changed and WHY (not HOW)
- For multi-faceted commits: Primary change in subject, others in body
- Focus on user/developer impact, not implementation details

---

## Output

Provide **only** the commit message(s) following the conventional commit regulations below, ready to copy-paste. No other text.

**Normal version:**
- First line: type(scope): subject
- Blank line + bullet points for significant details

**Concise version:**
- First line: type(scope): subject
- (Optional) blank line + bullet points for significant details
