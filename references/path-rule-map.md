# Path Rule Map

Codex cannot auto-inject path-scoped Claude rules, so use this map when reviewing or editing a game project.

| Project path | Rule reference | Review focus |
| --- | --- | --- |
| `src/gameplay/**` | `references/rules/gameplay-code.md` | Data-driven mechanics, delta time, no UI ownership |
| `src/core/**` | `references/rules/engine-code.md` | Stable APIs, lifecycle, memory-sensitive paths |
| `src/ai/**` | `references/rules/ai-code.md` | Debuggability, budgets, tunable parameters |
| `src/networking/**` | `references/rules/network-code.md` | Authority, validation, message versioning |
| `src/ui/**` | `references/rules/ui-code.md` | State separation, localization, accessibility |
| `design/gdd/**` | `references/rules/design-docs.md` | Pillars, loops, formulas, edge cases |
| `tests/**` | `references/rules/test-standards.md` | Naming, fixtures, evidence, flakiness |
| `prototypes/**` | `references/rules/prototype-code.md` | Explicit hypothesis, relaxed standards, exit path |
| `assets/**` | `scripts/check_assets.py` | File naming, JSON validity, asset evidence |

When a task mentions one of these paths, load the matching rule reference before giving final advice.
