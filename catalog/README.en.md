# Module catalog

[简体中文](README.md) | English

A module is a selectable installation unit containing rules, skills, or both. External entries record provenance without copying source. Filter by name, aliases, tags, and summary, then inspect the selected files.

| Module ID | English name | Contents | Source |
| --- | --- | --- | --- |
| development | General development | One rule file | Bundled |
| architecture-features-implementation | Architecture–Features–Implementation | Rules and skill | Bundled |
| development-log | Development log | Rules and skill | Bundled |
| dyd-tech/clear-communication | Clear communication | Every-task activation and complete skill | DYD-Tech/communication-skills |

The machine-readable catalog is [modules.json](modules.json). Follow the [installation guide](../INSTALL.en.md) for installation, updates, and removal. For example: “Install General development, Architecture–Features–Implementation, and Clear communication into the current project.” A bare URL without an installation request is a reading or consultation request.

## Add a module

Add an item to `modules` with a unique ID, name, aliases, tags, purpose, source, complete paths, activation, required dependencies, and optional suggestions. Namespace external IDs as `owner/skill-name`; check same-name conflicts before installing.

Current modules require no other modules. `requires` lists only modules without which the selection cannot work; `suggests` only recommends and never auto-installs. Check existence and dependency cycles. Rule paths are relative to the source repository root; bundled paths refer to this downloaded repository. Each `skill_paths` entry names a complete directory containing SKILL.md, not an individual file.

`activation.rules` requires loading `rule_paths`; `activation.skills` defines skill triggers. These are inputs to generating project instructions, not native client configuration. Substitute actual installed paths.

The catalog selects external sources and version policies; projects record actual installed commits. Resolve versions in this order: an explicitly requested commit or version; the existing installation record for ordinary reinstall, repair, or adding another agent; then catalog policy for first installation or an explicitly requested upgrade. With `source.version_policy: track-branch`, query the latest commit of `source.ref` in the selected `source.repo` once and fetch all module files by that full commit. With `pinned`, or a legacy entry without a policy, use the fixed ref without independently following a branch. Clear communication now uses `track-branch` with `refs/heads/main`. Honor explicit older versions and report them. If resolution fails, do not silently call cached content latest: report incomplete work and preserve existing installs. Reproduction may use a verifiable recorded commit without claiming freshness. Record the catalog commit, actual external `source_commit`, `version_policy`, `requested_ref`, and `resolved_at`. Latest means the selected branch at query time, not the latest release or reviewed content. Inspect content, licensing, and suitability before installation. Listing is not an audit or redistribution permission and does not authorize scripts or extra modules.

## Discovery and recommendation

Match requested names against IDs or aliases; ask only about ambiguous matches. For recommendations, provide a few suitable candidates with reasons, source, and scope, then wait for selection or use existing selection authorization. Do not load the entire catalog for every development task or turn recommendations into mandatory dependencies.

## Languages and stable identity

The manifest keeps one entry per module, with English descriptive and activation text and Chinese aliases/tags for discovery. Both language guides use the same IDs, paths, dependencies, sources, and versions. Install the canonical English runtime instructions only; agents follow the user's output language. Chinese human-readable counterparts live outside runtime packages in [doc/中文对照](../doc/中文对照/README.md). Do not create per-language modules or install both versions.

See [synchronization](../SYNC.en.md) for authority, forks, adapters, and project differences. Users can fork the catalog; use the selected repository rather than assuming its location identifies the original author.
