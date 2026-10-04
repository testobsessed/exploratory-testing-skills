# Durable Session Notes

This protocol preserves existing logs using the explore-software append-only marker. Use [exploratory-session-log](../../exploratory-session-log/SKILL.md) for new sessions and common logging rules. Read [application-records.md](application-records.md) when legacy callers need shared-record guidance. User-provided format and location instructions override this protocol.

## Start the record

When an existing integration requires a marker-based file, create it before substantive exploration. Adapt `../assets/session-notes-template.md` and capture:

- target and mission;
- known surprises or seed questions;
- expectations and other oracles;
- starting artifacts, build, and environment;
- behavioral interfaces and observation surfaces;
- authorized mutations and explicit exclusions;
- initial dimensions worth varying;
- stopping or check-in conditions.

Do not silently expand authorization. State whether source changes, persistent test additions, temporary diagnostic harnesses, external systems, or destructive experiments are allowed.

## Preserve a raw append-only stream

Treat everything under the active `## Experiments and Findings` heading as immutable after writing it.

- Append each meaningful experiment, discovery, correction, decision, or blocker promptly.
- Never edit, reorder, compress, or delete an earlier raw entry.
- Correct an error by appending a new entry that identifies the earlier entry and explains the correction.
- Preserve failed experiments, negative results, and hypotheses ruled out.
- Do not maintain an in-place running summary in the raw stream.
- Record temporary files or instrumentation and whether they were removed or retained.

Use `../scripts/append-session-note.py` to append entries when practical. It enforces the closed-session and repository-boundary checks.

An entry should communicate, in whatever compact form fits the work:

- **Question:** what the experiment was intended to learn;
- **Setup:** relevant build, state, artifact, configuration, and controlled variables;
- **Action:** what was done;
- **Observation:** what actually happened;
- **Interpretation:** what the observation might mean and how confident that interpretation is;
- **Next:** what follows from the result.

Do not force all six labels into trivial entries, but do not omit information needed to understand or reproduce the work.

## Close or pause

Append `## Summary` only when closing or pausing the session. Follow the [canonical closing rules](../../exploratory-session-log/SKILL.md#close-the-session), retaining this legacy heading for helper compatibility. Do not rewrite the raw stream while producing a summary. Select what matters from:

1. the charter and scope actually covered;
2. confirmed findings with evidence;
3. surprises or product questions not yet judged defects;
4. results that were not reproduced;
5. rejected and surviving hypotheses;
6. material coverage gaps and remaining unknowns;
7. useful next experiments;
8. the disposition of temporary artifacts.

If exploration resumes after a summary, use the append helper's `--continue` option. It appends a new continuation and raw-stream section after the previous summary; it does not alter the earlier record.

## Keep the record epistemically clear

Name whether a claim is observed, reproduced, a confirmed cause, a supported explanation, a hypothesis, not reproduced, an open question, a surprise, or a defect. Keep the evidence supporting that claim explicit. In particular, do not quietly turn a source-reading hypothesis into a finding, an unexplained difference into a defect, or a non-reproduction into proof that the reported behavior cannot occur.
