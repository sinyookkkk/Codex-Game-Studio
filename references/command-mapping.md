# Claude Command Mapping

Use this reference when a user asks for a Claude Code Game Studios slash command or wants parity with the original project.

## Onboarding and navigation

| Claude command | Codex workflow |
| --- | --- |
| `/start` | Use `game-studio-onboarding` to audit state and route the user. |
| `/help` | Use `game-studio-onboarding` with `workflow-catalog.md` to recommend the next step. |
| `/project-stage-detect` | Use `game-studio-onboarding` to inspect artifacts and infer phase. |
| `/setup-engine` | Use `game-studio-onboarding` plus `engine-routing.md`. |
| `/adopt` | Use `game-studio-onboarding` and `game-studio-gate` to audit existing artifacts. |

## Design

| Claude command | Codex workflow |
| --- | --- |
| `/brainstorm` | Use `game-studio-design`. |
| `/map-systems` | Use `game-studio-design` plus `workflow-catalog.md`. |
| `/design-system` | Use `game-studio-design` with the system design template. |
| `/quick-design` | Use `game-studio-design` for a compact change spec. |
| `/design-review` | Use `game-studio-gate` or `game-studio-design` depending on whether a verdict is needed. |
| `/review-all-gdds` | Use `game-studio-gate` for cross-document consistency. |
| `/propagate-design-change` | Use `game-studio-architecture` and `game-studio-gate` to identify impacted docs and code. |

## Art, UX, and assets

| Claude command | Codex workflow |
| --- | --- |
| `/art-bible` | Use `game-studio-design` with visual identity and art bible sections from templates. |
| `/asset-spec` | Use `game-studio-design` or `game-studio-flow` depending on whether the output is design or production planning. |
| `/asset-audit` | Use `game-studio-qa`. |
| `/ux-design` | Use `game-studio-design`. |
| `/ux-review` | Use `game-studio-gate`. |

## Architecture

| Claude command | Codex workflow |
| --- | --- |
| `/create-architecture` | Use `game-studio-architecture`. |
| `/architecture-decision` | Use `game-studio-architecture` and the ADR format. |
| `/architecture-review` | Use `game-studio-gate` with technical director and lead programmer lenses. |
| `/create-control-manifest` | Use `game-studio-architecture` to produce programmer rules. |

## Stories and sprints

| Claude command | Codex workflow |
| --- | --- |
| `/create-epics` | Use `game-studio-flow` with architecture and GDD evidence. |
| `/create-stories` | Use `game-studio-flow` to break epics into acceptance-tested work. |
| `/dev-story` | Use Codex normal implementation flow, guided by `game-studio-flow` and `game-studio-qa`. |
| `/sprint-plan` | Use `game-studio-flow`. |
| `/sprint-status` | Use `game-studio-flow` to summarize current sprint evidence. |
| `/story-readiness` | Use `game-studio-gate`. |
| `/story-done` | Use `game-studio-gate`. |
| `/estimate` | Use `game-studio-flow`. |

## QA and release

| Claude command | Codex workflow |
| --- | --- |
| `/qa-plan` | Use `game-studio-qa`. |
| `/smoke-check` | Use `game-studio-qa`. |
| `/soak-test` | Use `game-studio-qa`. |
| `/regression-suite` | Use `game-studio-qa`. |
| `/test-evidence-review` | Use `game-studio-qa` and `game-studio-gate`. |
| `/release-checklist` | Use `game-studio-release`. |
| `/launch-checklist` | Use `game-studio-release` and `game-studio-gate`. |
| `/patch-notes` | Use `game-studio-release`. |
| `/changelog` | Use `game-studio-release`. |
| `/hotfix` | Use `game-studio-release` with QA verification. |
| `/day-one-patch` | Use `game-studio-release`. |

## Team orchestration

Team commands such as `/team-combat`, `/team-ui`, `/team-release`, and `/team-polish` should be represented as role-lens reviews rather than automatic Claude subagent dispatch. Use `role-routing.md` to select two or three lenses and keep the output concise.
