# Templates

Use these compact templates when the user asks Codex to create or review game planning artifacts.

## Game concept

```markdown
# Game Concept

## Pitch
- One sentence:
- Target player:
- Platform:

## Pillars
1.
2.
3.

## Core Loop
1. Player action:
2. System response:
3. Reward or consequence:
4. Reason to repeat:

## Prototype Question
- The prototype only needs to prove:
- Success looks like:
- Stop if:
```

## System design

```markdown
# System Design: [Name]

## Purpose
- Player problem solved:
- Pillar supported:

## Rules
- Inputs:
- State:
- Outputs:
- Failure cases:

## Tuning
| Variable | Starting value | Reason |
| --- | --- | --- |

## Acceptance Criteria
- [ ] Runnable in game.
- [ ] Clear player feedback.
- [ ] Tested with at least one success and one failure path.
```

## Sprint plan

```markdown
# Sprint Plan

## Goal
- Playable outcome:
- Not included:

## Tasks
| Priority | Task | Owner lens | Estimate | Acceptance check |
| --- | --- | --- | --- | --- |

## Risks
| Risk | Impact | Mitigation |
| --- | --- | --- |

## Verification
- Run:
- Observe:
- Pass:
```

## Playtest report

```markdown
# Playtest Report

## Build
- Version:
- Date:
- Tester profile:

## Tasks Observed
| Task | Completed? | Notes |
| --- | --- | --- |

## Findings
| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |

## Next Test Question
-
```

## Release checklist

```markdown
# Release Checklist

## Build
- Version:
- Platform:
- Build command:

## Required Checks
- [ ] Starts from clean install.
- [ ] Main loop is playable.
- [ ] Settings, save, pause, restart, and quit paths work.
- [ ] Known issues documented.
- [ ] Patch notes drafted.

## Ship Decision
- Ship / hold:
- Reason:
- Follow-up:
```
