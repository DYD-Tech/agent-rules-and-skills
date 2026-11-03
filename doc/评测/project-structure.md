# project-structure 首次验证

日期：2026-11-03。作者试用，不是独立模型评测。

## 隔离试用

输入：虚构已有项目含用户旧计划“仅导出 CSV”、另一 agent 的草稿；当前任务明确改为 JSON。要求整理本任务说明与临时探查输出，不整理全库，不修改原件。

实际输出：

- 临时探查结果放 agent-workspace/current-task/probe.txt。
- 当前说明放 doc/架构-功能-实现/export.md，内容为“Current task specifies JSON export. The earlier CSV-only plan is historical input, not an active restriction. Implementation and tests have not been verified.”
- 调研说明放 doc/调研/export-options.md，文档导航为 doc/README.md。
- 旧计划和其他 agent 草稿的 SHA256 前后相同；doc 根只有 README.md。没有给旧计划加状态或重新执行旧计划。

试用由作者在已读取技能后执行，隔离夹具位于仓库已忽略的 agent-workspace 下；为测试创建的模拟输入不代表允许 agent 在真实用户输入目录里写文件。该试用只证明本次操作结果，不证明跨模型遵循效果。

## 静态与 Git 验证

154 个本地链接、代码围栏、doc 根目录、五模块清单路径、原备份哈希检查通过。git check-ignore 确认 /agent-workspace/ 与 /ref/ 忽略项生效，git ls-files 两处为空，未取消任何已有文件跟踪。git diff --check 通过。

技能专用 quick_validate.py 因当前 Python 缺少 PyYAML 无法运行；未声称完整 YAML 验证通过。未执行真实项目批量迁移、跨宿主安装或独立模型评测，未测量 token 或耗时收益。


## 目录语言修正

作者按修订指令进行命名试用：

- 输入“新建英文项目的架构总览和日志”：输出位置 doc/architecture-features-implementation/00-overview.md 与 doc/development-log/CHANGELOG.md。
- 输入“新建中文项目的架构总览和日志”：输出位置 doc/架构-功能-实现/00-总览与分层.md 与 doc/开发日志/CHANGELOG.md。
- 输入“已有 doc/开发日志，现在用英文回答”：保留原目录，仅输出语言改变，不新建英文副本。
- tasks-and-prompt 与通用根路径保持原名，原始输入保护不因语言变化放宽。

这些是作者命名输出，不是跨模型或真实项目迁移测试。文档链接检查通过，未重命名本仓库已有目录。


## 目录即文档：作者路径选择试用

输入：中文项目已有 doc/调研/，当前任务产生支付方案比较、临时接口探查脚本、长期维护的验证工具；还有首份需要用户保留的验收报告，没有验收目录。只给放置结果，不整理旧文件。

本次按规则给出的实际路径：

- 方案比较：doc/调研/支付方案比较.md，复用已有用途分类。
- 探查脚本：agent-workspace/支付接口探查/probe.py，作为临时工作材料。
- 维护工具：tools/validate_payment.py，承担可复用工具职责。
- 验收报告：doc/验收/支付验收报告.md，新分类承担独立长期用途；有一份文件也可建立，不为每份报告再套目录。将入口补到 doc/README.md 的验收分类。

这些是作者实际给出的路径选择，没有在真实项目创建这些样例文件，不是独立模型测试。结果没有把同一任务的全部产物堆在同一文件夹，没有使用根目录杂项，也未改写只读原件或整理无关旧内容。


## README 必要性：作者判断样例

- 新增 doc/调研/支付方案/，文件名已经清楚且总导航可达：不新增 README。
- 一组操作文档必须按备份、迁移、验证顺序执行，现有入口没有说明：在最合适的入口补充顺序；仅当局部入口确有必要时新建 README，不每层都建。
- tasks-and-prompt 内文件多且不易理解：不写 README，遵守用户原件目录只读边界。

这是作者按修订指令给出的判断，不是独立模型测试或真实目录清理。
