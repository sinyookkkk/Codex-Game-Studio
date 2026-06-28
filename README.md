# Codex Game Studio

Codex Game Studio is a Codex plugin for solo developers and small teams making games with AI assistance. It adapts the studio-style workflows from Claude Code Game Studios into a Codex-native skill pack.

This repository is designed to be shared on GitHub and installed as a Codex plugin.

## What is included

- `game-studio-flow`: project routing, milestone planning, task breakdown, vertical slices, and production rhythm.
- `game-studio-design`: game concept work, core loops, systems, balance, UX, playtest feedback, and design reviews.
- `game-studio-qa`: smoke tests, regression checks, playtest reports, bug triage, and evidence collection.
- `game-studio-release`: release readiness, launch checklists, patch notes, hotfix flow, and post-release retrospectives.

The plugin intentionally does not port every Claude Code slash command one-for-one. Codex works better with a smaller set of high-signal skills and references that load progressively.

## Installation

Clone this repository, then install it through the Codex plugin flow for local plugins. The plugin manifest is:

```text
.codex-plugin/plugin.json
```

After installing, ask Codex for tasks such as:

```text
Help me turn this game idea into a one-week playable prototype.
Review my combat design and identify the highest-risk assumptions.
Create a smoke test checklist for my Godot build.
Prepare a launch checklist and patch notes template.
```

## Repository layout

```text
.codex-plugin/
  plugin.json
skills/
  game-studio-flow/
  game-studio-design/
  game-studio-qa/
  game-studio-release/
references/
  studio-workflow.md
  role-routing.md
  templates.md
  engine-routing.md
```

## Design principles

1. Keep the user in control. Codex recommends, drafts, and verifies; the developer decides.
2. Build playable evidence early. Every plan should name how the game will be run and tested.
3. Guard scope. Prefer a smaller game that reaches professional quality over a large plan that never becomes playable.
4. Separate concept, systems, implementation, QA, and release concerns without creating ceremony for its own sake.
5. Preserve attribution. This project is inspired by and partially adapted from Claude Code Game Studios.

## Differences from Claude Code Game Studios

Claude Code Game Studios uses Claude Code-specific agents, slash commands, hooks, status lines, and tool names. Codex Game Studio converts the useful workflow content into Codex skills:

- No `.claude/settings.json` hooks.
- No Claude Code slash command dependency.
- No automatic 49-agent roster.
- No `AskUserQuestion` or Claude tool frontmatter.
- Codex-native skill frontmatter with only `name` and `description`.

## Attribution

This project is inspired by the MIT-licensed Claude Code Game Studios project by Donchitos. The Codex version is a compatibility-oriented adaptation, not a drop-in replacement.

If you publish this repository, keep the attribution and MIT license text.

## Status

Version `0.1.0` is a practical first migration. It favors a maintainable Codex-native workflow over a complete mechanical port.
