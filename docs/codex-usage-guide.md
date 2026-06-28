# Codex Usage Guide

Codex Game Studio is a Codex-native adaptation of Claude Code Game Studios. Use it as a plugin that gives Codex a small studio operating model for game projects: onboarding, design, production planning, architecture, gate reviews, QA, and release.

## Install and validate

Clone the repository and install it through the Codex local plugin flow. The plugin manifest is:

```text
.codex-plugin/plugin.json
```

Before sharing or reinstalling the plugin, run validation:

```bash
# Linux/macOS
sh scripts/validate_repository.sh

# Any platform with Python 3
python scripts/validate_repository.py
```

```powershell
# Windows PowerShell / PowerShell Core
.\scripts\validate_repository.ps1
```

## Start a game project

Ask Codex to use the onboarding workflow when the project state is unclear:

```text
Use Codex Game Studio to inspect this game project, identify its current phase, and tell me the next playable step.
```

Codex should load `game-studio-onboarding`, inspect existing docs and code, then route to the right follow-up skill.

## Choose the right skill

| Need | Skill |
| --- | --- |
| Start, adopt, detect phase, choose engine | `game-studio-onboarding` |
| Plan milestones, epics, stories, vertical slices | `game-studio-flow` |
| Create or review game design, UX, systems, balance | `game-studio-design` |
| Create technical plans, ADRs, boundaries, control manifests | `game-studio-architecture` |
| Decide readiness, phase gates, story done, design approval | `game-studio-gate` |
| Plan smoke, regression, playtest, evidence, bug triage | `game-studio-qa` |
| Prepare release, patch notes, hotfixes, retrospectives | `game-studio-release` |

## Work like a small studio

Use this loop for most projects:

1. Start with `game-studio-onboarding` to identify the phase.
2. Use `game-studio-design` to make the player promise and core loop testable.
3. Use `game-studio-architecture` to define implementation boundaries and risk.
4. Use `game-studio-flow` to produce a small playable milestone.
5. Use `game-studio-qa` to define evidence before claiming completion.
6. Use `game-studio-gate` to decide whether to advance.
7. Use `game-studio-release` when builds, patch notes, and launch risk matter.

## Claude Code feature replacements

Claude Code Game Studios uses slash commands, subagents, hooks, statusline scripts, and Claude settings. Codex Game Studio maps those features differently:

| Claude feature | Codex replacement |
| --- | --- |
| Slash commands | Seven broad Codex skills plus `references/command-mapping.md` |
| Subagents | Role lenses in `references/roles/studio-roles.md` |
| Hooks | Repository validator, GitHub Actions, QA checklists, and gate reviews |
| Statusline | Explicit phase summaries from `game-studio-onboarding` and `game-studio-flow` |
| Settings files | Plugin manifest and skill metadata |
| Skill testing framework | `tests/skill-catalog.json`, `tests/forward-tests.json`, `references/quality-rubric.md`, and `scripts/validate_repository.py` |

## Good prompts

```text
Use Codex Game Studio to adopt this existing Godot project and tell me what phase it is in.
```

```text
Create a vertical slice plan for this combat prototype with acceptance criteria and a smoke test.
```

```text
Review this GDD with game designer, UX, QA, and technical director lenses. Give me a PASS, CONCERNS, or FAIL verdict.
```

```text
Create an ADR for save data, scene loading, and platform storage risks.
```

```text
Prepare release notes, known issues, and a day-one patch triage plan for this build.
```
