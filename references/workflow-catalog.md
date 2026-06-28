# Workflow Catalog

This is the Codex-native phase catalog adapted from Claude Code Game Studios. Use it to answer "where are we?" and "what comes next?"

## Phase overview

| Phase | Goal | Next phase |
| --- | --- | --- |
| Concept | Turn an idea into a documented promise, pillars, engine choice, visual direction, and system map. | Systems design |
| Systems design | Author and review the GDD for each MVP system. | Technical setup |
| Technical setup | Convert design into architecture, ADRs, and programmer rules. | Pre-production |
| Pre-production | Create UX specs, asset specs, epics, stories, test setup, and vertical slice evidence. | Production |
| Production | Implement sprint stories and close them with evidence. | Polish |
| Polish | Improve performance, balance, UX, assets, playtest findings, and bug quality. | Release |
| Release | Validate launch readiness, package builds, write notes, and ship. | None |

## Concept

Required evidence:

- Engine and version decision.
- Game concept document with pitch, target player, pillars, scope, and core loop.
- Art bible or at least a visual identity direction.
- Systems map or systems index.

Recommended Codex skills:

- `game-studio-onboarding`
- `game-studio-design`
- `game-studio-flow`
- `game-studio-gate`

## Systems design

Required evidence:

- One system design or GDD per MVP system.
- Per-system review notes.
- Cross-GDD consistency review.

Checks:

- Every MVP system supports a pillar or core loop step.
- Dependencies between systems are explicit.
- Risky mechanics have prototype or playtest questions.

Recommended Codex skills:

- `game-studio-design`
- `game-studio-gate`

## Technical setup

Required evidence:

- Architecture document.
- At least three foundation ADRs for input, save/progress, scene/app lifecycle, data, build/export, or testing.
- Architecture review.
- Control manifest with programmer rules.

Recommended Codex skills:

- `game-studio-architecture`
- `game-studio-gate`

## Pre-production

Required evidence:

- UX specs for main menu, gameplay HUD, and pause/settings or equivalent core screens.
- Epics and implementable stories.
- First sprint plan.

Optional but valuable evidence:

- Throwaway prototype report.
- Vertical slice report.
- Test framework setup.
- Asset manifest.

Recommended Codex skills:

- `game-studio-flow`
- `game-studio-design`
- `game-studio-architecture`
- `game-studio-qa`
- `game-studio-gate`

## Production

Required evidence:

- Current sprint plan.
- Story files with acceptance criteria.
- Implemented stories with verification notes.
- Story done reviews.

Recommended recurring checks:

- Story readiness before implementation.
- Code review after implementation.
- QA plan per sprint or epic.
- Bug report and bug triage when defects appear.
- Scope check when work expands mid-sprint.

Recommended Codex skills:

- `game-studio-flow`
- `game-studio-qa`
- `game-studio-gate`

## Polish

Required evidence:

- Playtest reports covering new player experience, mid-game systems, and difficulty or pacing.
- Bug backlog triage.
- Performance, balance, UX, and asset audit notes for relevant projects.

Recommended Codex skills:

- `game-studio-design`
- `game-studio-qa`
- `game-studio-flow`

## Release

Required evidence:

- Release checklist.
- Launch checklist.
- Known issues.
- Build/version notes.
- Patch notes or release notes.

Recommended Codex skills:

- `game-studio-release`
- `game-studio-qa`
- `game-studio-gate`

## Gate policy

Gate verdicts are advisory. A FAIL or HOLD means the next phase has unmanaged risk, not that the user is forbidden from moving on. Always separate:

- Blockers: must fix before advancing.
- Risks: can advance if the user accepts the trade-off.
- Improvements: useful but not required.
