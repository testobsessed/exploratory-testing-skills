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

Use exploratory-session-log to record meaningful discoveries and decisions promptly in the raw session log and index reusable information, unless the user explicitly asks not to log. Reuse the current application records when invoked within an existing run. If that skill is unavailable, append dated evidence and uncertainties in the caller's shared workspace and link reusable entries from its application index.
