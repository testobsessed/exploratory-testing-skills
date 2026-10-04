# Using the exploratory testing skills

Call a focused skill by name when you need that capability, or ask `explore-software` to coordinate an exploratory session. The skills support web applications, desktop applications, services without a GUI, command-line tools, and other software. They are capabilities to use as needed, not a fixed sequence.

Reuse existing orientation, research, and caller-provided context. Use [orient-to-software](../skills/orient-to-software/SKILL.md) when missing knowledge prevents choosing a faithful first experiment, or when explicitly requested; a missing orientation.md alone does not trigger it. Its predefined charter is: “Explore the target software with all the information available, to discover what I can do with it.” Supply a bounded question or broad mission describing what you want to learn. The calling explorer agent or coordinator owns the mission, budget, charter list, and next selection. Focused skills contribute techniques and evidence within that shared context; they do not require explore-software or repeat session setup. Load only the guidance needed for the current question, reusing what is already in context.

## Defaults and supported overrides

State overrides in the request to the skill. A calling agent can also supply them. These are natural-language instructions, not command-line flags.

| Choice | Default | How to override or supply it |
|---|---|---|
| Target and startup | Use README or other obvious repository startup instructions | Supply a URL, endpoint, executable, or specific startup instructions |
| Total run duration | At most one hour across charters and sessions, including preparation, startup, exploration, record maintenance, and reporting | Supply another timebox, such as “Explore for two hours” |
| Orientation duration | At most five minutes including preparation, research, and closure, within the run deadline | “Use a ten-minute orientation timebox” |
| Initial domain research duration | At most five minutes when needed and no cached research exists, within the enclosing budget | “Timebox initial domain research to two minutes” |
| Further domain research | Reuse cached research; do not automatically refresh gaps or contradictions | Explicitly request additional research and describe its scope |
| Persistence | Keep raw session logs; create supporting records when useful and index at checkpoints | “Do not persist records; return findings directly”; research authority is unchanged |
| Information repository location | `exploration/` in the target application project, or an established project convention | Specify one shared application information directory |
| Session-log destination and format | Shared session paths and Markdown | Specify the log destination and required format |
| Session boundaries | A new charter starts a new session and separate log | Explicitly start additional sessions under the same charter |
| Diagnosis and fixes | Explore and report observed behavior; do not diagnose the code defect or fix production code | Explicitly request diagnosis or a fix; close or pause exploration before switching to implementation |
| Temporary instrumentation | Only when authorized by the request or project conventions; remove afterward | Explicitly authorize harnesses or instrumentation, and request retention if wanted |

Timeboxes are ceilings, not durations to fill. Record the run's start and deadline once, using available execution timestamps and clock checks at useful decision points. Include instruction loading and reporting, reserve time to close, and disclose unavailable timing or overruns. Session limits do not reset the run deadline. Hard cancellation requires support outside the model.

Orientation for a bounded investigation ends once enough context exists to choose a faithful experiment. Explicit broad orientation may continue useful discovery within its ceiling. It also stops after three consecutive experiments yield no new information; increasing the timebox does not remove this rule. Research ends once enough context exists for its current question. During orientation, research shares the session's budget and leaves room for behavioral interaction when access permits; its own five-minute ceiling is not an extra allowance.

A bounded investigation ends when the evidence answers the caller's question to the requested confidence; out-of-scope leads remain follow-ups. A broad discovery mission continues useful charters within scope and budget. Both stop when no charters remain that could yield novel risk information, or abort after five consecutive experiments with pervasive obvious failures where every attempted operation encounters a problem and further exploration is unlikely to yield useful information. The final report records the stopping reason and retains unfinished charters.

Supply login information through the prompt, an environment variable, or an available credential-vault connection. Secrets do not belong in logs. If authentication blocks useful work and no usable login method is available, the explorer asks the caller.

## Where the results go

Within the shared application information directory:

```text
exploration/
  index.md
  orientation.md
  runs/
    <run-id>/
      charters.md
      sessions/
        <session-id>.md
      report.md
```

`orientation.md` is the single reusable summary of what can be done with the application. Later sessions read it rather than automatically rerunning orientation. When a user or agent intentionally runs orientation again, update relevant portions of that same summary in place, preserving useful knowledge and evidence links.

The layout above gives destinations, not a startup checklist. Begin with one raw log using the self-contained [logging skill](../skills/exploratory-session-log/SKILL.md). Load shared-record guidance for indexes, reusable summaries, or multiple sessions. Create an index for reusable entries, a charter list for multiple candidates or a resumable backlog, and orientation.md for learned capabilities or reusable access requirements. Index at natural checkpoints such as session closure or handoff. A startup blocked solely by the environment may need only its raw log and closing summary.

Raw session logs remain separate and append-only, with a charter first, experiments and observations recorded as they occur, bug reports when warranted, and a closing findings summary. One report spans the run’s sessions and is at most 1,000 words; a short single-session run may use its closing findings summary, while multi-session runs or an explicit caller request use a separate report. The report cap, append-only raw history, canonical `orientation.md` filename, and reviewer ownership of severity and priority are established conventions, not configurable defaults currently offered by these skills.

Append without routinely rereading the whole log. Keep large evidence artifacts separately with precise links and concise observations; retrieve relevant entries for handoffs and reporting. The coverage ledger is optional for broad investigations where it helps steer. Systems with materially variable outputs may need fixed-input repetitions before interpreting a changed-input comparison; this is conditional, not a step in every session.

See [shared application records](../skills/exploratory-session-log/references/application-records.md) and [report-bugs](../skills/report-bugs/SKILL.md) for the maintained operational rules.

## Example requests

- “Use orient-to-software on this repository. Allow ten minutes, and use `testing-knowledge/` for the application information repository.”
- “Use orient-to-software on https://example.test. Authentication is available through the configured credential vault.”
- “Use explore-software with the charter: explore profile-name handling for valid punctuation. Reuse existing orientation and research.”
- “Use research-domain to investigate the unresolved account-retention rules; limit additional research to three minutes.”
- “Explore the command-line import workflow. Do not persist records; return a brief findings summary.”
- “Reproduce this search behavior at the supplied URL using the provided login and steps. Stop when the question is answered; use at most ten minutes including reporting.”
- “Research the terminology needed for this import experiment. Do not save notes; use at most two minutes and return the sources and uncertainties directly.”

Skill instructions remain authoritative for the workflow. When changing a supported default or override, update this guide alongside the owning skill.
