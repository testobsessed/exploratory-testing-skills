---
name: design-experiments
description: Choose controlled variations and comparisons that answer exploratory questions, distinguish explanations, and investigate delayed behavior.
---

# Designing Experiments

Identify the current question and choose an experiment that discriminates among plausible explanations. State what will be controlled, varied, and observed.

Do not vary everything at once. Choose a comparison that isolates a meaningful difference, then combine dimensions after finding a signal.

Read [references/experiment-design.md](references/experiment-design.md) when choosing comparisons, investigating asynchronous behavior, tracing data across surfaces, or following a surprise. Use observed results to choose the next useful experiment.

Use exploratory-session-log unless the caller opts out; reuse the active session and guidance already loaded. Capture raw evidence promptly, indexing at closure or handoff. Standalone requests need only a proportionate raw record; create supporting records when useful. If the logger is unavailable, append dated evidence in the caller's workspace.
