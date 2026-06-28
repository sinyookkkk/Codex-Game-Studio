#!/usr/bin/env python3
"""Lightweight asset folder validator for Codex Game Studio projects."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path.cwd()
ASSET_ROOT = ROOT / "assets"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    if not ASSET_ROOT.exists():
        print("Asset validation skipped: no assets directory")
        return
    checked = 0
    for path in ASSET_ROOT.rglob("*"):
        if not path.is_file():
            continue
        checked += 1
        if not NAME_RE.match(path.name):
            fail(f"Asset filename should be lowercase slug style: {path.relative_to(ROOT)}")
        if path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                fail(f"Invalid JSON asset {path.relative_to(ROOT)}: {exc}")
    print(f"Asset validation passed: {checked} files")


if __name__ == "__main__":
    main()
