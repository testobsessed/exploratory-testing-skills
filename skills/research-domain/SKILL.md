---
name: research-domain
description: Research user goals, domain terminology and rules, and common risks to inform software orientation and exploratory testing; reuse existing application research before gathering more.
---

# Researching the Domain

Build useful domain context for exploration: what users are trying to accomplish, terminology and domain rules, and common risks or failure patterns. Follow the current question; these topics have no fixed order. Documentation and repository access are useful, but neither is required.

Before researching, check the application's persistent index and read relevant linked research entries. If domain research already exists, reuse it and record gaps or contradictions. Do not automatically research more because the cache is incomplete, old, or contradictory; further research requires an explicit caller request.

When no cached domain research exists, timebox initial research to five minutes unless the caller specifies otherwise. Prioritize supplied canonical software documentation, then available repository material, then external sources as needed. Record source identity and applicable product/version; distinguish documented rules, domain conventions, and inferred expectations. Treat each source as fallible.

Use exploratory-session-log to record research as it happens, unless the user explicitly opts out of persistence. Reuse the active session and logging guidance already in context; index reusable entries at session closure or handoff. At the time limit, preserve partial results and unanswered questions and return to orientation. Do not extend research to fill every section. Research is input to hypotheses and experiments, not runtime proof.

If exploratory-session-log is unavailable, use the caller's shared record location: append dated research entries with scope, sources, interpretation, and gaps, and link them from a small application index. When logging is explicitly disabled, use only caller-provided or current-context research and return results directly; do not create a cache.
