---
name: development-log
description: Record meaningful completed changes, reasons, verification, and remaining work when the project adopts development log rules or the user asks for a change record. Maintain development history rather than chat transcripts; do not replace current architecture or feature documentation.
---

# Development log

Help maintainers understand what changed and the evidence available at the time. Current product documentation still describes the present. Use `doc/开发日志/` by default; reuse an existing changelog, development log, or decision record instead of duplicating it. Follow the user's requested language, otherwise the established project language. English instructions do not require English or bilingual output; preserve existing paths and identifiers.

## Workflow

1. Extract meaningful changes from the task, actual edits, and verification. Distinguish proposed, implemented, verified, and released work. Do not invent dates, versions, reasons, or test results. Tiny wording changes without behavior effects need no entry.
2. Check related entries and consolidate unfinished records for the same task. Put ordinary changes in the Unreleased section of `CHANGELOG.md`, explaining changes, necessary reasons, and validation limits by topic. Move them to a release only after release is confirmed. Significant history or decisions may have a dated topic file linked from the index; do not create a separate file for every small edit.
3. Keep current behavior and design rationale in current documentation; put chronology, abandoned approaches, and historical conclusions in logs or existing decision records. Preserve and link established decision records without forcing relocation. Mark replaced decisions as superseded and link the replacement rather than rewriting history as current policy.
4. Check dates, scope, status, and evidence. Do not copy complete diffs, chats, secrets, or raw output into logs. Logs are not another task tracker; link existing tasks for remaining work and summarize only when useful.

## Content and boundaries

Use prose or a few bullets to explain changes, necessary reasons, verification, and remaining limits. No fixed headings are required. Reuse existing version numbers; writing a log does not authorize a release, tag, commit, or push.

A wording request does not authorize historical migration. When asked to organize history, preserve original dates and evidence and mark gaps as unknown. Keep a change within its task instead of repeating it across indexes, diaries, weekly reports, and release notes.

Example: replace “Improved saving” with “Failed saves now preserve edited content so users can retry; previously failure cleared the input. Normal saves and simulated failures were checked; recovery after power loss remains unverified.” Use such claims only when supported; never invent tests to complete an entry.

At delivery, reuse the task summary and point to the record if useful. Do not append a fixed self-review report. This skill does not require other skills or a repository-wide scan.
