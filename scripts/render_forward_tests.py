#!/usr/bin/env python3
"""Render the forward-test catalog as Markdown."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "tests" / "forward-tests.json"


def main() -> None:
    suite = json.loads(SUITE.read_text(encoding="utf-8"))
    print("# Codex Game Studio Forward Tests\n")
    print(suite["description"])
    print()
    for case in suite["cases"]:
        print(f"## {case['skill']}\n")
        print(f"Prompt: {case['prompt']}\n")
        print("Expected evidence:")
        for item in case["expected_evidence"]:
            print(f"- {item}")
        print("\nRequired references:")
        for ref in case["required_references"]:
            print(f"- `{ref}`")
        print(f"\nExpected output: `{case['expected_output_path']}`\n")


if __name__ == "__main__":
    main()
