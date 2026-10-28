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

Pin external refs to immutable commits and maintain upgrades centrally in the catalog; business projects must not independently follow floating upstream branches. State unpinned-source limitations. Record catalog and external-source commits separately. Inspect selected content, licensing, and suitability. Listing does not establish security review, redistribution rights, or behavioral testing. Do not infer permission to mirror code, execute scripts, or install extra dependencies. Missing licenses do not imply redistribution permission.

## Discovery and recommendation

Match requested names against IDs or aliases; ask only about ambiguous matches. For recommendations, provide a few suitable candidates with reasons, source, and scope, then wait for selection or use existing selection authorization. Do not load the entire catalog for every development task or turn recommendations into mandatory dependencies.

## Languages and stable identity

The manifest keeps one entry per module, with English descriptive and activation text and Chinese aliases/tags for discovery. Both language guides use the same IDs, paths, dependencies, sources, and versions. Install the canonical English runtime instructions only; agents follow the user's output language. Chinese human-readable counterparts live outside runtime packages in [doc/中文对照](../doc/中文对照/README.md). Do not create per-language modules or install both versions.

See [synchronization](../SYNC.en.md) for authority, forks, adapters, and project differences. Users can fork the catalog; use the selected repository rather than assuming its location identifies the original author.
