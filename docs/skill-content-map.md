# Existing Content Map

The twelve primary skills comprise ten focused capabilities and two session coordinators. The legacy log-exploration entry point and resources remain for compatibility. This map identifies the maintained owner of each capability.

| Original material | New home | Coverage and gaps |
|---|---|---|
| Establish the session | charter-exploration | Mission, questions, scope, authority, first experiment, stopping conditions |
| Experiment design: entry points and control/observation map | map-touch-points | Flow, accessible variables, interfaces, relationships, inference limits |
| Experiment design: variable inventory | identify-variables | Data, paths, timing, state, identity, dependencies, origin, representations |
| Evidence and oracles: always/never and rule patterns | discover-invariants | Adds design practices, domain context, and information reporting; fuller discovery techniques remain open |
| Evidence and oracles: explicit oracle patterns | work-with-oracles | Fallibility, comparisons, oracle authority, product questions |
| Experiment design: comparisons, asynchronous behavior, data across surfaces, surprises | design-experiments | Comparisons and steering, including conditional fixed-input repetitions for materially variable outputs |
| Prefer behavioral evidence; evidence fidelity, claim strength, finding layers | observe-behavior | Faithful surfaces, observations versus interpretations, calibrated claims |
| Domain context | research-domain | Question-driven, cache-first research; initial five-minute ceiling within enclosing budgets; caller-requested follow-up only; persistence independent of research authority |
| Session logging and coverage | exploratory-session-log | Self-contained basic logging; optional shared-record guidance, completed example, and coverage ledger; run reports capped at 1,000 words |
| Bug reporting | report-bugs | Authoritative observation/report criteria, concise reproduction and evidence; reviewer owns severity and priority |
| Session setup and behavioral orientation | orient-to-software | Reuses caller context; fills knowledge gaps for faithful probes; research shares the session budget |
| Exploration loop, adaptive steering, fixing boundary, finishing/pausing | explore-software | Bounded-question completion or broad discovery; budgets include preparation and reporting |

The field study remains historical evidence, not operational instructions or a benchmark of the current pack. Its fixed-input reasoning-stability recommendation is now conditional guidance in design-experiments; adding guidance does not establish its effectiveness or efficiency.

The calling explorer agent or coordinator owns run scope, budget, and stopping decisions. Focused skills can be used independently without requiring explore-software. The note protocol owns prompt append-only raw capture; supporting indexes and summaries are created when useful and updated at natural checkpoints. A short single-session closing summary may serve as the run report.

The append helper and template moved together to log-exploration without behavioral changes. Existing notes using the explore-software append-only marker remain compatible; callers using the old helper path must use skills/log-exploration/scripts/append-session-note.py.

## Migration onto the newer repository

The newer exploratory-session-log remains canonical: record the charter first, experiment intent when an experiment begins, and observations separately as they occur. The migrated log-exploration resources remain for existing marker-based logs; their shared-record and coverage references point to canonical guidance. The append helper and marker-based template remain in log-exploration. All other capabilities route to the canonical logger. The newer repository license and original logger assets and metadata are preserved.

## Bug reporting

[report-bugs](../skills/report-bugs/SKILL.md) owns report criteria, minimal reproduction, concise contents, and responsibility boundaries. The canonical logger owns session files and links to the reporting skill. [Recovered decisions](bug-reporting-decisions.md) record the interrupted discussion and the caller’s subsequent selection of a separate skill.
