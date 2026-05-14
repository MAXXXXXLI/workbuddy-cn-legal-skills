# WorkBuddy 中国法务技能包

这是从 `claude-for-legal-main` 转换出的中国语境适配副本，供 WorkBuddy 使用。原始目录未被修改。

## 转换内容

- 151 个 `SKILL.md` 均保留原始工作流骨架，并在 frontmatter 中加入中文触发语境。
- 每个 skill 顶部加入 `WorkBuddy 中国语境适配（优先）`，覆盖原模板中的美国法、Delaware、ABA、CourtListener、DMCA、deposition、subpoena、attorney work product 等默认项。
- 根目录新增 `references/china-legal-context.md`，每个业务模块新增 `references/china-context.md`。
- 平台路径从 `~/.claude/plugins/config/claude-for-legal` 改为 `~/.workbuddy/skills/config/workbuddy-cn-legal`。
- 增加 `.workbuddy-plugin/marketplace.json` 和每个模块的 `.workbuddy-plugin/plugin.json`，保留 `.claude-plugin` 结构以便对照。

## 使用建议

1. 先在 WorkBuddy 中导入需要的模块，不必一次启用全部模块。
2. 对每个模块先运行或模拟 `cold-start-interview`，把公司情况、审查口径、审批人、资料库和输出格式补齐。
3. 对会引用法律/案例/监管规则的任务，连接官方来源或授权数据库；否则输出会标注 `[需核验]`。
4. 对外发送、提交监管、诉讼/仲裁文件、董事会/股东会文件、劳动解除决定、数据出境判断等，都必须由执业律师或公司法务负责人审阅。

## 目录说明

- `references/china-legal-context.md`：全局中国法域总则。
- `<plugin>/references/china-context.md`：模块级中国化参考。
- `<plugin>/skills/*/SKILL.md`：WorkBuddy 可读的技能说明和流程。

