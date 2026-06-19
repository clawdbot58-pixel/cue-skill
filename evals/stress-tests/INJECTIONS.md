# Progressive Complexification Injections

Apply these ON TOP of any seed prompt. Each injection increases difficulty along specific dimensions.

## Seed Prompt (Level 1 — Baseline)

"Analyze the following customer feedback and categorize each complaint by department (Sales, Product, Support). Return a JSON array with 'id', 'department', and 'severity' (1-5)."

---

## Injection 1: Constraint Conflicts

Stack on top of seed:

"Same task, but: (a) if a complaint mentions 'refund' it MUST go to Sales even if it sounds like Product, (b) if severity would be 5, downgrade it to 4 unless the word 'urgent' appears twice, (c) never assign more than 40% of complaints to Support, (d) if a complaint contains sarcasm, ignore the literal meaning and classify by intent, (e) return results sorted by a custom key: severity × (1 + department_priority) where Sales=3, Product=2, Support=1."

**Dimension**: Constraint Density (5 conflicting rules requiring arbitration)

---

## Injection 2: Buried Context & Noise

Stack on top of seed:

"The feedback is embedded in a 15,000-word transcript of a company all-hands meeting. The actual feedback lines are not marked — they blend into casual conversation. Extract them first, then classify. Some 'complaints' are actually employees role-playing customer scenarios. Distinguish real vs. simulated complaints."

**Dimension**: Context Volume + Ambiguity Resolution

---

## Injection 3: Multi-Format Output with Cross-References

Stack on top of seed:

"Return: (1) the JSON array, (2) a markdown table summarizing department load distribution, (3) a 2-paragraph executive summary, and (4) a separate 'audit trail' explaining every classification decision with line-item references to the source text. The audit trail must reference the JSON by ID and the table by row number. If you change your mind during generation, document the revision."

**Dimension**: Output Structure + Cross-references

---

## Injection 4: Counterfactual & Hypothetical Reasoning

Stack on top of seed:

"Before classifying, consider: if the company had already fixed the top 3 issues from last quarter (which are not provided), how would that change the severity scores? Provide two outputs — 'actual' and 'counterfactual' — with a diff showing what changed and why. You must infer last quarter's top 3 issues from industry context."

**Dimension**: Reasoning Depth + Counterfactuals

---

## Injection 5: Active Adversarial Input

Stack on top of seed:

"Some feedback contains deliberate misdirection: 'I love the product but...' followed by a severe complaint. Some complaints are written in second person ('You guys messed up my order') but refer to a competitor's service. Some are in reverse chronological order within nested quotes. Some severity indicators are negated ('not unimportant' = ?). Handle all of these without explicit flags."

**Dimension**: Ambiguity Resolution + Adversarial robustness

---

## Injection 6: Stateful Multi-Turn with Memory Decay

Stack on top of seed:

"This is turn 7 of a conversation. In turns 1-3, you established classification rules. In turn 4, the user overrode one rule. In turn 5, you were given new feedback that contradicted the override. In turn 6, you were told to 'forget everything before turn 4 except the original schema.' Now process this new batch of feedback using only the valid rule set — but the rules themselves are not restated in this prompt."

**Dimension**: Temporal/Stateful + Memory management

---

## Injection 7: Recursive Meta-Prompt

Stack on top of seed:

"Generate a prompt that would cause another AI to misclassify 30% of these complaints. Then generate a 'defense prompt' that would catch those errors. Then evaluate your own defense prompt for false positives. Return all three artifacts with confidence scores for each."

**Dimension**: Meta-Cognition + Recursive reasoning

---

## Stacking Order (Recommended)

For maximum difficulty, apply in this order:

1. **Injection 1** — Adds 5 conflicting constraints
2. **Injection 3** — Adds multi-format output with cross-references
3. **Injection 5** — Adds adversarial input handling
4. **Injection 7** — Adds recursive meta-prompting
5. **Injection 6** — Adds stateful multi-turn with memory decay

This stack tests: Constraint Density + Output Structure + Ambiguity + Meta-Cognition + Temporal/Stateful — all 5 primary dimensions simultaneously.
