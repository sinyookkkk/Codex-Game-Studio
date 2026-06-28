# Engine Routing

Use this reference when the user has chosen or is choosing an engine.

## Godot

Best for small to mid-sized 2D and 3D indie games, fast iteration, open-source workflows, and lightweight tooling. Prefer GDScript unless the project needs C# ecosystem integration or heavier architecture.

Check:
- `project.godot` exists.
- Scenes are small and composable.
- Input actions are configured.
- Export presets exist before release.
- Smoke tests can run headless when possible.

## Unity

Best for mobile, cross-platform commercial pipelines, asset-store-heavy workflows, and teams already comfortable with C#. Prefer clear assembly boundaries and avoid overengineering ECS unless the scale demands it.

Check:
- Unity version is pinned.
- Packages are documented.
- Scenes and prefabs have ownership rules.
- Build targets are known.
- Play mode and edit mode tests cover risky systems.

## Unreal

Best for high-fidelity 3D, complex animation, multiplayer-heavy work, and Blueprint/C++ hybrid teams. Be explicit about what lives in Blueprint versus C++.

Check:
- Engine version is pinned.
- Gameplay framework ownership is clear.
- Replication rules are documented if multiplayer exists.
- Packaging settings are tested early.
- Performance budgets are defined for target hardware.

## Web

Best for small experiments, jam games, portfolio games, and fast distribution. Keep the first loop tiny and test browser input, audio unlock, scaling, and save storage early.

Check:
- Game fits mobile or desktop target deliberately.
- Canvas sizing is stable.
- Assets load reliably.
- Keyboard, pointer, and touch behavior are tested.
