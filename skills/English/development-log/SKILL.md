---
name: development-log
description: Record completed changes, relevant reasons, and verification results when the project uses a development log or the user requests an entry.
---

# Development log

Help maintainers understand what changed and the evidence available at the time. Current product documentation still describes the present. Use `doc/开发日志/` (Chinese) or `doc/development-log/` (English) by default; reuse an existing changelog, development log, or decision record instead of duplicating it. Follow the user's requested language, otherwise the established project language. English instructions do not require English or bilingual output; preserve existing paths and identifiers.

## Workflow

1. Extract meaningful changes from the task, actual edits, and verification. Distinguish proposed, implemented, verified, and released work. Do not invent dates, versions, reasons, or test results. Tiny wording changes without behavior effects need no entry.
2. Record the actual completion date in the existing log. Entries completed on the same day may share a dated heading. Follow existing release groupings in projects that publish releases. Consolidate related entries and link a separate decision record for complex changes. Preserve dates supported by historical evidence.
3. Keep current behavior and design rationale in current documentation; put chronology, abandoned approaches, and historical conclusions in logs or existing decision records. Preserve and link established decision records without forcing relocation. Mark replaced decisions as superseded and link the replacement rather than rewriting history as current policy.
4. Check each statement against the evidence. Remove sentences that only list work left undone. If testing revealed a problem that affects users, describe the conditions and observed behavior and link the issue if available.

## Content and boundaries

Start with the specific change. Add reasons and verification results when useful. Reuse existing version numbers.

A wording request does not authorize historical migration. When asked to organize history, preserve original dates and evidence and mark gaps as unknown. Keep a change within its task instead of repeating it across indexes, diaries, weekly reports, and release notes.

For example, “After a failed save, users now retain their edits and can retry. We checked both successful saves and simulated save failures.”

At delivery, reuse the task summary and point to the record if useful. Do not append a fixed self-review report. This skill does not require other skills or a repository-wide scan.

Directory naming: honor an explicit project naming preference, then existing equivalent locations; for newly needed categories without an established name, use Chinese names in Chinese-language projects and English names in English-language projects. A single reply in another language does not change the project convention. Do not create both language trees or rename existing paths without a migration request. Keep standard entry names and shared paths such as README.md, AGENTS.md, doc/, tools/, agent-workspace/, ref/, and tasks-and-prompt/ unchanged. For other project languages, follow the user’s naming preference and existing conventions.
