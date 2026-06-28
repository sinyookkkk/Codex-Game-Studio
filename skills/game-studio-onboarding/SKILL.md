---
name: game-studio-onboarding
description: Codex-native onboarding and project-stage detection for game projects. Use when the user is starting a new game, adopting an existing project, asking what to do next, migrating from Claude Code Game Studios, choosing an engine, or needing a guided equivalent of /start, /help, /project-stage-detect, /setup-engine, or /adopt.
---

# Game Studio Onboarding

Use this skill as the entry point for a game project. It replaces Claude Code slash commands such as `/start`, `/help`, `/project-stage-detect`, `/setup-engine`, and `/adopt` with a Codex-native interview and audit flow.

## Required references

- Read `../../docs/session-lifecycle.md` when starting, resuming, or stopping a long project session.

- Read `../../references/workflow-catalog.md` before recommending a phase or next step.
- Read `../../references/command-mapping.md` when translating a Claude Code Game Studios command to a Codex workflow.
- Read `../../references/engine-routing.md`, then the matching `../../references/engines/*.md` file when engine setup or engine choice matters.
- Read `../../references/templates.md` when drafting the first artifact.
- Read `../../references/templates/game-concept.md` or `../../references/templates/systems-index.md` when creating early concept artifacts.

## Project audit

Inspect the project before asking broad questions. Look for:

- Engine files: `project.godot`, Unity `ProjectSettings/`, Unreal `.uproject`, web package files.
- Concept docs: `design/gdd/game-concept.md`, pitch docs, README descriptions.
- System docs: `design/gdd/`, `design/systems/`, architecture docs, ADRs.
- Source code: `src/`, `scripts/`, engine-specific source folders.
- Production artifacts: `production/epics/`, `production/sprints/`, playtest reports, release notes.
- Tests: `tests/`, CI files, smoke test scripts.

Do not treat missing files as failure. Use missing files to choose the next useful action.

## Guardrails

- Ask at most one clarifying question if the audit gives enough evidence to proceed.
- Prefer a concrete next artifact over a long generic roadmap.
- If the user says they want Claude Code Game Studios parity, translate commands through `command-mapping.md` rather than exposing Claude-only tool names.
- Do not create project files unless the user asks for implementation or artifact drafting.
