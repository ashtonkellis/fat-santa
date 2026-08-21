#!/usr/bin/env python3
"""Increment the integer build/version number in the repo-root VERSION file.
Run this before every deploy to main; the UI reads VERSION and shows it.
Usage: python3 scripts/bump_version.py  ->  prints the new version.
"""
import pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "VERSION"
n = int(p.read_text().strip() or "0") + 1
p.write_text(f"{n}\n")
print(n)
