# Audit And Cost Notes

Claude Code Game Studios uses agent logs and model tiers. Codex Game Studio represents this as review depth and explicit evidence.

## Review depth as cost control

- `solo`: one lens, lowest context cost.
- `lean`: two to four lenses, default.
- `full`: directors plus leads, highest context cost.

## Audit trail

For important decisions, record:

- Prompt or user request.
- Chosen mode and lenses.
- Options considered.
- User decision.
- Evidence or verification command.
- Follow-up owner or file.

Use project docs, ADRs, release notes, or test evidence files rather than hidden logs.
