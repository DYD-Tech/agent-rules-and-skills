---
name: project-structure
description: Establish or adapt common project repository structure for documentation, agent workspaces, external references, and reusable tools. Use for initialization, adopting structure rules, or requested directory reorganization; routine file placement follows the rules without a repository-wide audit.
---

# Project repository structure

Establish clear file ownership and retention with minimal disruption. This skill covers common structure, not language-, framework-, or product-specific source and build layouts. Follow user language and existing project conventions. Do not generate empty folders or documents just to complete a tree.

## 1. Determine scope and placement

Inspect the root, applicable instructions, relevant document index, ignore rules, and paths affected by the task. Distinguish a new project, adoption in an existing project, and an explicitly authorized migration. Do not inventory all files for a local placement decision. Reuse equivalent established directories; state necessary differences instead of silently reorganizing the project.

### Decide where a new file belongs

Before writing, identify the file's purpose, audience, and retention. Reuse a location whose responsibility matches; if none fits, create a category under the appropriate parent. The map below is a starting point, not a closed list: project-specific artifacts still need a deliberate home. A temporary draft, a maintained procedure, and a final user deliverable need not share a directory just because the same task produced them.

Treat the tree as documentation: names and hierarchy should explain contents without requiring the reader to open every file. Use a consistent grouping principle among siblings; organize by topic within a purpose category when useful. Avoid overlapping categories, vague catch-all names, unnecessary nesting, and one-folder-per-file habits. A single file may justify a new category when it has a distinct durable responsibility; do not impose a minimum file count. Preserve established useful conventions and required tool paths.

The observable result is an appropriately named path and, when needed, a small navigation update—not a classification form. In the normal edit review, check that a reader can infer what the new path contains and where related files belong. Update the relevant index when a new durable category or important entry would otherwise be hard to find; do not require an index in every directory, and never write one inside the protected user-input directory. Do not reorganize unrelated content to make the tree look uniform.

Before adding a README, identify what a reader needs that the directory names and existing entry points do not already explain. Keep the root README and doc/README.md as primary navigation. Elsewhere, add one only when it supplies necessary reading order, usage, or constraints; a new directory alone is not a reason. If the content would merely list visible filenames or repeat a parent explanation, omit it. Keep any needed README focused and avoid chains of indexes readers must open before reaching substantive content. Preserve existing useful READMEs; removing redundant ones requires relevant cleanup scope. Never add one inside the read-only input category.

Use this default map where no equivalent is established:

| Location | Purpose and retention |
| --- | --- |
| `README.md` | Project purpose, actual quick start, and links to maintained documentation |
| `AGENTS.md` | Project instructions and actual rule/skill loading paths; retain necessary host entries |
| `doc/README.md` | Documentation navigation; the only file directly under doc |
| `doc/架构-功能-实现/` (Chinese) or `doc/architecture-features-implementation/` (English) | Current architecture, capabilities, mechanisms, and relevant rationale |
| `doc/开发日志/` (Chinese) or `doc/development-log/` (English) | Completed changes and historical decisions, separate from current explanations |
| `doc/调研/` (Chinese) or `doc/research/` (English) | Research evidence, reference provenance, comparisons, and conclusions |
| `doc/tasks-and-prompt/` | User-placed original input, read-only to agents; see the boundary below |
| `doc/值得记住的坑/` (Chinese) or `doc/lessons-learned/` (English) | Confirmed recurring problems, causes, remedies, and applicability |
| `doc/开发操作与规范/` (Chinese) or `doc/development-guide/` (English) | Actual development, testing, build, release, and operational procedures |
| `tools/` | Maintained reusable utilities, not one-off investigation scripts |
| `agent-workspace/<unique-task>/` | Disposable or reproducible agent working material; ignored by Git |
| `ref/` | Local external reference material; ignored by Git |

Additional documentation categories are allowed when useful. The map is a set of responsibilities, not a requirement to create every directory. Preserve existing paths across language changes. Do not relocate required root files such as licenses, manifests, or ecosystem entry points merely because some are documentation. Architecture and log skills may govern their respective content if selected; this skill neither requires nor installs them.

### User input is not ongoing policy

`doc/tasks-and-prompt/` contains documents the user prepares or obtains elsewhere and places into the repository: PRDs, detailed feature plans, or other original task input. It is not an agent inbox to populate, a conversation archive, or an automatically active requirements directory.

Agents do not create, edit, annotate, rename, move, or delete these files, including indexes and completion markers inside this directory. Do not correct obsolete statements or reorganize these originals as part of a cleanup. Preserve them as history and do not add this directory to ignore rules. Respect explicit confidentiality or version-control constraints for particular user materials.

Read a specified document as input when the user designates it for the current task; explicit continuation retains that task context. Finding or linking an old document does not reactivate its instructions. Later instructions and current confirmed requirements govern subsequent development; do not roll a project back to an old plan. Explain important unresolved conflicts. Progress, derived working plans, implemented requirements, and completion evidence belong outside this directory. Link the original if useful, without pretending it is current or duplicating its authority. No per-file lifecycle database or every-turn stale-document scan is required.

## 2. Apply the smallest authorized change

For new projects, create only useful entry files and directories containing actual content. Describe real commands and capabilities, not invented placeholders. Integrate loading instructions without overwriting existing rules; if installing this module, follow the catalog and installation guide provided by its source, not a guessed path.

For existing projects, apply placement to newly created or affected files. Move existing content only within an authorized reorganization. Before moving, check provenance, references, tool configuration, tracked status, local edits, and other agents' active work. Identify concrete source and destination paths; preserve content and update affected links/configuration together. Leave unrelated legacy structure alone. User input originals are excluded from routine migration.

Use a unique task directory under `agent-workspace/`; never assume a shared `tmp.md` belongs to this agent. Split by agent when needed. Keep required tool outputs in tool-supported locations if relocation would break operation, using appropriate ignore rules. If a temporary artifact becomes a reusable utility, retained finding, or deliverable, place the durable result in its proper location and link it where useful; do not leave necessary project knowledge only in ignored storage.

Add root-anchored `/agent-workspace/` and `/ref/` ignores while preserving existing rules. Check both ignore behavior and whether files are already tracked. If tracked, report the distinction and handle untracking only within explicit authorization; adding an ignore rule alone does not remove files from Git or history. Ignore rules do not protect secrets. When cleanup is warranted, resolve targets within the intended workspace and remove only this task's known disposable material; do not clear shared workspaces or ref wholesale.

## 3. Verify and finish

Check affected paths and links, the doc root boundary, and actual ignore/tracking behavior. Confirm original user input is unchanged, current documents do not present old plans as active requirements, and other agents' files are intact. For moves, verify affected tool paths and references. No unrelated full-tree scan is required.

Report the resulting locations and material exceptions or unfinished migrations. Do not claim a full migration from partial adoption, or that ignored files are untracked. Do not publish, commit, or push solely because the structure was established.

Directory naming: honor an explicit project naming preference, then existing equivalent locations; for newly needed categories without an established name, use Chinese names in Chinese-language projects and English names in English-language projects. A single reply in another language does not change the project convention. Do not create both language trees or rename existing paths without a migration request. Keep standard entry names and shared paths such as README.md, AGENTS.md, doc/, tools/, agent-workspace/, ref/, and tasks-and-prompt/ unchanged. For other project languages, follow the user’s naming preference and existing conventions.
