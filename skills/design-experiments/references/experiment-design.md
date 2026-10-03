# Designing Experiments

## Use discriminating comparisons

Prefer paired experiments that can eliminate explanations:

- one path versus another path intended to perform the same operation;
- fresh versus previously exercised state;
- stable state versus state changing while work is in flight;
- direct versus indirect or derived interfaces;
- zero, one, and many elements;
- none, some, and all selections;
- beginning, middle, and end positions;
- too small, plausible, and too large values;
- valid, boundary, and rule-violating data;
- default versus non-default configuration.

When an operation has multiple mechanisms, enumerate **all the ways** that matter to the charter. Do not generalize from one mechanism to another without evidence.

## Explore delayed and asynchronous behavior

For every meaningful delay, identify:

- the state or candidate when work is scheduled;
- what can change while work is in flight;
- which snapshot or identity the result should apply to;
- what state is consulted when work completes;
- what happens to newer work afterward.

Exercise relevant changes before the operation starts, while it is in flight, and after it completes. Look for transient windows, starvation, stale references, races, duplicate work, lost work, and results applied to the wrong object.

## Follow data across surfaces

Trace important information through every meaningful representation, for example:

```text
user action → persisted configuration → loader/domain model → runtime state
            → events/history → aggregation → rendered output → export/import
```

At each transition, compare identity, values, relationships, and omissions. A consistent UI can hide corrupted state; correct internal state can be misrepresented by a chart.

## Use surprises as leads

When behavior surprises you:

1. record it before explaining it;
2. identify the expectation or comparison that made it surprising;
3. generate multiple plausible explanations;
4. choose the cheapest faithful experiment that distinguishes them;
5. seek disconfirming evidence, not only confirmation;
6. revise the model explicitly when evidence contradicts it.

A disproved hypothesis is useful information. Preserve it in the session record.
