---
description: Create a well-structured, human-readable Product Requirements Document through deep research and iterative refinement
argument-hint: [product-idea or feature-description]
allowed-tools: "*"
---

<!--
PRD Creation Workflow
- Transforms product ideas into comprehensive, scannable PRDs
- Deep research phase using knowledge and web search
- Iterative clarification to resolve ambiguities
- Creates PRD in .spec-dev/product_requirement_document/
- Subagent quality review for scannability and actionability
-->

You are guiding the user through a structured Product Requirements Document (PRD) creation process. Follow all phases completely - do not skip any phase.

**Input:** $ARGUMENTS

---

## Phase 1: Deep Understanding

**Goal:** Ultrathink and deeply understand what the user wants to build.

**Actions:**

1. **Parse and analyze input:**
   - What is the core product or feature being described?
   - What problem does it solve?
   - Who is the intended user/customer?
   - What is the business context?

2. **Think deeply about the product vision:**
   - What does "success" look like for this product?
   - What are the implicit assumptions in the request?
   - What adjacent problems might need addressing?
   - What makes this product unique or valuable?

3. **Extract key elements:**
   - Core value proposition
   - Primary user journey
   - Must-have vs nice-to-have signals
   - Constraints mentioned or implied

4. **Identify knowledge gaps:**
   - What domain knowledge is needed?
   - What industry context matters?
   - What technical landscape should inform the design?
   - What competitive or market context is relevant?

**Output:** Clear mental model of the product vision and identified research areas.

---

## Phase 2: Deep Research

**Goal:** Conduct comprehensive research to inform PRD decisions.

**Actions:**

1. **Leverage internal knowledge:**
   - Best practices for this type of product
   - Common pitfalls and how to avoid them
   - Industry standards and conventions
   - Relevant design patterns and approaches

2. **Web research for current context:**
   Use the `WebSearch`,`WebFetch` tools to research:
   - Current market landscape and competitors
   - Recent trends in the relevant domain
   - User expectations and pain points in this space
   - Technical considerations and modern approaches
   - Regulatory or compliance requirements (if applicable)

   Perform **2-4 targeted searches** based on the knowledge gaps identified in Phase 1.

3. **Synthesize research findings:**
   - Key insights that should influence requirements
   - Risks or challenges to address
   - Opportunities to differentiate
   - Technical or design decisions informed by research

4. **If codebase context is relevant:**
   Invoke a subagent with sonnet model to explore:
   - Existing architecture and patterns
   - Integration points and constraints
   - Related implementations to reference

   Read the relevant files yourself to validate findings.

**Output:** Research summary with actionable insights for the PRD.

---

## Phase 3: Clarifying Questions

**Goal:** Resolve all critical ambiguities before drafting.

**Actions:**

1. **Identify underspecified aspects:**
   Based on Phases 1-2, note gaps in:
   - Target user definition and personas
   - Scope boundaries (what's in/out)
   - Success metrics and KPIs
   - Priority and must-have vs nice-to-have features
   - Technical constraints or preferences
   - Timeline or delivery expectations
   - Integration requirements
   - Any domain-specific concerns

2. **Formulate strategic questions:**
   For each critical ambiguity, use `AskUserQuestion`:
   - Provide **one well-reasoned recommendation** as the first option based on:
     - Your understanding from Phase 1
     - Research insights from Phase 2
     - Best practices
   - Keep questions focused and actionable
   - Group related questions when possible (max 4 per call)

3. **Question format:**
   Each question should:
   - Be specific and consequential
   - Include context for why it matters
   - Offer your recommended approach first
   - Let user select recommendation or provide custom answer

4. **Iterate if needed:**
   If user answers reveal new ambiguities, ask follow-up questions.
   Continue until all critical decisions are resolved.

5. **Skip if fully specified:**
   If the input is comprehensive and research confirms clarity, proceed to Phase 4.

**Output:** All critical decisions documented, ready to draft.

---

## Phase 4: Draft the PRD

**Goal:** Create a well-structured, human-readable, scannable PRD document.

**Actions:**

1. **Ensure directory exists:**
   ```
   !`mkdir -p .spec-dev/product_requirement_document/`
   ```

2. **Determine filename:**
   Format: `prd-[brief-slug].md`
   - brief-slug = kebab-case summary (30 characters max)
   - Example: `prd-user-authentication.md`

3. **Check for existing PRD:**
   ```
   !`ls .spec-dev/product_requirement_document/ 2>/dev/null | grep -E '^prd-' || echo "NO_EXISTING_PRDS"`
   ```

   If a PRD with the same or similar slug exists:
   - Use `AskUserQuestion` to ask the user whether to:
     - **Update existing** — Revise and overwrite the current PRD
     - **Create new version** — Save as `prd-[slug]-v2.md` (or next version number)
     - **Use different name** — Choose a new slug entirely

   This prevents accidental data loss from overwriting existing work.

5. **Apply PRD design principles:**

   **Scannability:**
   - Use clear visual hierarchy (H1 > H2 > H3)
   - Keep paragraphs short (2-3 sentences max)
   - Use bullet points for lists
   - Bold key terms and decisions
   - Use tables for comparative information

   **Readability:**
   - Write in clear, concise language
   - Avoid jargon unless defined
   - Use active voice
   - Lead with the most important information

   **Actionability:**
   - Make requirements specific and testable
   - Include acceptance criteria
   - Define success metrics clearly
   - Specify priorities explicitly

6. **Write PRD content:**

   Use an adaptive structure based on the product. Core sections include:

   ```markdown
   # [Product Name] — Product Requirements Document

   **Version:** 1.0
   **Created:** [YYYY-MM-DD]
   **Status:** Draft

   ---

   ## Executive Summary

   [MAX 2-3 sentences: What is this product? What problem does it solve? Why now?]

   ---

   ## Problem Statement

   ### The Problem
   [Clear articulation of the problem being solved]

   ### Impact
   [Why this problem matters - quantify if possible]

   ### Current State
   [How users currently handle this / what exists today]

   ---

   ## Goals & Success Metrics

   ### Primary Goals
   - [ ] Goal 1: [Specific, measurable outcome]
   - [ ] Goal 2: [Specific, measurable outcome]

   ### Success Metrics (KPIs)
   | Metric | Target | Measurement Method |
   |--------|--------|-------------------|
   | [Metric name] | [Target value] | [How measured] |

   ### Non-Goals
   - [What this product explicitly does NOT aim to do]

   ---

   ## Target Users

   ### Primary Persona
   **[Persona Name]** — [One-line description]
   - **Who:** [Demographics/role]
   - **Needs:** [Key needs relevant to this product]
   - **Pain points:** [Current frustrations]
   - **Success looks like:** [What they want to achieve]

   ### Secondary Personas
   [Brief descriptions if applicable]

   ---

   ## Requirements

   ### Must Have (P0)
   - [ ] **[Requirement]** — [Brief rationale]
     - Acceptance: [How to verify it's done]

   ### Should Have (P1)
   - [ ] **[Requirement]** — [Brief rationale]

   ### Nice to Have (P2)
   - [ ] **[Requirement]** — [Brief rationale]

   ---

   ## User Experience

   ### Key User Flows
   1. **[Flow name]:** [Step-by-step journey]

   ### UX Principles
   - [Principle 1]
   - [Principle 2]

   ---

   ## Technical Considerations

   ### Architecture Notes
   [High-level technical approach]

   ### Constraints
   - [Technical constraint 1]
   - [Technical constraint 2]

   ### Dependencies
   - [External dependency 1]
   - [Internal dependency 1]

   ---

   ## Scope & Boundaries

   ### In Scope
   - [What IS included in this release]

   ### Out of Scope
   - [What is explicitly EXCLUDED]

   ### Future Considerations
   - [Items for future releases]

   ---

   ## Risks & Mitigations

   | Risk | Likelihood | Impact | Mitigation |
   |------|------------|--------|------------|
   | [Risk] | High/Med/Low | High/Med/Low | [Strategy] |

   ---

   ## Open Questions
   - [ ] [Question that still needs resolution]

   ---

   ## Appendix

   ### Research References
   - [Source 1]
   - [Source 2]

   ### Design Decisions Log
   | Decision | Rationale | Date |
   |----------|-----------|------|
   | [Decision] | [Why] | [Date] |
   ```

7. **Adapt structure as needed:**
   - Remove sections that don't apply
   - Add domain-specific sections if needed
   - Adjust depth based on product complexity
   - Keep the document focused and scannable

**Output:** Complete PRD draft saved to `.spec-dev/product_requirement_document/`.

---

## Phase 5: Quality Review

**Goal:** Ensure the PRD is well-designed, human-readable, scannable, and actionable.

**Actions:**

1. **Invoke opus subagent for review:**

   Use the Task tool with model `opus` to review the PRD:

   ```
   Review this PRD for quality. Evaluate:

   **Scannability (Can a reader quickly find what they need?)**
   - Clear visual hierarchy
   - Effective use of headings, bullets, tables
   - Key information is prominent
   - Document flows logically

   **Readability (Is it easy to understand?)**
   - Clear, concise language
   - No unnecessary jargon
   - Consistent terminology
   - Appropriate level of detail

   **Actionability (Can teams execute from this?)**
   - Requirements are specific and testable
   - Success metrics are measurable
   - Priorities are clear
   - Scope boundaries are defined

   **Completeness (Are critical elements present?)**
   - Problem is well-articulated
   - Users are clearly defined
   - Requirements cover key scenarios
   - Risks are identified

   Provide specific, actionable feedback. Rate each dimension 1-5.
   Suggest concrete improvements for any dimension scoring below 4.
   ```

2. **Apply review feedback:**
   - Address critical issues immediately
   - Improve scannability if flagged
   - Clarify ambiguous requirements
   - Fill any identified gaps

3. **Re-save if modified:**
   Update the PRD file with improvements.

**Output:** Reviewed and refined PRD document.

---

## Phase 6: Summary

**Goal:** Provide a concise summary and next steps.

**Actions:**

1. **Confirm creation:**
   State what was created:
   - PRD file path
   - Product name and scope

2. **Brief summary (3-5 bullets):**
   - Core problem being solved
   - Target users
   - Key requirements (top 3)
   - Critical success metrics
   - Notable decisions made

3. **Inform the user:**

   > **PRD saved to:** `.spec-dev/product_requirement_document/[filename]`
   >
   > **Next steps:**
   > - Review the PRD and refine as needed
   > - Share with stakeholders for feedback
   > - To create implementation tickets from this PRD:
   >   ```
   >   /spec-dev:refine-ticket [specific feature from PRD]
   >   ```

4. **Stop here:** Do NOT proceed with implementation unless explicitly requested.

---

## PRD Design Principles Reference

When creating PRDs, apply these principles:

### Visual Hierarchy
- **H1:** Product title only
- **H2:** Major sections (Problem, Goals, Requirements, etc.)
- **H3:** Subsections within major sections
- Use **bold** for key terms and decisions
- Use *italics* sparingly for emphasis

### Scannability Techniques
- Lead with summary/executive overview
- Use bullet points, not paragraphs, for lists
- Tables for comparative or structured data
- Checkboxes for actionable items
- Clear section breaks with horizontal rules

### Content Guidelines
- One idea per paragraph
- Active voice ("Users can..." not "It is possible for users to...")
- Specific over vague ("Load in <2 seconds" not "Load quickly")
- Quantify when possible
- Define acronyms on first use

### Document Length
- Aim for comprehensive but focused
- Use appendix for detailed specs that interrupt flow

---

## Important Notes

- **Do not skip phases.** Each phase builds on the previous one.
- **Research thoroughly.** A well-researched PRD prevents costly pivots later.
- **Ask strategic questions.** Better to clarify upfront than assume incorrectly.
- **Prioritize scannability.** Busy stakeholders will skim before reading.
- **Keep it living.** PRDs should evolve as understanding deepens.
- **Adapt the structure.** Add or remove sections based on product needs.
- **Focus on "why".** Requirements should explain rationale, not just features.
