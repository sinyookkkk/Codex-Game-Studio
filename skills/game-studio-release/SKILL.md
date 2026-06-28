---
name: game-studio-release
description: Game release workflow for Codex. Use for launch readiness, release checklists, build packaging, known issues, patch notes, changelog generation, hotfix triage, day-one patch planning, release retrospectives, and post-launch maintenance for indie games.
---

# Game Studio Release

Use this skill when work shifts from building features to shipping, stabilizing, communicating, and maintaining a game.

## Required references

- Read `../../references/audit-and-cost.md` when release decisions need a durable decision trail.

- Read `../../references/templates/release-checklist.md` for release readiness.
- Read `../../references/templates/release-notes.md` or `../../references/templates/changelog-template.md` for player-facing and internal notes.
- Read `../../references/engine-routing.md`, then the matching `../../references/engines/*.md` file when packaging differs by engine.
- Read `../../references/role-routing.md` and `../../references/roles/studio-roles.md` when release decisions need production, QA, technical, community, or localization lenses.
- Read `../../references/rules/test-standards.md` when deciding whether evidence is sufficient.

## Release process

1. Identify target platform, build version, and release channel.
2. List blockers, acceptable known issues, and deferred work.
3. Verify packaging and first-launch paths.
4. Confirm save, settings, input, resolution, audio, pause, restart, and quit behavior.
5. Draft player-facing notes.
6. Decide ship, hold, or hotfix.

## Guardrails

- Do not bury blockers inside general notes.
- Distinguish developer-facing bugs from player-facing known issues.
- Keep release notes honest and short.
- For hotfixes, minimize change scope and require a targeted regression pass.
