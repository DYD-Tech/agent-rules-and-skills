# General development rules

## Principles

**Maintain the project to the standard of a diligent professional team.** Treat it as software that must remain usable, maintainable, and transferable. Take responsibility for correctness, reliability, security, readability, and maintainability. Completion includes verification, future changes, and real use, not merely a working demonstration.

**Base development on applicable standards and established practice.** Where specifications or mature solutions exist, follow relevant conventions and learn from proven implementations. Ground decisions in verifiable technical facts and engineering evidence. Do not invent critical semantics or present a plausible custom solution as established practice.

The following rules make these goals actionable while preserving task scope and collaboration. Scale work to project maturity and change risk; diligence does not require perfection, enterprise architecture, or ceremonial processes.

## Task scope

- Describe requested work through deliverables and acceptance conditions. Leave unrequested features out of both the work and its records. A request to narrow the task updates the remaining deliverables. When an earlier plan defers a capability, check which milestone that decision covered. A later explicit request authorizes work on that capability within current project constraints. Seek clarification only when a specific, still-applicable constraint conflicts or its applicability would materially change the work.

- Understand the objective, relevant implementation, and constraints before editing. Establish expected behavior and how to verify completion. Handle simple tasks directly; use a brief plan for cross-module changes, data changes, or significant tradeoffs. Reuse existing requirements and task records rather than requiring a separate acceptance document.
- Complete the necessary authorized work without unrelated refactoring or overwriting user changes. Investigate important ambiguity using available evidence, then ask a specific question if needed. Decide routine implementation details yourself; do not request permission already granted.
- When asked to change rules or skills, work within the specified scope. Do not relax constraints for convenience. A review-only request calls for findings and suggestions, not replacement of active rules.

## Implementation and design

- Choose the simplest implementation that satisfies known functional, reliability, security, and operating constraints. Do not add abstractions, configuration layers, or extension points for hypothetical needs.
- Inspect relevant existing code and dependencies first. Before adding a library, consider suitability, maintenance, license, and adoption cost. Small local logic may be implemented directly; reuse should not create unnecessary dependencies.
- Keep responsibilities focused and interfaces clear. Follow suitable project patterns without copying known defects or splitting cohesive work solely to create layers.
- Establish one working path from input to result before expanding a new feature. Each stage should be usable and verifiable; placeholders and false success are not completion.
- Preserve supported external behavior and existing data by default. Check callers and dependencies before removing implementations. Follow the project's compatibility policy for breaking changes; explain effects and obtain authorization when not already granted. Ending legacy support, migrating data, and handling runtime failures are separate decisions.
- Check boundaries and failure paths relevant to the mechanism being changed: external input, resource release, timeouts, retries, concurrency, or interrupted data updates. Do not apply an exhaustive checklist to every task. Make errors diagnosable; do not swallow failures or report false success. Explain temporary measures, their limits, and removal conditions, recording useful follow-up work.

## Standards, established practice, and evidence

- Before designing relevant behavior, identify constraints from protocols, file formats, languages, platforms, and dependencies. Check the versions and environment actually used. Reuse verified project evidence; consult applicable primary sources when information is missing, uncertain, or changeable. Do not fill critical gaps from memory.
- Implement and verify applicable formal requirements. Use the corresponding official version documentation for library and platform behavior. Mature implementations help explain practical details and edge cases; they do not replace specifications, and one project's preference is not an industry standard. Explain conflicts between sources, observed behavior, and project requirements before resolving them.
- Where no formal specification applies but mature solutions exist, compare relevant approaches before committing to a critical design. Understand assumptions, failures, and maintenance costs. Choose for the actual scale and constraints instead of copying complex architectures. Simple local work may follow verified project practice without new web research.
- When designing a custom solution or departing from applicable conventions, explain why existing solutions are insufficient, what behavior is affected, and how it will be verified. Unauthorized compatibility or support changes still require confirmation; routine choices do not need additional approval. For security-sensitive mechanisms, prefer maintained, suitable standard libraries or established components over unverified custom algorithms or protocols.
- Recheck the evidence before the next fix whenever a new symptom needs an explanation, a fix fails to produce its predicted result, or the proposed change introduces a different API, lifecycle hook, or fallback. State what happened and which assumption now needs checking. Reuse earlier evidence only where it covers this specific question. Check the exact API contract for the proposed inputs, timing, supported versions and documented failures, and look for established handling of this particular case. Follow any project requirement for a comparable maintained implementation. If none is found, record what you checked and what remains unknown.
- Identify an observation that distinguishes the plausible causes. If the available evidence cannot distinguish them, gather a focused trace or run a minimal experiment before adding another production workaround. Apply the supported change and replay the original failing sequence, including the triggering state. If it still fails, revisit the assumption and review earlier workarounds before building on them. Reuse task notes and existing feature documentation for evidence and results.
- Before implementing a feature, check which published standards or established practices apply to its behavior and supported versions. For each one adopted, cite a verified primary source beside the affected behavior in the feature documentation. Give the applicable section or version and a retrievable link or source reference. Explain what it requires or recommends, how the implementation meets it, and what observation or test verifies that behavior. Use the existing feature page or create a concise entry in the project’s documentation. Share a reference across claims only when readers can tell which provision supports each one. Label project choices explicitly where the source leaves discretion. If evidence is unavailable, identify the uncertainty before relying on the claim.

- Preserve significant decisions in relevant documentation or comments, including conclusions, assumptions, key sources, and useful versions or sections. Mark missing evidence as unknown. Use implementation inspection, experiments, or tests to resolve critical uncertainty; do not invent citations or historical motives.
- Stop research when the applicable constraints, critical behavior, and validation approach support implementation. Retain unresolved questions that could change the design. Do not impose search quotas, investigate unrelated detail, or substitute source lists for verification.

## Verification and delivery

- Select relevant verification and run required project checks. Cover expected behavior and relevant boundaries and failures. For standards or interoperability, use suitable reference examples, conformance checks, or actual integration tests, not only internal consistency. Reproduce defects where practical, verify the fix, and add maintainable regression tests for reliably automated cases.
- Start with affected behavior. Expand checks when scope, failures, or project requirements justify it. Never remove correct assertions or ignore failures to manufacture a pass. If expected behavior changes, update tests based on the new requirements.
- Before delivery, inspect the change as a future maintainer: requirements, regressions, unnecessary complexity, understandable reasons and constraints, and consistency between documentation and evidence. Fix substantive issues without expanding scope for style preferences. State verification limits; do not claim checks that did not run.
- Report changes, verification, and material limits. Distinguish planned, implemented, installed, and released work. Reversible routine work needs no extra approval; destructive data operations, publication, and rewriting shared history require explicit authorization.
- Do not place secrets in code, documentation, or logs.

## Documentation and communication

- Follow the user's language and requested format; otherwise follow the conversation and established project language. English instructions do not require English output or bilingual output. Express each thought fully enough for readers to understand the conclusion, its reasons, and when it applies. Cut restatements of the same point and irrelevant lead-ins. Split unwieldy sentences while keeping the actions, their objects, and the connections readers need. Retain useful standard terms with enough context; do not invent vague jargon or replace mechanisms with analogies.
- User documentation explains behavior; development documentation explains mechanisms and choices; comments explain non-obvious intent. Preserve background useful for understanding and long-term learning without translating code line by line or adding unrelated tutorials.
- Update affected documentation in the same task when behavior, mechanisms, or important constraints change. Make edited passages coherent and clear while preserving accurate names and facts; do not rewrite the whole repository by default.
- For confirmed, non-obvious problems likely to recur and worth remembering, check for existing coverage, then record symptoms, cause, remedy, necessary evidence, and applicability. Reuse the project knowledge directory; if none exists, use `doc/值得记住的坑/` (Chinese) or `doc/lessons-learned/` (English) with topic-based filenames. Omit trial-and-error chronology while retaining evidence supporting conclusions.

## When interfaces are involved

- Give actions perceptible results. State changes can provide immediate feedback; long operations should visibly distinguish progress, completion, and failure with useful next steps. Avoid unnecessary notifications.
- Check affected keyboard interactions, focus, and basic accessibility, not only mouse operation.

Projects should separately provide actual installation and verification commands, key directories, supported environments, compatibility policies, and operational constraints. Project conventions refine these defaults. Resolve material conflicts using user authorization rather than guessing commands or silently dropping constraints.

Directory naming: honor an explicit project naming preference, then existing equivalent locations; for newly needed categories without an established name, use Chinese names in Chinese-language projects and English names in English-language projects. A single reply in another language does not change the project convention. Do not create both language trees or rename existing paths without a migration request. Keep standard entry names and shared paths such as README.md, AGENTS.md, doc/, tools/, agent-workspace/, ref/, and tasks-and-prompt/ unchanged. For other project languages, follow the user’s naming preference and existing conventions.
