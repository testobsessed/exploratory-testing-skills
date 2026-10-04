---
name: research-domain
description: Research user goals, domain terminology and rules, and common risks to inform software orientation and exploratory testing; reuse existing application research before gathering more.
---

# Researching the Domain

Build useful domain context for exploration: what users are trying to accomplish, terminology and domain rules, and common risks or failure patterns. Follow the current question; these topics have no fixed order. Documentation and repository access are useful, but neither is required.

Before researching, reuse caller-provided context and any existing application index, reading only relevant linked research entries. If domain research already exists, reuse it and record gaps or contradictions. Do not automatically research more because the cache is incomplete, old, or contradictory; further research requires an explicit caller request. Within exploration, gather initial research only when a domain question needs answering to choose or interpret the next experiment. A standalone research request supplies its own research question.

When no cached domain research exists, initial research has a five-minute ceiling unless the caller specifies otherwise. Stop once enough context exists for the current question; the ceiling is not a duration to fill. Stay within any enclosing session or run deadline, leaving time for behavioral probes and closure. Prioritize supplied canonical software documentation, then available repository material, then external sources as needed. Record source identity and applicable product/version; distinguish documented rules, domain conventions, and inferred expectations. Treat each source as fallible.

Use exploratory-session-log to record research as it happens, unless the user explicitly opts out of persistence. Reuse the active session and logging guidance already in context; index reusable entries at session closure or handoff. When sufficient context exists or the time limit is reached, preserve partial results and unanswered questions and return to the caller's work. Do not extend research to fill every section. Research is input to hypotheses and experiments, not runtime proof.

If exploratory-session-log is unavailable, use the caller's shared record location: append dated research entries with scope, sources, interpretation, and gaps, indexing reusable entries at closure or handoff. Disabling logging changes persistence, not research authority: otherwise-authorized research may still use available sources under the same scope and time limits. When logging is disabled, keep notes in the current context and return results directly; do not create a persistent cache or records.
