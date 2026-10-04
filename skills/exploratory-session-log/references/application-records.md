# Shared Application Records

Use one persistent knowledge base per application, shared by these skills across runs. A run may contain multiple sessions. Honor the caller's location and existing project conventions; otherwise use `exploration/` in the application project, with:

- `index.md`: a small persistent topic index;
- `orientation.md`: the single reusable summary of what can be done with the application, maintained by orient-to-software;
- `runs/<run-id>/charters.md`: the orchestrator’s running charter list, with status, priority rationale, and evidence/session links;
- `runs/<run-id>/sessions/<session-id>.md`: raw session logs;
- `runs/<run-id>/report.md`: the run's summary report.

Without a repository, use a caller-specified or suitable writable application workspace and report its location. Do not require Git to log; append directly using the canonical logger, which does not require Git. Identify the application and version/environment to avoid mixing unrelated systems. Reuse an existing index rather than creating a parallel knowledge base. Create only records needed by the work. Start with a raw session log, recording startup failures there too. Create an index when reusable knowledge needs routing, a charter list when multiple candidates or a resumable backlog need tracking, and an orientation summary when application capabilities or reusable access requirements have actually been learned. A blocked startup may need only its raw log and closing summary. These paths describe destinations, not files to scaffold before exploration.

## Reusable orientation

Reuse established `orientation.md` and caller-provided context rather than rerunning orientation for every exploratory session. A missing summary does not require orientation when enough context exists for a faithful experiment. When orientation is needed or explicitly requested, update relevant portions of this same file in place; do not create another summary or replace it wholesale. Preserve useful knowledge, evidence links, and visible uncertainty. The summary is mutable; each session's raw log remains separate and append-only.

## Index

Use a compact table: **Topic | Kind | Scope | Date | Evidence link | Related/conflicting entries**. Kinds include domain research, touch points, variables, candidate invariants, oracles, observations, findings, and open questions. Link directly to stable raw-log headings or explicit anchors. The index routes readers to evidence; do not duplicate detailed findings in it.

Update the index at natural checkpoints such as session closure or handoff, after capturing reusable information in the raw log. Create it only when reusable entries warrant it. Future sessions check the index and read only relevant entries. Preserve links to both sides of a contradiction and flag their relationship; never silently replace earlier evidence. Capture the contradiction in the current raw log too. A gap or conflict does not authorize additional domain research.

## Shared raw-entry structure

Use dated, uniquely addressable entries. Capture **scope**, **sources/evidence**, **claim kind**, **interpretation/uncertainty**, and **related entries** where relevant. Distinguish documented rules, design or domain expectations, inferred rules, and behavioral observations. Preserve enough context to understand applicability and reproduce experiments. Partial records are valid; do not populate empty sections just to complete a form.

Domain research entries cover user goals, terminology and rules, risks, and unanswered questions as discovered. Experiment entries record intent at the start; separate Observation entries record outcomes and their interpretation, with links to the originating experiment. Record discoveries, decisions, corrections, and contradictions immediately; do not hold them in a separate scratch record for later consolidation.

## Run report

Follow the [logger's closing rules](../SKILL.md#close-the-session), including the 1,000-word maximum across the run. Put a separate report at `runs/<run-id>/report.md` when needed and link it from session summaries. Retrieve relevant entries and artifact portions, rather than rereading every raw log or duplicating their contents. Logs remain append-only when reports or indexes change.

Raw logging is a default part of every skill's work; index maintenance follows when reusable entries warrant it. Reuse the caller's active session rather than starting another run for each focused capability. Omit persistence when the user explicitly asks. In that case, do not create persistent records and return a proportionate summary directly. If persistence is blocked by permissions or unavailable storage, disclose the limitation; do not claim records were saved.

## Example completed log

This fictional example illustrates entry structure and available timestamps; its results are not evidence for another session. Other sessions in this run would reference the run timing rather than reset it.

```markdown
# Charter

Explore search-query handling with empty queries and whitespace variations.

# Session log

Run started: 2026-10-04T09:00:00-07:00. Deadline: 2026-10-04T09:05:00-07:00.

### Experiment E1

2026-10-04T09:00:10-07:00 — Submit a query containing only spaces to explore how an empty search is handled.

### Observation O1

2026-10-04T09:00:20-07:00 — From [E1](#experiment-e1): The page returns all results without an explanation. Compare a text query with and without surrounding spaces to investigate whitespace handling further.

### Experiment E2

2026-10-04T09:00:30-07:00 — Compare the results for `duck` and ` duck `.

### Observation O2

2026-10-04T09:00:45-07:00 — From [E2](#experiment-e2): Both queries return the same results.

# Findings summary

- A spaces-only query returns all results without an explanation ([O1](#observation-o1)). Whether this is intended remains an open question.
- Surrounding spaces did not change the results for the text query tested ([O2](#observation-o2)). Other queries remain untested.
- Closed at 09:01:00 (one minute elapsed): the bounded behavior question is answered; the product-intent question remains a follow-up.
```
