# Demo Transcripts

Use these short transcripts when explaining the plugin on GitHub or when sanity-checking a fresh Codex install.

## Adopt a project

User:

```text
Use Codex Game Studio to adopt this existing Godot project and tell me the current phase.
```

Codex should:

- Load `game-studio-onboarding`.
- Inspect project files, docs, build scripts, and playable evidence.
- Name the current phase with confidence and caveats.
- Recommend the next playable step and the skill to use next.

## Gate a vertical slice

User:

```text
Review whether this prototype can move into vertical slice production.
```

Codex should:

- Load `game-studio-gate`.
- Compare evidence against `references/workflow-catalog.md`.
- Return `PASS`, `CONCERNS`, or `FAIL`.
- Name the missing evidence and next validation action.

## Prepare release

User:

```text
Prepare a launch checklist, known issues note, and hotfix triage plan for this build.
```

Codex should:

- Load `game-studio-release`.
- Use release and patch-note templates.
- Separate player-facing notes from internal risk handling.
- Include QA evidence required before release approval.
