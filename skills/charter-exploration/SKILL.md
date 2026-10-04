---
name: charter-exploration
description: Break an exploratory testing mission into focused charters and revise their priorities as observations reveal new risks.
---

# Chartering Exploration

Clarify from the request and repository context:

- the mission or charter;
- known surprises, risks, and questions;
- the oracle: why a result would be significant;
- available artifacts and behavioral surfaces;
- permitted mutations, including whether temporary harnesses are allowed;
- the session-note location and stopping conditions.

Do not turn an exploratory charter into a comprehensive test script before interacting with the software. Identify a small first experiment that is safe and likely to teach something.

An instruction to explore, investigate, reproduce, or characterize does not by itself authorize a production-code fix. Repository changes needed solely to preserve default exploration records (unless the user opts out) are in scope. Create temporary instrumentation or harnesses only when authorized by the request or repository conventions.

Use the charter to bound the investigation; revise the questions as observations change the working model.

Use exploratory-session-log unless the caller opts out; reuse the active session and guidance already loaded. Capture raw evidence promptly, indexing at closure or handoff. Standalone requests need only a proportionate raw record; create supporting records when useful. If the logger is unavailable, append dated evidence in the caller's workspace.

## Slice a broad mission into charters

The caller supplies the initial mission or charter; it may be as broad as “Explore DuckSim to discover unknown unknowns.” Use existing orientation, variables, observations, and other available evidence to carve off focused charters that can yield useful information. When an exploratory run needs missing orientation, use orient-to-software to establish what can be done with the target. For a standalone chartering request, use available context and state gaps without starting orientation.

Steer toward risk: favor the novelty of information a charter could reveal and the likelihood of undesirable behavior, grounded in existing observations and all other available information. Explain the evidence behind each candidate's priority; do not invent numerical risk scores or mistake an untested suspicion for a finding.

Give each candidate a concise mission, the question or risk it investigates, and why pursuing it could yield new information. Revise candidates and their priorities as findings emerge. Avoid repeating established information unless a new variation or contradiction makes further exploration informative.

The calling agent or coordinator owns the running charter list, budget, and next selection. This skill supplies focused missions and priority reasoning without requiring a particular coordinator skill. Contribute to the current run when one exists; a standalone chartering request does not initiate an exploratory run. Each charter selected for execution starts a separately logged session. A broad mission is an adaptive exploration plan, not a predetermined experiment script.
