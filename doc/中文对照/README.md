# 中文对照与双语维护

这些文件供中文读者和维护者阅读，不能作为另一套运行规则或技能安装。规范运行内容仍在根目录的 rules/ 和 skills/。用户使用中文或英文时，模块 ID、安装路径、来源版本与触发行为相同；运行指令的语言不决定输出语言。

These are Chinese reading counterparts, not additional installable rules or skills. Canonical runtime content lives in rules/ and skills/. Language does not change module identity, installation paths, provenance, or activation; English instructions do not require English output.

## 对照入口 / Reading counterparts

| 规范英文 / Canonical English | 中文对照 / Chinese counterpart |
| --- | --- |
| [General development](../../rules/development.md) | [通用规则](rules/development.md) |
| [Documentation rules](../../rules/architecture-features-implementation.md) | [文档规则](rules/architecture-features-implementation.md) |
| [Log rules](../../rules/development-log.md) | [日志规则](rules/development-log.md) |
| [Documentation skill](../../skills/architecture-features-implementation/SKILL.md) | [架构—功能—实现技能](skills/architecture-features-implementation/SKILL.md) |
| [Content guidance](../../skills/architecture-features-implementation/references/document-shapes.md) | [内容与示例](skills/architecture-features-implementation/references/document-shapes.md) |
| [Initial documentation](../../skills/architecture-features-implementation/references/initial-documentation.md) | [首次建档](skills/architecture-features-implementation/references/initial-documentation.md) |
| [Log skill](../../skills/development-log/SKILL.md) | [开发日志技能](skills/development-log/SKILL.md) |

## 同步维护 / Keep translations aligned

- 行为变更先明确规范运行内容，并在同一任务更新对应中文文本；不要让翻译成为独立政策。发现冲突时以规范文件为准，修复对照。
- README、INSTALL、SYNC、catalog 的指南与记录格式、adapters 的中英文版本同轮维护；核对范围、条件、授权、失败处理、触发和未验证限制，不以段落数量证明等义。
- 已有路径保持不变，不因语言选择迁移用户文档；中文默认目录名是路径约定，不限制文档语言。历史调研、备份及旧评测保留原文，不要求追溯翻译。
- 技能运行时不加载本目录；需要中文例子时也不能把整个开发文档目录作为技能依赖。

For behavioral changes, update canonical instructions and the matching Chinese text in the same task. Canonical runtime files govern discrepancies. Keep paired usage guides aligned on scope, conditions, permissions, failure handling, activation, and verification limits. Preserve existing paths and historical records. Do not load this directory at skill runtime.
