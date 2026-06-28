# Codex Game Studio

Codex Game Studio is a Codex plugin for solo developers and small teams making games with AI assistance. It adapts the studio-style workflows from Claude Code Game Studios into a Codex-native skill pack.

This repository is designed to be shared on GitHub and installed as a Codex plugin.

## What is included

- `game-studio-onboarding`: project onboarding, phase detection, engine routing, and Claude command translation.
- `game-studio-flow`: project routing, milestone planning, task breakdown, vertical slices, and production rhythm.
- `game-studio-design`: game concept work, core loops, systems, balance, UX, playtest feedback, and design reviews.
- `game-studio-architecture`: architecture docs, ADRs, engine technical planning, and control manifests.
- `game-studio-gate`: phase gates, readiness checks, story completion reviews, and advisory verdicts.
- `game-studio-qa`: smoke tests, regression checks, playtest reports, bug triage, and evidence collection.
- `game-studio-release`: release readiness, launch checklists, patch notes, hotfix flow, and post-release retrospectives.

## Parity assets

- `references/templates/`: compact document templates for concepts, GDDs, systems, UX, art, architecture, sprint planning, QA, release, and changelogs.
- `references/roles/`: 49 studio role cards adapted into Codex review lenses.
- `references/rules/`: 11 coding and content rules adapted from Claude Code Game Studios path-scoped rules.
- `references/engines/`: Godot, Unity, Unreal, and web-specific routing notes.
- `tests/skill-catalog.json`: validation catalog for the Codex skill surface.
- `references/quality-rubric.md`: quality rubric for skills, references, workflows, and release checks.

The plugin intentionally does not port every Claude Code slash command one-for-one. Codex works better with a smaller set of high-signal skills and references that load progressively.

## Installation

Clone this repository, then install it through the Codex plugin flow for local plugins. The plugin manifest is:

```text
.codex-plugin/plugin.json
```

After installing, ask Codex for tasks such as:

```text
Validate this Codex Game Studio plugin.
Find my current game development phase and tell me what to do next.
Draft a game concept using the Codex Game Studio template.
Review my combat design with game designer, UX, and QA lenses.
Create an ADR for my save system.
Check whether my project can move from systems design to technical setup.
Create a smoke test checklist for my Godot build.
Prepare a launch checklist and patch notes template.
```

## Validation

Run the repository validator before publishing changes:

```bash
python scripts/validate_repository.py
```

The validator checks the plugin manifest, skill frontmatter, skill catalog, required reference files, and placeholder text. GitHub Actions runs the same command on pushes and pull requests.

## Repository layout

```text
.codex-plugin/
  plugin.json
.github/workflows/
  validate.yml
scripts/
  validate_repository.py
skills/
  game-studio-onboarding/
  game-studio-flow/
  game-studio-design/
  game-studio-architecture/
  game-studio-gate/
  game-studio-qa/
  game-studio-release/
tests/
  skill-catalog.json
references/
  command-mapping.md
  engine-routing.md
  engines/
  quality-rubric.md
  role-routing.md
  roles/
  rules/
  templates/
  templates.md
  workflow-catalog.md
```

## Claude Code Game Studios parity

Claude Code Game Studios uses Claude Code-specific agents, slash commands, hooks, status lines, and tool names. Codex Game Studio converts the useful workflow content into Codex skills:

- Claude slash commands map to Codex skills through `references/command-mapping.md`.
- Phase progression maps to `references/workflow-catalog.md`.
- Claude subagents map to role lenses in `references/roles/studio-roles.md`.
- Claude path-scoped rules map to `references/rules/`.
- Claude document templates map to `references/templates/`.
- Claude skill testing concepts map to `tests/skill-catalog.json`, `references/quality-rubric.md`, and `scripts/validate_repository.py`.
- Codex-native skill frontmatter uses only `name` and `description`.

## Attribution

This project is inspired by the MIT-licensed Claude Code Game Studios project by Donchitos. The Codex version is a compatibility-oriented adaptation, not a drop-in replacement.

If you publish this repository, keep the attribution and MIT license text.

## Status

Version `0.4.0` adds the third parity layer: validation catalog, quality rubric, repository validator, and GitHub Actions.
