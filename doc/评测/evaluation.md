# 验证记录

日期：2026-10-28；对象：0.1.0 规则与 architecture-feature-docs 技能。

## 0.3.0 模块安装与日志验证

本次检查 catalog/modules.json 的四个唯一模块 ID、必要与可选依赖目标、依赖无环、本地来源路径及技能名称。44 个本地文件链接有效，代码围栏配对；原规则备份哈希不变。此检查不验证网页可达性、锚点或目标客户端发现机制。

作者在临时项目中执行“通用规则＋架构功能实现”的本地安装演练。输入为本仓库当前文件及一份已有 AGENTS.md；得到两份规则、一个完整技能包、合并入口与安装记录，原指引保留。第二次执行文件集合和内容相同，没有重复区块。来源标记为未提交本地快照，没有虚构远端提交。临时文件已随演练清理。

实际目标结构：

```text
.agent-rules/agent-rules-and-skills/development.md
.agent-rules/agent-rules-and-skills/architecture-features-implementation.md
.agents/skills/architecture-features-implementation/（完整四文件技能包）
AGENTS.md
agent-rules-and-skills.lock.json
```

演练由作者用本轮临时代码完成，不是仓库提供的自动安装器，也不是另一代理独立按说明操作。没有验证宿主真正加载，没有执行更新冲突、卸载共享文件或个人安装测试；也没有实际下载外部技能。communication-skills 的网页获取失败，目录已记录安装时重新核验要求。

日志技能的作者试用产出是 [开发变更记录](../开发日志/CHANGELOG.md) 的未发布 0.3.0 条目：只记录实际变化与验证限制，没有把本轮修改写成已经发布。当前架构页面已移除承担历史流水的职责，保留现行设计理由。尚未完成独立模型的历史污染或误触发评测。

## 作者实际试用：为本仓库首次建档

输入：当前 README、AGENTS.md、两份规则、技能及参考材料，以及用户对学习用途的说明和设计记录。执行者为本次编写技能的同一代理，已知设计目标，因此不构成独立或盲测。

实际动作：读取技能和两份对应参考材料，按其首次建档流程为这个真实仓库编写文档。没有伪造一个软件系统来填模板。

实际产出：

- [总览与分层](../架构-功能-实现/00-总览与分层.md)：解释规则、技能、项目指引之间的关系，包含关系图、选择理由及路径维护成本。
- [功能全貌](../架构-功能-实现/01-功能全貌.md)：列出当前提供的能力及手动接入方法，明确没有自动安装或后台同步服务。
- [文档技能](../架构-功能-实现/02-文档技能.md)：先写功能，再写执行机制和知识，区分源码可证实的机制与无法从源码推知的历史动机。

作者对实际产出的核对：内容与文件结构相符；未把文本指引写成自动执行程序；没有宣称已经降低 token 或完成跨模型测试；共享组织方式在总览解释，功能页补具体作用。该试用展示产出可行性，但不能证明其他代理也会正确选择范围或写清机制。用户理解与长期记忆尚未测量。

## 结构检查

使用 skill-creator 的 quick_validate.py 尝试官方校验：当前 Python 缺少 PyYAML，脚本在导入阶段失败，未完成官方校验。没有因此修改全局环境。

另行检查 Markdown 本地链接目标、代码围栏配对、技能入口的基础字段、技能包引用边界及备份哈希。该检查不等价于完整 YAML 解析，也不验证模型行为。实际检查通过：仓库含备份共 16 个 Markdown 文件，检查 34 个本地文件链接，未发现缺失目标或未闭合代码围栏；技能入口基础字段正确，包内引用未越出技能目录。技能入口 52 行、4478 UTF-8 字节，字节数不等于 token 用量。备份 SHA256 保持为 `495312d4ad251732a7207467c59a37a9cb54aca171a5e548deb0fa70c45aa3e3`。未自动检查外链可达性、Markdown 锚点或 Mermaid 渲染。

## 后续行为与成本验证

尚未执行：旧文档局部更新、文档与代码冲突、计划转实现、重要决策被替代、无需改文档的小修复，以及不同模型的对照运行。

后续应固定模型、项目快照和任务，比较原规则与当前版本，保存真实输入、改动和验证结果；重复运行后记录遗漏、事实错误、额外文档、工具调用、耗时及 token。不得用文件数量、格式检查或代理自评代替效果指标。

读者理解验证应检查：不看源码能否解释系统协作和设计取舍，面对变化的约束能否判断方案是否仍适用。仅在评测时征集反馈，不给每次开发增加答题或评分负担。


## 0.4.0 唯一真源与偏离检查

实际执行 `python -B -m unittest discover -s tests -v`，8 项测试通过。测试使用临时目录，覆盖未修改状态、内容改动、文件缺失、受管目录新增文件、CRLF 与有效空格差异、入口区块内外变化和重复标记、路径越界和重复登记、缺失目录、空记录、二进制哈希，以及命令行退出码和只读行为。测试不修改业务项目或个人配置。

输出始终将 source_freshness 标为 unchecked，避免把本地 clean 当成上游最新。该工具不校验来源声明真实性，不发现受管目录之外的未知副本，不执行语义适配或自动更新。

已用 git ls-remote 核对 communication-skills 的 main 为 33c284f4fbe5941f7e97d707149cfaf1fd6c84ad，并固定目录 ref。仅 ref 核验不代表完整远端代码审查。Qoder 与 Hermes 支持情况来自官方页面，TRAE 页面内容未取得；均未进行真实客户端安装测试。

完整三方更新、fork 切换、多宿主等效适配及本地改进汇回仍为代理执行协议，尚无端到端实测；没有声称所有项目已同步。


## 使用身份与源仓库维护流程补充

本次修改 README、INSTALL、SYNC 和当前架构说明，区分直接使用者安装升级、维护者修改发布、fork 自主管理及 PR 贡献。文档审查覆盖了仅安装、只改不推送、无写权限、PR 未合并、fork 迁移部分项目这些情形；这是作者对流程文本的核对，不是实际远端操作或独立 agent 实验。

实际重新运行 8 项检查器测试，全部通过；80 个本地文件链接、代码围栏、doc 根目录约束及原备份哈希检查通过。该结果不证明授权流程会被所有 agent 正确执行；未执行 clone、fork、推送、PR 或业务项目升级。


## 双语支持：作者试用与静态验证

本次采用单一英文运行指令，中文对照在 doc/中文对照；并提供中英文使用指南。以下是本轮作者根据已读取技能完成的有限试用，输入为虚构测试材料，输出为实际编写的样例，不是业务项目变更事实，也不是独立模型实验。

### 开发日志：中文请求

输入：请用中文给既有 doc/开发日志/CHANGELOG.md 写一条未发布记录。任务事实是“保存失败以前会清空编辑内容，现在保留；已测正常保存和模拟失败；未测断电恢复；未发布”。不要添加日期或版本。

输出：

> 保存失败时保留编辑内容，用户可以重试；此前失败会清空内容。已验证正常保存和模拟失败，断电恢复尚未验证。本项尚未发布。

该输出使用中文，没有把英文技能语言当作输出语言，也没有编造日期或发布状态。指定位置沿用既有路径，没有新建英文目录或另一份日志。

### 开发日志：英文请求

Input: Write the same unreleased change in English for the existing doc/开发日志/CHANGELOG.md. Do not invent dates or versions.

Output:

> Failed saves now preserve edited content so users can retry; previously, failure cleared the input. Normal saves and simulated failures were verified. Recovery after power loss remains unverified. This change has not been released.

两份输出保留相同事实、验证范围与未发布状态；这属于对同一测试材料的语言试用，不需要同时安装两份技能。

### 架构文档：局部英文说明

Input: Use the documentation skill to draft only a short feature and implementation passage in English. The existing document is doc/架构-功能-实现/报告.md; do not rename it. Fictional evidence: report requests create database job records; a worker writes a file and then marks the job complete; unfinished jobs rerun after restart. Duplicate prevention and tests are unknown. No historical decision record is available.

Output:

> **Feature:** Submitting a report request creates a job record. A worker generates the file and records completion. After a restart, unfinished jobs run again; this does not establish that partial work resumes.
>
> **Implementation:** File creation happens before completion is recorded. If the process stops between those operations, the unfinished job may run again. The available evidence does not establish how duplicate effects are prevented or what recovery tests cover. The historical reason for this design is unknown.

输出只覆盖请求段落，保留既有路径，没有开展整库建档；区分已知执行顺序、可推出的中断风险和未核实机制，没有编造测试、恢复保证或历史动机。该样例未修改实际业务文档。

### 检查结果与边界

实际运行 8 项已有检查器测试，全部通过。145 个本地文件链接、代码围栏、doc 根目录约束、原备份哈希、目录 JSON、模块 ID 唯一性、安装路径及中文对照覆盖检查通过。技能入口的 name/description 做了基础检查。skill-creator 的 quick_validate.py 因当前 Python 缺少 PyYAML 未能运行，不能报告完整 YAML 验证通过。

人工对照中英文关键要求：规则适用范围、按需读取、授权、触发、失败处理、源仓库与安装副本的区分均保留。上述样例验证作者本次能按英文指令生成指定语言，不能证明所有 agent 都能做到，也未测量 token、延迟或跨宿主加载。未安装到其他项目或个人环境。


## 2026-10-29：通用目录与首次安装版本

问题证据：用户报告其 Qoder 环境可识别 .agents/skills/，但安装代理优先用了 .qoder/skills/；未取得客户端版本或独立宿主测试。实际检查旧目录配置，发现清晰沟通固定为 33c284f4fbe5941f7e97d707149cfaf1fd6c84ad。执行 git ls-remote 查询其远端 refs/heads/main，实际返回 d3ff615458ae3c608e1e17fb514080cea6716783，确认旧目录与当前远端不同。

流程审查案例及本次结论（作者审查，不是独立 agent 执行）：

| 情形 | 应执行的结果 |
| --- | --- |
| 新项目，宿主已验证通用目录原生发现 | 使用 .agents/skills/ 与 .agent-rules/；不因 Qoder 品牌选择专用目录 |
| 通用目录不支持或尚未核实 | 区分不支持与未知；按证据选择替代方式，不宣称通用支持或专用必需 |
| 首装清晰沟通，未指定版本 | 读取当前目录策略，查询 main 并锁定查询所得完整提交；本次远端结果为 d3ff615，不使用旧 verification 文本作为版本 |
| 按旧锁记录重装或为项目新增 agent | 复用旧提交，不能擅自升级造成同项目版本分裂 |
| 明确升级，目录提交未变但外部 main 已更新 | 仍查询外部 main，比较本地修改后升级并更新实际提交记录 |
| 用户明确指定旧提交，或使用 pinned 条目 | 尊重指定版本，说明并不表示最新 |
| 最新查询失败 | 保持已有安装，说明未完成，不把缓存标为最新 |
| 已有 .qoder/skills/ 存在本地改动 | 先保留差异并核对引用及遮蔽，不直接复制覆盖或删除 |

实际执行现有 8 项只读检查器测试，全部通过；147 个本地文件链接、围栏、doc 根目录结构和目录策略字段检查通过。这些测试不实现或验证自动安装、版本解析或客户端发现；当前安装仍由 agent 按指南执行。未迁移用户业务项目，未改变个人技能目录，未对 Qoder 做独立加载实验。
