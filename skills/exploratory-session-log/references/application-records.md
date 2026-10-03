# Shared Application Records

Use one persistent knowledge base per application, shared by these skills across runs. A run may contain multiple sessions. Honor the caller's location and existing project conventions; otherwise use `exploration/` in the application project, with:

- `index.md`: a small persistent topic index;
- `runs/<run-id>/sessions/<session-id>.md`: raw session logs;
- `runs/<run-id>/report.md`: the run's summary report.

Without a repository, use a caller-specified or suitable writable application workspace and report its location. Do not require Git to log; append directly using the canonical logger, which does not require Git. Identify the application and version/environment to avoid mixing unrelated systems. Reuse an existing index rather than creating a parallel knowledge base. Create only records needed by the work.

## Index

Use a compact table: **Topic | Kind | Scope | Date | Evidence link | Related/conflicting entries**. Kinds include domain research, touch points, variables, candidate invariants, oracles, observations, findings, and open questions. Link directly to stable raw-log headings or explicit anchors. The index routes readers to evidence; do not duplicate detailed findings in it.

Update the index promptly after logging reusable information. Future sessions check the index and read only relevant entries. Preserve links to both sides of a contradiction and flag their relationship; never silently replace earlier evidence. Capture the contradiction in the current raw log too. A gap or conflict does not authorize additional domain research.

## Shared raw-entry structure

Use dated, uniquely addressable entries. Capture **scope**, **sources/evidence**, **claim kind**, **interpretation/uncertainty**, and **related entries** where relevant. Distinguish documented rules, design or domain expectations, inferred rules, and behavioral observations. Preserve enough context to understand applicability and reproduce experiments. Partial records are valid; do not populate empty sections just to complete a form.

Domain research entries cover user goals, terminology and rules, risks, and unanswered questions as discovered. Experiment entries record intent at the start; separate Observation entries record outcomes and their interpretation, with links to the originating experiment. Record discoveries, decisions, corrections, and contradictions immediately; do not hold them in a separate scratch record for later consolidation.

## Run report

At the end or pause of a run, write one report spanning its sessions. Briefly cover work performed, key findings and user impact, unresolved questions or contradictions, material coverage gaps, and useful next steps. Include direct references to specific session-log entries. Mention research only briefly; its detail remains in the logs.

The report must be at most **1,000 words**, regardless of run length. Scale down sharply for short runs; the cap is not a target. Keep reporting proportional and do not repeat every raw entry. Logs remain append-only when reports or indexes change. Session findings summaries are brief entries pointing to the run report; they do not replace it.

Logging and index maintenance are default parts of every skill's work. Omit them only when the user explicitly asks. In that case, do not create persistent records and return a proportionate summary directly. If persistence is blocked by permissions or unavailable storage, disclose the limitation; do not claim records were saved.
