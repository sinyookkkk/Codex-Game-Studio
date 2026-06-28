#!/usr/bin/env python3
"""Validate the Codex Game Studio repository without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_PATTERNS = ("TODO", "TBD", "[TODO", "your-name")
REQUIRED_ROOTS = (
    ".codex-plugin/plugin.json",
    "skills",
    "references",
    "references/templates",
    "references/roles/studio-roles.md",
    "references/rules",
    "references/engines",
    "tests/skill-catalog.json",
    "references/quality-rubric.md",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - diagnostic path
        fail(f"Could not parse JSON {path.relative_to(ROOT)}: {exc}")


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)} has unterminated YAML frontmatter")
    data: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)} has invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate_plugin() -> None:
    manifest = load_json(ROOT / ".codex-plugin" / "plugin.json")
    for field in ("name", "version", "description", "license", "skills", "interface"):
        if field not in manifest:
            fail(f"plugin.json missing {field}")
    if manifest["name"] != "codex-game-studio":
        fail("plugin.json name must be codex-game-studio")
    if not re.match(r"^\d+\.\d+\.\d+$", manifest["version"]):
        fail("plugin.json version must be semver")
    if manifest["skills"] != "./skills/":
        fail("plugin.json skills must be ./skills/")


def validate_required_paths() -> None:
    for rel in REQUIRED_ROOTS:
        if not (ROOT / rel).exists():
            fail(f"Missing required path: {rel}")


def validate_skills() -> set[str]:
    skill_root = ROOT / "skills"
    skills = {p.name for p in skill_root.iterdir() if p.is_dir()}
    if not skills:
        fail("No skills found")
    for skill in sorted(skills):
        skill_md = skill_root / skill / "SKILL.md"
        if not skill_md.exists():
            fail(f"Skill {skill} missing SKILL.md")
        fm = parse_frontmatter(skill_md)
        if fm.get("name") != skill:
            fail(f"Skill {skill} frontmatter name mismatch")
        if not fm.get("description"):
            fail(f"Skill {skill} missing description")
    return skills


def validate_catalog(skills: set[str]) -> None:
    catalog = load_json(ROOT / "tests" / "skill-catalog.json")
    entries = catalog.get("skills")
    if not isinstance(entries, list):
        fail("tests/skill-catalog.json missing skills list")
    catalog_names = {entry.get("name") for entry in entries}
    if catalog_names != skills:
        missing = sorted(skills - catalog_names)
        extra = sorted(catalog_names - skills)
        fail(f"Skill catalog mismatch. Missing={missing} Extra={extra}")
    for entry in entries:
        if entry.get("priority") not in {"critical", "high", "medium", "low"}:
            fail(f"Invalid priority for {entry.get('name')}")
        refs = entry.get("required_references", [])
        if not refs:
            fail(f"Catalog entry {entry.get('name')} has no required references")
        for rel in refs:
            if not (ROOT / rel).exists():
                fail(f"Catalog entry {entry.get('name')} references missing file: {rel}")


def validate_no_placeholders() -> None:
    ignored_parts = {".git"}
    checked_suffixes = {".md", ".json", ".yml", ".yaml"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in checked_suffixes:
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern in text:
                fail(f"Placeholder pattern {pattern!r} found in {path.relative_to(ROOT)}")


def main() -> None:
    validate_required_paths()
    validate_plugin()
    skills = validate_skills()
    validate_catalog(skills)
    validate_no_placeholders()
    print(f"Repository validation passed: {len(skills)} skills")


if __name__ == "__main__":
    main()
