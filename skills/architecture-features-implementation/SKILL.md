---
name: architecture-features-implementation
description: Create or maintain architecture, feature, and implementation documentation for development, acceptance, and long-term learning. Use when documentation is requested or adopted documentation needs updates after behavior, mechanism, or architecture changes. Local maintenance does not trigger full-repository documentation; handle tiny wording edits directly.
---

# Architecture–features–implementation

Help readers understand the software, design, and reusable knowledge without reading code line by line. Verify relevant implementation and evidence; fluent prose is not a substitute for facts. Follow the user's requested language, otherwise the established project language and document locations. English instructions do not require English or bilingual output. Preserve existing paths and identifiers; default to `doc/架构-功能-实现/` when no location is established.

## Choose the scope

- **Routine maintenance:** Reuse files, requirements, and evidence already read for this task. Locate affected passages. Update only when facts, explanations, or navigation change; otherwise stop without an extra report.
- **New or substantially rewritten pages:** Read [content and examples](references/document-shapes.md) for the relevant layer. These are information needs, not mandatory headings.
- **Explicitly authorized initial documentation or comprehensive reorganization:** Also read [initial documentation](references/initial-documentation.md). Routine changes, reading a document, or noticing missing pages do not authorize documenting the whole repository.

Reuse applicable material already in context. Load only necessary references. This skill does not prescribe internal reasoning or require outlines, review forms, or extra planning files.

## Responsibilities of the three layers

| Layer | What readers must understand | When to update |
| --- | --- | --- |
| Architecture | Boundaries, major responsibilities and collaboration, key data flows, and how choices address constraints | Structural, shared-mechanism, or important design changes |
| Features | Complete capabilities, inputs, results, significant defaults, and failures | Capability or externally visible behavior changes |
| Implementation | Critical execution paths, difficulties, mechanisms, tradeoffs, evidence, and maintenance references | Mechanism, constraint, or important rationale changes |

Explain overall architecture centrally and link focused topics. Put feature behavior before implementation. Explain shared knowledge once. Organize features around user goals, not every button or code file. Reuse an equivalent existing structure.

These pages describe the currently supported version. Put intended behavior and unimplemented proposals in existing requirements or task records; put dated chronology, previous implementations, and replaced decisions in development logs or existing decision records, defaulting to `doc/开发日志/`. Retain reasons and limits needed to explain the present. Link history without accumulating it on current pages. This does not require installing the log skill or migrating unrelated history.

## Workflow

### 1. Establish evidence and affected content

Compare the task, relevant documents, code, configuration, and verification. Distinguish implemented behavior, plans, and unknowns. Read only what resolves relevant uncertainty. Keep working notes in the current task context rather than creating another ledger.

When code and documentation disagree, determine whether the implementation violates requirements or the documentation is outdated. Use user requirements, applicable conventions, and actual behavior. Explain important unresolved conflicts; do not silently change code to match prose or document defects as correct behavior. Documentation work alone does not authorize product-code changes.

### 2. Explain behavior, mechanisms, and useful knowledge

Start with observable behavior, then explain critical paths and choices. Connect concrete constraints, mechanisms, effects, costs, and applicability. Do not force lessons or alternatives onto simple facts. Explain unfamiliar terms in context, then reuse them consistently.

Code establishes mechanisms, not historical motives. If decision records are absent, mark the historical reason as unknown or label the explanation as analysis of the present design. Consult primary sources when needed for external specifications or unfamiliar mechanisms; cite evidence that supports the claim without collecting citations for routine facts.

Prose must stand alone. Code references support verification and maintenance; they do not replace explanations. Prefer relative paths and stable names, adding symbol names when useful. Avoid large code dumps, command output, secrets, and chat transcripts. Describe actual validation coverage and limits; never claim unrun tests passed.

Edit coherent passages touched by the task and necessary adjacent text. Preserve accurate terms, identifiers, and useful explanations. Update current descriptions when decisions change. Preserve valuable superseded decisions in history with status and replacement links; do not leave old designs presented as current or rewrite history as if the change never happened.

### 3. Check the change and deliver

- Behavior, values, defaults, failures, and evidence agree. Plans are not presented as current, and unknowns are not polished into facts.
- Affected overviews, indexes, feature pages, shared explanations, and diagrams agree; links work and unrelated material remains untouched.
- Readers can explain the relevant collaboration, choices, and limits without reading source code.

Fix specific defects and stop. Report documentation changes and necessary unknowns using the existing task summary, without another review report. For broad authorized work, finish all agreed batches; if blocked, identify what remains.
