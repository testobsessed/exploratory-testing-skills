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

Use exploratory-session-log to record meaningful discoveries and decisions promptly in the raw session log and index reusable information, unless the user explicitly asks not to log. Reuse the current application records when invoked within an existing run. If that skill is unavailable, append dated evidence and uncertainties in the caller's shared workspace and link reusable entries from its application index.

## Slice a broad mission into charters

The caller supplies the initial mission or charter; it may be as broad as “Explore DuckSim to discover unknown unknowns.” Use existing orientation, variables, observations, and other available evidence to carve off focused charters that can yield useful information. When orientation is missing, use orient-to-software to establish what can be done with the target.

Steer toward risk: favor the novelty of information a charter could reveal and the likelihood of undesirable behavior, grounded in existing observations and all other available information. Explain the evidence behind each candidate's priority; do not invent numerical risk scores or mistake an untested suspicion for a finding.

Give each candidate a concise mission, the question or risk it investigates, and why pursuing it could yield new information. Revise candidates and their priorities as findings emerge. Avoid repeating established information unless a new variation or contradiction makes further exploration informative.

The explore-software orchestrator owns the running charter list and automatically selects the next charter. Chartering supplies focused missions and priority reasoning; each selected charter starts a separately logged session. A broad mission is an adaptive exploration plan, not a predetermined experiment script.
