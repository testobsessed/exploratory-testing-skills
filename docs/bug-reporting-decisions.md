# Bug reporting decisions recovered from the interrupted session

Source: Codex session `01a103e9-f7e8-7990-b7ee-8020ceeb8eb7`, October 3, 2026, in `new-realtime-voice-chat-15`. The session ended before repository files were changed. Its final user statement was cut off; only the completed decisions are captured here.

The operational rules are in [bug reporting](../skills/report-bugs/SKILL.md) and [session logging](../skills/exploratory-session-log/SKILL.md):

- Unspecified expectations rely on reasonable judgment informed by existing research.
- Explorers provide information, rather than resolve uncertainty. Potential problems are observations recording expectation and actual behavior.
- Reports are for specification violations or behavior obviously wrong in context, such as a catastrophic error for the valid surname O’Brien.
- Reduce reproductions to the simplest reproducible steps. Unreliable failures stay in observations.
- Reports have a short descriptive title, reproduction steps, the observed problem, expectation, and actual behavior; readers are assumed to have basic project context.
- Stick to observations, leaving code diagnosis and fixes to another agent unless the caller asks otherwise.
- Reports belong in a section of the session’s exploration log.
- Each session has a separate file. A new charter always starts a session; the caller can split a charter across multiple sessions.
- Severity and priority belong to reviewers. Explorers surface risks and information and make the judgments necessary to guide exploration.

The caller subsequently selected a separate bug-reporting skill in the recovery session. The reporting guidance lives in `report-bugs`; the canonical logger routes to it.
