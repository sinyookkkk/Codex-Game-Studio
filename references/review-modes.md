# Review Modes

Use review modes to control depth, cost, and output size.

| Mode | Use when | Lenses | Output |
| --- | --- | --- | --- |
| `solo` | User wants quick guidance or task is narrow | One primary lens | Short finding list and next action |
| `lean` | Most planning and review tasks | Two to four lenses | Risks, tradeoffs, recommendation, evidence |
| `full` | Phase gates, release gates, large architecture/design decisions | Directors, relevant leads, QA/release | Verdict, decision options, cascade, validation plan |

## Defaults

- Use `lean` unless the user asks for speed or full review.
- Use `solo` for small tactical tasks.
- Use `full` for irreversible decisions, release readiness, or high-cost architecture.

## Response discipline

Do not simulate a long meeting. Summarize what each lens contributes, then converge on one actionable recommendation.
