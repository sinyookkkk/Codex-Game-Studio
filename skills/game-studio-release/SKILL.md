---
name: game-studio-release
description: Game release workflow for Codex. Use for launch readiness, release checklists, build packaging, known issues, patch notes, hotfix triage, day-one patch planning, release retrospectives, and post-launch maintenance for indie games.
---

# Game Studio Release

Use this skill when work shifts from building features to shipping, stabilizing, communicating, and maintaining a game.

## Required references

- Read `../../references/templates.md` for release checklist and patch notes structure.
- Read `../../references/engine-routing.md` when packaging differs by engine.
- Read `../../references/role-routing.md` when release decisions need production, QA, and technical lenses.

## Release process

1. Identify target platform, build version, and release channel.
2. List blockers, acceptable known issues, and deferred work.
3. Verify packaging and first-launch paths.
4. Confirm save, settings, input, resolution, audio, pause, restart, and quit behavior.
5. Draft player-facing notes.
6. Decide ship, hold, or hotfix.

## Release output

```markdown
## Release Status
- Version:
- Platform:
- Channel:
- Verdict: Ship / Hold / Hotfix

## Blockers
| Issue | Impact | Required fix |
| --- | --- | --- |

## Known Issues
| Issue | Player workaround | Follow-up |
| --- | --- | --- |

## Checklist
- [ ] Clean launch.
- [ ] Main loop playable.
- [ ] Save or progress behavior verified.
- [ ] Settings verified.
- [ ] Input verified.
- [ ] Quit path verified.
- [ ] Patch notes drafted.

## Patch Notes Draft
-
```

## Guardrails

- Do not bury blockers inside general notes.
- Distinguish developer-facing bugs from player-facing known issues.
- Keep release notes honest and short.
- For hotfixes, minimize change scope and require a targeted regression pass.
