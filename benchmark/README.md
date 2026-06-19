# CUE vs Prompt-Master Benchmark

Head-to-head comparison of cue-skill against nidhinjs/prompt-master (v1.7.0).

## Structure

| File | Tests | What It Measures |
|------|-------|-----------------|
| `tool-routing.json` | 30 | Correct tool-specific prompt format for 30+ AI tools |
| `pattern-detection.json` | 20 | Detecting and fixing common prompt anti-patterns |
| `edge-cases.json` | 15 | Adversarial, ambiguous, conflicting inputs |
| `agentic.json` | 10 | Agent prompts with stop conditions, scope, safety |
| `visual-media.json` | 10 | Image/video generation prompts (MJ, SD, DALL-E, Sora) |
| `multi-domain.json` | 10 | Cross-domain fusion and specialized knowledge |
| `token-efficiency.json` | 10 | Conciseness without losing signal |
| `memory-context.json` | 5 | Session carry-forward and context management |
| `stacked.json` | 5 | Multiple dimensions simultaneously |
| `RUBRIC.md` | — | Scoring criteria and dimensions |

**Total: 115 test cases across 9 categories**

## Scoring

Each test is scored 0-5:
- **0**: Wrong tool/format, unusable output
- **1**: Recognizable intent but wrong structure
- **2**: Correct general approach, missing key elements
- **3**: Good output, minor gaps
- **4**: Excellent output, fully usable
- **5**: Perfect — production-ready, tool-optimized, zero re-prompts needed

## End Condition

Benchmark stops when cue-skill average score >= 4.5 across all categories AND beats prompt-master by >= 0.5 points average.

## Running

Use `run-benchmark.md` for manual evaluation or spawn subagents per test.
