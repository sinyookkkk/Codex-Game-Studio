---
name: game-studio-architecture
description: Game architecture and technical planning workflow for Codex. Use when the user needs a technical design document, architecture review, ADR, control manifest, engine architecture, module boundaries, save/input/build decisions, coding rules, or migration from design docs to implementation-ready technical plans.
---

# Game Studio Architecture

Use this skill to turn game design into implementation-ready technical structure. It adapts Claude Code Game Studios architecture commands such as `/create-architecture`, `/architecture-decision`, `/architecture-review`, and `/create-control-manifest`.

## Required references

- Read `../../references/workflow-catalog.md` when architecture readiness depends on phase.
- Read `../../references/engine-routing.md`, then the matching `../../references/engines/*.md` file when engine-specific patterns matter.
- Read `../../references/role-routing.md` and `../../references/roles/studio-roles.md` when choosing technical review lenses.
- Read `../../references/templates/technical-design-document.md` for technical designs.
- Read `../../references/templates/architecture-decision-record.md` for ADRs.
- Read relevant files from `../../references/rules/` when architecture affects code standards.

## Architecture workflow

1. Identify engine, language, target platform, and current repo structure.
2. Read concept, GDD, UX, and prototype evidence if present.
3. Define architecture layers:
   - Foundation: input, save, settings, scene/app lifecycle, build/export.
   - Core game: state, rules, entities, progression, data.
   - Presentation: UI, feedback, audio, camera, animation.
   - Tooling and QA: tests, debug tools, logging, telemetry.
4. Identify decisions that deserve ADRs.
5. Produce an implementation control manifest: rules programmers must follow.
6. Include verification commands or manual checks.

## Guardrails

- Do not choose architecture patterns that exceed the prototype or team size.
- Prefer engine-native patterns unless the project has a strong reason to diverge.
- Every architecture rule should be verifiable through code review, tests, or manual checks.
- Call out when design docs are too vague to support architecture decisions.
