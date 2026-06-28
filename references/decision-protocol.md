# Decision Protocol

Use this reference when a game decision has meaningful tradeoffs, role disagreement, scope pressure, or cross-discipline consequences.

## User owns the decision

Codex provides options and analysis. The user makes the final call. Do not present a recommendation as a command.

## Decision shape

1. State the decision question in one sentence.
2. List the constraints: player promise, time, budget, engine, team, release risk.
3. Present two to four options.
4. For each option, list benefit, cost, downstream impact, and risk.
5. Recommend one option with reasons.
6. Ask for or record the user's decision.
7. Cascade the decision to affected design, architecture, QA, release, and docs.
8. Define evidence that would prove the decision was correct or needs reversal.

## Conflict routing

| Conflict | Primary lenses | Escalation |
| --- | --- | --- |
| Creative direction | Creative director, game designer, UX designer | Creative director |
| Architecture or performance | Technical director, lead programmer, engine specialist | Technical director |
| Scope or schedule | Producer, release manager, QA lead | Producer |
| Release risk | Release manager, QA lead, community manager | Producer |

## Output template

```text
Decision: ...
Constraints: ...
Options:
1. ...
2. ...
Recommendation: ...
User decision: ...
Cascade:
- Design:
- Architecture:
- QA:
- Release:
Validation signal: ...
```
