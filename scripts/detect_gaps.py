#!/usr/bin/env python3
"""Detect missing game-project planning artifacts."""

from __future__ import annotations

from pathlib import Path


ROOT = Path.cwd()
EXPECTED = (
    "README.md",
    "design",
    "tests",
)


def main() -> None:
    missing = [item for item in EXPECTED if not (ROOT / item).exists()]
    if missing:
        print("Project gap check: missing " + ", ".join(missing))
        return
    print("Project gap check passed: basic project artifacts present")


if __name__ == "__main__":
    main()
