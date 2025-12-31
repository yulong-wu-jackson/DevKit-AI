---
description: Refine a task into well-structured ticket(s), splitting complex tasks into ordered sequences
argument-hint: [task-description or path/to/existing-ticket.md]
allowed-tools: "*"
---

<!--
Ticket Refinement Workflow
- Transforms vague tasks into actionable, well-specified tickets
- Automatically splits complex tasks into ordered ticket sequences
- Creates tickets in .spec-dev/tickets/ with sequential numbering
- Can refine existing tickets in workspace or create new from external files
-->

You are guiding the user through a structured ticket refinement process. Follow all phases completely - do not skip any phase.

**Input:** $ARGUMENTS

---

## Phase 1: Understand the Task

**Goal:** Deeply understand the task and relevant codebase context.

**Actions:**

1. **Parse input:** Determine if `$ARGUMENTS` is:
   - A task description (text explaining what needs to be done)
   - A path to an existing ticket file (ends in `.md`)

2. **If existing ticket file provided:**
   - Read the file content
   - Extract the core task/goal from it
   - Note any existing specifications to preserve

3. **Deep analysis:**
   - Think deeply about what this task entails
   - Identify the scope, goals, and expected outcomes
   - Consider potential challenges and dependencies

4. **Codebase exploration:**
   Use the Task tool with `subagent_type: "Explore"` to understand:
   - Relevant existing code patterns and conventions
   - Files and modules that will be affected
   - Related implementations to reference
   - Architectural context and constraints

   Ask the explore agent to trace through code flows relevant to the task.
   You MUST read and trace through the files that the subagents identified your self, and dive deep on your own if needed, to get accurate information.

5. **Synthesize understanding:**
   - Summarize your understanding of the task
   - List the key areas of the codebase involved
   - Identify integration points and dependencies

6. **Assess complexity for multi-ticket splitting:**
   Evaluate if the task should be split into multiple ordered tickets. Consider:
   - Can it be broken into distinct, sequential phases?
   - Are there natural boundaries (e.g., data model → API → UI)?
   - Would a single ticket be too large to implement in one session?
   - Are there hard dependencies where one part must complete before another?

   **If splitting is clearly warranted**, draft a preliminary breakdown:
   - Identify reasonable logical sub-tickets
   - Define the implementation order and dependencies
   - Note what each sub-ticket would cover

   This will be confirmed with the user in Phase 2.

---

## Phase 2: Clarifying Questions

**Goal:** Resolve all ambiguities before creating the ticket specification.

**Actions:**

1. **Confirm multi-ticket split (if applicable):**
   If you identified in Phase 1 that the task should be split into multiple tickets:
   - Present your recommended breakdown to the user
   - Use `AskUserQuestion` to confirm:
     - First option: Your recommended split with brief rationale
     - User can accept, modify, or choose single ticket

2. **Identify underspecified aspects:** Consider gaps in:
   - Edge cases and error handling
   - Integration points with existing code
   - Scope boundaries
   - Design preferences and patterns to follow
   - Backward compatibility requirements
   - Performance considerations
   - Testing requirements
   - User experience details
   - Any other task-specific concerns

3. **Formulate questions:** For each ambiguity:
   - Use the `AskUserQuestion` tool
   - Provide your best recommendation as the first option based on:
     - Task requirements
     - Codebase patterns discovered in Phase 1
     - Best practices
   - The user can select your recommendation or provide their own answer

4. **Question format:** Each question should:
   - Be specific and actionable
   - Include context for why it matters
   - Offer only ONE well-reasoned default recommendation

5. **Iterate if needed:** If user answers reveal new ambiguities, ask follow-up questions.

6. **Document decisions:** Track all clarifications for the ticket(s).

---

## Phase 3: Draft Ticket File

**Goal:** Create well-structured, actionable ticket specification.

**Actions:**

1. **Determine ticket location and naming:**

   Check if `.spec-dev/tickets/` exists:
   ```
   !`ls -la .spec-dev/tickets/ 2>/dev/null || echo "DIRECTORY_NOT_FOUND"`
   ```

   If directory doesn't exist, create it:
   ```
   !`mkdir -p .spec-dev/tickets/`
   ```

   Get next ticket number:
   ```
   !`ls .spec-dev/tickets/ 2>/dev/null | grep -E '^ticket_[0-9]+' | sed 's/ticket_\([0-9]*\).*/\1/' | sort -n | tail -1 || echo "0"`
   ```

   Increment to get next number (pad to 3 digits).

2. **Handle existing tickets:**
   - If input was a ticket file FROM `.spec-dev/tickets/`: Update in-place
   - If input was a ticket file from ELSEWHERE: Create new ticket, keep original

3. **Generate filename:**
   Format: `ticket_NNN_brief-slug.md`
   - NNN = zero-padded sequential number (001, 002, etc.)
   - brief-slug = kebab-case summary (30 letters max)
   - Example: `ticket_003_add-user-auth.md`

4. **Write ticket content:**

   Example structure (adapt sections structure as needed for the specific task):

   ```markdown
   # [Concise Task Title]

   **Created:** [YYYY-MM-DD HH:MM]
   **Status:** Draft


   ## Overview
   [1-2 sentence summary of what needs to be done and why]

   ## Context
   [Relevant codebase context discovered during exploration]
   - Key files: [list relevant files]
   - Patterns to follow: [conventions from codebase]
   - Dependencies: [related modules/systems]

   ## Requirements
   [Clear, actionable requirements derived from task + clarifications]
   - [ ] Requirement 1
   - [ ] Requirement 2
   - ...

   ## Design Decisions
   [Decisions made during clarification, with rationale]
   - **[Topic]:** [Decision] — [Brief rationale]

   ## Scope
   **In scope:**
   - [What this ticket covers]

   **Out of scope:**
   - [What this ticket explicitly does NOT cover]

   ## Technical Notes
   [Any technical details, constraints, or implementation hints]

   ## Acceptance Criteria
   [How to verify the task is complete]
   - [ ] Criterion 1
   - [ ] Criterion 2
   ```

   The structure may varies and should adaptive to specific codebase and tasks.

5. **Content guidelines:**
   - Be concise but include necessary details
   - Use clear, actionable language
   - Preserve all clarification decisions
   - Make it readable and scannable for human
   - Adapt structure to fit the specific task (remove unused sections)

---

## Phase 4: Summary

**Goal:** Provide clear next steps to the user.

**Actions:**

1. **Confirm creation:** State what was created/updated:
   - Ticket file path
   - Brief summary of each ticket's content

2. **Display key points:**
   - 2-3 bullet summary of the refined task(s)
   - Key decisions made during clarification

3. **Inform the user:**

   > Ticket saved to: `.spec-dev/tickets/[filename]`
   >
   > To implement this ticket, you may open a new session (to preserve context) and run:
   > ```
   > /spec-dev:implement-ticket .spec-dev/tickets/[filename]
   > ```

4. **Stop here:** Do NOT proceed with implementation unless the user explicitly asks you to continue in this session.

---

## Important Notes

- **Do not skip phases.** Each phase builds on the previous one.
- **Ask questions proactively.** Better to clarify upfront than assume incorrectly.
- **Adapt the ticket structure.** Remove sections that don't apply; add sections if needed.
- **Keep tickets focused.** One ticket = one coherent unit of work.
- **Split large tasks.** If a task clearly spans multiple domains or phases, create ordered tickets.
- **Respect existing work.** When refining existing tickets, preserve valuable context.
- **Document dependencies.** For multi-ticket sequences, clearly indicate order and blockers.