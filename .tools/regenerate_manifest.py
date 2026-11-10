#!/usr/bin/env python3
"""Generate or verify a stable SHA-256 inventory of the skill package files."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifest.json"
IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache"}
IGNORED_FILES = {"manifest.json", ".DS_Store"}


def build_manifest() -> dict:
    entries = []
    for path in sorted(ROOT.rglob("*")):
        if any(part in IGNORED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Refusing to hash symlink: {path.relative_to(ROOT)}")
        if not path.is_file() or path.name in IGNORED_FILES:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.endswith(".pyc"):
            continue
        data = path.read_bytes()
        entries.append({"path": rel, "sha256": hashlib.sha256(data).hexdigest(), "size_bytes": len(data)})
    return {"schema_version": 1, "skill": ROOT.name, "files": entries}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify manifest without modifying it")
    args = parser.parse_args()
    try:
        current = build_manifest()
        if args.check:
            if not MANIFEST.is_file():
                print("Missing manifest.json", file=sys.stderr)
                return 1
            stored = json.loads(MANIFEST.read_text(encoding="utf-8"))
            if stored != current:
                old = {x["path"]: x for x in stored.get("files", [])}
                new = {x["path"]: x for x in current["files"]}
                for key in sorted(old.keys() | new.keys()):
                    if old.get(key) != new.get(key):
                        print(f"Mismatch: {key}", file=sys.stderr)
                if stored.get("skill") != current["skill"] or stored.get("schema_version") != 1:
                    print("Manifest metadata mismatch", file=sys.stderr)
                return 1
            print(f"OK: {len(current['files'])} files match manifest.json")
            return 0
        MANIFEST.write_text(json.dumps(current, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Updated manifest.json ({len(current['files'])} files)")
        return 0
    except (ValueError, OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"Manifest error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
