# Migration Notes

This repository is not a mechanical copy of Claude Code Game Studios. It is a Codex-native adaptation.

## What changed

- Claude Code slash commands became Codex skills.
- Claude Code subagents became role-routing review lenses.
- Claude Code hooks and status line configuration were omitted.
- Claude-only frontmatter fields were removed.
- The 73-command surface is represented by seven broad skills and a command mapping reference.

## Phase 1 alignment

Version `0.2.0` added the first parity layer:

- `game-studio-onboarding` for `/start`, `/help`, `/project-stage-detect`, `/setup-engine`, and `/adopt` style work.
- `game-studio-gate` for `/gate-check`, `/story-readiness`, `/story-done`, `/design-review`, and related readiness reviews.
- `game-studio-architecture` for `/create-architecture`, `/architecture-decision`, `/architecture-review`, and `/create-control-manifest`.
- `references/workflow-catalog.md` as the Codex-native phase catalog.
- `references/command-mapping.md` as the Claude slash command translation table.

## Phase 2 alignment

Version `0.3.0` added the second parity layer:

- `references/templates/` with compact templates for concept, GDD, systems, UX, art, architecture, sprint, QA, release, and changelog work.
- `references/roles/` with the full 49-role studio roster adapted into Codex review lenses.
- `references/rules/` with 11 coding and content standards adapted from Claude path-scoped rules.
- `references/engines/` with Godot, Unity, Unreal, and web-specific guidance.
- Existing skills route to the new references through progressive disclosure.

## Phase 3 alignment

Version `0.4.0` added the third parity layer:

- `tests/skill-catalog.json` as a lightweight equivalent of the CCGS skill catalog.
- `references/quality-rubric.md` for skill, reference, workflow, and release quality checks.
- `scripts/validate_repository.py` for no-dependency repository validation.
- `.github/workflows/validate.yml` to run validation on pushes and pull requests.

## Why consolidate

Codex skills are most useful when they provide concise routing and load detailed references only when needed. A direct 73-skill migration would be harder to maintain and would duplicate many overlapping workflows.

## Cross-platform validation

Version `0.4.1` adds:

- `scripts/validate_repository.sh` for Linux and macOS.
- `scripts/validate_repository.ps1` for Windows PowerShell and PowerShell Core.
- `.gitattributes` rules to keep scripts and repository metadata with predictable line endings.
- A GitHub Actions matrix that validates Ubuntu, macOS, and Windows.

## Phase 4 alignment

Version `0.5.0` adds the fourth parity layer:

- `TODOS.md` to track the remaining migration gap by feature area.
- `docs/codex-usage-guide.md` to make plugin usage self-contained for Codex users.
- `references/codex-adaptation-map.md` to document replacements for Claude slash commands, agents, hooks, settings, and testing concepts.
- `tests/forward-tests.json` to give every Codex skill a realistic prompt and expected evidence checks.
- Validator coverage for the new forward-test suite.

## Future expansion

Good next additions:

- More detailed engine modules for Godot, Unity, and Unreal.
- Optional marketplace metadata and screenshots.
- Forward-test examples for each skill.
- Optional release tags and changelog automation.
