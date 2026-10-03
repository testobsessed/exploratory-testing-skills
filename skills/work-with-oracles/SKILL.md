---
name: work-with-oracles
description: Find and assess fallible expectations and comparisons to judge observed software behavior and distinguish surprises from defects.
---

# Working with Oracles

Use an oracle to explain why an observation matters. Read [references/oracle-patterns.md](references/oracle-patterns.md) when selecting a comparison or deciding whether surprising behavior is a defect.

Separate an observed result from the authority of the expectation. When stakeholders have not agreed that an oracle applies, preserve the observation and ask the product question.

Use exploratory-session-log to record meaningful discoveries and decisions promptly in the raw session log and index reusable information, unless the user explicitly asks not to log. Reuse the current application records when invoked within an existing run. If that skill is unavailable, append dated evidence and uncertainties in the caller's shared workspace and link reusable entries from its application index.
