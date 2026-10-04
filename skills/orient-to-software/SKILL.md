---
name: orient-to-software
description: Build initial software context through small behavioral probes when an exploratory agent is unfamiliar with the system.
---

# Orientation

Every session needs a charter. Orientation has the predefined charter: **Explore the target software with all the information available, to discover what I can do with it.** Record this charter at the top of the session log.

Use source code, documentation, and existing tests to orient, generate hypotheses, locate observation points, and explain established behavior. Treat every model, requirement, document, and source reading as a potentially fallible map.

Reuse the application's existing `orientation.md` and caller-provided context before new orientation. When that context already supports a faithful first experiment, proceed with the caller's investigation; a missing summary file alone does not require orientation. An explicit request to orient still starts an orientation session.

Establish one raw session log with exploratory-session-log before substantive work, unless the user explicitly opts out. Reuse the caller's active run and record location. Read only guidance relevant to the next probe; do not preload every focused skill or scaffold an index and summaries at startup. Reuse cached or caller-provided domain context. Use research-domain when a domain question needs answering to choose or interpret the next probe; stop researching once sufficient context exists. Initial research has a five-minute ceiling, constrained by the remaining session and run budgets. Further research requires an explicit caller request. If research-domain is unavailable, follow the same boundaries using available sources. Documentation and repository access help but are not prerequisites.

## Get running and map the first interface

First establish runtime access and attempt a small faithful probe as soon as the available context permits. Follow the caller’s supplied destination or instructions, such as a public URL. Otherwise use the repository README or other obvious repository startup instructions. Gather prerequisites needed for the probe, but do not make a general domain survey a startup requirement. Reserve time for behavioral interaction when access permits; research must not consume the whole orientation allowance merely because its own ceiling is five minutes.

Orientation applies to any kind of software, including desktop applications, web applications, services with endpoints and no GUI, and command-line tools. At the first page, endpoint, command, or other interface encountered, determine what actions are available and start mapping from there. Identify behavioral surfaces, control points, observation points, and initial variables as they become apparent; choose small faithful probes that extend the map.

Look for indications that authentication is needed, especially when it blocks useful actions. Use login information supplied through the prompt, an environment variable, or an available credential-vault connection without exposing secrets in logs. If authentication blocks progress and no usable login information or method is available, stop and ask the user. This is one of the few orientation conditions that warrants interrupting the caller.

Use [identify-variables](../identify-variables/SKILL.md) during orientation to map variables as the available actions become clear. Use its existing guidance rather than duplicating the variable-mapping process here or in charter-exploration. Draw on map-touch-points and observe-behavior as questions arise. Record what remains inferred or inaccessible and how that limits subsequent experiments.

Record discoveries and startup blockers promptly in the raw session log. Link reusable context from the application index at session closure or handoff. Use research to guide behavioral probes and revise the working model when evidence disagrees.

## Stop orientation

Default to a five-minute ceiling for the orientation session, including preparation, research, record maintenance, and closure; the caller may override it. Establish the session's start and deadline using available timestamps, within any enclosing run deadline. If timing is unavailable, disclose that limit. Stop probing early enough to close within the budget. Finish sooner when the context is sufficient for the caller's investigation or when three consecutive experiments yield no new information. Reset that count when an experiment produces new information. For an explicit broad orientation request, continue useful discovery within the ceiling. These are stopping heuristics, not claims of complete coverage.

On stopping, close the session log. Create or update `orientation.md` when application capabilities or reusable access requirements were learned; if startup yielded only an environment blocker, keep it in the raw log and closing summary without creating an empty orientation summary. Do not extend exploration merely to complete the map.

## Maintain the reusable orientation summary

Maintain one file named `orientation.md` at the top of the application’s structured information repository, alongside `index.md` (by default `exploration/orientation.md` in the target application’s folder). It summarizes what can be done with the target application, including discovered behaviors, access requirements, and links to variable mapping and supporting raw observations. Keep its structure recognizable through headings for Available behaviors, Access requirements, Variables, and Gaps and uncertainties; omit empty detail rather than inventing findings.

Each orientation session still produces its own append-only session log under the shared session-log convention. The reusable summary has no run or session ID in its filename and is distinct from those raw logs and the run report.

When orientation yields reusable knowledge, distill it into `orientation.md` at session closure and link it from the application index. If it already exists, modify the relevant portions in place with new information. Do not create another orientation summary or replace the existing summary wholesale. Preserve useful previous knowledge and evidence links; make changed understanding and unresolved contradictions visible. Retain the raw session logs as the history supporting these updates.
