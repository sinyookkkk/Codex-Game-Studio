---
name: game-studio-gate
description: Phase gate, readiness, and completion review workflow for Codex game projects. Use when the user asks whether a project can move to the next phase, needs a gate check, design review, architecture review, story readiness review, story done review, cross-GDD review, or a PASS/CONCERNS/FAIL verdict.
---

# Game Studio Gate

Use this skill to review evidence before advancing a game project. It adapts Claude Code Game Studios gate and readiness commands into one Codex-native review workflow.

## Required references

- Read `../../references/agent-hierarchy.md` when resolving cross-role disagreement.

- Read `../../references/review-modes.md` to choose solo, lean, or full review depth.

- Read `../../references/workflow-catalog.md` to identify expected phase artifacts.
- Read `../../references/role-routing.md` to choose review lenses.
- Read `../../references/templates.md` when recommending missing artifacts.

## Gate types

| Gate | Use when | Verdicts |
| --- | --- | --- |
| Concept gate | Moving from concept to systems design | PASS / CONCERNS / FAIL |
| Systems gate | GDDs and system map are ready for architecture | PASS / CONCERNS / FAIL |
| Architecture gate | Architecture and ADRs are ready for production planning | PASS / CONCERNS / FAIL |
| Pre-production gate | UX, epics, stories, tests, and slice evidence are ready | PASS / CONCERNS / FAIL |
| Story readiness | A story is ready to implement | READY / NEEDS WORK / BLOCKED |
| Story done | A story is complete | DONE / DONE WITH RISKS / NOT DONE |
| Release gate | Build can ship | SHIP / SHIP WITH RISKS / HOLD |

## Review process

1. Identify the requested gate and current phase.
2. Gather evidence from the repo, docs, tests, and build notes.
3. Compare evidence against the expected artifacts in `workflow-catalog.md`.
4. Review from two or three lenses only:
   - Phase gates: Producer, Creative director, Technical director, QA lead.
   - Story gates: Lead programmer, Game designer, QA lead.
   - Release gates: Release manager, QA lead, Technical director.
5. Lead with a verdict token.
6. List blockers, risks, and optional improvements separately.
7. Recommend the next action.

## Output

```markdown
## Verdict
PASS / CONCERNS / FAIL

## Evidence Reviewed
-

## Blockers
| Blocker | Impact | Required fix |
| --- | --- | --- |

## Risks
| Risk | Impact | Mitigation |
| --- | --- | --- |

## Optional Improvements
-

## Next Action
-
```

## Guardrails

- Do not produce a PASS verdict without concrete evidence.
- Distinguish blockers from risks. Blockers prevent advancement; risks can be accepted by the user.
- If evidence is missing, say what file or test would prove readiness.
- Gates are advisory. The user decides whether to proceed.
