---
name: explore-software
description: Coordinate adaptive, evidence-producing exploration around a charter. Use for behavioral investigations and reproductions, rather than implementation-only work or conventional test execution.
---

# Exploratory Sessions

Explore by simultaneously learning, designing experiments, executing them, interpreting results, and steering. Treat observed behavior as the territory and every model, requirement, document, and source reading as a potentially fallible map.

## Draw on capabilities as needed

Use the available focused skills when a question calls for them; they are not a fixed sequence. Load only the skill or reference needed for the current decision, and reuse guidance already in context. Do not preload the whole pack before the first behavioral probe. Keep one run context containing the mission, authority, elapsed budget, current charter, and record location; focused skills contribute to it without repeating setup. A calling explorer agent may own coordination directly; focused capabilities do not require this coordinator skill.

Available capabilities:

- charter-exploration: frame the mission, scope, authority, and stopping conditions;
- map-touch-points: discover connected places to control and observe behavior;
- identify-variables: identify conditions and values that could influence behavior;
- discover-invariants: surface candidate always and never rules;
- work-with-oracles: assess expectations and comparisons;
- design-experiments: choose variations that discriminate among explanations;
- observe-behavior: obtain faithful evidence and calibrate claims;
- exploratory-session-log: preserve raw notes, evidence, coverage, and questions by default;
- research-domain: reuse or gather timeboxed domain context for orientation;
- orient-to-software: build context when unfamiliar with the software.

The loop below remains usable when a focused skill is unavailable. Establish one raw session log before substantive exploration unless the user opts out; honor their format and location. Preserve intent, observations, and blockers as they occur. Create supporting records only when they have useful content, and update the application index at session closure or handoff. At run closure, report with links to raw evidence and a maximum of 1,000 words; a short single-session run may use its closing findings summary as the report. If logging guidance is unavailable, append dated raw records in the caller's workspace without deferring capture until reporting.

## Steer the run toward risk

The caller supplies the initial mission or charter. Maintain a running charter list beginning with that initial charter. Reuse existing orientation and caller-provided context. Use orient-to-software only when missing knowledge prevents choosing a faithful first experiment; the absence of orientation.md does not itself require an orientation session. Use charter-exploration to carve broad missions into focused charters and add new candidates as observations reveal interesting behavior within the mission.

Keep the initial charter in the raw session log. Create runs/<run-id>/charters.md when multiple candidates need tracking or the run needs a resumable backlog, unless the caller supplies another location or opts out of persistence. Record each charter's mission, status, priority rationale, and links to the observations and sessions that informed it. Preserve completed and unfinished charters rather than deleting their history.

Steer toward risk: prioritize novel information and the likelihood of undesirable behavior based on existing observations and all available evidence. Reassess priorities as information emerges and after each session. For a broad discovery mission, automatically select the next promising charter without asking the caller to approve each selection. For a bounded question, continue only while more evidence is needed to answer it to the requested confidence. A new charter starts a new session and log; the caller may also split one charter across multiple sessions. Keep the running list and the next selection within the caller's mission and authority.

## Run the exploration loop

1. Identify the current question and relevant variables, states, paths, or dependencies.
2. Choose an experiment that discriminates among plausible explanations.
3. State what will be controlled, varied, and observed.
4. Exercise actual behavior through the most faithful available interface; explain material fidelity gaps.
5. Record setup, action, observation, interpretation, and the resulting next question promptly.
6. Update the working model. Preserve disproved hypotheses, findings, and negative results.
7. Let the result determine the next useful experiment.

Begin with a small experiment likely to teach something. Do not turn the charter into a comprehensive test script before interacting with the software. Use source and documentation to form hypotheses and explain established behavior; do not treat source inspection alone as runtime proof. Report observed facts separately from product judgments.

## Keep exploration distinct from fixing

An instruction to explore, investigate, reproduce, or characterize does not by itself authorize a production-code fix. Repository changes needed solely to preserve default exploration records (unless the user opts out) are in scope. Create temporary instrumentation or harnesses only when authorized by the request or repository conventions; identify them in the notes and remove them afterward unless the user asks to retain them.

When the user asks to fix a confirmed problem, close or pause the exploration record first. Summarize the evidence and remaining uncertainty before switching to implementation.

## Finish or pause deliberately

Finish the current charter when its question is answered, further experiments would yield no useful new information, or another charter has greater information value. Update the list; continue with the next charter only while the mission still needs investigation and the run remains within its limits. Pause when useful continuation requires missing authority or information.

Record the run's start and deadline once in the first raw log, or in the active run context when persistence is disabled. Include instruction loading, startup, orientation, research, record maintenance, and reporting in the elapsed budget; do not reset it per charter. Reuse timestamps supplied by the execution environment, checking the clock at decisions such as starting a potentially long operation or selecting another charter. Leave enough time for a proportionate closing report. If reliable timing is unavailable, disclose that limit rather than inventing elapsed time. A prompted timebox does not independently enforce a hard deadline.

End the overall run at the first applicable stopping condition:

- The caller's bounded question is answered to the requested confidence. Preserve useful out-of-scope leads as follow-up candidates rather than extending the mission to pursue them.
- The total run timebox is reached: one hour by default across all charters and sessions. Honor a caller-specified timebox; it is a maximum, not a duration to fill. Stop experiments early enough to close within it. A longer budget does not remove the other stopping conditions.
- No charters remain to pursue: the available evidence offers no further identified source of novel risk information. This is exhaustion of the current candidate list, not proof that the software has no undiscovered risks.
- Abort after five consecutive experiments in which every attempted operation encounters an obvious problem and failures are so pervasive or catastrophic that further exploration is unlikely to yield valuable new information, such as every operation returning HTTP 500 or another error. Count consecutive experiments across charter and session boundaries; reset the streak when an experiment no longer meets this condition. Do not treat five distinct, informative defect discoveries as pervasive failure by themselves.

Record the stopping or pause reason, elapsed time when known, and any overrun, preserving evidence and unfinished charters with their current priorities. Do not claim exhaustive coverage merely because many cases ran.

Conclude with what was explored, confirmed findings and their evidence, unresolved surprises, rejected and untested hypotheses, material coverage gaps, useful next experiments, and the disposition of temporary artifacts. A session does not pass or fail.
