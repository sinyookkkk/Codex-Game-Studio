# unreal rendering Module

Use this reference when a Codex Game Studio task needs rendering decisions for a unreal game.

## Check first

- Identify the current project phase before recommending implementation depth.
- Name the smallest playable behavior that proves the module works.
- Keep the design, architecture, QA, and release evidence connected.
- Prefer maps, actors, components, assets, gameplay framework boundaries, and packaged build evidence.

## Evidence to ask for

- Current files or systems that own the module.
- A runnable scene, level, page, or build path.
- Player-facing success criteria.
- A failure case and how it will be observed.

## Review lens

- Design: Does the module support the intended player behavior?
- Architecture: Is ownership clear and testable?
- QA: Can a smoke check prove the module is not broken?
- Release: Is the risk visible in known issues or patch notes when needed?
