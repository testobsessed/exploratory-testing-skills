---
name: map-touch-points
description: Discover software entry points and connected places to control or observe behavior for an exploratory investigation.
---

# Mapping Touch Points

Start at an entry point relevant to the charter: a user action, API request, imported artifact, event, or other way work enters the software. Trace the flow from there, using observed behavior and available implementation evidence to discover further points where you can control what happens, observe what happens, or both. Extend the map as exploration reveals new paths and boundaries.

At each discovered point, record:

- what enters and leaves, including data, events, and state changes;
- which variables are accessible and their relevant values or conditions;
- what you can control, what you can observe, and through which interface;
- relationships to other points, including transformations, dependencies, and delays;
- what remains inferred or inaccessible and how that limits an experiment.

Use this map to choose where to vary a condition and where to observe its effects. A point may offer control without direct observation, observation without control, or both; connect points when an effect is visible elsewhere. Keep the map provisional rather than requiring a complete system inventory before experimenting.

Use exploratory-session-log unless the caller opts out; reuse the active session and guidance already loaded. Capture raw evidence promptly, indexing at closure or handoff. Standalone requests need only a proportionate raw record; create supporting records when useful. If the logger is unavailable, append dated evidence in the caller's workspace.
