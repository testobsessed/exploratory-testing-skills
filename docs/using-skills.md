# Using the exploratory testing skills

Call a focused skill by name when you need that capability, or ask `explore-software` to coordinate an exploratory session. The skills support web applications, desktop applications, services without a GUI, command-line tools, and other software. They are capabilities to use as needed, not a fixed sequence.

For unfamiliar software, use [orient-to-software](../skills/orient-to-software/SKILL.md). Its predefined charter is: “Explore the target software with all the information available, to discover what I can do with it.” For later exploration, supply a charter describing what you want to learn; reuse the application’s existing orientation and research.

## Defaults and supported overrides

State overrides in the request to the skill. A calling agent can also supply them. These are natural-language instructions, not command-line flags.

| Choice | Default | How to override or supply it |
|---|---|---|
| Target and startup | Use README or other obvious repository startup instructions | Supply a URL, endpoint, executable, or specific startup instructions |
| Orientation duration | Five minutes for the orientation session | “Use a ten-minute orientation timebox” |
| Initial domain research duration | Five minutes when no cached research exists | “Timebox initial domain research to two minutes” |
| Further domain research | Reuse cached research; do not automatically refresh gaps or contradictions | Explicitly request additional research and describe its scope |
| Persistence | Write session logs and maintain the application index | “Do not persist records; return findings directly” |
| Information repository location | `exploration/` in the target application project, or an established project convention | Specify one shared application information directory |
| Session-log destination and format | Shared session paths and Markdown | Specify the log destination and required format |
| Session boundaries | A new charter starts a new session and separate log | Explicitly start additional sessions under the same charter |
| Diagnosis and fixes | Explore and report observed behavior; do not diagnose the code defect or fix production code | Explicitly request diagnosis or a fix; close or pause exploration before switching to implementation |
| Temporary instrumentation | Only when authorized by the request or project conventions; remove afterward | Explicitly authorize harnesses or instrumentation, and request retention if wanted |

Orientation also stops after three consecutive experiments yield no new information, even if time remains. Increasing its timebox does not remove that stopping rule. Orientation’s five-minute session budget and domain research’s five-minute initial-research budget are separate limits; research performed during orientation consumes the session’s elapsed time.

Supply login information through the prompt, an environment variable, or an available credential-vault connection. Secrets do not belong in logs. If authentication blocks useful work and no usable login method is available, the explorer asks the caller.

## Where the results go

Within the shared application information directory:

```text
exploration/
  index.md
  orientation.md
  runs/
    <run-id>/
      sessions/
        <session-id>.md
      report.md
```

`orientation.md` is the single reusable summary of what can be done with the application. Later sessions read it rather than automatically rerunning orientation. When a user or agent intentionally runs orientation again, update relevant portions of that same summary in place, preserving useful knowledge and evidence links.

Raw session logs remain separate and append-only, with a charter first, experiments and observations recorded as they occur, bug reports when warranted, and a closing findings summary. One run report spans the run’s sessions and is at most 1,000 words. The report cap, append-only raw history, canonical `orientation.md` filename, and reviewer ownership of severity and priority are established conventions, not configurable defaults currently offered by these skills.

See [shared application records](../skills/exploratory-session-log/references/application-records.md) and [report-bugs](../skills/report-bugs/SKILL.md) for the maintained operational rules.

## Example requests

- “Use orient-to-software on this repository. Allow ten minutes, and use `testing-knowledge/` for the application information repository.”
- “Use orient-to-software on https://example.test. Authentication is available through the configured credential vault.”
- “Use explore-software with the charter: explore profile-name handling for valid punctuation. Reuse existing orientation and research.”
- “Use research-domain to investigate the unresolved account-retention rules; limit additional research to three minutes.”
- “Explore the command-line import workflow. Do not persist records; return a brief findings summary.”

Skill instructions remain authoritative for the workflow. When changing a supported default or override, update this guide alongside the owning skill.
