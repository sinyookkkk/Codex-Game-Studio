# Security And Permission Policy

Use this policy as the Codex-native replacement for Claude Code settings allow/deny rules.

## Safe by default

Prefer read-only inspection before edits:

- `git status`, `git diff`, `git log`
- directory listings
- repository validators
- test commands that do not need secrets

## Require explicit care

Treat these as high-risk:

- Recursive deletion or force resets.
- Force pushes or history rewriting.
- Commands that read or write `.env`, secrets, tokens, or credentials.
- Installers, network calls, cloud actions, deployment, payment, or account changes.
- Scripts that execute untrusted project data as code.

## Game-specific risks

- Save-data migrations can destroy player progress.
- Economy changes can create exploits.
- Network and backend changes can expose player data.
- Release notes must not hide known data-loss or security risks.

## Output rule

When risk is high, state the risk, the safer verification path, and the rollback or backup step.
