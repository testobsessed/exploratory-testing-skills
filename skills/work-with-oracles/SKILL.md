---
name: work-with-oracles
description: Find and assess fallible expectations and comparisons to judge observed software behavior and distinguish surprises from defects.
---

# Working with Oracles

Use an oracle to explain why an observation matters. Read [references/oracle-patterns.md](references/oracle-patterns.md) when selecting a comparison or deciding whether surprising behavior is a defect.

Separate an observed result from the authority of the expectation. When stakeholders have not agreed that an oracle applies, preserve the observation and ask the product question.

Use exploratory-session-log unless the caller opts out; reuse the active session and guidance already loaded. Capture raw evidence promptly, indexing at closure or handoff. Standalone requests need only a proportionate raw record; create supporting records when useful. If the logger is unavailable, append dated evidence in the caller's workspace.
