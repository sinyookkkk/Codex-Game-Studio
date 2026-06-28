# Unreal Reference

Use for Unreal Engine 5 projects.

## Architecture

- Define Blueprint versus C++ boundaries.
- Use Gameplay Framework classes deliberately: GameMode, GameState, PlayerState, Controller, Pawn, Components.
- Document replication ownership when multiplayer exists.
- Keep GAS, CommonUI, and plugin adoption decisions in ADRs.

## Checks

- `.uproject` exists and engine version is known.
- Packaging settings are tested early.
- Target hardware and performance budgets are explicit.
- Blueprint graphs follow naming and organization standards.
- Save, input, and settings systems are documented.

## Common risks

- Blueprint logic with no ownership boundaries.
- Replication added after systems are already coupled.
- Asset and shader complexity discovered too late.
