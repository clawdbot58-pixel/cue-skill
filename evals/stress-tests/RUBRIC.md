# CUE Stress Test — Scoring Rubric

## Complexity Dimensions

| Dimension | What It Tests | Escalation Levels |
|-----------|---------------|-------------------|
| **Reasoning Depth** | Multi-hop logic, counterfactuals, abduction | 2 steps → 5 steps → recursive self-verification |
| **Constraint Density** | Conflicting rules, hard limits, trade-offs | 1 constraint → 5 constraints → contradictory constraints requiring arbitration |
| **Context Volume** | Signal-to-noise ratio, long-range dependencies | 1K tokens → 50K tokens → buried critical info at 90% context depth |
| **Output Structure** | Schema complexity, cross-references, conditional formatting | JSON → nested JSON with references → self-validating schemas |
| **Ambiguity Resolution** | Vague inputs, missing prerequisites, implicit assumptions | Clear → implicit → actively misleading |
| **Meta-Cognition** | Prompts about prompts, self-correction, uncertainty quantification | Direct → reflective → adversarial self-audit |
| **Domain Fusion** | Cross-disciplinary reasoning | Single domain → two domains → three+ with conflicting terminology |
| **Temporal/Stateful** | Sequences, state changes, time-dependent logic | Static → sequential → branching timelines |

## Test-to-Dimension Mapping

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

## Scoring Metrics

| Metric | How to Measure | Target |
|--------|----------------|--------|
| **Constraint Adherence** | % of hard constraints satisfied | 85%+ |
| **Reasoning Transparency** | Can you audit why it made each decision? | Yes/No + quality |
| **Graceful Degradation** | When it fails, does it fail predictably and report it? | Fails with explanation |
| **Token Efficiency** | Does it solve complex tasks without burning context? | Under 2x baseline |
| **Self-Awareness** | Does it know when it doesn't know? | Reports uncertainty |

## Pass/Fail Interpretation

- **Full pass**: All assertions met, output is coherent and complete
- **Partial pass**: 70%+ assertions met, output shows understanding but has gaps
- **Fail**: <70% assertions met, or output is incoherent/missing critical elements
- **Graceful degradation**: Failed assertions are acknowledged in output (e.g., "I couldn't verify X because...")

## Stacking Instructions

For maximum difficulty, stack injections:

1. Start with Seed Prompt (Level 1)
2. Add Injection 1 (Constraint Conflicts)
3. Add Injection 3 (Multi-Format Output)
4. Add Injection 5 (Adversarial Input)
5. Add Injection 7 (Recursive Meta-Prompt)
6. Add Injection 6 (Stateful Multi-Turn)

Each injection should be applied ON TOP of previous ones. Run the stacked version and measure degradation.
