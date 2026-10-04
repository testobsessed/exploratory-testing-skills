---
name: exploratory-session-log
description: "Record exploratory testing sessions with a charter first, append-only experiment and observation entries, and a final findings summary. Use during exploration or when preparing a session log for a user report or explorer handoff."
license: MIT
---

# Exploratory Session Log

Keep a live record linking findings to their experiments and observations. Logging is enabled unless the user opts out; then return findings directly without persistent records. Reuse the caller's scope, run, session, and record location. Do not repeat setup or chartering.

## Start the log

- Honor the caller's destination and format, then project conventions. Otherwise use `exploration/runs/<run-id>/sessions/<session-id>.md` in the target project. Without a repository, use a suitable writable application workspace and report its location. Git is not required. Disclose unavailable storage; do not claim unsaved records exist.
- Put the supplied charter first. A charter from the request is sufficient; obtain a missing charter before logged exploration. Start one raw log before substantive work. Each new charter starts a separate session file; the caller may also split a charter across sessions. Resume a file only for that same session, preserving its contents.
- Record the run start and any supplied or coordinator-established deadline once in the first log using available timing; subsequent sessions reference them. Reuse available timestamps to date entries; a separate clock call per entry is not required. Disclose unavailable timing rather than inventing it.

The starting structure is sufficient without reading another file; replace the charter placeholder. The existing [template](assets/session-log-start.md) is also available for copying.

```markdown
# Charter

{{charter}}

# Session log
```

## Record experiments and observations

- **Experiment:** Append the question, intended action, and relevant conditions before the action begins.
- **Observation:** Append what happened, including blocked attempts, useful evidence, and interpretation or the next question when relevant. Name the originating experiment when applicable; one experiment may have multiple observations. Distinguish runtime observations, source evidence, and hypotheses.

Use unique headings such as `### Experiment E1` and `### Observation O1`, or explicit anchors, for precise evidence links. Capture research, discoveries, decisions, contradictions, negative results, and rejected hypotheses promptly. Preserve chronology: never edit, reorder, replace, or delete earlier entries. Append corrections identifying the earlier entry, including corrections to summaries.

Append directly with available tools; do not routinely reread the whole growing log to add an entry. Keep enough setup and evidence to understand and reproduce the work. For large outputs, preserve artifacts at the agreed record location and link precise portions with a concise observation rather than repeatedly copying full output. Retrieve relevant entries for summaries or handoffs; do not defer raw capture until reporting.

## Potential problems and bug reports

Flag uncertain concerns as potential problems in Observations, stating expectation and actual behavior. Use [report-bugs](../report-bugs/SKILL.md) to decide whether and how to report a bug. Append qualifying reports in a `Bug reports` section linked to observations, without moving earlier entries.

## Close the session

Append a brief `Findings summary` with work performed, findings and impact, unresolved questions or contradictions, material limits, and useful next steps linked to raw entries. Include the stopping reason and elapsed time when known. Preserve uncertainty; mention research only briefly. A short single-session summary, including blocked startup, can serve as the run report. Multiple sessions or a caller request need a separate report, linked from session summaries. The run report is at most 1,000 words and much shorter for short runs; the cap is not a target.

Read [shared application records](references/application-records.md) when maintaining indexes or reusable summaries, or coordinating multiple sessions; create supporting records only when useful and index at closure or handoff. A [completed example](references/application-records.md#example-completed-log) is available if the entry structure needs illustration. For broad investigations where tracking neglected dimensions would help, use the optional [coverage ledger](references/coverage-ledger.md); it is not required paperwork.
