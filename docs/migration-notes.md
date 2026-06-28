# Migration Notes

This repository is not a mechanical copy of Claude Code Game Studios. It is a Codex-native adaptation.

## What changed

- Claude Code slash commands became Codex skills.
- Claude Code subagents became role-routing review lenses.
- Claude Code hooks and status line configuration were omitted.
- Claude-only frontmatter fields were removed.
- The 73-command surface was consolidated into four broad skills.

## Why consolidate

Codex skills are most useful when they provide concise routing and load detailed references only when needed. A direct 73-skill migration would be harder to maintain and would duplicate many overlapping workflows.

## Future expansion

Good next skills to add:

- `game-studio-architecture`
- `game-studio-godot`
- `game-studio-unity`
- `game-studio-unreal`
- `game-studio-playtest`

Add them only when the broad skills become too crowded or a workflow needs specific deterministic scripts.
