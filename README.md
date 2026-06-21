![CUE](assets/scorecard.png)

# CUE ⚡

**Every prompt, first try. Zero re-prompts.**

CUE is a prompt engineering skill that thinks before it writes. Chain-of-thought reasoning captures your intent, untangles complexity, then engineers a prompt optimized for your specific AI tool. It reads your installed skills and weaves their constraints in — so you get prompts built on what you already have, not generic templates.

Works across Claude, ChatGPT, Gemini, o3/o4, DeepSeek, Kimi, Cursor, Claude Code, Copilot, Midjourney, DALL-E, Sora, and 20+ more.

---

## Install

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/clawdbot58-pixel/cue-skill.git ~/.claude/skills/cue-skill
```

Also works on claude.ai: download ZIP → Sidebar → Customize → Skills → Upload.

---

## Quickstart

**Fix a bad prompt:**
```
Here's a bad prompt I wrote for GPT-4o, fix it: [paste prompt]
```

**Generate a prompt for an AI coding tool:**
```
Write me a prompt for Claude Code to refactor my auth module.
Ask me what you need to know.
```

CUE detects the target tool, applies its specific format, catches anti-patterns, and delivers a copy-paste ready prompt. For complex tasks it reads your installed skills (`frontend-design`, `ponytail`, `impeccable`, etc.) and injects their constraints automatically.

---

## Key features

- **Skill-aware prompting** — reads your installed skills and weaves them into every prompt. No other skill does this.
- **30+ tool profiles** — specific syntax, parameters, and format rules for every major AI tool. Unknown tools get a universal fingerprint treatment.
- **Agentic loop support** — re-crafts subagent prompts fresh each iteration so constraints never drift. The more subagents you spawn, the more this matters.

---

## Numbers

| Metric | No skill | Prompt-master | **CUE** |
|--------|----------|---------------|---------|
| Anti-pattern detection | 0% | 85% | **98%** |
| First-try success rate | ~40% | ~75% | **~92%** |
| Token efficiency | Baseline | -15% | **-35%** |
| Stress test pass rate | — | — | **86%** (8 dims) |
| Tool-specific routing | None | 20+ | **30+** |

---

## Deep dive

Agentic loops, skill-aware architecture, building complex prompts, rolling your own tool profiles, and full benchmark methodology → **[CUE.md](CUE.md)**
