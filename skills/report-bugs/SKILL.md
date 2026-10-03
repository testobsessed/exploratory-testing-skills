---
name: report-bugs
description: Write concise exploratory-testing bug reports for reliably reproducible specification violations or behavior obviously wrong in context. Record reports in the current session log; keep uncertain or unreliable failures as observations.
---

# Bug Reporting

The explorer surfaces risks and information. Make judgments needed to choose what to explore and describe findings; leave severity and priority to the reviewer. Resolving product uncertainty is not the explorer’s responsibility.

## Observation or bug report

When the specification does not state expected behavior, use judgment about what is reasonable, informed by the domain research already available. Log the expectation and actual observation and flag an uncertain concern as a potential problem. Do not require agreement or resolution before supplying that information.

A bug report is warranted when observed behavior violates a specification, if one exists, or is obviously wrong in context, and the problem can be reproduced reliably. For example, a valid last name such as O’Brien causing a catastrophic error on a contact or profile form is obviously wrong: the user took a reasonable action. This example does not establish the technical cause.

Isolate the simplest steps that still reproduce the problem. If a failure cannot be reproduced reliably, keep it in Observations rather than promoting it to a bug report.

## Report contents and destination

Append each report in a `Bug reports` section of the current session’s exploration log. Include:

- A short descriptive title capturing the failure or incorrect behavior.
- The simplest reproducible steps, including input or conditions necessary to reproduce it.
- The nature of the problem as observed, the expectation, and actual observed behavior.

Link supporting observations where useful. Keep reports concise for readers with basic project context; do not expand them to educate readers about the project. Do not assign severity or priority.

Stick to what the explorer observed. Unless the caller explicitly requests otherwise, do not spend exploration effort locating the exact code defect, offering a suspected cause, or fixing it. Reproducible steps can be handed to another agent to locate and fix the defect without duplicating that agent’s work.
