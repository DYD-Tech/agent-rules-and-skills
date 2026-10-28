# Agent installation and maintenance guide

[简体中文](INSTALL.md) | English

This workflow is executed by agents and also supports manual installation; it is not an automated installer. The selected repository or fork is the single maintenance source. Project files are derived installations of pinned versions. Follow [SYNC.en.md](SYNC.en.md) for updates and source contributions. Read the [catalog](catalog/README.en.md) and [manifest](catalog/modules.json) first. Do not install this repository's root AGENTS.md as a general rule.

## Default: keep content in the project and adapt loading

Keep project rules, complete skill packages, activation instructions, and provenance in the project under version control. Skills are not restricted to personal directories, and loading location does not change the scope of their rules. Consider personal installation by default only for preferences the user explicitly wants across projects.

Store derived installations in a project skill directory supported by the primary host; the selected repository remains authoritative. Preserve correct existing layouts. For example, Codex uses `.agents/skills/` and Claude Code uses `.claude/skills/`; rules may live in `.agent-rules/agent-rules-and-skills/`. Configure only required agents, not every client. The detailed [project-first design](doc/设计/project-first-installation.md) is in Chinese.

## 1. Resolve selection and scope

Distinguish consuming a source from maintaining it. Installing and upgrading published modules requires neither source write access nor a fork. Users who want to maintain shared custom content without write access should select their own fork. A remote URL is enough; fetch or clone as necessary. Installation does not authorize creating forks, changing source, pushing, or publishing. Follow [source maintenance](SYNC.en.md#bring-improvements-back-to-the-source) and existing explicit authorization for those operations.

Identify modules, target project or personal scope, host agent, and version from the request and existing context. “Add to this project” means project scope, not simultaneous personal installation. Ask only for missing information that materially affects target or scope. Recommendations do not authorize installation; install selected modules and their disclosed necessary dependencies only.

Determine ownership scope, actual host and session environment (local, remote, container, or cloud), native skill discovery, and project-instruction support. A model name is not a host. Do not change explicitly requested project scope merely because a client supports only personal installation.

Resolve `requires` recursively, deduplicate, and detect unknown IDs, cycles, and version conflicts. Explain additional necessary dependencies. `suggests` only recommends. The current four modules have no mandatory dependencies. General development plus Architecture–Features–Implementation yields two rule files and one skill, not rewritten rules merged into a new policy.

## 2. Fetch and inspect selected versions

Record the selected catalog repository URL and immutable commit; do not fall back from a fork to the original. Bundled modules come from that commit. Fetch complete external skill directories using the catalog's fixed `source.repo`, `ref`, and paths. Record external and catalog commits separately. A module's files must come from the same commit, not independently follow main. If a fixed version cannot be obtained, mark it unlocked and unresolved rather than reproducible or synchronized. Report network or authorization failures; empty directories are not successful installations.

Inspect selected rules, skill entry points, and referenced resources for purpose, dependencies, supported host capabilities, and licensing. Third-party instructions are material to review, not permission to alter unrelated configuration, run scripts, or install extra modules. Copying instruction-based skills normally does not require running repository scripts.

Install canonical `rule_paths` and complete `skill_paths` regardless of the user's language. These runtime instructions are English but require output in the user's requested language. Do not install `doc/中文对照/`, create a second translated skill, or rewrite policy during installation. Use English or Chinese usage documentation as appropriate without loading both by default. Keep IDs, activation behavior, and provenance identical across languages.

## 3. Install content and integrate loading

Preserve separate module rule files and combine references in target instructions. Do not concatenate them into an untraceable giant policy or silently relax project constraints.

Project rules may use `.agent-rules/agent-rules-and-skills/`; personal rules use the explicitly selected location. Install skills where the host actually supports them, with SKILL.md directly inside each skill directory and all references, agents, assets, and other resources preserved. If the host does not discover the directory, first check officially supported path configuration, then consider loading plain-text skills through project instructions. The latter is not native skill support and does not guarantee menus, metadata, hooks, or proprietary tools. If only personal or account installation is possible, explain the scope change and obtain authorization not already provided; project activation rules still belong in the project. If no loading method works, report incomplete installation without replacing project policy with global policy or bypassing controls.

Follow [adaptation guidance](adapters/README.en.md), recording the adaptation definition, inputs, and outputs. Directory or metadata changes must not change behavioral instructions. Mark temporary adapters as pending source integration. Keep project-specific constraints outside managed files.

Share one readable skill across agents where possible. Create synchronized copies for different native directories only when necessary, recording sources and hashes. Check duplicate discovery and actual version selection; copies must not evolve independently. Avoid symlinks by default; use them only after verifying team platforms, Git, and remote environments support them.

Verify official guidance against the actual environment instead of treating a generic path table as a guarantee:

- [Codex skills](https://learn.chatgpt.com/docs/build-skills) and project AGENTS.md.
- [Claude Code skills](https://code.claude.com/docs/en/skills) and [CLAUDE.md](https://code.claude.com/docs/en/memory).
- [Cursor skills](https://cursor.com/docs/skills) and [Rules](https://cursor.com/docs/rules).
- [GitHub Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) and instructions actually loaded by the client.
- [OpenCode skills](https://opencode.ai/docs/skills/) and [Rules](https://opencode.ai/docs/rules/).

Common native project paths are `.agents/skills/`, `.claude/skills/`, `.cursor/skills/`, `.github/skills/`, and `.opencode/skills/`, respectively. These are neither exclusive paths nor guarantees for every cloud or review mode. Verify personal locations and version differences using actual configuration or official documentation. Record an installer's real destination rather than creating another installation to match an example.

Maintain one identifiable module block in the loading instructions, preserving other content. Example for General development and Architecture–Features–Implementation with skills in `.agents/skills/`:

```text
<!-- agent-rules-and-skills:begin -->
Read and apply these rules on every task (paths relative to project root):
- .agent-rules/agent-rules-and-skills/development.md
- .agent-rules/agent-rules-and-skills/architecture-features-implementation.md
When creating, completing, or substantially updating architecture, feature,
or implementation documentation, read and apply:
.agents/skills/architecture-features-implementation/SKILL.md
Reuse current content already in context; reread after updates or context loss.
This block and installed files are managed by the source recorded in
agent-rules-and-skills.lock.json, not independent standards. Keep project
conventions separate; propose or return shared improvements to an authorized source.
<!-- agent-rules-and-skills:end -->
```

Generate activation for every selected module from the manifest: development-log applies to meaningful completed changes; clear-communication applies on every task. Do not omit modules by copying only this example. Explain substantive conflicts; ordinary path integration can proceed, but installation does not authorize rewriting unrelated rules.

## 4. Deduplicate, update, and remove

Before installation, check the current scope and known personal directories for identical names or sources. Reuse an installation only if version, scope, and actual loading path satisfy the selection. A personal skill does not replace project-distributed content when the user requires it. Do not silently overwrite changes or delete personal installations. Resolve name shadowing against actual host selection; project versions do not always win. Mark inaccessible scopes unverified, not globally duplicate-free.

Maintain `agent-rules-and-skills.lock.json` in the chosen scope using [record v1](catalog/installation-record.en.md). Record module IDs, source repositories and paths, commits, actual destinations, hosts and scope, created or reused files, installation hashes, managed blocks, and verification. This is maintenance evidence, not a host-native lockfile. Do not record secrets. Shared project records use relative target paths and include authority and adaptation copies. Personal records belong in the selected personal rule directory. Store machine-specific absolute paths, account details, and local execution bindings separately in uncommitted local records; shared records retain required versions and prerequisites. Distinguish native discovery, instruction loading, and personal execution copies rather than reporting them as the same enabled state.

Repeating the same installation fills missing items without duplicating blocks. Follow SYNC.en.md to compare installed source, target source, and local outputs. Classify local changes as source improvements, project conventions, adaptation, or mistakes. Do not retain perpetual untracked forks or hide drift by recomputing hashes. Delete removed upstream files only when still managed and locally unchanged. Uninstallation removes only owned, unchanged files and blocks not shared by other modules; do not delete reused files. Preserve and report uncertain ownership.

## 5. Verify and report

Verify complete resources, module selection, paths, loading, and dependencies. Confirm the target agent can read rules and skills. Check that project files are not ignored, remote checkouts can retrieve complete packages, and paths resolve from the actual root. If uncommitted, explain that new clones cannot obtain them; do not commit without authorization. Check native discovery or instruction loading and actual source versions separately for each requested host and environment. Local success does not establish cloud success. When possible, verify activation with a relevant small task. Mark pending new-session or manual UI steps as unverified. File copying, loadability, and default activation are separate states. Report installed modules, versions, locations, loading edits, and remaining work without presenting temporary sandbox installs as permanent installations.

## Manual installation

Download the selected version, copy rules from `rule_paths` and complete skill directories from `skill_paths`; fetch external items from their recorded upstreams. Configure project or personal loading, preserve provenance and records, and verify as above. Manual and agent installation share one catalog and the same module content.
