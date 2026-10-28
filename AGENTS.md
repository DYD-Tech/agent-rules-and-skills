# 本仓库的工作规则

本项目维护可复用的开发规则和技能，帮助用户通过代理完成开发，并从文档中理解项目、积累知识。

## 每次工作

- 读取并应用 [通用开发规则](rules/development.md)。当前上下文已有最新内容时复用；文件更新或上下文丢失后重读。
- 应用可用的 clear-communication 技能。当前本地配套仓库入口为 `../communication-skills/skills/clear-communication/SKILL.md`；先使用已安装版本，无已安装版本时读取该路径。若两者都不存在，说明缺失并按通用规则的表达要求继续任务。迁移本仓库时核实路径，不假定其他机器有相邻仓库。
- 应用 [文档维护规则](rules/architecture-features-implementation.md)。本仓库的技能入口是 [architecture-features-implementation](skills/architecture-features-implementation/SKILL.md)，满足触发条件时读取并执行，无需用户重复点名。

- 应用 [开发日志规则](rules/development-log.md)，有值得记录的变更时读取 [开发日志技能](skills/development-log/SKILL.md)。

## 本仓库的维护约定

- `rules/` 是分发给其他项目的规则；`skills/` 是技能包。根 AGENTS.md 只指导本仓库工作，不作为通用模板复制。
- 调研、设计、变更及评测记录放在 `doc/`，运行必需的材料放在技能包内。`doc/` 根目录只允许 README.md，其他文档按用途放入子文件夹；新增文档优先复用现有分类，移动文件时同步修正引用。`doc/backup/` 是用户保存的历史备份，不修改或当成当前规则。
- 修改用户指定的规则或技能属于已授权工作；不得为绕开约束自行修改其他生效规则。
- 新增或实质修改技能时，检查结构、资源链接和真实任务表现。保存评测输入与实际输出，区分静态检查、作者试用和独立模型实验；不以自检声明证明行为或成本改善。
- 保持变更与说明一致，不将尚未运行的实验、尚未安装的技能或尚未发布的内容报告为完成。


## 真源维护与验证工具

- 本仓库是产品源码，用户授权的改进在这里维护；不要把业务项目的安装副本当成标准。适配规则集中在 adapters/，不得把宿主差异变成多个独立技能正文。
- 修改同步协议或检查器时，运行 `python -B -m unittest discover -s tests -v`；工具使用标准库，不需要全局安装依赖。只读检查不等于远端版本核验。
