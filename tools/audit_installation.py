"""Read-only local drift audit. Does not fetch upstream or modify files."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys


def digest(data, mode):
    if mode == "utf8-lf":
        data = data.decode("utf-8").replace("\r\n", "\n").encode("utf-8")
    elif mode != "bytes":
        raise ValueError("Unsupported hash_mode")
    return hashlib.sha256(data).hexdigest()


def bounded(root, value):
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise ValueError("Expected a project-relative POSIX path")
    path = PurePosixPath(value)
    if path.is_absolute() or value == "." or any(p in ("..", ".", "") for p in value.split("/")):
        raise ValueError("Path must stay within project: " + value)
    result = root.joinpath(*path.parts)
    current = root
    for part in path.parts:
        current = current / part
        if current.is_symlink() or (hasattr(current, "is_junction") and current.is_junction()):
            raise ValueError("Linked path requires separate verification: " + value)
    if not result.resolve().is_relative_to(root):
        raise ValueError("Path outside project: " + value)
    return result


def audit(root, record):
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError("Project root is not a directory")
    if record.get("schema_version") != 1:
        raise ValueError("Expected installation record schema_version 1")
    artifacts = record.get("artifacts")
    roots = record.get("managed_roots")
    if not isinstance(artifacts, list) or not artifacts or not isinstance(roots, list):
        raise ValueError("Non-empty artifacts and managed_roots list required")
    expected = set()
    prepared = []
    for item in artifacts:
        if not isinstance(item, dict):
            raise ValueError("Invalid artifact")
        path = bounded(root, item.get("path"))
        key = item["path"].casefold()
        if key in expected:
            raise ValueError("Duplicate artifact path")
        expected.add(key)
        if not re.fullmatch(r"[0-9a-f]{64}", item.get("sha256", "")):
            raise ValueError("Invalid SHA256")
        if item.get("hash_mode") not in ("bytes", "utf8-lf"):
            raise ValueError("Invalid hash_mode")
        if item.get("role") not in ("source-copy", "adapter-output", "entry-block"):
            raise ValueError("Invalid artifact role")
        if item["role"] == "entry-block":
            start, end = item.get("begin_marker"), item.get("end_marker")
            if not isinstance(start, str) or not start or not isinstance(end, str) or not end or start == end:
                raise ValueError("Distinct non-empty block markers required")
            if item["hash_mode"] != "utf8-lf":
                raise ValueError("Entry blocks use utf8-lf")
        prepared.append((item, path))
    managed = [(name, bounded(root, name)) for name in roots]
    changes = []
    for item, path in prepared:
        if not path.is_file():
            changes.append({"path": item["path"], "state": "missing"})
            continue
        data = path.read_bytes()
        if item["role"] == "entry-block":
            text = data.decode("utf-8").replace("\r\n", "\n")
            start, end = item["begin_marker"], item["end_marker"]
            if text.count(start) != 1 or text.count(end) != 1 or text.index(end) < text.index(start):
                changes.append({"path": item["path"], "state": "invalid-entry-block"})
                continue
            data = text[text.index(start):text.index(end) + len(end)].encode("utf-8")
        if digest(data, item["hash_mode"]) != item["sha256"]:
            changes.append({"path": item["path"], "state": "modified"})
    extras = set()
    for name, directory in managed:
        if not directory.is_dir():
            changes.append({"path": name, "state": "managed-root-missing"})
            continue
        for path in directory.rglob("*"):
            relative = path.relative_to(root).as_posix()
            bounded(root, relative)
            if path.is_file() and relative.casefold() not in expected:
                extras.add(relative)
    changes.extend({"path": name, "state": "unrecorded"} for name in sorted(extras))
    return {"local_state": "changed" if changes else "clean", "source_freshness": "unchecked",
            "scope": "recorded artifacts and managed_roots only", "changes": changes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--record", type=Path, help="Defaults to ROOT/agent-rules-and-skills.lock.json")
    args = parser.parse_args()
    path = args.record or args.root / "agent-rules-and-skills.lock.json"
    try:
        record = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(record, dict):
            raise ValueError("Record must be an object")
        result = audit(args.root, record)
    except (ValueError, OSError, TypeError) as exc:
        print(json.dumps({"error": str(exc), "source_freshness": "unchecked"}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["changes"] else 0


if __name__ == "__main__":
    sys.exit(main())
