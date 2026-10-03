# Field Study: `explore-software` in Discussion Copilot

## Purpose

This field study evaluated whether Elisabeth Hendrickson's `explore-software` skill changes an agent's default mode from code review or task execution into adaptive, evidence-producing exploration of real software behavior. The study used Discussion Copilot as the system under investigation and treated observed runtime behavior as primary evidence. Its purpose was to learn both about the product and about the investigative behavior encouraged by the skill.

## Charter

The agent was asked to investigate how Discussion Copilot derives meeting participants' decisions and action items. It would compare faithful transcript and audio input paths and look for missing, duplicate, or incorrectly attributed information. The scope was investigation only: no production fixes or persistent tests. The agent would maintain durable notes and pause after three experiments.

## Skill method in practice

The skill shaped the session around a charter and explicit oracles: conservation of decisions and commitments, correct attribution, no unexplained duplication, path equivalence, and consistency across representations. It encouraged the agent to:

- begin with a small experiment that could teach something;
- compare meaningful variables rather than enumerate a test script in advance;
- exercise the real UI and inspect persisted, API, and rendered evidence;
- let each observation determine the next useful experiment;
- maintain a durable, append-only session record;
- preserve uncertainty, negative results, and rejected hypotheses; and
- keep behavioral investigation separate from fixing the product.

The resulting sequence moved from an attributed transcript, to a comparable audio path, and then back to a controlled transcript variation that isolated repetition and ownership. That progression was driven by observations rather than by a prewritten checklist.

## Experiments and learning

### 1. Explicit decision, commitment, and rollback

A timestamped, speaker-attributed transcript contained an explicit decision, a delivery commitment, and a rollback requirement. Discussion Copilot preserved the decision, attribution, and ownership across the observed analysis and review surfaces. The delivery commitment was present, but it was represented through a decision or claim rather than through a dedicated action-item object.

This changed the working model: action semantics were not absent, but they were distributed across general analysis structures. A consumer expecting a first-class action list could therefore overlook information that the product had derived.

### 2. Comparable audio import

A comparable discussion imported through the real audio path preserved much of the decision and commitment meaning. However, transcription changed some content and assigned the conversation to `speaker_unknown`. The reasoning layer retained that upstream evidence rather than reconstructing participant identities, so individual ownership was withheld.

This comparison exposed an input-fidelity risk rather than simply a reasoning failure. Attribution and action ownership depended materially on the quality and identity information supplied by the upstream transcription path.

### 3. Repeated decision phrasing and scoped ownership

An attributed transcript repeated and paraphrased the same decision while distinguishing Priya's delivery commitment from Jordan's narrower review responsibility. The product produced one decision rather than duplicates and preserved the two responsibilities as distinct, correctly attributed commitments.

This was useful negative evidence: the seeded duplication and misattribution concern was not reproduced under clear, single-window language. It did not establish that ambiguous phrasing or cross-window repetition would behave the same way.

## Reasoning stability was not tested

The study did **not** repeat analysis of the exact same input. It compared different input paths and deliberately varied transcript content, so it cannot support a claim about run-to-run reasoning stability.

That remains an important AI-system risk. The same evidence may yield different decision counts, action counts, ownership, evidence links, wording, or omissions across runs even when the application and input are unchanged. Path fidelity and within-run attribution can be sound while repeated reasoning remains unstable.

## What the study taught us about the skill

The skill helped move the investigation from assumed explanations to an evidence-backed working model. In particular, it prompted a faithful path comparison that separated upstream attribution loss from downstream reasoning behavior. It also preserved a result that did not reproduce the suspected duplication problem instead of forcing the session toward a defect finding.

Its value is therefore not merely finding bugs. It supports better product knowledge: where information changes, which boundaries matter, what has actually been observed, which explanations have been rejected, and what uncertainty remains.

## Feedback for the skill creator

The skill was effective at steering comparison of real input paths and at identifying attribution loss upstream of the reasoning layer. Its evidence vocabulary also helped avoid overstating a single successful or unsuccessful reproduction.

For exploration of AI systems, the guidance should add an explicit reasoning-stability check: repeat the same fixed input through the same analysis path and compare semantic outputs across runs. This dimension is different from varying input paths and deserves separate treatment in the experiment-design guidance.

## Next experiment charter

Repeat one fixed, speaker-attributed transcript through the same analysis path multiple times. Compare:

- decision count;
- action or commitment count;
- ownership and responsibility boundaries;
- evidence links;
- wording and semantic framing; and
- missing or newly introduced information.

Classify observed variation as harmless presentation variation or as trust-affecting variation that changes what a participant would believe, own, or act on. Keep runtime configuration, input, and starting state fixed; record unavoidable nondeterministic dependencies.

## Evidence boundary

Discussion Copilot's durable session note, **Exploratory Testing Session: Decisions and action items**, contains the detailed runtime evidence in that repository's `validation/decisions-actions-exploration-2026-08-22.md`. This field study does not reproduce raw transcripts or personally identifying content, and it does not claim exhaustive product or skill coverage.
