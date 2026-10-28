# Content requirements and examples

Use the relevant layer when creating or substantially rewriting a page. These are questions readers need answered, not mandatory headings. Combine information into prose and omit inapplicable detail.

## Architecture overview

The default page is `00-总览与分层.md`. Explain purpose, users, and system boundaries, followed by major parts, responsibilities, and relationships. A representative flow should show how input becomes a result. Use a small diagram when helpful, explaining arrow meanings rather than presenting unexplained boxes.

Explain constraints and central choices: why responsibilities are divided this way, what problem that solves, its costs, and when changing conditions would require another choice. Expand on databases, external services, deployment, and recovery only when useful to understanding. Technology lists and directory trees locate things; they do not explain architecture.

Link focused topics instead of squeezing all knowledge onto one page. Simple systems need neither forced layers nor multiple diagrams. Check diagrams and prose together when either changes.

## Feature index and feature sections

The default index is `01-功能全貌.md`; reuse an existing README if it serves the purpose. Organize capabilities, purposes, and detailed references by user goals. State unverified coverage. Plans belong in requirements or tasks and may be linked, but are not current capabilities.

For a feature, explain who uses it, in what situation, with what inputs and results, important defaults or limits, and failure recovery. Explain distinct paths when they actually exist. Background operations, command-line use, and library calls count as features too.

Avoid irrelevant class and module names in feature descriptions, while preserving commands, configuration keys, and product names users need. Do not list every button or mistake internal modules for the complete feature set.

## Implementation sections

Follow the feature section or link a separate page for long explanations. Describe a critical path from entry to result, necessary state or data changes, collaborating modules, and constraints that determine success. Explain why the mechanisms are needed instead of translating code line by line.

Select useful causal relationships: how a specific problem motivates a mechanism, what it costs, and when it can or should not be reused. Distinguish analysis of current benefits from documented historical reasons.

Provide enough evidence references for important facts: source paths and symbols, tests or measurements, decision records, or primary sources. State only confirmed validation coverage and limits; do not publish all execution logs or invent completeness when evidence is missing.

## Shared knowledge, history, and lessons

Maintain shared mechanisms once in the overview or a topic page. Features explain their use and differences, linking shared material. Separate architectural decision records are for significant choices requiring traceability; include context, choice, status, and consequences in the development log or an existing decision directory. Current pages retain current rationale and useful links. Do not create a directory without such a need.

Reuse the project knowledge base for confirmed troubleshooting symptoms, causes, remedies, and applicability. Architecture and feature pages keep relevant design conclusions and links rather than full investigation history. Preserve necessary evidence and mark unconfirmed causes as unknown.

## Example: background report generation

This fictional design illustrates explanatory depth. Do not copy it as a real project fact.

**Architecture:** The interface accepts requests and displays results, background jobs generate reports, and the database stores job state. Slow generation runs independently to keep the interface responsive; persistent state makes unfinished jobs discoverable after a restart. This requires job-claiming and recovery logic. Fast operations that are cheap to restart may need only direct execution.

**Feature:** Submitting a request creates a job record, and users may continue working. They retrieve a report on success or inspect the failure and retry. This design restarts unfinished jobs after a restart; it does not promise to resume partial progress.

**Implementation and knowledge:** If a process exits after generating a file but before recording completion, recovery may execute the job again. The design must establish whether repetitions create extra effects. Producing a consistent result when the same job repeats is called idempotency. Stable job identifiers can identify existing results, but preventing concurrent duplicates still depends on storage and claiming mechanisms. Real documentation must describe the actual solution and its evidence; a queue alone does not imply that duplicates are impossible.

These explanations are understandable without code; real projects should add accurate source and verification references. The feature section need not explain idempotency internals, while the implementation section needs more than “an asynchronous architecture improves stability.”
