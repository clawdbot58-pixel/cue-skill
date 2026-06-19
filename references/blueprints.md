# CUE Blueprints

Reference file for detailed prompt structures. Read when building a specific prompt type.

---

## System Prompt Blueprint

```
# IDENTITY
[Name + role + expertise + personality]

# CORE CAPABILITIES
[Abilities with scope boundaries]

# BEHAVIORAL RULES
- [Rule with reasoning]

# TOOL USAGE
[When to use which tools, priority, fallbacks]

# OUTPUT FORMAT
[Default format + special cases]

# BOUNDARIES
[What NOT to do + escalation triggers]

# EXAMPLES
[2-3 interactions showing correct behavior]
```

Anti-pattern: Generic "You are a helpful assistant." Always specify domain expertise.

---

## Agent Prompt Blueprint

```
# AGENT IDENTITY
[Name + specialization + autonomy level]

# OBJECTIVE
[Mission with success criteria]

# WORKFLOW
1. [Step] — [Action]
2. [Step] — [Action]

# TOOL PRIORITY
1. [Primary tool + when]
2. [Fallback + when]
3. [Manual reasoning + when tools fail]

# STATE MANAGEMENT
[What to remember across turns]

# ERROR HANDLING
[Recovery + escalation]

# OUTPUT RULES
[Format + delivery tags]
```

Key: Define step budget. Unlimited steps = infinite loops.

---

## User Prompt Blueprint

Simple (1-2 requirements): output ONLY the prompt, no extras.
```
[Role if needed] [Action] + [Deliverable]
[Constraints: length, format]
[Output structure]
```

Medium/Complex: add context, examples as needed.

Rule: One task per prompt. Don't add meta-sections to simple prompts.

---

## Design Description Blueprint

```
# CONCEPT
[One-sentence essence]

# VISUAL DIRECTION
- Style: [e.g., Minimalist / Brutalist / Glassmorphism]
- Mood: [e.g., Calm / Energetic / Premium]
- Color: [Palette with hex codes]
- Typography: [Font family + weight hierarchy]

# COMPOSITION
- Layout: [Grid / Asymmetric / Centered]
- Hierarchy: [Eye flow: first → second → third]

# ELEMENTS
[Each with: purpose, style, position, behavior]

# INTERACTIONS
[Hover, animations, transitions, responsive]

# CONSTRAINTS
[Technical limits, accessibility, brand rules]

# REFERENCES
[Comparable designs, mood boards]
```

Rule: Always include "Why" for each choice.

---

## Meta-Prompt Blueprint

```
# TEMPLATE
[Role with {role} variable]
[Action with {task} variable]
[Context with {context} variable]
[Examples with {examples} variable]
[Expectations with {format} variable]

# VARIABLES
| Variable | Description | Example |
|----------|-------------|---------|

# USAGE
[When to use + how to fill variables]
```

---

## Description Blueprint

```
# OVERVIEW
[What it is + why it matters]

# DEFINITION
[Precise technical/conceptual definition]

# COMPONENTS
[Parts with descriptions + relationships]

# HOW IT WORKS
[Process, mechanism, logic flow]

# USE CASES
[When and why someone would use this]

# EXAMPLES
[Concrete instances with context]
```

Tone: Neutral, informative. No persuasion unless requested.
