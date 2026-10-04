# Existing Content Map

This split maps the original explore-software material into nine focused capabilities and two session coordinators. It preserves the existing touch point mapping edit. Domain research and shared record conventions extend the split with user-defined research and persistence boundaries.

| Original material | New home | Coverage and gaps |
|---|---|---|
| Establish the session | charter-exploration | Mission, questions, scope, authority, first experiment, stopping conditions |
| Experiment design: entry points and control/observation map (existing uncommitted addition) | map-touch-points | Flow, accessible variables, interfaces, relationships, inference limits |
| Experiment design: variable inventory | identify-variables | Data, paths, timing, state, identity, dependencies, origin, representations |
| Evidence and oracles: always/never and rule patterns | discover-invariants | Adds design practices, domain context, and information reporting; fuller discovery techniques remain open |
| Evidence and oracles: explicit oracle patterns | work-with-oracles | Fallibility, comparisons, oracle authority, product questions |
| Experiment design: comparisons, asynchronous behavior, data across surfaces, surprises | design-experiments | Substantial comparison and steering guidance |
| Prefer behavioral evidence; evidence fidelity, claim strength, finding layers | observe-behavior | Faithful surfaces, observations versus interpretations, calibrated claims |
| Domain context (new) | research-domain | User goals, terminology/rules, risks; cache-first, five-minute initial research; caller-requested follow-up only |
| Session notes protocol, template, append helper; coverage ledger | exploratory-session-log | Default raw logs, persistent evidence index, run reports capped at 1,000 words; helper and legacy marker unchanged |
| Session setup and source orientation | orient-to-software | Relies on cache-first domain research and default shared logging; fuller behavioral orientation techniques remain open |
| Exploration loop, adaptive steering, fixing boundary, finishing/pausing | explore-software | Coordinator retains its existing name and invocation |

The field study remains historical evidence, not operational instructions. Its suggested fixed-input reasoning-stability check remains a future experiment-design improvement; this content split does not claim to implement that recommendation.

The calling explorer agent or coordinator owns run scope, budget, and stopping decisions. Focused skills can be used independently without requiring explore-software. The note protocol owns prompt append-only raw capture; supporting indexes and summaries are created when useful and updated at natural checkpoints. A short single-session closing summary may serve as the run report.

The append helper and template moved together to log-exploration without behavioral changes. Existing notes using the explore-software append-only marker remain compatible; callers using the old helper path must use skills/log-exploration/scripts/append-session-note.py.

## Migration onto the newer repository

The newer exploratory-session-log remains canonical: record the charter first, experiment intent when an experiment begins, and observations separately as they occur. The migrated log-exploration resources remain for existing marker-based logs. All other capabilities route to the canonical logger. The newer repository license and original logger assets and metadata are preserved.

## Bug reporting

[report-bugs](../skills/report-bugs/SKILL.md) owns report criteria, minimal reproduction, concise contents, and responsibility boundaries. The canonical logger owns session files and links to the reporting skill. [Recovered decisions](bug-reporting-decisions.md) record the interrupted discussion and the caller’s subsequent selection of a separate skill.
