---
name: charter-exploration
description: Frame an exploratory testing mission, risks, scope, and stopping conditions before choosing the first experiment.
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
