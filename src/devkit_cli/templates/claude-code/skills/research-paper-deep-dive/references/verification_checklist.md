# Verification Checklist for Research Paper Deep Dive Reports

## Phase 1: Multi-Agent Verification

Deploy 5 specialized verification agents in parallel to verify different aspects:

### Agent 1: System Architecture & Pipeline Verification

**Focus Areas**:
- [ ] Verify all core components are accurately described
- [ ] Check pipeline steps match paper's methodology
- [ ] Verify ASCII diagrams match paper's figures
- [ ] Check technical details (models, formats, APIs)
- [ ] Verify component interactions

**Report Requirements**:
- List accurate items with page references
- List errors found with corrections
- Note clarity issues
- List missing details from paper

### Agent 2: Mathematical & Numerical Verification

**Focus Areas**:
- [ ] Verify every numerical claim (exact values)
- [ ] Check all mathematical formulas and bounds
- [ ] Verify improvement claims (before → after)
- [ ] Check percentage claims and metrics
- [ ] Verify table data if summarized

**Critical**: Every number must match paper exactly.

**Report Requirements**:
- Verify each number with page/table reference
- Flag any numerical errors
- Assess clarity of mathematical explanations
- Note missing mathematical details

### Agent 3: Code Examples & Implementation Verification

**Focus Areas**:
- [ ] Verify code snippets match paper
- [ ] Check algorithm pseudocode accuracy
- [ ] Verify example code is from paper (not fabricated)
- [ ] Check syntax and format correctness
- [ ] Verify programming language claims

**Critical**: Distinguish between paper examples and illustrative examples.

**Report Requirements**:
- Verify code matches paper figures
- Flag fabricated or incorrect code
- Assess clarity of code examples
- Note missing implementation details

### Agent 4: Real-World Impact & Results Verification

**Focus Areas**:
- [ ] Verify all performance metrics (percentages)
- [ ] Check deployment/application claims
- [ ] Verify time savings or efficiency gains
- [ ] Check real-world use cases
- [ ] Verify comparison with baselines

**Critical**: Every percentage must have exact paper reference.

**Report Requirements**:
- Verify each metric with section/page
- Flag incorrect numbers
- Assess clarity of impact explanations
- Note missing applications

### Agent 5: Comparisons & Ablations Verification

**Focus Areas**:
- [ ] Verify comparison tables (vs other systems)
- [ ] Check ablation study results
- [ ] Verify component importance claims
- [ ] Check related work accuracy
- [ ] Verify any performance degradation numbers

**Critical**: Ablation results often lack exact percentages - use qualitative terms unless paper provides specific values.

**Report Requirements**:
- Verify comparisons with paper tables
- Flag fabricated percentages
- Assess clarity of comparisons
- Note missing comparative data

---

## Phase 2: Cross-Verification by Main Agent

After receiving all 5 agent reports, the main agent MUST:

### Step 1: Validate Agent Findings

For EACH issue flagged by agents:
- [ ] Read the specific section in the report
- [ ] Read the corresponding section in the paper (exact page)
- [ ] Confirm or refute the agent's finding
- [ ] Document the cross-verification result

**DO NOT** blindly trust agent conclusions. Verify personally.

### Step 2: Prioritize Issues

Categorize verified issues:
- [ ] **Critical**: Fabricated content, wrong numbers
- [ ] **High**: Missing important information, misleading claims
- [ ] **Medium**: Clarity issues, minor inaccuracies
- [ ] **Low**: Formatting, style improvements

### Step 3: Prepare Correction List

For each verified issue:
- [ ] Exact location in report (line numbers)
- [ ] What is wrong
- [ ] What it should be (with paper reference)
- [ ] Priority level

---

## Phase 3: Report Refinement

### Correction Execution

Apply corrections in priority order:

1. **Remove all fabricated content**
   - [ ] Delete sections not based on paper
   - [ ] Add disclaimers to illustrative examples
   - [ ] Replace invented examples with paper-based ones

2. **Fix all numerical errors**
   - [ ] Correct every wrong number
   - [ ] Add page references to all numbers
   - [ ] Replace vague claims with specific citations

3. **Add missing information**
   - [ ] Include important omitted details
   - [ ] Reference all relevant appendices
   - [ ] Add technical depth where needed

4. **Improve clarity**
   - [ ] Simplify cumbersome explanations
   - [ ] Add context where needed
   - [ ] Improve diagram labels

### Validation After Corrections

- [ ] Re-read entire report for flow
- [ ] Verify all edits were applied correctly
- [ ] Check no new errors introduced
- [ ] Ensure page references present

---

## Quality Assurance Checklist

### Numerical Accuracy
- [ ] Every percentage has page reference
- [ ] Every mathematical bound verified
- [ ] All performance metrics match paper
- [ ] All improvement claims accurate
- [ ] Table data matches paper tables

### Content Authenticity
- [ ] No fabricated examples
- [ ] All code from paper or clearly labeled
- [ ] No invented ablation percentages
- [ ] All workflows based on paper
- [ ] No speculative claims

### Completeness
- [ ] All major contributions covered
- [ ] All applications mentioned
- [ ] All key results included
- [ ] Limitations discussed
- [ ] Future work noted

### Citations & References
- [ ] Every section has page references
- [ ] All figures cited
- [ ] All tables cited
- [ ] Appendices referenced
- [ ] Supplementary materials linked

### Visual Quality
- [ ] Minimum 5 diagrams present
- [ ] Diagrams are clear and labeled
- [ ] Flow arrows show direction
- [ ] ASCII format renders correctly
- [ ] Examples have visual components

### Readability
- [ ] Clear section structure
- [ ] Progressive complexity
- [ ] No unnecessary jargon
- [ ] Concrete before abstract
- [ ] Examples support concepts

---

## Common Verification Failures

### Type 1: Fabricated Numbers
**Problem**: Ablation studies show "No X: -40% performance"
**Check**: Does Figure/Table provide this exact percentage?
**Fix**: Use qualitative terms ("substantial degradation") unless exact number in paper

### Type 2: Invented Examples
**Problem**: "User wants to optimize sorting..."
**Check**: Does paper mention this application?
**Fix**: Remove or replace with actual paper example, or add [ILLUSTRATIVE ONLY] label

### Type 3: Wrong Metrics
**Problem**: "20% improvement in accuracy"
**Check**: What does paper actually report? (might be 23%, might be different metric)
**Fix**: Correct number and add page reference

### Type 4: Oversimplified Code
**Problem**: Shows 10-line pseudocode for 200-line implementation
**Check**: Does paper show more complex version in figures?
**Fix**: Add disclaimer noting actual complexity + reference to paper figures

### Type 5: Missing Context
**Problem**: "Uses evolutionary algorithm"
**Check**: Does paper specify which one? (e.g., MAP-Elites + island-based)
**Fix**: Add specific algorithm names from paper

---

## Verification Success Criteria

A report passes verification when:

✅ **100% numerical accuracy** - Every number matches paper
✅ **Zero fabricated content** - All examples from paper
✅ **Complete coverage** - All major contributions included
✅ **Full citations** - Every claim has page reference
✅ **Clear disclaimers** - Simplifications and illustrations labeled
✅ **Quality diagrams** - Minimum 5 clear visual aids
✅ **Readable flow** - Builds understanding progressively

---

## Agent Prompt Templates

### Template for Verification Agents

```
You are a [SPECIALIZATION] verification agent. Your task is to verify the accuracy of [SPECIFIC ASPECT].

READ these files:
1. [REPORT PATH] (focus on sections [X-Y]: [TOPIC])
2. [PAPER PATH] (focus on [SECTIONS/FIGURES])

VERIFY:
- [Specific check 1]
- [Specific check 2]
- [Specific check 3]
...

RETURN a detailed report with:
1. ✅ ACCURATE items - list what's correct with page references
2. ❌ ERRORS found - any inaccuracies with corrections
3. 📝 CLARITY issues - anything confusing or unclear
4. ⚠️ MISSING details - important information from paper not included

Be thorough and cite specific sections/pages from the paper.
```

Use this template for each of the 5 verification agents, customizing the specialization and focus areas.
