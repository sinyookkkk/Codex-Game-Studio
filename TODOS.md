# Codex Game Studio Migration TODOs

This list tracks the remaining gap between Codex Game Studio and Claude Code Game Studios. The goal is not a mechanical clone; the goal is a Codex-native plugin that can cover the full game-studio workflow with installable skills, references, validation, examples, and release hygiene.

## Current parity snapshot

| Area | Current state | Gap | Status |
| --- | --- | --- | --- |
| Plugin packaging | Codex plugin manifest exists and points to `./skills/`. | Add richer usage docs, marketplace-ready screenshots later. | In progress |
| Command surface | 73 Claude slash commands are represented by 7 Codex skills plus `references/command-mapping.md`. | Add forward-test examples that prove each aggregate skill handles the mapped commands. | In progress |
| Role system | 49 Claude agents are represented as role lenses. | Add role-specific review examples and richer coordination recipes. | Open |
| Hooks and statusline | Claude-only hooks are intentionally omitted. | Document Codex replacements: skills, validators, CI, and manual review gates. | In progress |
| Skill testing | Basic skill catalog and validator exist. | Add forward-test specs, scenario examples, and expected evidence checks. | In progress |
| Engine references | Godot, Unity, Unreal, and web notes exist. | Add module-level references for input, UI, save, build, networking, performance, and rendering. | Open |
| Templates | Core game, QA, release, UX, art, and architecture templates exist. | Add missing collaborative protocols, accessibility requirements, pitch, player journey, and incident response templates. | Open |
| Public GitHub readiness | README, license, validation workflow exist. | Add contributing guide, security policy, issue templates, PR template, changelog, and release process. | Open |
| Examples | README prompts exist. | Add full walkthrough sessions for brownfield adoption, combat feature planning, scope crisis, release, and UX review. | Open |

## Phase 0: Finish platform support

- [x] Add Linux/macOS validation wrapper.
- [x] Add Windows PowerShell validation wrapper.
- [x] Run validation through Ubuntu, macOS, and Windows in GitHub Actions.
- [ ] Commit and push the cross-platform validation change.

## Phase 1: Make Codex usage self-contained

- [x] Add a Codex usage guide.
- [x] Add a Claude-to-Codex adaptation map.
- [x] Update README to point users at the usage guide, adaptation map, and forward tests.
- [ ] Add screenshots or short demo transcripts for GitHub readers.

## Phase 2: Make skills testable

- [x] Add one forward-test case per Codex skill.
- [x] Extend the repository validator to check forward-test coverage.
- [ ] Add expected-output examples for the most important workflows.
- [ ] Add a script that renders a human-readable test report from `tests/forward-tests.json`.

## Phase 3: Restore depth from Claude Code Game Studios

- [ ] Expand engine references into module pages for Godot, Unity, Unreal, and web.
- [ ] Add role-specific coordination recipes for combat, UI, QA, release, narrative, audio, live ops, and polish.
- [ ] Add missing public templates: accessibility requirements, pitch document, player journey, incident response, post-mortem, and collaborative protocols.
- [ ] Add example sessions based on the original project's workflow examples.

## Phase 4: GitHub project maturity

- [ ] Add `CONTRIBUTING.md`.
- [ ] Add `SECURITY.md`.
- [ ] Add `.github/ISSUE_TEMPLATE/bug_report.md`.
- [ ] Add `.github/ISSUE_TEMPLATE/feature_request.md`.
- [ ] Add `.github/PULL_REQUEST_TEMPLATE.md`.
- [ ] Add a changelog and release tagging checklist.

## Definition of complete

Codex Game Studio is complete enough to share broadly when:

- A user can install the plugin and understand the entry points from README alone.
- Every skill has at least one forward-test case with expected evidence.
- The validator checks plugin shape, skill frontmatter, catalogs, forward tests, references, wrappers, and placeholder patterns.
- The repository documents how Claude-only agents, hooks, statusline, and settings map to Codex-native behavior.
- GitHub readers see contribution, security, issue, PR, and release guidance.
