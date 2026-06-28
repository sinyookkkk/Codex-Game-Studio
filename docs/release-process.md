# Release Process

Use this process before tagging a public release.

1. Run `python scripts/validate_repository.py`.
2. Run `python scripts/render_forward_tests.py` and skim the generated report.
3. Validate plugin metadata with the Codex plugin validator.
4. Confirm README, changelog, usage guide, and migration notes describe the same version.
5. Create a release commit with the version bump.
6. Tag the release as `vMAJOR.MINOR.PATCH`.
7. Publish GitHub release notes from `CHANGELOG.md`.
