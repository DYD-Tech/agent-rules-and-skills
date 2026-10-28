# 安装记录 v1

文件名为目标项目根的 `agent-rules-and-skills.lock.json`。这是本项目协议，不是任何代理的原生配置。完整记录真源、模块和宿主适配信息；只读工具检验其中 artifacts 的已安装基线。无记录或记录不完整时不能报告已同步。

核心字段：

- `schema_version`: 1。
- `registry`: 用户选定的目录仓库 `url`、锁定 `commit`；本地试用可明确标未提交快照，不能用于声明远端同步。
- `modules`: 每项含 `id`、实际 `source_repo`、`source_commit`、`source_paths`。外部模块提交独立于 registry 提交。
- `artifacts`: 每项含目标项目相对 `path`、安装结果 `sha256`、`hash_mode`（`bytes` 或 `utf8-lf`）、`role`（`source-copy`、`adapter-output` 或 `entry-block`），以及 `module_id` 和来源映射。`adapter-output` 还记录 `adapter_id`、适配定义版本和变换说明。
- `managed_roots`: 完全由安装管理的独立技能或规则目录；不要把整个项目、整个 `.agents/skills` 或混有用户文件的目录列入。检查器报告这些目录中未登记的文件，便于发现代理自行添加的内容。
- `hosts`: 每个实际目标宿主的版本、加载方式、目标路径、验证状态；机器专用绝对路径另存不提交的本地绑定。

`utf8-lf` 只将 UTF-8 文本的 CRLF 规范为 LF，便于跨平台 Git 检出；不忽略空格、BOM 或其他内容改动。二进制用 bytes。源提交用于取回原件，输出哈希用于判断安装结果是否被改动，二者不能互相代替。

混合指引文件只登记受管区块：role 为 entry-block，并提供 `begin_marker` 和 `end_marker`。哈希内容包含标记在内，结束于结束标记末尾。检查器要求两个标记各出现一次；其他用户内容可自由维护。完整托管文件则对整个文件计算哈希。

检查器不能判断语义等效、更新是否发布、当前文件是否来自声明的仓库或远端是否最新，也不能发现未登记且在 managed_roots 之外的副本。记录来源须由安装者核验；不能用工具的 clean 替代源版本比较。个人范围可对单独明确的个人安装根运行，不把主目录作为整个项目的受管根。

旧流程生成的非标准记录先追溯原始来源和安装基线，再迁移；不以当前文件重算哈希清除未知差异。
