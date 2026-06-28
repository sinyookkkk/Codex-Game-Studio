---
name: game-studio-flow
description: Game development production workflow for Codex. Use when the user wants to plan an indie game, migrate from idea to prototype, define milestones, split work into tasks, create a vertical slice, organize sprint work, create epics or stories, estimate scope, or decide the next playable step for Godot, Unity, Unreal, or web games.
---

# Game Studio Flow

Use this skill to turn loose game work into a playable, testable plan. Start from the current project state, then produce a small next step with a run and verification path.

## Required references

- Read `../../references/workflow-catalog.md` for phase routing.
- Read `../../references/studio-workflow.md` for the compact phase summary.
- Read `../../references/role-routing.md` when the request needs multiple studio perspectives.
- Read `../../references/roles/studio-roles.md` when a specialized role lens is needed.
- Read `../../references/engine-routing.md`, then the matching `../../references/engines/*.md` file when an engine is known or being chosen.
- Read `../../references/templates.md` to choose a planning artifact.
- Read `../../references/templates/sprint-plan.md`, `../../references/templates/risk-register-entry.md`, `../../references/templates/prototype-report.md`, or `../../references/templates/vertical-slice-report.md` when drafting those artifacts.

## Workflow

1. Identify the current phase: concept, prototype, systems design, technical setup, vertical slice, production, polish, or release.
2. Name the next playable outcome in one sentence.
3. Define what is out of scope for this step.
4. Break work into one-day to three-day tasks.
5. Add acceptance checks for each task.
6. Include the command or manual steps needed to run the build.
7. End with the smallest useful follow-up.

## Guardrails

- Prefer a smaller playable plan over a comprehensive plan that cannot be tested.
- Do not invent engine commands; inspect the repo or ask when necessary.
- Tie every task to player value, risk reduction, or release readiness.
- When the user asks for a full roadmap, still include the first concrete playable milestone.
