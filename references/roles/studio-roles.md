# Studio Roles

Use these roles as review lenses, not as automatic subagents.

## Leadership

| Role | Use for | Owns | Must not |
| --- | --- | --- | --- |
| Creative director | Vision, pillars, theme, player promise | Experience consistency | Override production constraints without trade-off |
| Technical director | Architecture, engine fit, long-term technical risk | Technical direction | Micromanage feature code |
| Producer | Scope, milestones, risks, coordination | Shipping path | Make creative or technical decisions alone |

## Department leads

| Role | Use for | Owns | Must not |
| --- | --- | --- | --- |
| Game designer | Mechanics, progression, balance, loops | Player decisions | Approve technical architecture |
| Lead programmer | Implementation plan, APIs, code quality | Code structure | Rewrite design goals |
| Art director | Visual style, asset standards, UI visual direction | Visual identity | Promise impossible asset scope |
| Audio director | Music, SFX palette, mix strategy | Audio identity | Ignore implementation constraints |
| Narrative director | Story arcs, lore, dialogue strategy | Narrative coherence | Add story that fights gameplay |
| QA lead | Test strategy, bug triage, release risk | Quality evidence | Treat unrun tests as passing |
| Release manager | Builds, versions, launch readiness | Release process | Hide known issues |
| Localization lead | String externalization, locale QA | Localization readiness | Translate without context |

## Design and content specialists

| Role | Use for | Owns |
| --- | --- | --- |
| Systems designer | Formulas, systemic loops, buildcraft, tuning |
| Level designer | Level flow, encounters, pacing, spatial learning |
| Economy designer | Currencies, sinks, rewards, loot, progression |
| UX designer | User flows, HUD, menus, onboarding, accessibility |
| Prototyper | Throwaway proof-of-fun builds and feasibility tests |
| Writer | Dialogue, item text, barks, prose |
| World builder | Factions, geography, history, world rules |
| Sound designer | SFX lists, feedback sounds, implementation notes |
| Technical artist | Shaders, VFX, asset optimization, art pipeline |
| Accessibility specialist | Remapping, contrast, text scaling, assistive options |
| Live-ops designer | Events, seasons, retention loops |
| Community manager | Player communication, patch messaging, feedback health |

## Programming specialists

| Role | Use for | Owns |
| --- | --- | --- |
| Gameplay programmer | Player mechanics and gameplay systems |
| Engine programmer | Rendering, physics, memory, low-level systems |
| AI programmer | NPC behavior, state machines, pathfinding |
| Network programmer | Replication, matchmaking, latency, net security |
| Tools programmer | Editor tools, debug tools, pipeline automation |
| UI programmer | UI implementation, binding, screen logic |
| Performance analyst | Profiling, budgets, bottleneck diagnosis |
| DevOps engineer | CI, build scripts, deployment, versioning |
| Analytics engineer | Telemetry, event schemas, dashboards |
| Security engineer | Anti-cheat, exploit prevention, save/network security |
| QA tester | Test cases, manual execution, bug reports |

## Engine specialists

| Role | Use for |
| --- | --- |
| Godot specialist | Godot scene architecture, signals, resources, exports |
| Godot GDScript specialist | Static typing, script patterns, coroutines, performance |
| Godot C# specialist | .NET interop, signals, async, typed nodes |
| Godot shader specialist | Godot shading language, particles, post-processing |
| Godot GDExtension specialist | Native extensions, C++/Rust bindings |
| Unity specialist | MonoBehaviour architecture, packages, scenes, builds |
| Unity DOTS specialist | ECS, Jobs, Burst, data-oriented performance |
| Unity shader specialist | Shader Graph, VFX Graph, URP/HDRP |
| Unity Addressables specialist | Asset groups, async loading, memory |
| Unity UI specialist | UI Toolkit, UGUI, input and canvas performance |
| Unreal specialist | UE gameplay framework, Blueprint/C++ boundaries |
| UE GAS specialist | Abilities, effects, attributes, tags |
| UE Blueprint specialist | Blueprint architecture and graph standards |
| UE replication specialist | RPCs, replicated properties, relevancy |
| UE UMG specialist | UMG, CommonUI, input, widget performance |

## Selection rule

- Planning: Producer, Creative director, Technical director.
- Game design: Creative director, Game designer, UX designer.
- Architecture: Technical director, Lead programmer, engine specialist.
- Implementation: Lead programmer, relevant programmer, QA lead.
- Release: Release manager, QA lead, Producer.
