# Studio Workflow

Use this reference when a user asks how to move a game from idea to playable build, from playable build to production, or from production to release.

## Phase map

| Phase | Goal | Evidence |
| --- | --- | --- |
| Concept | Define the promise, audience, pillars, and core loop. | One-sentence pitch, pillars, prototype question. |
| Prototype | Prove the main interaction can be fun quickly. | A small playable scene or simulation. |
| Systems design | Describe the MVP systems and how they reinforce the core loop. | GDD sections for each MVP system. |
| Technical setup | Choose engine, architecture, data model, input, save, and build path. | Architecture notes and runnable skeleton. |
| Vertical slice | Build one production-quality path through the game. | Playable slice with UI, feedback, audio, fail/retry, and test notes. |
| Production | Implement scoped stories in small batches. | Sprint plan, story acceptance criteria, test evidence. |
| Release | Stabilize, package, document, and ship. | Release checklist, known issues, patch notes, build artifact. |

## Default decision rhythm

1. Ask what the player should feel or do.
2. Identify the smallest playable proof.
3. Name what is deliberately out of scope.
4. Break work into one-day to three-day tasks.
5. Define a run command and acceptance check for each task.
6. Review evidence before expanding scope.

## Quality gates

- Concept gate: The core loop is understandable in one paragraph.
- Prototype gate: The game can be run and the core interaction can be tested.
- Systems gate: Every MVP system supports a pillar or core loop step.
- Vertical slice gate: First-time players can understand, act, fail, recover, and retry.
- Release gate: The build can be installed or launched cleanly and has a known-issues list.
