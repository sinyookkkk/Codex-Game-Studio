# Codex Adaptation Map

This map explains how to use Claude Code Game Studios concepts inside Codex without copying Claude-only mechanics.

## Command migration

Claude Code Game Studios exposes many narrow slash commands. Codex Game Studio groups them into seven skills so Codex can load fewer instructions and route through references only when needed.

| Claude command family | Codex skill |
| --- | --- |
| `/start`, `/help`, `/adopt`, `/setup-engine`, `/project-stage-detect` | `game-studio-onboarding` |
| `/brainstorm`, `/quick-design`, `/map-systems`, `/design-system`, `/ux-design` | `game-studio-design` |
| `/create-architecture`, `/architecture-decision`, `/create-control-manifest` | `game-studio-architecture` |
| `/create-epics`, `/create-stories`, `/dev-story`, `/sprint-plan`, `/estimate` | `game-studio-flow` |
| `/gate-check`, `/story-readiness`, `/story-done`, `/design-review` | `game-studio-gate` |
| `/qa-plan`, `/smoke-check`, `/regression-suite`, `/bug-triage`, `/playtest-report` | `game-studio-qa` |
| `/release-checklist`, `/launch-checklist`, `/patch-notes`, `/hotfix`, `/retrospective` | `game-studio-release` |

Use `references/command-mapping.md` for command-level details.

## Agent migration

Claude subagents become Codex role lenses. A role lens is a review perspective Codex applies inside the current task instead of dispatching a separate Claude agent.

| Claude agent idea | Codex role-lens behavior |
| --- | --- |
| Creative director | Check player promise, scope, theme, and product coherence. |
| Technical director | Check architecture risk, engine fit, build constraints, and maintainability. |
| Producer | Check milestone realism, dependency order, and decision timing. |
| QA lead | Check evidence, reproduction, coverage, and release-blocking risk. |
| UX designer | Check player comprehension, friction, feedback, and accessibility. |
| Engine specialist | Check Godot, Unity, Unreal, or web implementation constraints. |

Use `references/role-routing.md` and `references/roles/studio-roles.md` when a task needs multiple perspectives.

## Hook migration

Claude hooks are not portable to Codex plugins. Replace them with explicit checks:

| Claude hook purpose | Codex replacement |
| --- | --- |
| Validate before commit | Run `scripts/validate_repository.py` and skill validation. |
| Validate before push | GitHub Actions matrix on Ubuntu, macOS, and Windows. |
| Detect workflow gaps | Use `game-studio-gate` with `references/quality-rubric.md`. |
| Log agent sessions | Record outcomes in project docs, release notes, or sprint status. |
| Validate assets | Use `game-studio-qa` with asset-audit and smoke-check prompts. |

## Testing migration

The original testing framework has many granular specs. Codex Game Studio uses:

- `tests/skill-catalog.json` for the canonical skill list.
- `tests/forward-tests.json` for realistic prompts and expected evidence.
- `references/quality-rubric.md` for review criteria.
- `scripts/validate_repository.py` for deterministic repository checks.

## Completion strategy

Prefer depth where Codex benefits most:

1. Keep the seven skills concise.
2. Put detailed workflows in references.
3. Add forward tests before adding more skills.
4. Expand engine and role references before duplicating slash commands.
5. Use GitHub documentation for humans and validator checks for machines.
