# Installation record v1

[简体中文](installation-record.md) | English

Use `agent-rules-and-skills.lock.json` at the target project root. This is this project's protocol, not a native agent configuration. Record authority, modules, and host adaptations. The read-only tool checks the installed baseline in `artifacts`; absent or incomplete records cannot establish synchronization.

Core fields:

- `schema_version`: 1.
- `registry`: selected catalog repository `url` and pinned `commit`. A local experiment may explicitly identify an uncommitted snapshot, but cannot claim remote synchronization.
- `modules`: each includes `id`, actual `source_repo`, `source_commit`, and `source_paths`. External commits are independent of the registry commit.
- `artifacts`: each includes project-relative `path`, installation `sha256`, `hash_mode` (`bytes` or `utf8-lf`), `role` (`source-copy`, `adapter-output`, or `entry-block`), `module_id`, and source mapping. Adapter outputs also record `adapter_id`, definition version, and transformations.
- `managed_roots`: separate skill or rule directories entirely owned by the installation. Do not list the entire project, all of `.agents/skills`, or directories mixed with user files. The checker reports unregistered files inside these roots to detect independently added content.
- `hosts`: actual host versions, loading methods, destinations, and verification status. Store machine-specific absolute bindings separately and do not commit them.

`utf8-lf` normalizes only UTF-8 CRLF to LF for cross-platform Git checkouts; it does not ignore spaces, BOMs, or other changes. Use `bytes` for binary files. Source commits retrieve originals; output hashes detect installed changes. Neither replaces the other.

For mixed instruction files, register only the managed block using role `entry-block` with `begin_marker` and `end_marker`. Hash the content including both markers, ending at the end marker's last character. Each marker must occur exactly once. Other user content remains independently editable. Hash an entire file when the whole file is managed.

The checker cannot establish semantic equivalence, publication status, authenticity of claimed provenance, or upstream freshness. It cannot discover unregistered copies outside managed roots. Installers must verify sources; a clean result does not replace source comparison. For personal scope, use a separately identified installation root rather than managing the whole home directory.

Before migrating legacy records, recover original provenance and the installation baseline. Do not recompute current hashes to erase unknown drift. Language does not change this schema: record canonical runtime files, not Chinese reading copies.
