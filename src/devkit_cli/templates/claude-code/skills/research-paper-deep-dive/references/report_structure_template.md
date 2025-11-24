# Research Paper Deep Dive Report - Structure Template

## Required Sections

A comprehensive deep dive report MAY include these sections, the sections can be dynamic in topics and length depends on the realistic scenario:

### 1. Executive Summary (Required)
- **Purpose**: 2-3 paragraph overview of the paper
- **Content**:
  - What the paper presents
  - Key innovation/contribution
  - Main achievement/result in one sentence
- **Length**: ~150-200 words

### 2. What is [System Name]? (Required)
- **Purpose**: Explain what the system/method is
- **Content**:
  - Core purpose (3-5 bullet points)
  - Main innovation compared to prior work
- **Length**: ~200-300 words

### 3. System Architecture (Required)
- **Purpose**: Visual and textual explanation of components
- **Content**:
  - High-level architecture diagram (ASCII)
  - Core components diagram (ASCII)
  - Component descriptions (2-3 sentences each)
- **Requirements**: At least 2 ASCII diagrams

### 4. Key Innovations (Required if applicable)
- **Purpose**: Compare with predecessor/baseline
- **Content**:
  - Comparison table with 5-8 dimensions
  - What's improved and why it matters
- **Format**: Markdown table

### 5. Problems It Solves (Required)
- **Purpose**: Categorize application domains
- **Content**:
  - 3-5 categories of problems
  - Specific examples in each category
  - Real-world applications
- **Length**: ~300-400 words

### 6. Detailed Pipeline/Methodology (Required)
- **Purpose**: Step-by-step explanation of how it works
- **Content**:
  - Each major step with description
  - Data flow between steps
  - ASCII flowchart showing the process
  - Technical details (algorithms, hyperparameters)
- **Length**: ~500-800 words
- **Requirements**: Detailed flowchart

### 7. Concrete Example with User Workflow (Required)
- **Purpose**: Show end-to-end example from user perspective
- **Content**:
  - User provides input (specific example from paper)
  - System processes step-by-step
  - Shows intermediate outputs
  - Final result
  - Timeline/progression if evolutionary/iterative
- **Length**: ~400-600 words
- **Requirements**: Must be based on actual example from paper (NOT fabricated)

### 8. Key Results & Impact (Required)
- **Purpose**: Highlight main findings and real-world impact
- **Content**:
  - Quantitative results (with page references)
  - Comparison with baselines
  - Real-world deployment impact (if any)
- **Format**: Tables and bullet points
- **Critical**: ALL numbers must be verified against paper

### 9. Technical Deep Dive (Required)
- **Purpose**: Explain sophisticated technical details
- **Content**:
  - Advanced techniques used
  - Implementation details
  - Hyperparameters, configuration
  - Why certain design choices matter
- **Length**: ~400-600 words

### 10. Ablation Studies (If present in paper)
- **Purpose**: Show what makes the system work
- **Content**:
  - Components tested
  - Impact of removing each component
  - Conclusions from ablations
- **Critical**: Use ONLY qualitative terms unless paper provides exact percentages

### 11. Limitations & Future Directions (Required)
- **Purpose**: Honest assessment of constraints
- **Content**:
  - Current limitations (from paper's discussion)
  - Future research directions
  - Potential extensions
- **Length**: ~200-300 words

### 12. Key Takeaways (Required)
- **Purpose**: Distill insights for different audiences
- **Content**:
  - For researchers
  - For practitioners
  - For the field
- **Length**: ~200-300 words

### 13. References (Required)
- **Purpose**: Proper attribution
- **Content**:
  - Paper citation (arxiv ID, authors, date)
  - Supplementary materials links
  - Related work mentioned

---

## Quality Guidelines

### Writing Style:
- **Explanatory**: Explain WHY, not just WHAT
- **Concise**: No unnecessary jargon or filler
- **Clear**: Progressive disclosure - simple to complex
- **Not Cumbersome**: Each section focused and purposeful

### Technical Accuracy:
- **Every number** must have page reference
- **Every claim** must be verifiable in paper
- **No fabrication** - only use examples from paper
- **No speculation** - stick to what paper says

### Visual Elements:
- **Minimum 5 diagrams**: Architecture, pipeline, flow, etc.
- **ASCII format**: Works in markdown
- **Clear labels**: Every component labeled
- **Arrows show flow**: Data/control flow visible

### Examples:
- **Must be from paper**: No invented examples
- **Complete workflows**: Show full process end-to-end
- **Specific details**: Actual parameters, actual results
- **Page references**: Cite figures/sections

---

## Common Pitfalls to Avoid

1. ❌ **Fabricating examples** - Only use examples from the paper
2. ❌ **Missing page references** - Every claim needs citation
3. ❌ **Vague ablation results** - Don't invent percentages
4. ❌ **Too technical** - Balance depth with accessibility
5. ❌ **Missing diagrams** - Visual aids are essential
6. ❌ **Incomplete workflows** - Examples must show full process
7. ❌ **No verification** - Always verify numbers against source
8. ❌ **Copying paper text** - Synthesize and explain, don't copy
