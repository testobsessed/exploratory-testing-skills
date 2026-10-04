# Exploratory Testing Skills

Skills, supporting research, and behavioral evaluations for an agent that explores software as it is being developed.

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

Raw exploration logs are kept by default unless the user opts out. Supporting records are created when useful; indexes are updated at session closure or handoff. The calling explorer agent can own coordination directly and use focused skills without explore-software. Domain research reuses cached entries; initial research is capped at five minutes unless the caller specifies otherwise. Further research requires a caller request. A run can span multiple sessions and ends with a proportionate report of at most 1,000 words linking to raw evidence. See [shared application records](skills/exploratory-session-log/references/application-records.md) for storage and structure and [the content map](docs/skill-content-map.md) for capability boundaries.

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
