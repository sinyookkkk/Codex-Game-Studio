# Unity Reference

Use for Unity projects.

## Architecture

- Pin Unity version and package versions.
- Keep scene, prefab, scriptable object, and runtime service ownership clear.
- Prefer simple MonoBehaviour architecture unless DOTS is justified.
- Isolate save, input, audio, and scene loading services.

## Checks

- `ProjectSettings/ProjectVersion.txt` exists.
- Packages are documented.
- Build target and render pipeline are known.
- Play Mode or Edit Mode tests cover risky systems.
- Addressables or asset loading strategy is explicit when needed.

## Common risks

- Prefab dependencies hidden in inspector state.
- Scene singleton sprawl.
- Package upgrades without regression checks.
