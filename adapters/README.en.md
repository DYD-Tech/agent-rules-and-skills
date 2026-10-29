# Host adaptation guidance

[简体中文](README.md) | English

Maintain host loading differences here. Standard content remains in `rules/` and `skills/`, without independent versions for each agent. This directory provides guidance and support evidence, not an automatic converter or a claim that all clients have been tested.

## Adaptation order

1. Verify and prefer `.agents/skills/` and `.agent-rules/agent-rules-and-skills/`. Do not choose proprietary directories by brand when shared discovery works. Use host-specific paths only when needed, recording evidence. Distinguish native discovery from file reading; migrate existing installs within authorization and check shadowing instead of blindly keeping both copies.
2. Add a thin project entry point referencing the same rules. Prefer AGENTS.md as a shared entry, without assuming every client, mode, or version reads it.
3. Convert necessary metadata or invocation syntax only when native requirements demand it, preserving complete resources. Record original and target fields, reasons, host version, and affected capabilities.
4. If equivalent expression is impossible, report lost capabilities and stop that host adaptation if necessary. Do not delete conditions, abbreviate steps, or change triggers to make files appear compatible.

Keep adaptation definitions in the selected source repository. Project installation records identify definition and version. Mark new, unregistered adapters temporary and pending source integration; they must not silently become permanent agent-specific policies. Unchanged copies in different directories still need provenance and destination records.

Language is not a reason to rewrite the installed skill. Runtime instructions remain canonical English, with user-language output. Host display metadata may be localized when supported and recorded, without changing the skill ID, behavior, or activation.

## Evidence and limits as of 2026-10-28

| Host | Evidence | Handling |
| --- | --- | --- |
| Codex | Project `.agents/skills/` and AGENTS.md; official guidance previously checked | Prefer unchanged packages and project instructions; [project installation research, Chinese](../doc/设计/project-first-installation.md) |
| Cursor | Multiple project skill directories supported in official guidance | Prefer a shared discoverable directory; check duplicate discovery and Rules overriding the shared entry; same research |
| Qoder CLI | Official project `.qoder/skills/`; personal same-name skills take precedence | Verify actual source; do not generalize CLI behavior to IDE or newer desktop products. [CLI skills](https://docs.qoder.com/cli/Skills) |
| Qoder IDE | AGENTS.md compatibility; Rules win conflicts | Inspect existing Rules, not only the root file. [IDE rules](https://docs.qoder.com/user-guide/rules) |
| Hermes | Official technical guide lists project `.hermes/skills/` and `.agents/skills/`, with project trust and distinct automatic-maintenance policies | Prefer unchanged project packages; do not automatically switch to personal copies or alter trust and management configuration. [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) |
| TRAE | Official skills page located, but retrieval returned no body; rules page timed out | Paths, format, and automatic activation remain unverified. Check current official or local evidence at installation; do not infer support from other agents. [Skills page](https://docs.trae.ai/ide/skills) |

Add equivalent evidence for other agents. Reading documentation is not client testing. Matching SKILL.md filenames do not establish identical metadata, tool support, or invocation semantics.

2026-10-29 user report: their Qoder environment also recognizes `.agents/skills/`. Thus `.qoder/skills/` is not the only candidate. Version and mode were not recorded, so this is not a guarantee for all Qoder environments. Verify the shared directory first.
