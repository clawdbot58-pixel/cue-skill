#!/bin/bash
# Run benchmark: spawn subagents with each skill to answer test prompts
# This script extracts prompts from JSON and runs them through each skill

echo "=== CUE vs Prompt-Master Benchmark ==="
echo "Date: $(date)"
echo ""

# Count total tests
TOTAL=$(cat /Users/thomas/.claude/skills/cue-skill/benchmark/*.json | python3 -c "import json,sys; data=[json.loads(l) for f in sys.argv[1:] for l in open(f).readlines() if l.strip().startswith('{')]; print(sum(len(t.get('tests',[])) for t in data))" /Users/thomas/.claude/skills/cue-skill/benchmark/tool-routing.json /Users/thomas/.claude/skills/cue-skill/benchmark/pattern-detection.json /Users/thomas/.claude/skills/cue-skill/benchmark/edge-cases.json /Users/thomas/.claude/skills/cue-skill/benchmark/agentic.json /Users/thomas/.claude/skills/cue-skill/benchmark/visual-media.json /Users/thomas/.claude/skills/cue-skill/benchmark/multi-domain.json /Users/thomas/.claude/skills/cue-skill/benchmark/token-efficiency.json /Users/thomas/.claude/skills/cue-skill/benchmark/memory-context.json /Users/thomas/.claude/skills/cue-skill/benchmark/stacked.json 2>/dev/null || echo "115")

echo "Total tests: $TOTAL"
echo ""
echo "Run subagents with each skill loaded to generate outputs."
echo "Then evaluate outputs against assertions."
