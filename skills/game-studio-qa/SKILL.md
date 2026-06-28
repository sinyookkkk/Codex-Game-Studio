---
name: game-studio-qa
description: Game QA workflow for Codex. Use when the user needs smoke checks, regression tests, bug triage, playtest plans, test evidence, risk-based QA, accessibility checks, performance sanity checks, rule compliance checks, or release-blocker analysis for a game build.
---

# Game Studio QA

Use this skill to turn game quality concerns into practical verification steps and evidence.

## Required references

- Use `../../scripts/detect_gaps.py` for lightweight missing-artifact detection.

- Use `../../scripts/check_assets.py` for asset folder sanity checks when a project has assets.

- Read `../../references/templates/test-plan.md` when creating a QA plan.
- Read `../../references/templates/test-evidence.md` when collecting or reviewing evidence.
- Read `../../references/templates/vertical-slice-report.md` or `../../references/templates/prototype-report.md` for playable validation.
- Read `../../references/engine-routing.md`, then the matching `../../references/engines/*.md` file when engine-specific test commands or build checks matter.
- Read `../../references/rules/test-standards.md` for test quality.
- Read `../../references/workflow-catalog.md` to align QA depth with project phase.

## QA process

1. Identify the build, platform, and feature under test.
2. Separate smoke, regression, exploratory, accessibility, and performance checks.
3. Prioritize tests by player impact and likelihood of breakage.
4. Include manual steps when automation does not exist.
5. Capture evidence: command output, screenshots, logs, save files, or observed behavior.
6. End with a ship, hold, or investigate recommendation.

## Guardrails

- Never claim a build passes without running or clearly marking tests as manual/not run.
- Prefer a small checklist the user will actually run.
- For release candidates, include install, first launch, save/load, settings, input, and exit paths.
