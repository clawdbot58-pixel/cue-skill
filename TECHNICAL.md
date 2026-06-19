# CUE Technical Documentation

Benchmarks, evaluation methodology, stress tests, and scoring rubrics.

---

## Benchmarks Overview

CUE is tested against three benchmark suites:

| Suite | Tests | What It Measures |
|-------|-------|------------------|
| **Pattern Detection** | 20 | Anti-pattern identification and fixing |
| **Visual Media** | 10 | Image/video generation prompt quality |
| **Stress Tests** | 10 | Complexity handling across 8 dimensions |

---

## Pattern Detection Tests (20)

Tests whether CUE can detect and fix common prompt anti-patterns.

| ID | Test | What It Catches |
|----|------|-----------------|
| PD-01 | Vague task verb | "help me with my code" → specific operation |
| PD-02 | Two tasks in one | "explain AND rewrite" → split into separate prompts |
| PD-03 | No success criteria | "look more professional" → measurable goals |
| PD-04 | Emotional description | Panic language → calm bug report format |
| PD-05 | Build the whole thing | Full-stack request → sequential sub-prompts |
| PD-06 | Assumed prior knowledge | "continue where we left off" → self-contained context |
| PD-07 | Missing output format | "explain microservices" → explicit format constraints |
| PD-08 | No file path for IDE AI | Missing anchors → file paths + do-not-touch list |
| PD-09 | No stop condition | "add comments feature" → checkpoint + review triggers |
| PD-10 | CoT on reasoning model | "think step by step" on o3 → removed |
| PD-11 | Vague aesthetic | "beautiful portrait" → concrete visual specs |
| PD-12 | Prose for Midjourney | Paragraph format → comma-separated descriptors |
| PD-13 | Over-permissive agent | "do whatever it takes" → allowed/forbidden action lists |
| PD-14 | Missing grounding rule | Summarization → hallucination constraints |
| PD-15 | No negative prompts | Missing negative prompt → comprehensive block |
| PD-16 | Whole codebase pasted | Context dump → scoped file selection |
| PD-17 | Implicit length | "write a summary" → word/sentence count |
| PD-18 | No role assignment | Complex task without expert identity |
| PD-19 | Wrong template for tool | Multi-section prompt for Copilot → docstring format |
| PD-20 | Multiple anti-patterns | 4+ issues at once → clean, specific prompt |

### Assertions per Test

Each test has 3-7 specific assertions. A test passes if ≥80% of assertions are met.

---

## Visual Media Tests (10)

Tests image and video generation prompt quality across tools.

| ID | Test | Tool Focus | Key Assertions |
|----|------|------------|----------------|
| VM-01 | Midjourney basic | Midjourney | Comma-separated, --ar/--v, negative prompt |
| VM-02 | SD weighted | Stable Diffusion | (word:weight) syntax, CFG, steps |
| VM-03 | DALL-E 3 prose | DALL-E 3 | Foreground/midground/background |
| VM-04 | Sora video | Sora | Camera movement, duration, cinematic language |
| VM-05 | Reference editing | Universal | Detects editing vs. generation |
| VM-06 | ComfyUI split | ComfyUI | Positive/negative blocks, sampler config |
| VM-07 | Runway video | Runway | Motion intensity, camera angle |
| VM-08 | Neg prompt | Universal | Tool-adapted negative prompts |
| VM-09 | Style chain | Midjourney | --sref and style consistency |
| VM-10 | Ambiguous tool | Universal | Detects tool ambiguity, asks or adapts |

---

## Stress Tests (8 Dimensions)

### Complexity Dimensions

| Dimension | What It Tests | Escalation Levels |
|-----------|---------------|-------------------|
| **Reasoning Depth** | Multi-hop logic, counterfactuals | 2 steps → recursive self-verification |
| **Constraint Density** | Conflicting rules, trade-offs | 1 constraint → contradictory constraints |
| **Context Volume** | Signal-to-noise ratio | 1K tokens → 50K with buried critical info |
| **Output Structure** | Schema complexity, cross-references | JSON → self-validating schemas |
| **Ambiguity Resolution** | Vague inputs, implicit assumptions | Clear → actively misleading |
| **Meta-Cognition** | Self-correction, uncertainty | Direct → adversarial self-audit |
| **Domain Fusion** | Cross-disciplinary reasoning | Single → three+ domains |
| **Temporal/Stateful** | Sequences, state changes | Static → branching timelines |

### Test-to-Dimension Mapping

| Test ID | Test Name | Primary Dimension | Secondary Dimensions |
|---------|-----------|-------------------|---------------------|
| stress-1 | Constraint Saturation | Constraint Density | Output Structure |
| stress-2 | Signal Extraction | Context Volume | Ambiguity |
| stress-3 | Adversarial Robustness | Meta-Cognition | Ambiguity |
| stress-4 | Cross-Domain Fusion | Domain Fusion | Reasoning Depth |
| stress-5 | Temporal Logic | Temporal/Stateful | Reasoning Depth |
| stress-6 | Self-Correction | Meta-Cognition | Reasoning Depth |
| stress-7 | Schema Negotiation | Output Structure | Ambiguity |
| stress-8 | Ethical Arbitration | Reasoning Depth | Constraint Density |
| stress-9 | Context Window Stress | Context Volume | — |
| stress-10 | Emergent Behavior | Meta-Cognition | Reasoning Depth |

### Progressive Injection Stack

Injections are applied ON TOP of a seed prompt to increase difficulty:

| Injection | Name | Dimension | What It Adds |
|-----------|------|-----------|--------------|
| 1 | Constraint Conflicts | Constraint Density | 5 contradictory rules requiring arbitration |
| 2 | Buried Context | Context Volume | 15K-word transcript with unmarked feedback |
| 3 | Multi-Format Output | Output Structure | JSON + table + summary + audit trail |
| 4 | Counterfactual Reasoning | Reasoning Depth | Hypothetical scenarios + diff analysis |
| 5 | Adversarial Input | Ambiguity | Misdirection, negation, competitor references |
| 6 | Stateful Memory Decay | Temporal | Turn history with rule overrides and forgetting |
| 7 | Recursive Meta-Prompt | Meta-Cognition | Generate attack → defense → evaluate defense |

#### Recommended Stacking Order (Maximum Difficulty)

1. Injection 1 — Constraint Conflicts
2. Injection 3 — Multi-Format Output
3. Injection 5 — Adversarial Input
4. Injection 7 — Recursive Meta-Prompting
5. Injection 6 — Stateful Memory Decay

This stack tests 5 primary dimensions simultaneously.

---

## Scoring Rubric

### Metrics

| Metric | How to Measure | Target |
|--------|----------------|--------|
| **Constraint Adherence** | % of hard constraints satisfied | 85%+ |
| **Reasoning Transparency** | Can you audit why it made each decision? | Yes/No + quality |
| **Graceful Degradation** | When it fails, does it fail predictably? | Fails with explanation |
| **Token Efficiency** | Does it solve complex tasks without burning context? | Under 2x baseline |
| **Self-Awareness** | Does it know when it doesn't know? | Reports uncertainty |

### Pass/Fail Interpretation

- **Full pass**: All assertions met, output is coherent and complete
- **Partial pass**: 70%+ assertions met, output shows understanding but has gaps
- **Fail**: <70% assertions met, or output is incoherent/missing critical elements
- **Graceful degradation**: Failed assertions are acknowledged in output

---

## Core Evaluation Prompts

| ID | Prompt | Expected Output |
|----|--------|-----------------|
| 1 | System prompt for SaaS billing chatbot | Structured system prompt with identity, capabilities, rules, tool usage, boundaries, examples |
| 2 | Agent prompt for code review bot | Agent prompt with identity, objective, workflow, tool priority, state management, error handling |
| 3 | User prompt to summarize research paper | Concise user prompt with action, constraints, format |
| 4 | Design brief for fitness app landing page | Design description with visual direction, composition, elements, rationale |
| 5 | Reusable social media post template | Meta-prompt with variables, definitions table, usage instructions |
| 6 | Explain RAG to non-technical PM | Neutral description with overview, definition, components, use cases |

---

## Token Efficiency Rules

1. **Static first, dynamic last** — System instructions before user query (50-90% cache savings)
2. **Positive over negative** — "only use X" > "don't use Y"
3. **Specific over vague** — "3 bullets" > "be concise"
4. **One task per prompt** — Chain complex workflows

---

## Model Adaptations

| Model | Tweak |
|-------|-------|
| GPT-4o | Crisp constraints, markdown delimiters, JSON mode |
| Claude | XML tags, explicit reasoning requests |
| Gemini | Hierarchical headings, format at TOP |
| Kimi | Skill-loading pattern, KIMI_REF tags |
| Llama | Explicit role + step-by-step |
| DeepSeek | Structured reasoning blocks |

---

## Anti-Patterns Detected

| Category | Pattern | Fix |
|----------|---------|-----|
| **Task** | Vague verb ("help me") | Specific operation ("refactor", "debug") |
| **Task** | Two tasks in one | Split into separate prompts |
| **Task** | No success criteria | Binary pass/fail condition |
| **Task** | Emotional description | Calm, technical bug report format |
| **Task** | Build the whole thing | Sequential sub-prompts |
| **Task** | Over-permissive agent | Allowed/forbidden action lists |
| **Task** | Implicit reference | Self-contained context block |
| **Context** | Assumed prior knowledge | Memory block with decisions |
| **Context** | No project context | Stack + role + constraints |
| **Context** | Hallucination invite | Grounding constraint |
| **Format** | Missing output format | Explicit format specification |
| **Format** | Implicit length | Word/sentence count |
| **Format** | Vague aesthetic | Concrete visual specs |
| **Format** | No negative prompts | Comprehensive negative block |
| **Format** | Prose for Midjourney | Comma-separated descriptors |
| **Scope** | No scope boundary | File path + do-not-touch list |
| **Scope** | No stack constraints | Version + framework + limits |
| **Scope** | No stop condition | Checkpoint + review triggers |
| **Scope** | Wrong template | Adapted to tool format |
| **Reasoning** | No CoT for logic | Step-by-step instruction |
| **Reasoning** | CoT on reasoning model | Removed (degrades output) |
| **Agentic** | No starting state | Empty project description |
| **Agentic** | No target state | File + function + behavior spec |
| **Agentic** | Silent agent | Progress output after each step |
| **Agentic** | Unlocked filesystem | Explicit file restrictions |
| **Agentic** | No human review trigger | Stop before irreversible actions |
