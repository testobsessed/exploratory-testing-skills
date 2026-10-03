---
name: exploratory-session-log
description: "Record exploratory testing sessions with a charter first, append-only experiment and observation entries, and a final findings summary. Use during exploration or when preparing a session log for a user report or explorer handoff."
license: MIT
---

# Exploratory Session Log

Keep a live record of an exploratory testing session so its findings can be traced to the experiments and observations that produced them. Chartering is a separate concern: record the supplied charter and follow the session's existing scope.

Logging is enabled by default unless the user explicitly asks not to persist records. Read [shared application records](references/application-records.md) for storage, the persistent application index, and the run report. Reuse the active run and session when called by another skill.

## Start the log

- Use the log destination specified by the user or delegating agent, or an established project convention. Default to a Markdown file when no other format is required.
- Put the session charter at the very top of the file, before the session entries. A charter already stated in the session request is sufficient; preserve its meaning rather than introducing another chartering process. If no charter is available, obtain it before starting the logged exploration.
- Use [the starting template](assets/session-log-start.md), replacing its charter placeholder before writing the file. It contains only the charter and the session-log heading. Add the findings summary when the session finishes.
- Read an existing log before continuing it. Preserve its existing contents.

## Record experiments and observations

The session body has two entry types:

- **Experiment:** A concise statement of the experiment being undertaken. State the action and the question it explores, with conditions needed to understand what was tried. Record it when the experiment starts.
- **Observation:** What was actually observed from an experiment. Include useful evidence or a reference to it, and explain how the observation informs the next experiment when that connection matters. Distinguish an observed result from an interpretation or hypothesis.

Use recognizable labels, such as `Experiment E1` and `Observation O1 (E1)`, so observations and findings can point back to their experiments. One experiment can produce several observations; do not impose a fixed number of entries or experiments.

Append entries to the end of the file as the session unfolds. Let observations guide the next small experiment, and record that experiment as its own entry when it begins. Keep the actual chronology instead of reconstructing a cleaner story afterward. An experiment statement records intent; its observation records what happened, including an inability to carry it out.

Do not edit, reorder, replace, or delete earlier entries. Correct a mistaken observation by appending another Observation that identifies the earlier entry and the correction. Preserve the original evidence and make the change in understanding visible.

Record research, discoveries, decisions, blockers, and contradictions promptly as Observation entries, distinguishing source evidence from runtime behavior. Index reusable entries immediately. Never keep a separate scratch record for later consolidation.

## Close the session

Append a brief `Findings summary` section at the bottom of the log, linking to the run report. Summarize findings that may interest the user or receiving agent, with references to the supporting entries. Include unresolved questions, limits of the exploration, or useful follow-up experiments when they affect what the recipient can conclude. Treat unexpected behavior as an observation until there is enough context to establish a defect.

At run closure or pause, produce one separate report across all sessions: at most 1,000 words, and much shorter for short runs. Briefly cover work performed, findings and impact, gaps, contradictions, and next steps with references to specific raw entries. Research receives only a brief mention.

Use this summary to guide the user-facing report or handoff to another agent, including an agent acting as an explorer. Point the recipient to the log and relevant evidence. Preserve uncertainty and avoid claims that the session did not establish. If a completed summary needs correction, append the correction or a revised summary; retain the earlier text.

## Example completed log

This example illustrates the structure; its experiments and results are not evidence for another session.

```markdown
# Charter

Explore search-query handling with empty queries and whitespace variations.

# Session log

- **Experiment E1:** Submit a query containing only spaces to explore how an empty search is handled.
- **Observation O1 (E1):** The page returns all results without an explanation. Compare a text query with and without surrounding spaces to investigate whitespace handling further.
- **Experiment E2:** Compare the results for `duck` and ` duck `.
- **Observation O2 (E2):** Both queries return the same results.

# Findings summary

- A spaces-only query returns all results without an explanation (O1). Whether this is intended remains an open question.
- Surrounding spaces did not change the results for the text query tested (O2).
```
