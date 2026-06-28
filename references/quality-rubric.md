# Quality Rubric

Use this rubric when reviewing Codex Game Studio skills, references, and outputs. It is inspired by the Claude Code Game Studios testing framework but adapted for Codex.

## Skill quality

| Check | Pass signal |
| --- | --- |
| Frontmatter | `SKILL.md` has `name` and `description`; the name matches the folder. |
| Triggering | Description names the workflow and concrete user requests that should trigger it. |
| Progressive disclosure | The skill points to specific reference files instead of embedding every detail. |
| Output guidance | The skill gives a clear process, verdict, or artifact shape. |
| Guardrails | The skill states what not to claim or do without evidence. |

## Reference quality

| Check | Pass signal |
| --- | --- |
| Discoverability | Referenced files exist and are linked from a skill or index. |
| Scope | A reference covers one clear topic. |
| Usability | Templates include headings and fields a user can fill immediately. |
| Codex-native wording | References avoid Claude-only tool names unless in compatibility mapping. |
| Maintenance | No unfinished markers or placeholder publisher names remain. |

## Workflow quality

| Category | Required behavior |
| --- | --- |
| Onboarding | Inspect project evidence before asking broad questions. |
| Design | Tie recommendations to player behavior and validation evidence. |
| Architecture | Prefer engine-native patterns and produce verifiable decisions. |
| Gate | Lead with a verdict and separate blockers from risks. |
| QA | Mark manual or unrun tests clearly; never imply unrun tests passed. |
| Release | Distinguish blockers, known issues, and patch-note language. |

## Repository release quality

- Plugin manifest validates.
- All skills validate.
- Skill catalog matches actual skill directories.
- Required references in the catalog exist.
- GitHub Actions runs repository validation.
- README lists skills, parity assets, and validation command.
