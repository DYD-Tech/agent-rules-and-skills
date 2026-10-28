# Agent Rules and Skills

[简体中文](README.md) | English

Manage development rules and skills across projects and agents from one repository. Maintain content and versions centrally, install selected modules into projects, and adapt loading to each agent. The modules promote verifiable, maintainable development and help users learn from project documentation. Current development version: 0.4.0. This repository, or a user-selected fork, is the single maintenance source; installations must remain traceable and comparable rather than evolving into independent standards.

## Choose how to use the repository

| Use case | Source of truth | Available actions |
| --- | --- | --- |
| Owner or maintainer with write access | This repository | Install and upgrade modules; authorize source changes, verification, and pushes |
| Direct user of the public repository | This repository | Install modules and upgrade to published versions; no direct writes to this repository |
| User maintaining custom shared rules and skills | Their own fork | Change and publish versions in the fork; compare projects against that fork |

Upgrading an installation and modifying its source are different operations. Direct users need no fork to install or upgrade. For ongoing custom maintenance, select your own fork as the source of truth. Project-specific conventions stay in the project and do not require a fork. Contributions to this repository may be submitted through a fork and pull request; maintainers decide whether to accept them.

You do not need to clone manually. Give an agent the repository URL and task; it can fetch files or clone as needed. For source changes, reuse a verified local checkout or clone into a separate directory. A URL does not grant write access, and account access does not authorize a push for the current task. See [source maintenance](SYNC.en.md#bring-improvements-back-to-the-source).

## Recommended use: give an agent the repository URL

Provide [this repository](https://github.com/DYD-Tech/agent-rules-and-skills) and say:

> Install General development, Architecture–Features–Implementation, Development log, and Clear communication from this repository into the current project. First read README.en.md, INSTALL.en.md, and catalog/modules.json. Install the selected modules and integrate their loading instructions, preserve existing rules and local changes, and verify actual loading.

You may select fewer modules. General development plus Architecture–Features–Implementation installs two rule files and one skill. Clear communication retrieves the complete skill from the separate communication-skills repository and configures use on every task; no second URL is needed.

If unsure what to choose:

> Inspect the module catalog and recommend a few modules for this project. Explain their purpose, source, and installation scope. Install them after I select them.

Start with the [catalog](catalog/README.en.md), [machine-readable manifest](catalog/modules.json), and [installation guide](INSTALL.en.md). Agents execute this workflow; it is not a background installation service. Network access, permissions, and host capabilities must be verified. When using a fork, provide its URL as the selected source of truth.

## Available modules

| Module | Installation | Source |
| --- | --- | --- |
| General development | Development rules | This repository |
| Architecture–Features–Implementation | Current-version documentation rules and skill | This repository |
| Development log | Change-record rules and skill | This repository |
| Clear communication | Every-task activation and clear-communication skill | [External upstream](https://github.com/DYD-Tech/communication-skills) |

Modules are independently selectable; suggestions are not installed automatically. Third-party modules can be cataloged without mirroring source. Listing does not establish an audit or verified license permission.

## Languages

Usage documentation is available in Chinese and English. Distributable rules, skill entry points, and runtime references use one English version; agents follow the user's requested output language. Do not install a second skill or load both languages. [Chinese counterparts and maintenance policy](doc/中文对照/README.md) support human review and are not runtime dependencies. Historical research and backups remain in their original language. Module IDs, paths, and version tracking do not change with language.

## Updates and contributions

Ask an agent to “Compare these modules with their recorded source” or “Update installed modules from the selected source, preserving and explaining conflicts.” Follow [SYNC.en.md](SYNC.en.md). A check-only request does not authorize updates; routine development does not check the network every turn.

Source repositories maintain content. Project files are installations of pinned versions; host adaptation handles necessary format and loading differences only. Keep project requirements separate. Return reusable improvements to the source before redistribution and record temporary patches as pending upstream work. The catalog pins external skill versions; their upstream repositories still own the source. Fork users select their own standard without automatic fallback to the original repository.

The [read-only checker](tools/audit_installation.py) detects registered files changed since installation:

```text
python tools/audit_installation.py --root <target-project-path>
```

Run it from this repository with the actual target project path. Do not fabricate an installation record for this source checkout. It requires Python 3.10+ and no third-party dependencies. See the [record format](catalog/installation-record.en.md). Exit 0 means checked local files match their baseline, 1 means differences, and 2 means a record or read error. Exit 0 does not mean upstream is current.

## Recommended installation scope

Keep selected rules, complete skills, activation instructions, and provenance in the project under version control. Skills need not be personal installations. Adapt project loading for the agents actually used. Store derived files in a project directory supported by the primary host; preserve a working existing layout. Central adaptation guidance lives in [adapters](adapters/README.en.md).

If a host lacks project skills, check supported path configuration or plain-text instruction loading. Explain limitations and obtain any missing scope authorization before using personal or account installation; project requirements must not silently become global policy. The detailed [project-first design](doc/设计/project-first-installation.md) is currently in Chinese.

## Manual installation

Use the [manual procedure](INSTALL.en.md#manual-installation): copy the selected rules and complete skill packages from cataloged sources, then add actual paths and activation conditions to instructions the host reads. Do not copy this repository's root AGENTS.md; it governs this repository only.

## Documentation responsibilities

- [Architecture–features–implementation](doc/架构-功能-实现/00-总览与分层.md) describes current capabilities, mechanisms, and rationale.
- [Development log](doc/开发日志/CHANGELOG.md) records changes, history, evidence, and remaining work.
- Other `doc/` research, design, and evaluation records explain development of these modules and are not loaded during normal skill use. These records are currently in Chinese.

See the [feature overview](doc/架构-功能-实现/01-功能全貌.md), [modular design](doc/设计/module-installation-design.md), and [evaluation record](doc/评测/evaluation.md). Skills cannot guarantee model compliance or replace testing and access controls. This repository has not been installed into a personal global environment, and cross-host installation tests remain incomplete.
