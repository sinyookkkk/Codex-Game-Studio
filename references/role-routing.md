# Role Routing

Use this reference to decide which studio perspective Codex should simulate during a game development task. Do not pretend these are autonomous agents. Treat them as review lenses.

For the full 49-role roster, read `references/roles/studio-roles.md`.

## Quick routing

| Lens | Use when | Main question |
| --- | --- | --- |
| Producer | Planning, milestones, scope, risk, cross-discipline coordination. | Can this ship with the available time and evidence? |
| Creative director | Vision, pillars, theme, player promise, consistency. | Does this serve the intended experience? |
| Game designer | Mechanics, loops, balance, progression, player motivation. | Does the system create the intended decisions and emotions? |
| Technical director | Architecture, engine fit, maintainability, performance risk. | Can this be built safely and changed later? |
| Lead programmer | Implementation sequence, task decomposition, code quality. | What should be built first and how will it be verified? |
| UX designer | Menus, HUD, onboarding, interaction clarity, accessibility. | Can players understand and operate the game smoothly? |
| QA lead | Test strategy, risk areas, regression coverage, evidence. | What could break and how will we know? |
| Release manager | Packaging, launch checklist, patch flow, known issues. | Is the build ready for real players? |

## Routing rule

For broad tasks, use two or three lenses only. Too many review voices create noise. For implementation tasks, use Producer, Lead programmer, and QA lead. For design tasks, use Creative director, Game designer, and UX designer.
