---
name: discover-invariants
description: Identify always and never expectations and their applicable scope when exploring software behavior.
---

# Discovering Invariants

Identify candidate domain rules that should hold across inputs, sequences, configurations, and failures. Sources include canonical documentation, available repository material, cached domain research, user goals, and good design practices for the interface being explored. These are useful inputs, not prerequisites. Infer candidate rules from domain relationships and observed workflows as well as explicit always/never statements. Use research-domain for domain context within its cache and research limits.

For example, saving a form that receives a server error while leaving the user blocked with no useful feedback challenges a design expectation that users receive meaningful feedback on their actions. Record the visible outcome, response evidence, expectation source, and user impact separately.

Existing patterns include:

- conservation: data, work, money, defects, or records do not appear or disappear without a modeled event;
- isolation: actions on one user, scenario, tenant, stream, or object do not unexpectedly affect another;
- temporal integrity: delayed results apply to the state or candidate actually evaluated.

Record why each candidate should hold and the conditions in which it applies. Treat a candidate as a fallible expectation, not an established fact. Use [report-bugs](../report-bugs/SKILL.md) as the authority for deciding whether an observation warrants a bug report. An unresolved expectation remains a product question unless the behavior meets that skill's reporting criteria; explicit stakeholder agreement is not required for reliably reproducible behavior that is obviously wrong in context.

Surface information for the human or downstream agent to decide what to do; stakeholder agreement is not a prerequisite to reporting a surprise. This skill need not adjudicate or argue whether intended behavior is acceptable. Preserve candidate rules and contradictory evidence promptly in the existing raw log, using exploratory-session-log by default unless the user opts out. Index reusable entries at session closure or handoff; do not repeat run setup or load logging guidance already in context.
