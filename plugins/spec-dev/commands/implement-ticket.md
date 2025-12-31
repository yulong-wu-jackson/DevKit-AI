---
description: Implement a task or ticket with exploration, coding, testing, review, and summary phases
argument-hint: [task-description or path/to/ticket.md]
allowed-tools: "*"
---

<!--
Ticket Implementation Workflow
- Accepts task description text OR path to ticket file
- Phases: Understand → Clarify → Implement → Review → Refine → Summary
- Invokes code-reviewer subagent for code changes
- Uses Task/Explore for non-code verification
- Does not stage/commit unless explicitly requested
-->

You are implementing a task following a structured 6-phase workflow. **You must complete every phase - do not skip any phase.**

**Input:** $ARGUMENTS

---

## Phase 1: Understand the Task

**Goal:** Deeply understand the task and explore relevant codebase context.

**Actions:**

1. **Parse input:** Determine if `$ARGUMENTS` is:
   - A task description (text explaining what needs to be done)
   - A path to a ticket file (ends in `.md`)

2. **If ticket file provided:**
   - Read the file content
   - Extract the requirements, context, and acceptance criteria
   - Note the scope boundaries (in-scope vs out-of-scope)

3. **Deep analysis:**
   - Think deeply about what this task entails
   - Identify the scope, goals, and expected outcomes
   - Consider potential challenges and edge cases

4. **Codebase exploration:**
   Use the Task tool with `subagent_type: "general-purpose"` with sonnet model to understand:
   - Relevant existing code patterns and conventions
   - Files and modules that will be affected
   - Related implementations to reference
   - Architectural context and constraints

   Ask the subagent to trace through code flows relevant to the task.
   **You MUST read and trace through the files that the subagent identifies yourself**, diving deeper as needed to get accurate information.

5. **Synthesize understanding:**
   - Summarize your understanding of the task
   - List the key areas of the codebase involved
   - Identify dependencies and integration points
   - Confirm you understand what "done" looks like

**Output:** Clear understanding of task, codebase context, and implementation approach.

---

## Phase 2: Clarifying Questions

**Goal:** Resolve ambiguities before implementing.

**Actions:**

1. **Identify gaps:** Based on Phase 1, note any unclear aspects:
   - Design decisions not specified in the task
   - Multiple valid approaches where user preference matters
   - Edge cases or error handling not defined
   - Any other task-specific concerns

2. **Ask if needed:** Use `AskUserQuestion` for critical ambiguities:
   - Provide your recommended approach as the first and only option based on: Task requirements / Codebase discovered / Best practices
   - Keep questions focused and actionable
   - Skip this if the task is fully specified

3. **Document decisions:** Note any clarifications for reference during implementation.

**Output:** All ambiguities resolved, ready to implement.

---

## Phase 3: Implementation

**Goal:** Implement accurate, DRY, elegant, and functionally correct code.

**Principles:**
- Write clean, readable code that follows existing patterns
- Implement exactly what's needed, nothing more
- Prefer editing existing files over creating new ones

**Actions:**

1. **Plan the implementation:**
   - Identify the files to create or modify
   - Determine the order of changes
   - Consider how to test the implementation

2. **Implement the changes:**
   - Write code that is accurate, DRY, and elegant
   - Only add necessary comments (for example: basic function docstrings)
   - Avoid over-engineering or adding features beyond the task scope

3. **Create tests if needed:**
   - Write tests for new functionality when appropriate
   - Run the project's test suite to verify tests pass
   - **Tests must pass before proceeding to Phase 4**
   - If tests fail, fix the issues before continuing

4. **Self-verification:**
   - Verify the implementation meets the requirements
   - Check that no unnecessary changes were introduced
   - Try out the code yourself, ensure the code compiles/runs without errors

**Important constraints:**
- Do NOT add unnecessary comments or docstrings to unchanged code
- Do NOT refactor code outside the task scope
- Do NOT stage, add, commit, or push any code during implementation
- Focus solely on completing this specific task

**Output:** Working implementation with passing tests (if applicable).

---

## Phase 4: Quality Review

**Goal:** Verify the implementation through independent review.

**Actions:**

1. **Determine review type:**
   - If implementation involved **code creation or editing** → You MUST Use spec-dev:code-reviewer agent
   - If implementation was **non-code** (docs, config, etc.) → Use Task/Explore for verification

2. **For code changes - invoke code-reviewer subagent:**

   Use the Task tool to launch the `spec-dev:code-reviewer` agent with:
   - The original task description and ticket file path (You MUST provide the ticket file path if exist and you must let the subagent to confirm the changes fulfill the goal and Acceptance Criteria in the ticket file)
   - Current date for reference
   - Instruction to review unstaged changes (`git diff`)

   Example prompt for the subagent:
   ```
   Review the code changes for this task:

   Original requirement: [task description / ticket path]
   Date: [current date]

   Review the unstaged changes from `git diff`. Verify:
   - Implementation aligns with the requirements
   - No bugs, security issues, or logic errors
   - Code follows project conventions
   - No missing requirements from the task
   ```

3. **For non-code changes - use Task/Explore:**

   Use the Task tool with `subagent_type: "Explore"` to verify:
   - Changes are correct and complete
   - Documentation is accurate
   - Configuration is valid
   - No unintended side effects

4. **Wait for review results:**
   - The subagent will return findings with confidence scores
   - Only issues with confidence ≥ 80 are reported
   - Review will be grouped by severity (Critical vs Important)

**Output:** Review results from the appropriate subagent.

---

## Phase 5: Refine and Improve

**Goal:** Critically evaluate review feedback and apply appropriate fixes.

**Actions:**

1. **Review the subagent findings:**
   - Read through all reported issues
   - Note the confidence scores and severity levels

2. **Critical evaluation:**
   **Do NOT take the review results as granted.** For each finding, you should find it in the real codebase yourself:
   - Is this actually a real issue for this specific task?
   - Is the suggested fix appropriate for this codebase?
   - Does fixing this align with the original requirements?
   - Could the fix introduce new problems?

3. **Prioritize and decide:**
   - **Critical issues:** Must fix (security, crashes, data corruption)
   - **Important issues:** Should fix if clearly valid
   - **Minor issues:** Fix only if clearly beneficial
   - **False positives:** Skip with brief reasoning

4. **Apply fixes:**
   - Fix issues you've validated as genuine problems
   - Maintain code consistency while fixing
   - Re-run tests after fixes to ensure nothing broke

5. **Document decisions:**
   - Note which suggestions were applied
   - Note which were skipped and why (briefly)

**Output:** Refined implementation with validated fixes applied.

---

## Phase 6: Summary

**Goal:** Provide a clear, concise summary of what was accomplished.

**Actions:**

1. **Summarize the implementation:**
   Provide a well-structured summary including:
   - **Task completed:** Brief description of what was implemented
   - **Files changed:** List of created/modified files
   - **Key decisions:** Any notable implementation choices made
   - **Tests:** Status of tests (passed/created/N/A)
   - **Review notes:** Summary of review findings and actions taken

2. **Format for readability:**
   - Use clear headings and bullet points
   - Keep it concise but complete
   - Make it easy for the user to understand what changed
   - Make it human readable and human scannable

3. **Suggest next steps:**

   > **Changes ready for commit.**
   >
   > To stage and commit these changes:
   > 1. Review the changes: `git diff`
   > 2. Stage the files: `git add <files>`
   > 3. Generate commit message: `/commit-msg`
   >
   > Note: I have not staged or committed any changes. Please review before committing.

**Output:** Human-readable summary with clear next steps.

---

## Important Notes

- **Complete all phases.** Each phase builds on the previous one.
- **Stay focused.** Only implement what the task requires - no extra features or refactoring.
- **Be critical.** Review feedback is guidance, not gospel. Apply your judgment.
- **No git operations.** Do not stage, commit, or push unless the user explicitly requests it.
- **Test thoroughly.** Ensure tests pass before moving to review phase.
