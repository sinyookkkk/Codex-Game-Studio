# Session Lifecycle

Codex plugins do not run Claude Code session hooks. Use this explicit lifecycle instead.

## Session start

1. Check git status.
2. Identify project phase with `game-studio-onboarding` if uncertain.
3. Read only the references needed for the request.
4. Name the next playable or verifiable step.

## Before context gets long

Record:

- Current goal.
- Files changed.
- Tests run.
- Open risks.
- Next command or review step.

## Session stop

Before stopping, run relevant validation and summarize:

- What changed.
- What evidence passed.
- What remains risky.
- What the next session should pick up.
