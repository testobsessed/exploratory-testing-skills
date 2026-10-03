---
name: explore-software
description: Coordinate adaptive, evidence-producing exploration around a charter. Use for behavioral investigations and reproductions, rather than implementation-only work or conventional test execution.
---

# Exploratory Sessions

Explore by simultaneously learning, designing experiments, executing them, interpreting results, and steering. Treat observed behavior as the territory and every model, requirement, document, and source reading as a potentially fallible map.

## Draw on capabilities as needed

Use the available focused skills when a question calls for them; they are not a fixed sequence:

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

The loop below remains usable when a focused skill is unavailable. Use logging guidance before substantive exploration unless the user explicitly opts out; honor their format and location. Maintain the application index promptly and produce one proportionate report per run, spanning its sessions, with links to raw evidence and a maximum of 1,000 words. If logging guidance is unavailable, append dated raw records immediately and maintain a small topic index in the caller's workspace; do not defer capture until reporting.

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

Stop or pause when the charter is answered, the next experiment requires new authority or information, further information would not change a decision, or another question now has greater value. Do not claim exhaustive coverage merely because many cases ran.

Conclude with what was explored, confirmed findings and their evidence, unresolved surprises, rejected and untested hypotheses, material coverage gaps, useful next experiments, and the disposition of temporary artifacts. A session does not pass or fail.
