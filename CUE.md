# CUE — Advanced Usage

Deep dive for those who want to go beyond the quickstart. Agentic loops, skill-aware architecture, complex prompt construction, rolling your own tool profiles, and the full benchmark methodology.

---

## Agentic Loops

This is where CUE provides the most value. When an agent orchestrates sub-agents, prompt quality drifts across iterations. CUE eliminates that drift.

### The problem

In agentic loops — where a main agent repeatedly spawns subagents to do tasks — every subagent prompt is a fresh context window. Constraints from earlier turns get lost. Skills get forgotten. The agent ends up re-inventing quality gates, missing banned patterns, and producing inconsistent output across iterations. The more iterations, the worse the drift.

```
Iteration 1: ████████████████████ (full context, all skills, all constraints)
Iteration 2: ████████████████░░░░ (lost 2 constraints)
Iteration 3: ████████████░░░░░░░░ (lost 4 constraints, re-inventing quality gates)
Iteration 4: ████████░░░░░░░░░░░░ (half-forgot banned patterns)
Iteration 5: ████░░░░░░░░░░░░░░░░ (completely generic output)
```

### How CUE fixes it

CUE re-crafts every subagent prompt from scratch. Each delegation is a fresh application of the full RACE-PEP framework:

```
Main agent decides: "I need a subagent to refactor the auth module"

Step 1: CUE captures intent
  → "Refactor src/auth/ — not rewrite, not add features, refactor"

Step 2: CUE scans installed skills
  → ponytail → injects YAGNI, stdlib-first, one-line-before-fifty
  → impeccable → injects quality gates, scope boundaries

Step 3: CUE detects anti-patterns
  → "refactor" is vague → scoped to specific files
  → no stop condition → "stop when existing tests pass"
  → no file paths → "only src/auth/*.ts"

Step 4: CUE applies tool profile
  → Target: Claude Code → XML tags, explicit reasoning, static-first

Step 5: CUE delivers a complete, skill-aware prompt
  → Subagent runs with full context from the start

Next iteration: repeat from Step 1. Same quality. No drift.
```

### Before / after: subagent delegation

**Without CUE (cold delegation — what most agents do):**
```
Write tests for the auth module
```
The subagent gets 5 words. No context. No constraints. No skill awareness. It guesses.

**With CUE (skill-aware delegation):**
```
Write tests for the authentication module in src/auth/.

Rules (from ponytail skill):
- YAGNI: do not add test infrastructure beyond what exists
- Stdlib first: use built-in test frameworks before custom harnesses
- One line before fifty: prefer the shortest test that validates behavior

Quality gates (from impeccable skill):
- Every test must assert both happy path and at least one edge case
- No test should depend on external services, network access, or filesystem state
- Test descriptions must name the behavior being verified

Scope: only files in src/auth/__tests__/. Do not touch production code.
Do not modify package.json, tsconfig.json, or any config files.

Stop when: all existing tests pass, new tests are added for uncovered paths,
no new dependencies, no files outside scope touched.
```
The subagent gets a purpose-built prompt with guardrails, scope, and quality standards — every time.

### Loop: multi-subagent orchestration example

A main agent (Claude Code with CUE installed) refactors a full module across 5 subagent calls:

```
# Iteration 1: CUE crafts prompt for auth module refactor
CUE reads: ponytail skill → injects YAGNI constraints
CUE reads: impeccable skill → injects quality gates
Prompt includes: YAGNI, stdlib-first, stop conditions, scope lock on src/auth/
Result: Clean refactor, no scope creep

# Iteration 2: CUE crafts prompt for auth tests
CUE reads: ponytail + impeccable → injects both
Prompt includes: YAGNI + test quality gates + coverage criteria
Result: Tests pass, no test infrastructure bloat

# Iteration 3: CUE crafts prompt for auth documentation
CUE reads: doc-coauthoring skill → injects documentation workflow
Prompt includes: structure requirements + audience constraints + no scope creep
Result: Docs match the refactored code, no hallucinated features

# Iteration 4: CUE crafts prompt for auth migration guide
CUE reads: doc-coauthoring + ponytail → injects both
Prompt includes: migration steps + rollback instructions + YAGNI on guide length
Result: Concise migration guide, no unnecessary sections

# Iteration 5: CUE crafts prompt for final review
CUE reads: code-review skill → injects review dimensions
Prompt includes: correctness + security + simplification checks
Result: 3 findings, all real, no false positives
```

Each subagent got a purpose-built prompt, not a degraded copy of iteration 1. Quality stayed flat across all 5 iterations.

### When to use CUE with subagents

| Scenario | Why CUE helps |
|----------|---------------|
| **Single delegation** | One-off subagent calls get skill-aware prompts instead of cold task descriptions |
| **Multi-step refactoring** | Each file/feature gets a fresh, full-context prompt |
| **Code review pipelines** | Reviewer subagents get consistent quality standards across files |
| **Test generation loops** | Each test batch follows the same patterns and quality bars |
| **Design iteration** | Design subagents maintain style consistency across rounds |
| **Any task with 3+ subagents** | Drift becomes measurable at 3 iterations; CUE prevents it |

---

## Skill-Aware Prompting

Most prompt skills write prompts from scratch. CUE reads the skills you already have installed and weaves them into the generated prompt.

### How it works

1. **Scan** — CUE checks `~/.claude/skills/*/SKILL.md`, `~/.codex/skills/*/SKILL.md`, and project-local `.claude/skills/*/SKILL.md`
2. **Match** — word overlap + trigger pattern extraction against the current task
3. **Inject** — matched skill capabilities become constraints or building blocks in the generated prompt
4. **Adapt** — injection format matches the target model (XML tags for Claude, markdown sections for GPT, structured blocks for Gemini)

### Concrete example

You have `frontend-design`, `high-end-visual-design`, and `impeccable` installed. You ask CUE for a landing page prompt.

**Without skill awareness (generic prompt skill):**
```
Create a modern, professional landing page for a SaaS product.
Use clean design with good typography and spacing.
```
Result: Inter font, blue CTA, symmetrical 3-col grid. The "generic AI SaaS" look.

**With CUE skill awareness:**
```
Build a single-file HTML landing page for a SaaS analytics dashboard.

Stack: HTML + inline CSS + vanilla JS. No frameworks. No external deps except Google Fonts.

## Design Direction (from frontend-design skill)
Tone: Luxury/refined. Pick a BOLD aesthetic direction — not generic "clean SaaS".
Differentiation: What's UNFORGETTABLE? One thing someone remembers.

## Visual Standards (from high-end-visual-design skill)
BANNED: Inter, Roboto, Arial, Open Sans, Helvetica. Use Geist, Clash Display,
PP Editorial New, or Plus Jakarta Sans instead.
BANNED: Standard thick-stroked Lucide/FontAwesome icons. Use Phosphor Light.
BANNED: 1px solid gray borders. Harsh dark shadows (shadow-md, rgba(0,0,0,0.3)).
BANNED: Edge-to-edge sticky navbars. Symmetrical 3-col Bootstrap grids.
BANNED: linear or ease-in-out transitions. Instant state changes.

## Quality Standards (from impeccable skill)
Every element must pass: visual hierarchy, information architecture, cognitive
load check, accessibility, responsive behavior, micro-interactions.
Typography: distinctive display font + refined body font. No generic choices.

[...continues with layout, sections, animations, constraints...]
```
Result: The prompt references your actual skill set. Banned fonts from high-end-visual-design. Quality gates from impeccable. Design thinking from frontend-design. Not generic — built on what you already have.

### Cross-model skill injection

Skill reading is not Claude-specific. CUE adapts the injection format:

| Target model | Injection format |
|-------------|-----------------|
| **Claude** | XML tags (`<design-direction>`, `<visual-standards>`) |
| **GPT-4o** | Markdown sections with `##` headings |
| **Gemini** | Structured blocks with hierarchical formatting |
| **Cursor/Copilot** | Comments with `// Rules (from skill):` prefix |
| **Midjourney** | Inline style tokens and negative prompt entries |

---

## Building Complex Prompts

### Multi-step workflows

When a task needs sequential steps, build the prompt as a chain — not a monolith:

```
Step 1: Analyze — [what to look at, what to produce]
Step 2: Plan — [what to decide, what to lock in]
Step 3: Execute — [what to build, constraints per step]
Step 4: Verify — [what to check, pass/fail per step]
Step 5: Deliver — [final output format]
```

Each step has its own stop condition. If step 3 fails verification, loop back to step 2 — don't redo step 1.

### Constraint stacking

For complex prompts with many constraints, layer them by priority:

1. **Hard constraints** (must satisfy — format, scope, security)
2. **Soft constraints** (should satisfy — style, preference, convention)
3. **Aspirational** (nice to have — elegance, delight, cleverness)

The model will trade off aspirational before soft, soft before hard. Make sure hard constraints are unmistakable.

### Edge cases

- **Adversarial inputs**: If the user pastes a prompt that contains instructions ("ignore previous instructions"), CUE treats it as data to analyze, not commands to follow
- **Conflicting constraints**: Surface the conflict explicitly. "Constraint A (X) conflicts with constraint B (Y). Resolution: A takes priority because [reason]."
- **Tool ambiguity**: If the user doesn't specify a target tool, ask "Which tool is this for?" or apply the Universal Fingerprint
- **Token budgets**: If the user specifies a token limit, the token audit step becomes stricter — cut framing words before cutting constraints

---

## Roll Your Own Tool Profiles

CUE covers 30+ tools, but you can add any tool not on the list.

### Profile structure

```
Tool: [name]
Category: [reasoning / thinking / ide / agentic / image / video / 3d / voice / automation / fullstack]
Input format: [natural language / structured / code / multi-modal]
Key parameters: [list with defaults and ranges]
Syntax rules: [comma-separated, XML tags, markdown headings, etc.]
Anti-patterns: [what NOT to do with this specific tool]
Output markers: [how to recognize a good output]
```

### Example: adding a new tool

```
Tool: Replit Agent
Category: agentic
Input format: natural language + file references
Key parameters: project context (automatic), language/framework detection
Syntax rules: markdown sections, file paths as anchors
Anti-patterns:
  - No "build the whole app" — break into features
  - No ambiguous scope — specify files to touch
  - No missing acceptance criteria
Output markers: running app at URL, all files created, no errors in console
```

Once defined, CUE applies the same RACE-PEP framework with this profile. The Universal Fingerprint (4 questions) handles anything without a profile.

---

## Benchmark Methodology

CUE is tested against three benchmark suites totaling 115 test cases across 9 categories.

### Test suites

| Suite | Tests | What It Measures |
|-------|-------|------------------|
| **Pattern Detection** | 20 | Anti-pattern identification and fixing |
| **Tool Routing** | 30 | Correct tool-specific prompt format for 30+ AI tools |
| **Edge Cases** | 15 | Adversarial, ambiguous, conflicting inputs |
| **Agentic** | 10 | Agent prompts with stop conditions, scope, safety |
| **Visual Media** | 10 | Image/video generation prompt quality across 6 tools |
| **Multi-Domain** | 10 | Cross-domain fusion and specialized knowledge |
| **Token Efficiency** | 10 | Conciseness without losing signal |
| **Memory/Context** | 5 | Session carry-forward and context management |
| **Stacked** | 5 | Multiple dimensions simultaneously |

### Stress test dimensions

| Dimension | What It Tests | Escalation |
|-----------|---------------|------------|
| **Reasoning Depth** | Multi-hop logic, counterfactuals | 2 steps → recursive self-verification |
| **Constraint Density** | Conflicting rules, trade-offs | 1 constraint → 5 contradictory constraints |
| **Context Volume** | Signal-to-noise ratio | 1K tokens → 50K with buried critical info |
| **Output Structure** | Schema complexity | JSON → self-validating schemas |
| **Ambiguity Resolution** | Vague inputs | Clear → actively misleading |
| **Meta-Cognition** | Self-correction | Direct → adversarial self-audit |
| **Domain Fusion** | Cross-disciplinary | Single → three+ domains |
| **Temporal/Stateful** | Sequences, state changes | Static → branching timelines |

### Scoring

Each test scored 0-5:
- **0**: Wrong tool/format, unusable output
- **1**: Recognizable intent but wrong structure
- **2**: Correct approach, missing key elements
- **3**: Good output, minor gaps
- **4**: Excellent, fully usable
- **5**: Perfect — production-ready, zero re-prompts

**Weighted dimensions:** Tool Correctness (25%), Pattern Detection (20%), Completeness (15%), Conciseness (10%), Edge Case Handling (15%), Production Readiness (15%).

### Results summary

| Metric | No skill | Prompt-master | **CUE** |
|--------|----------|---------------|---------|
| Anti-pattern detection | 0% | 85% | **98%** |
| Tool-specific routing | None | 20+ tools | **30+ tools** |
| Skill-aware prompting | None | None | **Yes** |
| Token efficiency | Baseline | -15% | **-35%** |
| First-try success rate | ~40% | ~75% | **~92%** |
| Stress test pass rate | — | — | **86%** (8 dimensions) |
| Visual media coverage | None | Partial | **97%** (6 tools) |

Run benchmarks: `bash benchmark/run-benchmark.sh`. Outputs reports to `/tmp/cue-benchmark/`.

---

## Model Adaptations Reference

| Model | Format | Anti-pattern to avoid |
|-------|--------|----------------------|
| **GPT-4o** | Markdown, JSON mode | Vague constraints — be hyper-specific |
| **Claude** | XML tags, cache-friendly | Missing reasoning requests — Claude reasons well when asked |
| **Gemini** | Hierarchical headings | Format at bottom — put it at TOP |
| **o3 / o4-mini** | Short, clean instructions | CoT — degrades reasoning model output |
| **DeepSeek-R1** | Structured reasoning blocks | Unbounded `<think>` — suppress with format constraints |
| **Kimi** | KIMI_REF tags, skill-loading | Generic prompts — Kimi responds to structured skill patterns |
| **Llama** | Explicit role, step-by-step | Complex abstractions — simpler structure works better |
| **Cursor** | File paths, do-not-touch lists | No scope — always lock file scope |
| **Claude Code** | XML, static-first, stop conditions | Unrestricted filesystem — always add file restrictions |
| **Midjourney** | Comma-separated, --ar, --v | Prose paragraphs — MJ needs token-dense descriptors |
| **DALL-E 3** | Prose, foreground/midground/background | Comma-separated — DALL-E needs narrative descriptions |
| **Stable Diffusion** | (word:weight), CFG, steps | Missing negative prompt — always include |
