---
name: game-studio-qa
description: Game QA workflow for Codex. Use when the user needs smoke checks, regression tests, bug triage, playtest plans, test evidence, risk-based QA, accessibility checks, performance sanity checks, or release-blocker analysis for a game build.
---

# Game Studio QA

Use this skill to turn game quality concerns into practical verification steps and evidence.

## Required references

- Read `../../references/templates.md` when creating playtest reports or release checks.
- Read `../../references/engine-routing.md` when engine-specific test commands or build checks matter.
- Read `../../references/studio-workflow.md` to align QA depth with project phase.

## QA process

1. Identify the build, platform, and feature under test.
2. Separate smoke, regression, exploratory, accessibility, and performance checks.
3. Prioritize tests by player impact and likelihood of breakage.
4. Include manual steps when automation does not exist.
5. Capture evidence: command output, screenshots, logs, save files, or observed behavior.
6. End with a ship, hold, or investigate recommendation.

## Smoke checklist

```markdown
## Smoke Test
- Build:
- Platform:

| Check | Steps | Expected | Result |
| --- | --- | --- | --- |
| Launch | Start the game from a clean state. | Main menu or first scene appears. | Not run |
| Core loop | Complete one normal loop. | Player can progress and receive feedback. | Not run |
| Failure | Trigger one failure path. | Failure is readable and recoverable. | Not run |
| Restart | Restart or retry. | State resets correctly. | Not run |
| Quit | Exit cleanly. | No crash or hang. | Not run |

## Verdict
- PASS / PASS WITH RISKS / HOLD:
- Evidence:
```

## Bug triage

Use this format:

```markdown
| Priority | Bug | Player impact | Repro steps | Recommended owner lens |
| --- | --- | --- | --- | --- |
```

## Guardrails

- Never claim a build passes without running or clearly marking tests as manual/not run.
- Prefer a small checklist the user will actually run.
- For release candidates, include install, first launch, save/load, settings, input, and exit paths.
