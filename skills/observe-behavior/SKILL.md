---
name: observe-behavior
description: Exercise faithful behavioral surfaces, compare observation points, and calibrate evidence and claims during software exploration.
---

# Observing Behavior

Use source code, documentation, and existing tests to orient, generate hypotheses, locate observation points, and explain established behavior. Do not treat source inspection alone as proof of runtime behavior when the behavior can reasonably be exercised.

Prefer the user's exact artifact and action path before synthetic approximations. When an exact path is impractical, explain the fidelity gap. Compare multiple observation surfaces when possible: user interface, exported or persisted state, API results, domain objects, events, logs, metrics, and rendered summaries.

Read [references/behavioral-evidence.md](references/behavioral-evidence.md) when choosing evidence, characterizing confidence, or reporting a finding. Record observations before interpreting them.

Use exploratory-session-log unless the caller opts out; reuse the active session and guidance already loaded. Capture raw evidence promptly, indexing at closure or handoff. Standalone requests need only a proportionate raw record; create supporting records when useful. If the logger is unavailable, append dated evidence in the caller's workspace.
