# Behavioral Evidence

Load this reference when choosing evidence, characterizing confidence, or reporting a finding.

## Prefer faithful evidence

Use the most faithful available evidence for the question:

1. reproduction through the real user-visible path;
2. reproduction through a faithful browser, component, CLI, or API path;
3. the user's exact artifact executed through the real runtime;
4. focused instrumentation or a diagnostic harness;
5. a direct domain-level experiment;
6. existing automated tests;
7. source inspection;
8. speculation.

This ordering is contextual, not absolute. A lower-level experiment can isolate a cause better, while a higher-level experiment establishes that users can encounter it. State any fidelity gap that could change the conclusion.

Source and documentation are maps. Use them to form hypotheses and explain observed behavior, but favor the territory when they disagree.

## Name the strength of the claim

- **Observed:** occurred during a recorded experiment.
- **Reproduced:** occurred repeatedly under stated conditions.
- **Confirmed cause:** isolating or changing the proposed cause changed behavior as predicted.
- **Supported explanation:** evidence fits the explanation, but alternatives remain.
- **Hypothesis:** plausible and awaiting a discriminating experiment.
- **Not reproduced:** attempted under stated conditions without observing it.
- **Open question:** material uncertainty remains.
- **Surprise:** behavior differs from an expectation whose authority is unresolved.
- **Defect:** observed behavior conflicts with an applicable oracle strongly enough to warrant correction.

Do not use “not reproduced” to mean impossible. Do not use “confirmed” when the evidence only shows correlation.

## Separate the layers of a finding

Record findings in this order:

1. **Observation:** externally verifiable behavior and evidence.
2. **Oracle:** the expectation or rule used for comparison.
3. **Impact:** what capability, user, data, or decision may be affected.
4. **Interpretation:** the best current explanation.
5. **Uncertainty:** alternatives, scope limits, and missing evidence.

This keeps credible behavioral evidence intact even when the explanation later changes.
