---
name: log-exploration
description: Compatibility entry point for callers of the former exploration logger; use exploratory-session-log for new sessions.
---

# Logging Exploration Compatibility

Use exploratory-session-log as the canonical logging skill. Its charter-first, experiment-before-observation structure and shared application records govern new work. If unavailable, read [the canonical instructions](../exploratory-session-log/SKILL.md).

The references, template, and append helper in this directory are retained for existing logs with the explore-software append-only marker. Continue those logs without rewriting their history. Apply the canonical default logging, application indexing, conflict preservation, and per-run reporting rules to them. Do not create a second log or index solely because a caller used the legacy skill name.
