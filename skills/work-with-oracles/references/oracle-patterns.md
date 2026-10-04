# Oracle Patterns

## Make the oracle explicit

An oracle is a fallible basis for evaluating behavior. Useful oracle patterns include:

- **Identity:** copies match after fields required to differ are normalized.
- **Round trip:** export/import or encode/decode preserves relevant meaning.
- **Path equivalence:** interfaces intended to perform the same operation produce equivalent state.
- **Conservation:** data, work, money, defects, or records do not appear or disappear without a modeled event.
- **Isolation:** actions on one user, scenario, tenant, stream, or object do not unexpectedly affect another.
- **Internal consistency:** related product surfaces behave or represent results consistently.
- **Representation consistency:** summaries and charts agree with underlying events and state.
- **Temporal integrity:** delayed results apply to the state or candidate actually evaluated.
- **Monotonicity:** changing a control in one direction does not produce the opposite effect without another mechanism explaining it.
- **Range or characteristics:** a complex result is plausible even when its exact value is difficult to predict.
- **Always/Never:** domain rules hold across inputs, sequences, configurations, and failures.
- **Comparable or standard:** behavior agrees with an applicable product convention, protocol, regulation, or agreed reference.

An oracle supplies an expectation, not automatic proof of a defect. Follow [report-bugs](../../report-bugs/SKILL.md) when classifying a finding; unresolved expectations remain product questions unless the observed behavior meets its reporting criteria.
