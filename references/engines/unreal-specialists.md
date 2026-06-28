# Unreal Specialist Notes

Use with `references/engines/unreal.md` when a task needs deeper Unreal guidance.

## Gameplay Ability System

- Use GAS for ability-heavy, network-aware, status-effect-rich games.
- Avoid GAS for tiny prototypes unless it proves a future architecture.

## Blueprint

- Keep Blueprint ownership clear and avoid hidden global logic.
- Move repeated or performance-sensitive logic into C++ when needed.

## Replication

- Define authority, prediction, rollback expectations, and bandwidth risk.
- Test multiplayer behavior early with real packaged builds when possible.

## UMG and CommonUI

- Keep input mode, focus, navigation, and platform UI rules explicit.
- Test controller and keyboard navigation before release gates.
