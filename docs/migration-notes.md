# Migration Notes

This repository is not a mechanical copy of Claude Code Game Studios. It is a Codex-native adaptation.

## What changed

- Claude Code slash commands became Codex skills.
- Claude Code subagents became role-routing review lenses.
- Claude Code hooks and status line configuration were omitted.
- Claude-only frontmatter fields were removed.
- The 73-command surface is represented by seven broad skills and a command mapping reference.

## Phase 1 alignment

Version `0.2.0` adds the first parity layer:

- `game-studio-onboarding` for `/start`, `/help`, `/project-stage-detect`, `/setup-engine`, and `/adopt` style work.
- `game-studio-gate` for `/gate-check`, `/story-readiness`, `/story-done`, `/design-review`, and related readiness reviews.
- `game-studio-architecture` for `/create-architecture`, `/architecture-decision`, `/architecture-review`, and `/create-control-manifest`.
- `references/workflow-catalog.md` as the Codex-native phase catalog.
- `references/command-mapping.md` as the Claude slash command translation table.

## Why consolidate

Codex skills are most useful when they provide concise routing and load detailed references only when needed. A direct 73-skill migration would be harder to maintain and would duplicate many overlapping workflows.

## Future expansion

Good next additions:

- `references/templates/` with the most important GDD, ADR, UX, art bible, QA, and release templates.
- `references/roles/` with role cards adapted from the 49 Claude agents.
- `references/rules/` with coding standards adapted from Claude path-scoped rules.
- Engine-specific references for Godot, Unity, and Unreal.
- A lightweight skill validation catalog inspired by the CCGS Skill Testing Framework.
