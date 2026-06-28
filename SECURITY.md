# Security Policy

Codex Game Studio is a workflow and documentation plugin. It should not require secrets, credentials, or privileged services.

## Reporting

Open a private security advisory on GitHub if available, or contact the repository owner before publishing exploit details.

## Scope

Security-relevant issues include:

- Instructions that encourage exposing secrets.
- Scripts that execute untrusted input.
- Plugin metadata that misrepresents capabilities.
- Release guidance that hides known player-impacting data loss risks.

## Baseline

Run validation before release:

```bash
python scripts/validate_repository.py
```
