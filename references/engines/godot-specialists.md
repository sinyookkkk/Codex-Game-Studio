# Godot Specialist Notes

Use with `references/engines/godot.md` when a task needs deeper Godot guidance.

## GDScript

- Prefer typed variables and clear signal ownership.
- Keep autoloads small and service-like.
- Use resources for data when designers need editable tuning.

## C#

- Use C# when static typing, tooling, or library access matters.
- Keep Godot node lifecycle boundaries explicit.

## GDExtension

- Reserve for performance-critical native integrations or platform APIs.
- Require build, packaging, and fallback notes before committing.

## Shaders

- Tie shader cost to a visual reason.
- Capture before/after screenshots or frame timing for risky effects.
