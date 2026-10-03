---
name: observe-behavior
description: Exercise faithful behavioral surfaces, compare observation points, and calibrate evidence and claims during software exploration.
---

# Observing Behavior

Use source code, documentation, and existing tests to orient, generate hypotheses, locate observation points, and explain established behavior. Do not treat source inspection alone as proof of runtime behavior when the behavior can reasonably be exercised.

Prefer the user's exact artifact and action path before synthetic approximations. When an exact path is impractical, explain the fidelity gap. Compare multiple observation surfaces when possible: user interface, exported or persisted state, API results, domain objects, events, logs, metrics, and rendered summaries.

Read [references/behavioral-evidence.md](references/behavioral-evidence.md) when choosing evidence, characterizing confidence, or reporting a finding. Record observations before interpreting them.

Use exploratory-session-log to record meaningful discoveries and decisions promptly in the raw session log and index reusable information, unless the user explicitly asks not to log. Reuse the current application records when invoked within an existing run. If that skill is unavailable, append dated evidence and uncertainties in the caller's shared workspace and link reusable entries from its application index.
