# Interactive Research Paper Documentation - Design Guide

## Overview

Create **distinctive, production-grade interactive web pages** for research paper deep dives that are:
- Visually striking and memorable
- Highly functional and accessible
- Content-rich with smooth navigation
- Unique to the paper's subject matter

**CRITICAL**: This is NOT a generic documentation page. Design a unique aesthetic that matches the paper's domain and character.

---

## Phase 6 Implementation Checklist

When creating the interactive web page:

### Step 1: Choose Bold Aesthetic Direction ⭐

**BEFORE writing any code**, commit to a distinctive aesthetic based on the paper's subject:

#### For AI/ML Papers (like AlphaEvolve):
**Potential Directions**:
- **Algorithmic Brutalism**: Monospace everything, ASCII art backgrounds, terminal aesthetics, stark contrasts
- **Futuristic Lab**: Glowing accents, dark backgrounds, cyan/magenta highlights, neural network patterns
- **Data Visualization**: Chart-inspired design, graph paper grids, infographic style
- **Evolutionary Organic**: Natural curves, growth animations, tree/network visualizations
- **Retro Computer**: 80s terminal green on black, pixel fonts, CRT scanline effects

#### For Mathematics Papers:
**Potential Directions**:
- **Theorem Elegance**: Serif fonts, classical proportions, margin notes, proof-like structure
- **Geometric Precision**: Perfect grids, ruler lines, compass circles, drafting aesthetics
- **Blackboard Academic**: Chalk-style typography, dark slate backgrounds, handwritten annotations
- **Modern Mathematical**: Clean sans-serif, equation-focused, generous whitespace
- **Playful Abstract**: Colorful geometric shapes, animated diagrams, visual proofs

#### For Systems Papers:
**Potential Directions**:
- **Architecture Blueprint**: Technical drawing style, blueprint blue, engineering aesthetics
- **Network Topology**: Node-link diagrams, connection animations, infrastructure themes
- **Performance Dashboard**: Metrics-focused, speedometer gauges, real-time data aesthetics
- **Industrial Minimal**: Gray scale, precise alignment, technical specifications
- **Neon Cyberpunk**: Dark with vibrant highlights, glitch effects, digital themes

**Choose ONE direction and commit fully.** Bold execution beats safe mediocrity.

### Step 2: Typography Selection

**NEVER use**: Inter, Roboto, Arial, system fonts, or other overused choices

**BOLD CHOICES** (pick combinations):

**Display Fonts** (for headings):
- **Geometric/Modern**: Space Mono, JetBrains Mono, IBM Plex Mono, Azeret Mono
- **Distinctive Sans**: Archivo Black, Work Sans Bold, Outfit, Syne, Cabinet Grotesk
- **Classical**: Playfair Display, Crimson Pro, Spectral, Fraunces
- **Unique**: Syne, Epilogue, Darker Grotesque, Anybody, Manrope

**Body Fonts** (for content):
- **Readable Mono**: JetBrains Mono, Fira Code, Source Code Pro, Commit Mono
- **Refined Sans**: Synonym, Satoshi, General Sans, Plus Jakarta Sans
- **Classical Serif**: Lora, Merriweather, Source Serif Pro, Newsreader
- **Technical**: IBM Plex Sans, Red Hat Text, Manrope, DM Sans

**Pair thoughtfully**: Mono display + Serif body (unexpected), or Bold display + Light mono body (contrast)

**Load via Google Fonts**:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
```

### Step 3: Color Palette & Theme

**AVOID**: Purple gradients on white, generic blue, default grays

**BOLD PALETTES** (based on aesthetic direction):

#### Algorithmic Brutalism
```css
--bg-primary: #0a0a0a;
--bg-secondary: #1a1a1a;
--text-primary: #00ff00;
--text-secondary: #00cc00;
--accent: #ff00ff;
--border: #333333;
```

#### Futuristic Lab
```css
--bg-primary: #0d1117;
--bg-secondary: #161b22;
--text-primary: #c9d1d9;
--text-secondary: #8b949e;
--accent-cyan: #00e5ff;
--accent-magenta: #ff006e;
--glow: rgba(0, 229, 255, 0.4);
```

#### Theorem Elegance
```css
--bg-primary: #faf8f5;
--bg-secondary: #f5f2ed;
--text-primary: #2d2d2d;
--text-secondary: #666666;
--accent: #8b4513;
--border: #d4c5b9;
```

#### Geometric Precision
```css
--bg-primary: #ffffff;
--bg-secondary: #f8f9fa;
--text-primary: #000000;
--text-secondary: #666666;
--accent: #0066cc;
--grid: #e0e0e0;
```

**Create depth with theme**:
- Use 3-4 background layers (primary, secondary, tertiary, elevated)
- Accent colors should be bold and used sparingly
- Consider dark/light mode toggle

### Step 4: Layout Architecture

**AVOID**: Generic centered container with default padding

**DISTINCTIVE LAYOUTS**:

#### Option 1: Asymmetric Sidebar
```
┌─────────────────────────────────────┐
│  SIDEBAR (25%)  │  CONTENT (75%)    │
│                 │                   │
│  [Navigation]   │  [Hero Section]   │
│  [Progress]     │                   │
│  [TOC]          │  [Content Cards]  │
│  [Search]       │                   │
│                 │  [Diagrams]       │
│  [Sticky]       │                   │
│                 │  [Scrollable]     │
└─────────────────────────────────────┘
```

#### Option 2: Magazine Layout
```
┌─────────────────────────────────────┐
│      [FULL-WIDTH HERO]              │
├─────────────────────────────────────┤
│  [Left Content]  │  [Right Sidebar] │
│   (2 columns)    │   [TOC/Nav]      │
│                  │   [Metadata]     │
│  [Wide Section - Full Width]        │
│                                     │
│  [3 Column Grid for Results]        │
└─────────────────────────────────────┘
```

#### Option 3: Scroll-Driven Narrative
```
┌─────────────────────────────────────┐
│  [Floating Nav - Top Right]         │
│                                     │
│  [Full-Width Sections]              │
│  Each section = full viewport       │
│  Scroll-triggered reveals           │
│  Diagrams animate in                │
│  Parallax effects                   │
└─────────────────────────────────────┘
```

#### Option 4: Grid-Based Modular
```
┌───────┬───────┬───────┬───────┐
│ Title │ Title │ Meta  │ Nav   │
├───────┴───────┼───────┴───────┤
│  Architecture │  Key Results  │
│  (2 cols)     │  (2 cols)     │
├───────────────┴───────────────┤
│  Pipeline Flow (Full Width)   │
├─────────┬─────────┬───────────┤
│ Example │ Diagram │ Code      │
└─────────┴─────────┴───────────┘
```

Choose based on content volume and aesthetic direction.

---

## Required Functional Components

### 1. Hero Section (Required)

**Purpose**: Immediate visual impact + paper overview

**Must include**:
- Paper title (large, bold, distinctive typography)
- Authors (subtle, secondary typography)
- Key achievement (highlighted, attention-grabbing)
- Visual element (abstract visualization, key diagram, or animated accent)
- Scroll indicator (animate to encourage exploration)

**Example Structure**:
```html
<section class="hero">
  <div class="hero-background">
    <!-- Animated background: circuit patterns, math symbols, or abstract -->
  </div>
  <div class="hero-content">
    <h1 class="hero-title">AlphaEvolve</h1>
    <p class="hero-subtitle">A Coding Agent for Scientific Discovery</p>
    <div class="hero-highlight">
      <span class="achievement-badge">First improvement in 56 years</span>
      <p class="achievement-text">4×4 matrix multiplication using 48 scalar multiplications</p>
    </div>
    <div class="scroll-indicator">↓</div>
  </div>
</section>
```

**Aesthetic Requirements**:
- Full viewport height
- Distinctive background (NOT solid color)
- Bold typography hierarchy
- Entrance animation (fade + slide)
- Smooth scroll transition to content

### 2. Navigation Sidebar (Required)

**Purpose**: Easy navigation and progress tracking

**Must include**:
- Table of contents with section links
- Visual progress indicator
- Scroll-spy highlighting current section
- Search functionality
- Quick actions (download, print, share)

**Technical Implementation**:
```javascript
// Sticky sidebar with scroll-spy
const observeIntersection = () => {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Update active nav link
        navLinks.forEach(link => link.classList.remove('active'));
        document.querySelector(`[href="#${entry.target.id}"]`)
          ?.classList.add('active');

        // Update progress bar
        updateProgress(entry.target);
      }
    });
  }, { threshold: 0.5 });

  sections.forEach(section => observer.observe(section));
};
```

**Design Requirements**:
- Sticky positioning
- Smooth scroll behavior
- Active state clearly visible
- Progress visualization (bar, circle, or creative)
- Collapse on mobile

### 3. Content Sections (Required)

**Purpose**: Organize report content in digestible, interactive cards

**Each section must have**:
- Clear heading with anchor link
- Collapsible/expandable state (optional, based on aesthetic)
- Smooth transitions
- Visual hierarchy
- Syntax-highlighted code blocks
- Properly formatted diagrams

**Section Card Structure**:
```html
<section id="architecture" class="content-section">
  <div class="section-header">
    <h2>System Architecture</h2>
    <button class="collapse-toggle">−</button>
  </div>
  <div class="section-content">
    <div class="section-intro">
      <p>AlphaEvolve orchestrates four core components...</p>
    </div>
    <div class="diagram-container">
      <pre class="ascii-diagram">
        <!-- ASCII diagram with proper formatting -->
      </pre>
    </div>
    <div class="section-details">
      <!-- Additional content -->
    </div>
  </div>
</section>
```

**Interaction Requirements**:
- Smooth collapse/expand (300ms transition)
- Deep-linkable (URL hash navigation)
- Print-friendly (auto-expand all)
- Mobile-responsive

### 4. Code Block Display (Critical)

**Purpose**: Beautiful, functional code presentation

**Requirements**:
- Syntax highlighting (use Prism.js or highlight.js)
- Copy-to-clipboard button
- Line numbers (optional, based on aesthetic)
- Language indicator
- Theme-matched colors

**Implementation**:
```html
<div class="code-block">
  <div class="code-header">
    <span class="language-label">Python</span>
    <button class="copy-button" onclick="copyCode(this)">
      <svg><!-- copy icon --></svg>
      Copy
    </button>
  </div>
  <pre><code class="language-python">
def alpha_evolve_score(required, free):
    cpu_residual = required.cpu / free.cpu
    mem_residual = required.mem / free.mem
    return -1.0 * (cpu_residual + mem_residual + ...)
  </code></pre>
</div>
```

**Styling Requirements**:
- Rounded corners OR sharp edges (commit to one)
- Background distinct from page background
- Monospace font (matching overall aesthetic)
- Hover effects on copy button
- Success state after copying

### 5. Diagram Rendering (Required)

**Purpose**: Present ASCII/visual diagrams beautifully

**Requirements**:
- Preserve ASCII formatting (monospace, exact spacing)
- Add visual enhancement (backgrounds, borders, shadows)
- Zoom functionality for complex diagrams
- Mobile-friendly scrolling for wide diagrams

**Enhanced ASCII Display**:
```css
.ascii-diagram {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  line-height: 1.4;
  background: var(--diagram-bg);
  padding: 2rem;
  border-radius: 12px;
  border: 2px solid var(--diagram-border);
  overflow-x: auto;
  position: relative;

  /* Add subtle glow for futuristic themes */
  box-shadow: 0 0 20px rgba(var(--accent-rgb), 0.1);
}

.ascii-diagram::before {
  content: "ARCHITECTURE DIAGRAM";
  position: absolute;
  top: 0.5rem;
  right: 1rem;
  font-size: 0.7rem;
  letter-spacing: 2px;
  opacity: 0.5;
}
```

**Interaction**:
- Click to zoom (fullscreen overlay)
- Keyboard navigation (ESC to close)
- Pinch-zoom on mobile

### 6. Search Functionality (Required)

**Purpose**: Quick navigation to specific content

**Implementation**:
```javascript
const implementSearch = () => {
  const searchInput = document.getElementById('search');
  const sections = document.querySelectorAll('.content-section');

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();

    sections.forEach(section => {
      const text = section.textContent.toLowerCase();
      const matches = text.includes(query);

      // Highlight matches
      if (matches && query.length > 2) {
        section.classList.add('search-match');
        highlightText(section, query);
      } else {
        section.classList.remove('search-match');
        removeHighlights(section);
      }
    });
  });
};
```

**Features**:
- Instant search (no delay)
- Highlight matches in content
- Jump to first match
- Clear search button
- Keyboard shortcuts (Cmd/Ctrl + K)

### 7. Dark/Light Mode Toggle (Recommended)

**Purpose**: User preference + aesthetic flexibility

**Implementation**:
```javascript
const initThemeToggle = () => {
  const toggle = document.getElementById('theme-toggle');
  const root = document.documentElement;

  // Load saved preference
  const savedTheme = localStorage.getItem('theme') || 'dark';
  root.setAttribute('data-theme', savedTheme);

  toggle.addEventListener('click', () => {
    const current = root.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';

    root.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);

    // Smooth transition
    root.style.transition = 'background-color 0.3s, color 0.3s';
  });
};
```

**Design Requirements**:
- Smooth transition (300ms)
- Toggle button visually distinctive
- Both themes fully designed (not just inverted colors)
- System preference detection

---

## Animation & Interaction Patterns

### Entrance Animations (On Load)

**Hero Section**:
```css
@keyframes heroFadeIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero-title {
  animation: heroFadeIn 0.8s ease-out;
}

.hero-subtitle {
  animation: heroFadeIn 0.8s ease-out 0.2s backwards;
}

.hero-highlight {
  animation: heroFadeIn 0.8s ease-out 0.4s backwards;
}
```

**Staggered Section Reveals**:
```css
.content-section {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.content-section.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger by index */
.content-section:nth-child(1) { transition-delay: 0s; }
.content-section:nth-child(2) { transition-delay: 0.1s; }
.content-section:nth-child(3) { transition-delay: 0.2s; }
```

### Scroll-Triggered Animations

```javascript
const observeScrollReveal = () => {
  const sections = document.querySelectorAll('.content-section');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.1 });

  sections.forEach(section => revealObserver.observe(section));
};
```

### Micro-Interactions

**Hover States**:
```css
.nav-link {
  position: relative;
  transition: color 0.3s;
}

.nav-link::before {
  content: '';
  position: absolute;
  left: -10px;
  height: 100%;
  width: 2px;
  background: var(--accent);
  transform: scaleY(0);
  transition: transform 0.3s;
}

.nav-link:hover::before,
.nav-link.active::before {
  transform: scaleY(1);
}
```

**Interactive Diagrams**:
```css
.diagram-container {
  position: relative;
  cursor: zoom-in;
  transition: transform 0.3s;
}

.diagram-container:hover {
  transform: scale(1.02);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}
```

---

## Background & Visual Effects

**CRITICAL**: Create atmosphere, not blandness

### Pattern 1: Animated Grid (Technical Papers)
```css
.page-background {
  background-image:
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 50px 50px;
  background-position: 0 0;
  animation: gridScroll 20s linear infinite;
}

@keyframes gridScroll {
  to { background-position: 50px 50px; }
}
```

### Pattern 2: Noise Texture (Modern Papers)
```css
.hero-background::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,..."); /* Noise SVG */
  opacity: 0.05;
  mix-blend-mode: overlay;
}
```

### Pattern 3: Gradient Mesh (Abstract/Creative)
```css
.page-background {
  background:
    radial-gradient(at 20% 30%, rgba(0, 229, 255, 0.15) 0, transparent 50%),
    radial-gradient(at 80% 70%, rgba(255, 0, 110, 0.15) 0, transparent 50%),
    radial-gradient(at 50% 50%, rgba(100, 200, 255, 0.1) 0, transparent 60%),
    var(--bg-primary);
  background-attachment: fixed;
}
```

### Pattern 4: Geometric Patterns (Math Papers)
```css
.section-background {
  background-image:
    repeating-linear-gradient(45deg, transparent, transparent 35px,
                              rgba(var(--accent-rgb), 0.03) 35px,
                              rgba(var(--accent-rgb), 0.03) 70px);
}
```

---

## Component Specifications

### Section Card Design

**Basic Structure**:
```html
<div class="content-card">
  <div class="card-accent"></div> <!-- Colored edge -->
  <div class="card-content">
    <h3 class="card-title">
      <span class="section-number">01</span>
      What is AlphaEvolve?
    </h3>
    <div class="card-body">
      <!-- Content -->
    </div>
  </div>
</div>
```

**Styling Options**:

**Option A: Elevated Cards** (Refined aesthetic)
```css
.content-card {
  background: var(--card-bg);
  border-radius: 16px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow:
    0 1px 3px rgba(0, 0, 0, 0.05),
    0 10px 30px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow:
    0 4px 6px rgba(0, 0, 0, 0.07),
    0 20px 50px rgba(0, 0, 0, 0.12);
}
```

**Option B: Flat with Borders** (Brutalist aesthetic)
```css
.content-card {
  background: transparent;
  border: 2px solid var(--border);
  border-left: 4px solid var(--accent);
  padding: 1.5rem;
  margin-bottom: 1rem;
  transition: border-color 0.3s;
}

.content-card:hover {
  border-left-width: 8px;
}
```

### Results Table Design

**For displaying paper results** (like Table 2):

```html
<div class="results-table-container">
  <table class="results-table">
    <thead>
      <tr>
        <th>Configuration</th>
        <th>Best Known</th>
        <th>AlphaEvolve</th>
        <th>Improvement</th>
      </tr>
    </thead>
    <tbody>
      <tr class="highlight-row">
        <td><code>⟨4,4,4⟩</code></td>
        <td>49</td>
        <td class="result-highlight">48</td>
        <td class="improvement">+1 ✓</td>
      </tr>
    </tbody>
  </table>
</div>
```

**Styling**:
```css
.results-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
}

.results-table th {
  background: var(--table-header-bg);
  padding: 1rem;
  text-align: left;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  font-size: 0.75rem;
  border-bottom: 2px solid var(--accent);
}

.results-table td {
  padding: 0.875rem 1rem;
  border-bottom: 1px solid var(--border);
}

.results-table tr.highlight-row {
  background: rgba(var(--accent-rgb), 0.05);
}

.result-highlight {
  font-weight: 700;
  color: var(--accent);
  font-size: 1.1rem;
}

.improvement {
  color: var(--success);
  font-weight: 600;
}
```

**Interactivity**:
- Sortable columns (click header)
- Row hover effects
- Responsive (stack on mobile)
- Export to CSV button

### Diagram Zoom Modal

**For clickable diagram expansion**:

```html
<div id="diagram-modal" class="modal" style="display: none;">
  <div class="modal-backdrop" onclick="closeModal()"></div>
  <div class="modal-content">
    <button class="modal-close" onclick="closeModal()">×</button>
    <div class="modal-diagram">
      <!-- Enlarged diagram -->
    </div>
  </div>
</div>
```

```javascript
const zoomDiagram = (diagramElement) => {
  const modal = document.getElementById('diagram-modal');
  const modalDiagram = modal.querySelector('.modal-diagram');

  // Clone and enlarge
  modalDiagram.innerHTML = diagramElement.innerHTML;
  modal.style.display = 'flex';

  // Prevent body scroll
  document.body.style.overflow = 'hidden';
};
```

---

## Typography Hierarchy

**Establish clear hierarchy** (example for futuristic aesthetic):

```css
/* Hero Title */
h1.hero-title {
  font-family: 'Space Mono', monospace;
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
  background: linear-gradient(135deg, var(--text-primary), var(--accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Section Headings */
h2 {
  font-family: 'Space Mono', monospace;
  font-size: clamp(1.75rem, 4vw, 2.5rem);
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: var(--text-primary);
  position: relative;
  padding-bottom: 0.5rem;
}

h2::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 60px;
  height: 3px;
  background: var(--accent);
}

/* Subsection Headings */
h3 {
  font-family: 'Lora', serif;
  font-size: clamp(1.25rem, 3vw, 1.75rem);
  font-weight: 600;
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: var(--text-primary);
}

/* Body Text */
p {
  font-family: 'Lora', serif;
  font-size: 1.0625rem;
  line-height: 1.7;
  color: var(--text-secondary);
  margin-bottom: 1.25rem;
}

/* Code Inline */
code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.9em;
  background: rgba(var(--accent-rgb), 0.1);
  padding: 0.2em 0.4em;
  border-radius: 4px;
  color: var(--accent);
}
```

---

## Responsive Design Requirements

### Breakpoints

```css
:root {
  --mobile: 768px;
  --tablet: 1024px;
  --desktop: 1440px;
}

/* Mobile First */
@media (min-width: 768px) {
  /* Tablet adjustments */
}

@media (min-width: 1024px) {
  /* Desktop layout */
  .sidebar {
    position: sticky;
    top: 2rem;
  }
}
```

### Mobile Optimizations

**Navigation**:
- Sidebar becomes hamburger menu
- Floating action button for scroll-to-top
- Bottom navigation bar for key actions

**Content**:
- Single column layout
- Larger tap targets (min 44px)
- Horizontal scroll for wide diagrams
- Collapsible sections default to collapsed

**Code Blocks**:
- Horizontal scroll with indicators
- Copy button always visible
- Larger font size (min 14px)

---

## Performance Optimizations

### 1. Lazy Loading

```javascript
// Lazy load heavy sections
const lazyLoadSections = () => {
  const sections = document.querySelectorAll('.content-section');

  const lazyObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Load heavy content
        loadSectionContent(entry.target);
        lazyObserver.unobserve(entry.target);
      }
    });
  }, { rootMargin: '50px' });

  sections.forEach(section => lazyObserver.observe(section));
};
```

### 2. CSS Optimization

```css
/* Use transforms for animations (GPU accelerated) */
.smooth-animation {
  transform: translateZ(0); /* Force GPU layer */
  will-change: transform;
}

/* Reduce paint area */
.isolated-section {
  contain: layout style paint;
}
```

### 3. Font Loading

```html
<!-- Preload critical fonts -->
<link rel="preload" href="/fonts/display-font.woff2" as="font" type="font/woff2" crossorigin>
```

---

## Accessibility Requirements

### Keyboard Navigation

```javascript
// Arrow key navigation between sections
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowDown') {
    scrollToNextSection();
  } else if (e.key === 'ArrowUp') {
    scrollToPreviousSection();
  } else if (e.key === 'Escape') {
    closeModal();
  }
});
```

### Screen Reader Support

```html
<!-- Proper ARIA labels -->
<nav aria-label="Table of contents">
  <ul role="list">
    <li><a href="#intro" aria-current="page">Introduction</a></li>
  </ul>
</nav>

<!-- Skip to content -->
<a href="#main-content" class="skip-link">Skip to content</a>

<!-- Section landmarks -->
<main id="main-content" role="main">
  <article aria-labelledby="paper-title">
    <h1 id="paper-title">AlphaEvolve</h1>
  </article>
</main>
```

### Color Contrast

```css
/* Ensure WCAG AA compliance (4.5:1 for body text) */
--text-primary: #e1e1e1; /* On dark bg: 14:1 contrast */
--text-secondary: #a1a1a1; /* On dark bg: 7:1 contrast */

/* Check with browser dev tools or online contrast checkers */
```

---

## Content Integration Strategy

### From Markdown Report to Web Page

**Process**:
1. Parse markdown sections
2. Convert to HTML with proper structure
3. Enhance with interactive components
4. Add visual hierarchy
5. Inject animations

**Section Mapping**:
```javascript
const sectionConfig = {
  'executive-summary': {
    icon: '📄',
    color: '--accent-blue',
    animation: 'fadeInUp'
  },
  'architecture': {
    icon: '🏗️',
    color: '--accent-cyan',
    animation: 'slideInLeft',
    hasInteractiveDiagram: true
  },
  'pipeline': {
    icon: '⚙️',
    color: '--accent-magenta',
    animation: 'slideInRight',
    hasFlowchart: true
  },
  // ... map all sections
};
```

### Code Block Enhancement

**Transform** from markdown:
````markdown
```python
def example():
    return "code"
```
````

**To enhanced HTML**:
```html
<div class="code-block" data-language="python">
  <div class="code-header">
    <span class="language">Python</span>
    <button class="copy-btn">Copy</button>
  </div>
  <pre><code class="language-python hljs">
    <span class="hljs-keyword">def</span>
    <span class="hljs-title">example</span>():
        <span class="hljs-keyword">return</span>
        <span class="hljs-string">"code"</span>
  </code></pre>
</div>
```

### Diagram Enhancement

**Transform** from ASCII:
```
┌─────────┐
│ System  │
└─────────┘
```

**To styled container**:
```html
<div class="diagram-wrapper">
  <div class="diagram-label">System Architecture</div>
  <div class="diagram-content ascii" onclick="zoomDiagram(this)">
    <pre>
┌─────────┐
│ System  │
└─────────┘
    </pre>
  </div>
  <div class="diagram-caption">
    Click to enlarge | Figure from paper p.4
  </div>
</div>
```

---

## Technical Stack Recommendations

### Minimal Approach (Single HTML File)
**Best for**: Simple deployment, sharing, archiving

**Stack**:
- Pure HTML/CSS/JavaScript
- Inline CSS (critical) + external stylesheet
- Prism.js for syntax highlighting (CDN)
- No build process

**File size target**: < 500KB (including embedded fonts)

### Modern Approach (React/Vue)
**Best for**: Complex interactivity, future updates

**Stack**:
- React or Vue.js
- Tailwind CSS or styled-components
- Framer Motion for animations
- Build to static export

**Libraries**:
```javascript
// Package.json
{
  "dependencies": {
    "react": "^18.0.0",
    "framer-motion": "^10.0.0",
    "prism-react-renderer": "^2.0.0",
    "react-markdown": "^9.0.0"
  }
}
```

---

## Example: Complete Page Template

### HTML Structure

```html
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AlphaEvolve: Deep Dive Analysis</title>

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">

  <!-- Syntax Highlighting -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">

  <style>
    /* CSS Variables for theme */
    :root[data-theme="dark"] {
      --bg-primary: #0d1117;
      --bg-secondary: #161b22;
      --text-primary: #c9d1d9;
      --text-secondary: #8b949e;
      --accent: #00e5ff;
      --accent-rgb: 0, 229, 255;
      --border: #30363d;
    }

    /* Global styles */
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Lora', serif;
      background: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.7;
    }

    /* Add all component styles here */
  </style>
</head>
<body>
  <!-- Hero Section -->
  <section class="hero">
    <!-- Hero content -->
  </section>

  <!-- Main Layout -->
  <div class="main-layout">
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <!-- Navigation content -->
    </aside>

    <!-- Main Content -->
    <main class="content">
      <!-- Section cards -->
    </main>
  </div>

  <!-- Modals -->
  <div id="diagram-modal" class="modal"></div>

  <!-- Scripts -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script>
    // Initialize all functionality
    document.addEventListener('DOMContentLoaded', () => {
      initThemeToggle();
      observeIntersection();
      observeScrollReveal();
      implementSearch();
      initCopyButtons();
      initDiagramZoom();
    });
  </script>
</body>
</html>
```

---

## Quality Checklist for Web Page

### Visual Quality ✓
- [ ] Distinctive aesthetic (not generic)
- [ ] Cohesive color scheme with CSS variables
- [ ] Typography hierarchy clear (3-4 levels)
- [ ] Spacing consistent (use rem/em)
- [ ] Backgrounds add atmosphere
- [ ] Hover states on interactive elements

### Functionality ✓
- [ ] All navigation links work
- [ ] Search finds and highlights content
- [ ] Code copy buttons function
- [ ] Diagrams clickable for zoom
- [ ] Smooth scrolling between sections
- [ ] Theme toggle persists preference
- [ ] Print stylesheet works

### Performance ✓
- [ ] Page loads in < 3 seconds
- [ ] Smooth 60fps scrolling
- [ ] No layout shift (CLS < 0.1)
- [ ] Fonts preloaded
- [ ] Images optimized (if any)

### Accessibility ✓
- [ ] Keyboard navigation works
- [ ] Screen reader compatible
- [ ] Color contrast meets WCAG AA
- [ ] Focus indicators visible
- [ ] ARIA labels present

### Responsive ✓
- [ ] Mobile layout functional
- [ ] Tablet layout optimized
- [ ] Desktop layout spacious
- [ ] No horizontal scroll (except diagrams)
- [ ] Touch targets min 44px

---

## Creative Direction Examples

### Example 1: "Neural Lab" Aesthetic (for AlphaEvolve)

**Direction**: Dark futuristic laboratory with neural network motifs

**Key Decisions**:
- **Fonts**: Space Mono (display), JetBrains Mono (body/code)
- **Colors**: Deep blacks with cyan/magenta accents
- **Background**: Animated neural network connections
- **Cards**: Glass morphism with subtle borders
- **Animations**: Smooth reveals, glowing effects
- **Special**: Animated "evolution" visualization in hero

**Code Sample**:
```css
.hero-background {
  background: radial-gradient(circle at 30% 40%, #00e5ff15 0%, transparent 50%),
              radial-gradient(circle at 70% 60%, #ff006e15 0%, transparent 50%),
              #0a0a0a;
}

.neural-network {
  position: absolute;
  inset: 0;
  opacity: 0.1;
  background-image:
    repeating-linear-gradient(0deg, transparent, transparent 100px, #00e5ff 100px, #00e5ff 101px),
    repeating-linear-gradient(90deg, transparent, transparent 100px, #00e5ff 100px, #00e5ff 101px);
}
```

### Example 2: "Academic Manuscript" Aesthetic

**Direction**: Classical scholarly document with modern interactivity

**Key Decisions**:
- **Fonts**: Crimson Pro (display), Lora (body), Fira Code (code)
- **Colors**: Cream background with warm browns and deep blues
- **Background**: Subtle paper texture
- **Cards**: Subtle shadows, serif numbers, margin notes
- **Animations**: Gentle fades, page-turn effects
- **Special**: Interactive footnotes, citation hover previews

**Code Sample**:
```css
body {
  background: #faf8f5;
  background-image: url('data:image/svg+xml,...'); /* Paper texture */
}

.content-card {
  background: #ffffff;
  border: 1px solid #e8e4df;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: relative;
  padding: 2rem 3rem;
}

.margin-note {
  position: absolute;
  right: -200px;
  width: 180px;
  font-size: 0.85rem;
  color: #8b7355;
  font-style: italic;
}
```

### Example 3: "Data Dashboard" Aesthetic

**Direction**: Modern analytics platform with live data feel

**Key Decisions**:
- **Fonts**: Outfit (display), IBM Plex Sans (body), Fira Code (code)
- **Colors**: Whites and light grays with vibrant accent colors
- **Background**: Subtle gradients, grid patterns
- **Cards**: Elevated with metrics-style displays
- **Animations**: Counter animations for numbers, bar chart builds
- **Special**: Animated progress indicators, metric comparisons

---

## Implementation Workflow

### Step-by-Step Process:

1. **Choose aesthetic direction** (5 min thinking time)
2. **Set up HTML structure** with semantic sections
3. **Implement CSS variables** for theming
4. **Build hero section** with impact
5. **Create navigation** with scroll-spy
6. **Style content sections** with chosen aesthetic
7. **Add code highlighting** and copy functionality
8. **Enhance diagrams** with zoom and styling
9. **Implement search** functionality
10. **Add animations** (entrance, scroll, hover)
11. **Test responsiveness** (mobile, tablet, desktop)
12. **Optimize performance** (lazy load, font preload)
13. **Accessibility pass** (keyboard, ARIA, contrast)
14. **Final polish** (micro-interactions, edge cases)

---

## Success Criteria

A completed interactive web page must:

✅ **Visual Impact**: Memorable first impression, distinctive aesthetic
✅ **Functionality**: All interactions work smoothly
✅ **Content Fidelity**: Accurately represents the verified report
✅ **Performance**: Loads quickly, scrolls smoothly
✅ **Accessibility**: Keyboard, screen reader, high contrast
✅ **Responsive**: Works on all screen sizes
✅ **Polish**: Details refined, no rough edges

---

## Tips for Excellence

1. **Commit to the aesthetic** - Half-hearted design shows
2. **Details matter** - Hover states, transitions, spacing
3. **Test on real devices** - Emulators miss issues
4. **Animation restraint** - One bold move better than many small ones
5. **Typography is 80%** - Get font pairing and hierarchy right
6. **Use real content** - Don't use lorem ipsum
7. **Mobile-first** - Easier to enhance than to strip down
8. **Performance budget** - Every animation should earn its bytes
9. **Accessibility from start** - Don't retrofit
10. **Be bold** - Generic is worse than polarizing

---

## Anti-Patterns to Avoid

❌ **Generic white page with default fonts**
❌ **Purple gradient hero (overused)**
❌ **Boring gray cards in a column**
❌ **No personality or character**
❌ **Animations on everything (visual noise)**
❌ **Tiny text on mobile**
❌ **Inaccessible color combinations**
❌ **Slow page load (> 3s)**
❌ **Broken on mobile**
❌ **Copy-paste from another project without adaptation**

---

## Reference: Complete Minimal Example

See the following page for a complete, copy-paste-ready template that can be customized for any research paper.

This template includes:
- Full HTML structure
- Complete CSS with dark theme
- All JavaScript functionality
- Responsive design
- Accessibility features
- Performance optimizations

The template is designed with the "Neural Lab" aesthetic but can be easily adapted to any direction by changing CSS variables and font selections.

**Use this as starting point**, then customize typography, colors, and layout to match the paper's domain and character.
