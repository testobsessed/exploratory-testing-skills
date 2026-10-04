# Delegating an exploratory investigation

Give an explorer agent a mission, access to focused skills, and a usable execution environment. The calling agent owns the delegation contract; the explorer may own charter selection and steering within it. A separate coordinator skill is optional.

## Define the assignment

Supply the target and checkout or destination, the bounded question or broad mission, total budget, permitted actions, and record location. Include existing orientation, access instructions, and other context needed for a faithful first experiment. Name the intended skills source when multiple versions or repositories exist. Ask the explorer to load capabilities as questions arise, reuse one run context, and record experiment intent and observations in a live append-only raw log. Create indexes and other supporting files only when useful; update them at closure or handoff.

Distinguish these permissions explicitly:

- **Run the software:** normal documented startup can generate caches, compiled artifacts, and other runtime files. Allow these when needed for the assignment, subject to the environment's execution approvals.
- **Change the software:** production source fixes and new diagnostic harnesses are separate actions. State whether either is authorized.
- **Keep records:** specify where raw logs and reports belong. Keeping logs outside the target repository does not prohibit ordinary startup writes inside it.
- **Use Git:** writing a file does not authorize staging, committing, or pushing it. State the applicable Git boundary separately.

Task authorization does not change sandbox permissions. If an authorized startup command is blocked, request the platform's scoped execution approval rather than concluding that startup is out of scope. Reuse installed dependencies where possible. Before downloading software, verify official project and publisher sources and follow the caller's supply-chain requirements.

## Establish runtime access

Read target instructions and the README, then attempt the documented startup when the caller has not supplied an already running destination. An absent localhost listener is a reason to start the application, not evidence that exploration cannot proceed. Confirm the resulting server address and process outcome.

Check separately that the agent can interact with the required interface. Browser automation, desktop controls, a supported CLI, and direct engine execution offer different fidelity. The presence of one shell tool does not establish browser access; failure of one browser provider does not establish that every available provider is unusable. Inspect available capabilities before choosing another path. Do not silently substitute source inspection or engine behavior for a user-interface investigation.

Keep startup blockers in the current raw log. Describe the attempted command or interface, the actual failure, and the next action needed. Ask the caller about a genuinely missing permission or capability before closing a longer run when resolution is practical. Repeated attempts must stay within the run budget.

## Use a compact delegation prompt

Adapt this example to the target; it is not a requirement to load every skill:

> Explore [target] to discover unexpected behavior that could affect [user goal]. Use focused skills from [verified skills location] as needed and own charter selection within this mission. Use at most [duration] for the entire attempt, including preparation, startup, record maintenance, and reporting; record the start and deadline and leave time to close. Reuse [available context]; orient only when knowledge is missing for a faithful experiment. Follow the target's instructions and attempt its documented startup using existing tools and dependencies. Normal generated startup files are allowed; request scoped execution approval if required. Production source fixes and new diagnostic harnesses are not authorized. Preserve live append-only raw evidence in [record location], reusing one run context and adding supporting records only when useful. Do not stage, commit, or push in the target repo. Report startup results and the first useful behavioral experiment. If access remains blocked, report what was attempted and the specific capability or authorization needed. Distinguish observed behavior from hypotheses and disclose fidelity limits.

For a bounded investigation, replace the broad discovery mission with the question and requested confidence, and ask the explorer to stop when it is answered. Adjust the diagnosis, harness, and Git clauses when the caller authorizes different actions. Give the agent only the permissions and tools needed for that assignment.

## Review execution and overhead

Check whether a runtime experiment actually occurred before interpreting the trial as evidence about testing effectiveness. Account for instruction reading, repository orientation, startup, and record maintenance separately where possible. A blocked startup can expose administrative overhead without establishing how the skills perform during productive exploration.

For unattended runs, enforce hard deadlines and action permissions outside the model. A prompted timebox is an instruction, not an independent cancellation mechanism. Do not claim stronger enforcement than the runtime supplies.

## Compare revisions before claiming efficiency gains

Use a small descriptive pilot before a larger restructuring: compare the current and proposed skill revisions on one bounded investigation and one broad charter against an accessible application. Identify the exact skill and application versions, keep the model, tools, permissions, starting state, and mission prompts the same, and repeat each condition several times in varied order. Isolate each trial's records and context to avoid leaking discoveries between conditions. Establish runtime access first; measure startup separately when it is part of the question.

Collect from execution traces where available:

- time to the first useful behavioral observation and total time including reporting;
- uncached, cache-write, and cache-read input tokens, plus output tokens, using the provider's category definitions;
- tool calls for instruction loading, runtime interaction, evidence reads, and record writes;
- useful, supported learning: grounded findings, meaningful negative results, and rejected hypotheses, without counting duplicate observations as new findings;
- evidence quality: faithful paths, sufficient reproduction context, calibrated claims, and whether a recipient can act without repeating the investigation.

Define the usefulness and evidence rubric before examining results, and assess findings without knowing the skill condition where practical. Report per-condition results and variation rather than treating a single run as proof. Instruction-size estimates are not execution token counts; cached input, generated output, elapsed time, and useful learning are distinct measures.

Evaluate reuse in a separate follow-up session for each condition, allowing only that condition's earlier records. Record both sessions' costs and what work the records save. Treat this as a planned comparison until trials have actually run; source review and the historical field study do not establish runtime savings.

## Lesson from the first DuckSim trial

The first trial found startup instructions, checked for an existing server, and tried an unavailable browser, but never attempted the documented dev-server command. The delegation treated ordinary generated files as forbidden target modifications; the parent then closed the attempt instead of resolving that restriction. No new DuckSim behavior was established.

The corrective lesson is to separate startup, source changes, record persistence, and Git actions. Preserve the original trial evidence and report this as a delegation/execution limitation rather than a missing README or a product defect. A subsequent trial must establish runtime access before assessing the exploratory method's effectiveness.
