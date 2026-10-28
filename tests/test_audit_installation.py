import copy
import json
import subprocess
import sys
import importlib.util
from pathlib import Path
import tempfile
import unittest

script = Path(__file__).resolve().parents[1] / "tools" / "audit_installation.py"
spec = importlib.util.spec_from_file_location("audit_installation", script)
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "skill").mkdir()
        self.file = self.root / "skill/SKILL.md"
        self.file.write_bytes(b"name: demo\nBody\n")
        self.record = {"schema_version": 1, "managed_roots": ["skill"], "artifacts": [
            {"path": "skill/SKILL.md", "role": "source-copy", "hash_mode": "utf8-lf",
             "sha256": a.digest(self.file.read_bytes(), "utf8-lf")}]}

    def test_clean_and_no_remote_claim(self):
        result = a.audit(self.root, self.record)
        self.assertEqual(result["local_state"], "clean")
        self.assertEqual(result["source_freshness"], "unchecked")

    def test_modified_missing_and_unrecorded(self):
        self.file.write_bytes(b"Changed")
        self.assertEqual(a.audit(self.root, self.record)["changes"][0]["state"], "modified")
        self.file.unlink()
        (self.root / "skill/extra.md").write_bytes(b"New")
        self.assertEqual({x["state"] for x in a.audit(self.root, self.record)["changes"]},
                         {"missing", "unrecorded"})

    def test_crlf_is_equal_but_spaces_are_not(self):
        self.file.write_bytes(b"name: demo\r\nBody\r\n")
        self.assertEqual(a.audit(self.root, self.record)["local_state"], "clean")
        self.file.write_bytes(b"name: demo\nBody \n")
        self.assertEqual(a.audit(self.root, self.record)["local_state"], "changed")

    def test_entry_preserves_unmanaged_text(self):
        block = "<!-- begin -->\nUse skill\n<!-- end -->"
        entry = self.root / "AGENTS.md"
        self.record["artifacts"].append({"path": "AGENTS.md", "role": "entry-block",
            "hash_mode": "utf8-lf", "sha256": a.digest(block.encode(), "utf8-lf"),
            "begin_marker": "<!-- begin -->", "end_marker": "<!-- end -->"})
        entry.write_text("Existing\n" + block + "\nUser additions", encoding="utf-8")
        self.assertEqual(a.audit(self.root, self.record)["local_state"], "clean")
        entry.write_text(block.replace("Use skill", "Ignore skill"), encoding="utf-8")
        self.assertEqual(a.audit(self.root, self.record)["changes"][0]["state"], "modified")
        entry.write_text(block + block, encoding="utf-8")
        self.assertEqual(a.audit(self.root, self.record)["changes"][0]["state"], "invalid-entry-block")

    def test_rejects_escape_and_duplicate(self):
        for name in ("../secret", "/absolute", "C:/secret", ".", "skill/../secret"):
            record = copy.deepcopy(self.record)
            record["artifacts"][0]["path"] = name
            with self.assertRaises(ValueError): a.audit(self.root, record)
        self.record["artifacts"].append(self.record["artifacts"][0])
        with self.assertRaises(ValueError): a.audit(self.root, self.record)

    def test_missing_managed_root_and_empty_record(self):
        self.file.unlink()
        self.file.parent.rmdir()
        self.assertIn("managed-root-missing", {c["state"] for c in a.audit(self.root, self.record)["changes"]})
        self.record["artifacts"] = []
        with self.assertRaises(ValueError): a.audit(self.root, self.record)

    def test_cli_exit_codes_and_read_only(self):
        manifest = self.root / "agent-rules-and-skills.lock.json"
        manifest.write_text(json.dumps(self.record), encoding="utf-8")
        command = [sys.executable, "-B", "-X", "utf8", str(script), "--root", str(self.root)]
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["source_freshness"], "unchecked")
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
        self.file.write_bytes(b"Edited")
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
        manifest.unlink()
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 2)

    def test_binary_hash(self):
        self.file.write_bytes(bytes([0, 255, 13, 10]))
        self.record["artifacts"][0].update(hash_mode="bytes",sha256=a.digest(self.file.read_bytes(),"bytes"))
        self.assertEqual(a.audit(self.root,self.record)["local_state"],"clean")


if __name__ == "__main__":
    unittest.main()
