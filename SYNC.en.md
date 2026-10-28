# Source of truth, adaptation, and synchronization

[简体中文](SYNC.md) | English

This repository, or the explicitly selected fork, is the sole maintenance source for reusable rules, skills, and adaptation guidance. Projects hold installations of pinned versions; agent-specific files are derived outputs, not new standards. See [installation](INSTALL.en.md) and [adaptation](adapters/README.en.md).

## What identifies the source of truth

The installation record must identify the selected registry repository URL and immutable commit. A selected fork remains authoritative; do not infer authority from origin, a fork's upstream remote, or matching filenames. Switching authority is an explicit change with module, path, and version differences explained.

This repository maintains bundled modules. For external modules, the catalog selects upstream and version while that upstream maintains the code. The unified authority concerns selection and versions, not ownership of third-party code. Pin external refs to commits and update the catalog before projects upgrade; individual projects must not independently track upstream main.

Projects may retain an older pinned version with its pending upgrade recorded rather than being treated as broken or silently updated. Different content at the same version is local drift that requires explanation.

## Separate three types of content

1. **Source content:** Shared rules, skill instructions, and resources. Improve and verify these at the source, then distribute them. Installed files are not the normal editing location.
2. **Host adaptation:** Paths, supported metadata, loading, and necessary invocation syntax. Make only justified minimal conversions, recording transformations, adapter version, source input, and output hashes. Changing triggers, steps, promises, or failure handling changes behavior and must not be disguised as adaptation.
3. **Project conventions:** Commands, directories, architectural constraints, and explicit exceptions. Keep these in separate project instructions or override files loaded by the project entry point, outside managed content. Explain scope and reasons for overrides; do not claim complete agreement with the default policy.

Multiple physical copies are allowed when each traces to the same selected source version and recorded adaptation. Consistency must not depend on agents independently rewriting instructions. Report unsupported capabilities or documented degraded behavior when lossless conversion is impossible; do not claim equivalence.

## When to compare

Compare at initial installation, adding an agent, explicit check or update requests, or before editing managed content. Routine development uses the pinned version without network calls or repository-wide scans each turn. Schedule recurring checks only when requested.

“Check for updates” produces differences and recommendations without writing target files. “Update modules” permits compatible updates to unchanged managed files within authorized scope. Handle compatibility-policy changes, conflicts, and scope changes explicitly. Do not ask again when existing authorization is sufficient.

## Comparison and update procedure

1. Read the lock record to identify source, modules, and actual hosts. Mark untraceable legacy copies as unknown pending investigation or migration; similar text does not establish provenance.
2. Check whether local outputs changed since installation, optionally using the [read-only checker](tools/audit_installation.py). Hashes detect local changes, not upstream freshness or equivalent adaptation. Migrate old records using [record v1](catalog/installation-record.en.md) and verifiable evidence, not hashes of current files that erase unknown drift.
3. Fetch installed and target commits from the selected source. Compare old source, target source, and local installation; reproduce the target using the recorded adaptation. Preserve differences rather than directly merging different host formats. Explain inability to reconstruct safely when old commits or adaptation evidence are unavailable.
4. If only upstream changed, generate an update. If only local content changed, classify it as a project need, source improvement, or mistake. If both changed, preserve local differences before resolving conflicts. Review adapter changes separately. Rehashing different content at the same version does not make it authoritative.
5. Update all registered related host entries and copies, checking removed files, links, and actual loading. Do not leave a module half-upgraded. On failure, restore pre-update files and records or explicitly mark the operation incomplete; do not report synchronization success.
6. Update the lock record after files are complete and verified. Mark inaccessible personal, cloud, or remote copies pending, not fully synchronized. Do not commit, push, or change other projects without authorization.

## Bring improvements back to the source

This workflow governs content shared across projects and agents. Installing or upgrading modules requires source read access, not write access. Source changes and pushes require both appropriate access and user authorization. Owners follow the same distinction: account privileges do not make routine project work permission to publish shared rules.

1. **Classify the change.** Reuse task records for the problem, original source version, minimal proposal, and available evidence. Project exceptions stay local; reusable content or adaptation improvements belong at the source. Routine development allows suggestions, not automatic source changes or publication.
2. **Identify target and authorization.** Read the selected source from the installation record. Owners and authorized maintainers may authorize direct maintenance. Users without write access who want their own maintained versions should select a fork. For contributions only, prepare an authorized fork branch and PR without claiming upstream changed or switching project authority. Distinguish editing, committing, pushing, and creating a PR. Reuse sufficient existing authorization.
3. **Obtain a working copy.** A URL is sufficient; users need not clone manually. Reuse a local checkout only after checking the actual remote, branch, and uncommitted work; otherwise clone into a separate directory outside the business project. Directory and remote names alone do not prove identity. Do not reset user work. If access fails, preserve reviewable differences or a patch and explain incomplete work; do not ask users to paste secrets into chat.
4. **Edit and verify at the source.** Follow that repository's instructions and use an appropriate working branch for shared changes, related documentation, and verification. Host adaptation still cannot silently change semantics. Identify the actual upstream for external modules; do not patch installed files and retain the original upstream version label.
5. **Commit and publish as authorized.** With direct access, push according to branch policy; create a PR when review is required. Without write access, create or use a fork and push only with user authorization. An unmerged PR does not mean upstream is updated. If authorized only to edit locally, deliver the changes and verification and stop there.
6. **Update consuming projects afterward.** Once the source has a retrievable target commit, follow the comparison procedure in authorized projects and record that commit. Unpublished local changes do not establish synchronization with the remote. Other projects retain their pins until requested to update; do not scan and change all projects.

Explicitly authorized emergency patches may remain locally but must be recorded as temporary differences pending source integration, not lasting standards. At delivery, separately report source edits, commits, pushes or PR status, and which projects were upgraded or remain pending.

Project-specific needs become project conventions, shared improvements go to the source, and host compatibility improvements go to source adaptation guidance. Third-party improvements belong at their actual upstream or an explicitly selected fork with an updated catalog mapping. Do not label modified external content as the original upstream version. PRs, pushes, and messages require user authorization.

## Switch to a fork

Users without source write access who want custom shared content should fork this repository and explicitly select it as their registry. An agent may create the fork with user authorization and appropriate account capabilities; otherwise the user supplies a fork URL. Creating it does not migrate existing projects. For each authorized project, compare the original source, corresponding fork modules, and target commit, then update provenance and necessary files while preserving project conventions and local differences. Leave other projects pending rather than claiming complete migration.

Migrated projects compare against that fork. Its maintainer decides whether to incorporate original upstream changes: compare, merge, verify, and publish in the fork before upgrading projects. Do not automatically overwrite fork choices with upstream updates. Forking the catalog does not fork external skill code; independently maintained external modules require their own forks and explicit source mappings. Keep module IDs stable for migration, but record changed repository identity; matching IDs do not imply matching sources.
