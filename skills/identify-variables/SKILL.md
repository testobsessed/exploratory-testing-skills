---
name: identify-variables
description: Identify conditions, values, states, and paths that could influence software behavior during exploratory testing.
---

# Identifying Variables

Identify anything whose value or condition could affect behavior. Look beyond visible inputs:

- data values, formats, sizes, counts, selections, and relationships;
- operation, input method, navigation path, order, repetition, and timing;
- current, prior, transitional, and persisted state;
- identity, random seed, cache, clock, and accumulated history;
- topology, configuration, permissions, resources, and external dependencies;
- loaded, restored, copied, imported, or interactively constructed origin;
- live runtime, saved representation, derived projection, and rendered view.

Use the variable map to choose meaningful variations; design comparisons around the current question rather than varying everything at once.

Use exploratory-session-log unless the caller opts out; reuse the active session and guidance already loaded. Capture raw evidence promptly, indexing at closure or handoff. Standalone requests need only a proportionate raw record; create supporting records when useful. If the logger is unavailable, append dated evidence in the caller's workspace.
