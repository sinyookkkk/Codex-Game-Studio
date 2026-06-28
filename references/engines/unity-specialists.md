# Unity Specialist Notes

Use with `references/engines/unity.md` when a task needs deeper Unity guidance.

## DOTS and ECS

- Use only when data volume or performance justifies complexity.
- Keep authoring and runtime data boundaries clear.

## Addressables

- Use for memory control, DLC, remote content, or large asset sets.
- Define labels, lifecycle, and failure handling.

## Shader and VFX

- Budget effects by target hardware.
- Keep fallbacks for low-end devices.

## UI Toolkit and UGUI

- Choose UI Toolkit for tool-like or modern UI flows.
- Choose UGUI when project legacy, package support, or runtime patterns require it.
