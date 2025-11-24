---
name: research-paper-deep-dive
description: Transform academic research papers into verified, comprehensive, interactive documentation through multi-phase analysis and verification. Use this skill when users provide research paper URLs (especially from arxiv.org or direct PDFs) and request deep analysis, explanation, or documentation. The skill produces thoroughly verified markdown reports with diagrams, flowcharts, examples, and optional interactive web pages. Particularly effective for complex ML/AI papers, systems papers, and mathematical research requiring detailed pipeline explanations.
---

# Research Paper Deep Dive

## Overview

Transform academic research papers into verified, comprehensive documentation through a systematic 6-phase workflow. This skill combines deep analysis, multi-agent verification, and cross-validation to produce highly accurate reports with interactive web presentations.

**Outputs**:
- Verified markdown deep dive report (Should be concise and not cumbersome)
- Optional: Interactive web page for browsing

**Quality Guarantee**: 100%+ accuracy through multi-agent verification and cross-validation.

---

## When to Use This Skill

Trigger this skill when users:
- Provide an academic paper URL and ask for comprehensive analysis
- Request explanation of "how it works" with diagrams and examples
- Want to understand a complex paper's pipeline, methodology, or contributions
- Need verified documentation of research for presentations or teaching
- Ask for flowcharts, diagrams, and concrete examples
- Request interactive documentation of research papers

**Typical user requests**:
- "Deep dive on this paper and explain how it works"
- "Create comprehensive documentation with diagrams and examples"
- "Explain this paper's pipeline with flowcharts"
- "Analyze this paper and verify everything is accurate"

---

## Workflow: The 6-Phase Process

### PHASE 1: Setup & Paper Acquisition

**Objective**: Create organized workspace and download source material

**Steps**:
1. Create a dedicated folder for this research task:
   ```bash
   mkdir research_[paper_name]
   cd research_[paper_name]
   ```

2. Download the paper using the bundled script:
   ```bash
   bash [skill-path]/scripts/download_paper.sh [paper_url] . paper.pdf
   ```
   Or manually with curl if paper requires special handling.

3. Verify paper downloaded correctly:
   ```bash
   file paper.pdf  # Should show "PDF document"
   ```

**Deliverable**: `paper.pdf` in dedicated folder

---

### PHASE 2: Deep Dive Analysis & Report Creation

**Objective**: Create comprehensive markdown report explaining the research

**Use TodoWrite** to track this phase:
- [ ] Read and analyze paper
- [ ] Extract key information
- [ ] Create diagrams and flowcharts
- [ ] Write comprehensive report
- [ ] Verify structure completeness

#### 2.1: Read the Paper Thoroughly

Read the entire PDF using the Read tool:
```
Read: paper.pdf
```

Focus on:
- Abstract and introduction (what problem, why it matters)
- Methodology section (how it works, pipeline)
- Results section (what was discovered/achieved)
- Figures and tables (architecture diagrams, results)
- Discussion/conclusion (impact, limitations)
- Appendices (additional examples, detailed results)

#### 2.2: Extract Key Information

Systematically extract:
- **System/method name** and core purpose
- **Key innovation** (what's new vs. prior work)
- **Architecture components** (from figures)
- **Pipeline steps** (methodology section)
- **All numerical results** (with page references!)
- **Real-world applications** (if any)
- **Limitations** (from discussion)

#### 2.3: Create the Markdown Report

**CRITICAL**: Follow the structure in `references/report_structure_template.md`

**Required sections** (in order):
1. Executive Summary
2. What is [System Name]?
3. System Architecture (with diagrams!)
4. Key Innovations vs. [Predecessor]
5. Problems It Solves
6. Detailed Pipeline/Methodology
7. Concrete Example with User Workflow
8. Key Results & Impact
9. Technical Deep Dive
10. Ablation Studies (if present)
11. Limitations & Future Directions
12. Key Takeaways
13. References

**Writing Guidelines**:
- **Explanatory**: Explain WHY, not just WHAT
- **Concise**: No unnecessary words or jargon
- **Clear**: Build from simple to complex
- **Not Cumbersome**: Each section focused and purposeful

**Visual Requirements**:
- Minimum **5 ASCII diagrams**: architecture, pipeline, flow, etc.
- Each diagram must be clearly labeled
- Show data/control flow with arrows

**Example Requirements**:
- **ONLY use examples from the paper** - DO NOT fabricate
- If creating illustrative examples, add **[ILLUSTRATIVE - NOT FROM PAPER]** label
- Complete workflows showing full process
- Cite figure/section for each example

**Numerical Requirements**:
- **Every number** must have page reference
- Format: "23% kernel speedup (Section 3.3.2, p.16)"
- Double-check all numbers against paper

**Deliverable**: `[paper_name]_deep_dive.md` (3,000-5,000 words)

---

### PHASE 3: Multi-Agent Verification

**Objective**: Deploy 5 specialized agents to verify different aspects

**CRITICAL**: Use **TodoWrite** to track verification progress:
- [ ] Launch 5 verification agents in parallel
- [ ] Collect all agent reports
- [ ] Prepare for cross-verification

#### 3.1: Launch Verification Agents in Parallel

Deploy exactly **5 agents in a SINGLE message** using the Task tool:

**Agent 1: System Architecture & Pipeline**
```
Task(subagent_type="general-purpose",
     description="Verify system architecture",
     prompt="""
You are a system architecture verification agent.

READ:
1. [report_path] (sections 2-3: Architecture and Pipeline)
2. paper.pdf (Section 2, Figures 1-2, methodology)

VERIFY:
- Are core components accurately described?
- Is the pipeline accurate?
- Do ASCII diagrams match paper's figures?
- Are technical details (models, APIs) correct?

RETURN:
1. ✅ ACCURATE items with page references
2. ❌ ERRORS with corrections
3. 📝 CLARITY issues
4. ⚠️ MISSING details

Cite specific pages/figures.
""")
```

**Agent 2: Mathematical & Numerical**
```
Focus: All numbers, mathematical formulas, improvement claims, table data
Verify: Every numerical value matches paper exactly
```

**Agent 3: Code Examples & Implementation**
```
Focus: Code snippets, algorithms, pseudocode
Verify: All code is from paper (not fabricated)
Critical: Distinguish paper examples from illustrations
```

**Agent 4: Real-World Impact & Results**
```
Focus: Performance metrics, deployment claims, efficiency gains
Verify: Every percentage has exact paper reference
```

**Agent 5: Comparisons & Ablations**
```
Focus: Comparison tables, ablation studies, component importance
Critical: Ablations often lack exact percentages - check carefully
```

**See** `references/verification_checklist.md` for complete agent specifications.

#### 3.2: Collect Agent Reports

Each agent returns a detailed report. Save key findings:
- What's accurate
- What's incorrect
- What's missing
- What's unclear

**DO NOT** immediately trust agent conclusions - they require cross-verification!

**Deliverable**: 5 verification reports from agents

---

### PHASE 4: Cross-Verification (CRITICAL PHASE)

**Objective**: Main agent verifies each agent finding against actual paper

**CRITICAL REQUIREMENT**: Do NOT blindly accept agent conclusions. Verify each claim personally.

**Use TodoWrite** to track:
- [ ] Review each agent report
- [ ] Cross-verify critical findings
- [ ] Document confirmation/refutation
- [ ] Prepare correction list

#### 4.1: Systematic Cross-Verification

For **EACH issue** flagged by agents:

1. **Read the report section** mentioned
2. **Read the paper section** cited (exact page)
3. **Confirm or refute** the agent's finding
4. **Document**: Is the issue real? What's the fix?

**Example workflow**:
```
Agent claims: "Ablation section shows -40% which is not in paper"
↓
1. Read report Section 12 (ablation table)
2. Read paper Section 4 + Figure 8 (p.17-18)
3. Confirm: Figure 8 shows only curves, states "significant improvement"
4. Verdict: AGENT CORRECT - percentages are fabricated
5. Fix: Replace with qualitative terms
```

#### 4.2: Categorize Verified Issues

Priority classification:

**CRITICAL** (must fix):
- Fabricated content (examples not in paper)
- Wrong numbers (incorrect metrics/results)
- Misleading claims

**HIGH** (should fix):
- Missing important information
- Oversimplified without disclaimer
- Incorrect attributions

**MEDIUM** (nice to fix):
- Clarity improvements
- Minor terminology corrections
- Additional context

**LOW** (optional):
- Formatting improvements
- Style consistency

#### 4.3: Prepare Detailed Correction List

For each **verified** issue:
- Location (section, line numbers)
- What's wrong (specific problem)
- What it should be (with paper page reference)
- Priority (Critical/High/Medium/Low)

**Deliverable**: Cross-verified correction list with priorities

---

### PHASE 5: Report Refinement

**Objective**: Apply corrections to produce verified report

**Use TodoWrite** to track corrections:
- [ ] Fix critical issues (fabrications, wrong numbers)
- [ ] Fix high priority issues (missing info, oversimplifications)
- [ ] Fix medium priority issues (clarity, terminology)
- [ ] Validate all changes applied
- [ ] Final quality check

#### 5.1: Apply Corrections Systematically

**Order of corrections** (strict priority):

1. **Remove/replace all fabricated content**
   - Delete invented examples
   - Replace with paper-based examples
   - Add [ILLUSTRATIVE ONLY] labels where appropriate

2. **Fix all numerical errors**
   - Correct every wrong number
   - Add missing page references
   - Format: "Value (Section X.Y, p.ZZ)"

3. **Add disclaimers to oversimplifications**
   - Note when code is simplified
   - Reference paper figures for complete version
   - List what's omitted

4. **Add missing critical information**
   - Important technical details
   - Omitted results or applications
   - Missing context

5. **Improve clarity**
   - Simplify cumbersome explanations
   - Add helpful context
   - Improve diagrams

#### 5.2: Validation After Corrections

- [ ] Re-read entire report for consistency
- [ ] Verify all numbers still have page references
- [ ] Check no new errors introduced
- [ ] Ensure all agent issues addressed
- [ ] Verify report flows well

**Deliverable**: Refined report (100%+ accuracy)=

---

### PHASE 6: Interactive Web Page Creation (Optional)

**Objective**: Create browsable, rich interactive documentation

**When to execute**: If user requests "interactive" or "web page" or "browsable" documentation

#### 6.1: Convert Markdown to Interactive HTML

Use the `artifacts-builder` or `frontend-design` skill to create:

**Required features**:
- Collapsible sections for each report section
- If the deep dice report is too long, you don't have to include everything inside the web page, you can design on your decision to make it concise and clear to user to know about the main overview and workflow of it.
- Syntax-highlighted code blocks
- Responsive layout (mobile-friendly)
- Navigation sidebar with:
  - Table of contents
  - Progress tracking
  - Quick jump to sections
- Light/Dark mode toggle (light mode by default)
- Search functionality
- Print-friendly stylesheet

**Content structure**:
```html
<!-- Hero Section -->
- Paper title
- Authors
- Key achievement
- Visual abstract

<!-- Interactive Sections -->
- Each report section as collapsible card
- Diagrams rendered with proper formatting
- Code blocks with syntax highlighting
- Tables with sorting/filtering

<!-- Navigation -->
- Sticky sidebar
- Progress indicator
- Quick links
```

#### 6.2: Enhance with Interactivity

Add interactive elements:
- **Diagram zoom**: Click to enlarge
- **Code copy buttons**: One-click copy
- **Tooltip definitions**: Hover for term explanations
- **Comparison sliders**: Before/after visualizations
- **Accordion sections**: Collapsible details

#### 6.3: Polish & Deploy

- Test on different screen sizes
- Verify all links work
- Check print stylesheet
- Optimize load time
- Generate standalone HTML file

**Deliverable**: Single HTML file or web application

---

## Skill Usage Patterns

### Pattern 1: Quick Analysis (Phases 1-2 only)
```
User: "Analyze this paper: https://arxiv.org/pdf/XXX"
→ Execute Phases 1-2 only
→ Deliver markdown report
```

### Pattern 2: Verified Analysis (Phases 1-5)
```
User: "Deep dive with verification on this paper: URL"
→ Execute all 5 phases
→ Deliver verified report + verification summary
```

### Pattern 3: Complete Package (All 6 phases)
```
User: "Create interactive documentation for this paper: URL"
→ Execute all 6 phases
→ Deliver verified report + web page
```

---

## Critical Requirements

### MUST DO:
✅ Follow phases in strict order (no skipping without reason)
✅ Use TodoWrite to track each phase
✅ Verify EVERY number against paper (with page reference)
✅ Launch verification agents in PARALLEL (single message, 5 agents)
✅ Cross-verify agent findings personally (don't blindly trust)
✅ Use examples from paper (or label as illustrative)
✅ Add page references to all major claims

---

## Quality Standards

### Accuracy Targets:
- Mathematical results: **100%** (every number verified)
- Impact metrics: **100%** (all percentages verified)
- System architecture: **100%+** (all components correct)
- Overall accuracy: **100%+**

### Writing Standards:
- **Explanatory**: Focus on WHY and HOW
- **Concise**: Remove unnecessary words
- **Progressive**: Simple concepts before complex
- **Accessible**: Avoid jargon, define terms
- **Structured**: Clear sections, logical flow

### Visual Standards:
- **Diagrams** required
- ASCII format for markdown compatibility
- Clear labels on all components
- Arrows showing flow direction
- Legend when needed

---

## Phase-by-Phase Checklist

### Phase 1: Setup ✓
- [ ] Folder created
- [ ] Paper downloaded
- [ ] Paper verified (is valid PDF)

### Phase 2: Analysis ✓
- [ ] Paper fully read
- [ ] Key info extracted
- [ ] Report written (13+ sections)
- [ ] 5+ diagrams included
- [ ] All numbers have page refs
- [ ] Examples from paper only

### Phase 3: Verification ✓
- [ ] 5 agents deployed in parallel
- [ ] All agent reports received
- [ ] Key findings documented

### Phase 4: Cross-Verification ✓
- [ ] Each agent claim verified personally
- [ ] Paper sections checked
- [ ] Issues confirmed/refuted
- [ ] Correction list prepared

### Phase 5: Refinement ✓
- [ ] Critical issues fixed
- [ ] Numbers corrected
- [ ] Disclaimers added
- [ ] Missing info added
- [ ] Verification summary created

### Phase 6: Web Page ✓ (Optional)
- [ ] HTML created
- [ ] Interactivity added
- [ ] Responsive design
- [ ] All content renders correctly

---

## Resources

### scripts/download_paper.sh
Bash script to download papers from URLs (supports arxiv and direct PDFs).

**Usage**:
```bash
bash scripts/download_paper.sh <paper-url> <output-dir> [filename]
```

### references/report_structure_template.md
Complete template showing required sections, content guidelines, length targets, and quality standards.

**When to use**: Reference when writing Phase 2 report to ensure all required sections included.

### references/verification_checklist.md
Comprehensive checklist for verification phases including:
- Agent specifications for all 5 verification agents
- Cross-verification methodology
- Common verification failures
- Quality assurance checklist

**When to use**: Reference in Phases 3-5 for verification workflow.

### assets/
Directory for interactive web page templates (Phase 6).

---

## Tips for Effectiveness

1. **Start with TodoWrite**: Track all 6 phases for transparency
2. **Read paper completely**: Don't skip appendices - they contain details
3. **Reference the template**: Use `report_structure_template.md` as guide
4. **Parallel agent deployment**: All 5 agents in single message for speed
5. **Don't trust agents**: Phase 4 cross-verification is essential
6. **Page references**: Add them as you write, not afterward
7. **Diagram first**: Create diagrams early, build text around them
8. **Examples matter**: Concrete examples make abstract concepts clear
9. **Iterate carefully**: Each correction should fix, not break
10. **Verify the verification**: Double-check your own corrections

---

## Example Usage

### User Request:
```
"Can you give a deep dive on this paper: https://arxiv.org/pdf/2506.13131
Explain the pipeline, how it works, what problems it solves, with diagrams
and examples. Make sure it's verified and accurate."
```

### Claude's Workflow:
```
Phase 1: Setup
- Create folder: research_alphaevolve/
- Download paper.pdf
✓ Paper acquired

Phase 2: Analysis
- Read 44-page paper thoroughly
- Extract: AlphaEvolve = evolutionary coding agent
- Create report with 15 sections, 7+ diagrams
- Include matrix multiplication example from paper
✓ alphaevolve_deep_dive.md created

Phase 3: Verification
- Deploy 5 agents in parallel
- Collect reports:
  * Architecture: 95% accurate, missing async details
  * Mathematics: 100% accurate
  * Code: Found fabricated sorting example
  * Impact: 100% accurate
  * Comparisons: Found fabricated ablation percentages
✓ 5 verification reports received

Phase 4: Cross-Verification
- Verify sorting claim: Searched PDF - CONFIRMED not in paper
- Verify ablation %: Checked Figure 8 - CONFIRMED no percentages
- Verify all numbers: CONFIRMED all accurate
✓ All findings cross-verified

Phase 5: Refinement
- Remove fabricated sorting section
- Replace ablation percentages with qualitative terms
- Add disclaimers to simplified code
- Expand mathematical discoveries from 4 to 13
- Add missing technical details
✓ Report refined to 98% accuracy

Phase 6: Web Page (if requested)
- Create interactive HTML
- Add collapsible sections
- Implement dark mode
- Add search functionality
✓ Interactive documentation complete
```

**Deliverables**:
1. `alphaevolve_deep_dive.md` - Verified comprehensive report
2. `alphaevolve_interactive.html` - Interactive web page

---

## Skill Maintenance

When updating this skill:
1. Test on different paper types (ML, systems, theory, applied)
2. Refine agent prompts based on common failure modes
3. Update report template with new best practices
4. Enhance web template with better interactivity
5. Add examples of excellent reports as references

---

## Related Skills

This skill works well with:
- **pdf** skill - For PDF manipulation and extraction
- **artifacts-builder** skill - For creating interactive web artifacts
- **frontend-design** skill - For polished web page design
- **document-skills:docx** - For creating presentation-ready documents
