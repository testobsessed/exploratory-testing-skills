# Exploratory Testing Skills

Skills, supporting research, and behavioral evaluations for an agent that explores software as it is being developed.

Friday October 16: This is a work in progress, very much incomplete. Feedback welcome.

## Repository layout

- `skills/`: independently discoverable agent skills; each skill will have its own `SKILL.md`
- `research/`: working notes derived from source material and exploratory-testing research
- `scripts/`: repository development and local-installation utilities

## Skills

The twelve primary skills separate focused capabilities from session coordination. Use them as questions arise during exploration, rather than as a fixed sequence.

| Capability | Skill |
|---|---|
| Chartering | [charter-exploration](skills/charter-exploration/SKILL.md) |
| Mapping touch points | [map-touch-points](skills/map-touch-points/SKILL.md) |
| Identifying variables | [identify-variables](skills/identify-variables/SKILL.md) |
| Discovering invariants | [discover-invariants](skills/discover-invariants/SKILL.md) |
| Working with oracles | [work-with-oracles](skills/work-with-oracles/SKILL.md) |
| Designing experiments | [design-experiments](skills/design-experiments/SKILL.md) |
| Observing behavior | [observe-behavior](skills/observe-behavior/SKILL.md) |
| Reporting bugs | [report-bugs](skills/report-bugs/SKILL.md) |
| Logging exploration | [exploratory-session-log](skills/exploratory-session-log/SKILL.md) |
| Domain research | [research-domain](skills/research-domain/SKILL.md) |
| Orientation sessions | [orient-to-software](skills/orient-to-software/SKILL.md) |
| Exploratory sessions | [explore-software](skills/explore-software/SKILL.md) |

Raw exploration logs are kept by default unless the user opts out. Basic logging is self-contained in [exploratory-session-log](skills/exploratory-session-log/SKILL.md); supporting records are created when useful and indexed at closure or handoff. The calling explorer agent can own coordination directly and use focused skills without explore-software.

Reuse existing orientation and caller-provided context; a missing orientation file alone does not require a session. Research answers domain questions needed for the next experiment, reuses cached entries, and stops once sufficient context exists. Initial research has a five-minute ceiling within the enclosing budget; further research requires a caller request. Disabling persistence does not disable otherwise-authorized research.

A run can span multiple sessions. Its timebox includes preparation, startup, exploration, record maintenance, and reporting; a bounded investigation ends when its question is answered to the requested confidence. Reports are at most 1,000 words, with links to raw evidence. See [shared application records](skills/exploratory-session-log/references/application-records.md) for multi-session storage and indexing and [the content map](docs/skill-content-map.md) for capability boundaries.

## Usage and overrides

See [Using the skills](docs/using-skills.md) for default behavior, supported caller overrides, result locations, and example requests. See [Delegating an exploratory investigation](docs/delegating-exploration.md) for startup authorization, runtime access, and a reusable explorer assignment.

## Local installation

Run:

```sh
./scripts/install-local.sh
```

The installer creates links for every valid skill under `skills/` in both:

- Codex: `${CODEX_SKILLS_DIR:-$HOME/.agents/skills}`
- Claude Code: `${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}`

It records the links it owns separately in each destination, removes its stale links after skills are renamed or deleted, and leaves unrelated files and links untouched. Set either environment variable to override that agent's destination. If both destinations resolve to the same path, the installer processes it only once.

## Compatibility and license

The newer charter-first session logger is canonical; `log-exploration` and its append helper remain for compatibility with older records. Skills follow the [Agent Skills specification](https://agentskills.io/specification). Licensed under the [MIT License](LICENSE).
