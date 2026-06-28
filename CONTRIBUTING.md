# Contributing

Thanks for improving Codex Game Studio.

## Development flow

1. Keep skills concise and move detailed material into `references/`.
2. Add or update forward tests when behavior changes.
3. Run repository validation before opening a pull request.

```bash
python scripts/validate_repository.py
python scripts/render_forward_tests.py
```

On Windows, also run:

```powershell
.\scripts\validate_repository.ps1
```

## Skill changes

- Every skill must have `name` and `description` frontmatter.
- Descriptions must include when Codex should use the skill.
- Reference files should be loaded only when needed.

## Documentation changes

- Keep public docs useful for GitHub readers.
- Keep skill internals useful for Codex.
- Avoid platform-specific instructions unless a cross-platform alternative is also present.
