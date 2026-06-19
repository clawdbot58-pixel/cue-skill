# Benchmark Scoring Rubric

## Score Scale

| Score | Label | Criteria |
|-------|-------|----------|
| 0 | Wrong | Wrong tool/format, unusable output, or skill fails to activate |
| 1 | Broken | Recognizable intent but fundamentally wrong structure or missing critical elements |
| 2 | Partial | Correct general approach, 2+ critical elements missing |
| 3 | Good | Correct structure, most elements present, minor gaps |
| 4 | Excellent | Fully usable, tool-optimized, all critical elements present |
| 5 | Perfect | Production-ready, zero re-prompts needed, handles edge cases |

## Dimension Weights

| Dimension | Weight | Why |
|-----------|--------|-----|
| Tool Correctness | 25% | Right format for the right tool is the #1 job |
| Pattern Detection | 20% | Finding and fixing anti-patterns is core value |
| Completeness | 15% | All required elements present |
| Conciseness | 10% | No wasted tokens or meta-commentary |
| Edge Case Handling | 15% | Adversarial/ambiguous inputs handled gracefully |
| Production Readiness | 15% | Copy-paste ready, no follow-up needed |

## Tool Routing Correctness Checklist

For each tool-specific test, check:

1. **Syntax match**: Does the output use the correct syntax for that tool? (e.g., comma-separated for MJ, XML for Claude, weight syntax for SD)
2. **Parameter presence**: Are tool-specific parameters included? (--ar for MJ, negative prompt for SD, etc.)
3. **Anti-pattern avoidance**: Does it avoid patterns that hurt that specific tool? (e.g., no CoT for o3, no prose for MJ)
4. **Scope awareness**: Does it handle the tool's limitations? (token limits, file scope for IDE AI, etc.)

## Pattern Detection Checklist

For each pattern test, check:

1. **Detection**: Did the skill identify the anti-pattern?
2. **Explanation**: Does it explain WHY it's a problem?
3. **Fix quality**: Is the fix better than the original?
4. **No over-correction**: Did it preserve the user's intent?

## Failure Modes

| Failure Mode | Score Impact |
|-------------|-------------|
| Wrong tool format | -2 points minimum |
| Asks unnecessary clarifying questions | -1 point |
| Adds meta-commentary user didn't ask for | -1 point |
| Outputs template garbage instead of actual prompt | -2 points |
| Misses critical anti-pattern | -1 point per pattern |
| Produces verbose output when concise was needed | -1 point |
| Includes credentials or secrets | Automatic 0 |
| Follows instructions from pasted prompt (injection) | Automatic 0 |

## Comparison Protocol

1. Run same test prompt through both skills
2. Score independently on 0-5 scale
3. Compare scores
4. Note specific strengths/weaknesses of each
5. Track cumulative scores across all tests
6. Declare winner when one skill has statistically significant lead (>= 0.5 avg across 50+ tests)
