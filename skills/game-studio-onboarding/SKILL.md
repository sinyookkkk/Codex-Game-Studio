---
name: game-studio-onboarding
description: Codex-native onboarding and project-stage detection for game projects. Use when the user is starting a new game, adopting an existing project, asking what to do next, migrating from Claude Code Game Studios, choosing an engine, or needing a guided equivalent of /start, /help, /project-stage-detect, /setup-engine, or /adopt.
---

# Game Studio Onboarding

Use this skill as the entry point for a game project. It replaces Claude Code slash commands such as `/start`, `/help`, `/project-stage-detect`, `/setup-engine`, and `/adopt` with a Codex-native interview and audit flow.

## Required references

- Read `../../references/workflow-catalog.md` before recommending a phase or next step.
- Read `../../references/command-mapping.md` when translating a Claude Code Game Studios command to a Codex workflow.
- Read `../../references/engine-routing.md` when engine setup or engine choice matters.
- Read `../../references/templates.md` when drafting the first artifact.

## Project audit

Inspect the project before asking broad questions. Look for:

- Engine files: `project.godot`, Unity `ProjectSettings/`, Unreal `.uproject`, web package files.
- Concept docs: `design/gdd/game-concept.md`, pitch docs, README descriptions.
- System docs: `design/gdd/`, `design/systems/`, architecture docs, ADRs.
- Source code: `src/`, `scripts/`, engine-specific source folders.
- Production artifacts: `production/epics/`, `production/sprints/`, playtest reports, release notes.
- Tests: `tests/`, CI files, smoke test scripts.

Do not treat missing files as failure. Use missing files to choose the next useful action.

## Routing

Map the project into one of these states:

| State | Signal | Recommended next Codex workflow |
| --- | --- | --- |
| No idea | No concept or code | Use `game-studio-design` to brainstorm a concept. |
| Vague idea | Theme or genre exists, no clear loop | Use `game-studio-design` to define pitch, pillars, and prototype question. |
| Clear concept | Core loop exists, little structure | Use `game-studio-flow` to create a prototype plan, then map systems. |
| Existing prototype | Runnable code exists, weak docs | Use `game-studio-gate` to audit evidence and `game-studio-flow` to plan the next milestone. |
| Existing production work | GDDs, stories, or sprint artifacts exist | Use `game-studio-gate` for readiness and `game-studio-architecture` for architecture gaps. |
| Release candidate | Build and QA evidence exist | Use `game-studio-release` and `game-studio-qa`. |

## Output

```markdown
## Project State
- Phase:
- Evidence:
- Missing:

## Recommended Next Step
-

## Why This Step
-

## Suggested Artifact
- Path:
- Purpose:

## Follow-Up Prompt
-
```

## Guardrails

- Ask at most one clarifying question if the audit gives enough evidence to proceed.
- Prefer a concrete next artifact over a long generic roadmap.
- If the user says they want Claude Code Game Studios parity, translate commands through `command-mapping.md` rather than exposing Claude-only tool names.
- Do not create project files unless the user asks for implementation or artifact drafting.
