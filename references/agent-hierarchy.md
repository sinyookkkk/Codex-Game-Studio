# Studio Hierarchy

Codex Game Studio uses role lenses rather than live Claude subagents, but it keeps the same studio logic.

## Tier 1: Directors

| Lens | Owns | Must not |
| --- | --- | --- |
| Creative director | Vision, pillars, tone, player promise | Ignore scope or implementation reality |
| Technical director | Architecture, performance, technical debt | Micromanage every feature |
| Producer | Scope, schedule, dependencies, release timing | Override creative goals without tradeoff |

Tier 1 resolves conflicts and makes strategic recommendations.

## Tier 2: Leads

Game designer, lead programmer, art director, audio director, narrative director, QA lead, release manager, localization lead, and similar roles translate strategy into department guidance.

Tier 2 can consult horizontally but should escalate binding cross-discipline decisions.

## Tier 3: Specialists

Specialists focus on execution: gameplay, engine, AI, networking, tools, UI, systems, level, economy, technical art, sound, writing, worldbuilding, accessibility, performance, analytics, security, live ops, community, and engine-specific concerns.

## Delegation pattern

Use this compact chain:

```text
Director frames decision -> Lead shapes plan -> Specialist identifies implementation evidence -> QA verifies result
```

## Conflict pattern

When two lenses disagree:

1. Name the disagreement.
2. Identify the shared higher-level owner.
3. Apply the decision protocol.
4. Record the accepted tradeoff.
