# Godot Reference

Use for Godot 4 projects.

## Architecture

- Prefer small scenes with clear ownership and signal-based communication.
- Use resources for shared data and authored configuration.
- Keep autoloads minimal: services such as save, settings, audio, or scene routing.
- Avoid deeply coupled node paths; use exported references or typed lookup wrappers.

## Checks

- `project.godot` exists and engine version is known.
- Input Map contains documented actions.
- Export presets exist before release.
- Save paths and settings paths are platform-safe.
- Headless smoke tests are available when practical.

## Common risks

- Large scene scripts doing state, UI, input, and persistence together.
- Unclear signal ownership.
- Runtime-only node references that break when scenes are reorganized.
