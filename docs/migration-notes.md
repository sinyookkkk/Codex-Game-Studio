# Migration Notes

This repository is not a mechanical copy of Claude Code Game Studios. It is a Codex-native adaptation.

## What changed

- Claude Code slash commands became Codex skills.
- Claude Code subagents became role-routing review lenses.
- Claude Code hooks and status line configuration became validation scripts, CI checks, and gate reviews.
- Claude-only frontmatter fields were removed.
- The 73-command surface is represented by seven broad skills and command mapping references.

## Completed parity layers

Version `0.2.0` added onboarding, gate, architecture, workflow catalog, and command mapping.

Version `0.3.0` added templates, role lenses, rules, engine routing, and progressive-disclosure references.

Version `0.4.0` added the skill catalog, quality rubric, repository validator, and GitHub Actions.

Version `0.4.1` added Linux, macOS, and Windows validation wrappers.

Version `0.5.0` added Codex usage guidance, adaptation mapping, and forward-test validation.

Version `0.6.0` completes the tracked migration items:

- Demo transcripts and example sessions for GitHub readers.
- Expected outputs and a forward-test report renderer.
- Module-level engine references for Godot, Unity, Unreal, and web.
- Role coordination recipes for combat, UI, QA, release, narrative, audio, live ops, and polish.
- Accessibility, pitch, player journey, incident, post-mortem, and collaboration templates.
- GitHub contribution, security, issue, pull request, changelog, and release process files.
- Validator coverage for the completed asset set.

## Why consolidate

Codex skills are most useful when they provide concise routing and load detailed references only when needed. A direct 73-skill migration would be harder to maintain and would duplicate many overlapping workflows.
Version `0.7.0` adds the deep studio-intelligence layer:

- Game design theory for MDA, SDT, flow, and Bartle player motivation.
- User-owned decision protocol, review modes, and studio hierarchy.
- Path rule mapping and Codex-native replacements for Claude hooks.
- Security, audit, session lifecycle, and cost-control references.
- Deeper Godot, Unity, and Unreal specialist notes.
- Command-level specs for high-risk workflow commands.
The deep parity checklist is documented in migration notes and validation rules rather than committed as a TODO file.
