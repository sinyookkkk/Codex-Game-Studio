#!/usr/bin/env python3
"""Validate the Codex Game Studio repository without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_PATTERNS = ("[TO" + "DO", "T" + "BD", "your" + "-name")
REQUIRED_ROOTS = (
    ".codex-plugin/plugin.json",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "docs/codex-usage-guide.md",
    "docs/demo-transcripts/README.md",
    "docs/examples/README.md",
    "docs/release-process.md",
    "references/codex-adaptation-map.md",
    "references/engine-modules/README.md",
    "references/roles/coordination-recipes.md",
    "references/templates/accessibility-requirements.md",
    "references/templates/pitch-document.md",
    "references/templates/player-journey.md",
    "references/templates/incident-response.md",
    "references/templates/post-mortem.md",
    "references/templates/collaborative-protocols.md",
    "scripts/render_forward_tests.py",
    "skills",
    "references",
    "references/templates",
    "references/roles/studio-roles.md",
    "references/rules",
    "references/engines",
    "tests/skill-catalog.json",
    "tests/forward-tests.json",
    "tests/expected-outputs",
    "references/quality-rubric.md",
)
ENGINES = ("godot", "unity", "unreal", "web")
ENGINE_MODULES = ("input", "ui", "save", "build", "networking", "performance", "rendering")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Could not parse JSON {path.relative_to(ROOT)}: {exc}")


def parse_frontmatter(path: Path) -> dict[str, str]:
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


def validate_required_paths() -> None:
    if (ROOT / "TODOS.md").exists():
        fail("TODOS.md should be removed after tracked migration work is complete")
    for rel in REQUIRED_ROOTS:
        if not (ROOT / rel).exists():
            fail(f"Missing required path: {rel}")
    for engine in ENGINES:
        for module in ENGINE_MODULES:
            path = ROOT / "references" / "engine-modules" / engine / f"{module}.md"
            if not path.exists():
                fail(f"Missing engine module reference: {path.relative_to(ROOT)}")


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
        fail(f"Skill catalog mismatch. Missing={sorted(skills - catalog_names)} Extra={sorted(catalog_names - skills)}")
    for entry in entries:
        if entry.get("priority") not in {"critical", "high", "medium", "low"}:
            fail(f"Invalid priority for {entry.get('name')}")
        validate_reference_list(entry.get("required_references", []), f"Catalog entry {entry.get('name')}")


def validate_forward_tests(skills: set[str]) -> None:
    suite = load_json(ROOT / "tests" / "forward-tests.json")
    cases = suite.get("cases")
    if not isinstance(cases, list):
        fail("tests/forward-tests.json missing cases list")
    case_skills = {case.get("skill") for case in cases}
    if case_skills != skills:
        fail(f"Forward-test skill coverage mismatch. Missing={sorted(skills - case_skills)} Extra={sorted(case_skills - skills)}")
    for index, case in enumerate(cases, start=1):
        label = f"Forward test case {index} ({case.get('skill')})"
        if not isinstance(case.get("prompt"), str) or len(case["prompt"].strip()) < 40:
            fail(f"{label} needs a realistic prompt")
        evidence = case.get("expected_evidence")
        if not isinstance(evidence, list) or len(evidence) < 3:
            fail(f"{label} needs at least three expected evidence checks")
        validate_reference_list(case.get("required_references", []), label)
        expected_path = case.get("expected_output_path")
        if not isinstance(expected_path, str) or not (ROOT / expected_path).exists():
            fail(f"{label} has missing expected_output_path: {expected_path}")


def validate_reference_list(refs: list[str], label: str) -> None:
    if not isinstance(refs, list) or not refs:
        fail(f"{label} needs required references")
    for rel in refs:
        if not isinstance(rel, str) or not rel:
            fail(f"{label} has invalid reference path: {rel!r}")
        if not (ROOT / rel).exists():
            fail(f"{label} references missing file: {rel}")


def iter_checked_text_files() -> Iterator[Path]:
    ignored_parts = {".git"}
    checked_suffixes = {".md", ".json", ".yml", ".yaml", ".py", ".ps1", ".sh"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in checked_suffixes:
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        yield path


def validate_no_placeholders() -> None:
    for path in iter_checked_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern in text:
                fail(f"Placeholder pattern {pattern!r} found in {path.relative_to(ROOT)}")


def validate_no_control_characters() -> None:
    allowed = {"\n", "\r", "\t"}
    for path in iter_checked_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for index, char in enumerate(text):
            if char in allowed:
                continue
            if ord(char) < 32 or ord(char) == 127:
                fail(f"Control character U+{ord(char):04X} found in {path.relative_to(ROOT)} at offset {index}")


def main() -> None:
    validate_required_paths()
    validate_plugin()
    skills = validate_skills()
    validate_catalog(skills)
    validate_forward_tests(skills)
    validate_no_placeholders()
    validate_no_control_characters()
    print(f"Repository validation passed: {len(skills)} skills, {len(skills)} forward tests, {len(ENGINES) * len(ENGINE_MODULES)} engine modules")


if __name__ == "__main__":
    main()
