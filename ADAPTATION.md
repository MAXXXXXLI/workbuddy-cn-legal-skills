# 改编说明

本文件记录从上游 `claude-for-legal-main` 到 `workbuddy-cn-legal-main` 的主要转换范围，方便维护者和使用者判断本仓库适合什么用途。

## 转换原则

- 保留原始 Skills 的流程骨架和分模块组织方式。
- 不逐条重写全部法律分析内容，而是在每个 skill 顶部加入中国语境优先段。
- 通过全局 `references/china-legal-context.md` 和模块级 `references/china-context.md` 统一覆盖法域、引用、审查姿态和输出边界。
- 对高风险正式动作设置人工审阅门：对外发送、监管提交、诉讼/仲裁文件、董事会/股东会文件、劳动解除、数据出境判断等。

## 已转换内容

- `151` 个 `SKILL.md` frontmatter 和顶部说明。
- 根目录 `.workbuddy-plugin/marketplace.json`。
- 各模块 `.workbuddy-plugin/plugin.json`。
- 全局中国法律语境参考。
- 13 个模块级中国语境参考文件。
- 监管动态来源目录。
- `151` 个 source `SKILL.md` 的 `name` 改为中文显示名，并在 `description` 开头补充中文用途说明。
- `dist/workbuddy-skill-zips/` 下的 `151` 个 WorkBuddy 单 skill 直导 zip，每个 zip 顶层直接包含 `SKILL.md`。
- `scripts/package_workbuddy_skills.py`，用于批量同步中文名称并重新生成 WorkBuddy 直导 zip。
- `scripts/install_all_workbuddy_skills.sh`，用于一次性安装全部 skills 到 `~/.workbuddy/skills`。
- WorkBuddy v4.22.11 图形界面导入流程截图和 README 使用说明。

## WorkBuddy 实测记录

- 上传旧模块 zip 时，WorkBuddy 报错 `SKILL.md not found in zip archive`，说明 zip 顶层必须直接包含 `SKILL.md`。
- 上传 `dist/workbuddy-skill-zips/commercial-legal--nda-review.zip` 时，WorkBuddy 已通过 zip 结构校验并进入安全检测。
- 本次测试中，WorkBuddy 官方上传安全检测长时间停留在“安全检测中”；README 已记录本地目录安装兜底方式。
- 将 `commercial-legal--nda-review.zip` 解压至 `~/.workbuddy/skills/commercial-legal--nda-review` 并重启 WorkBuddy 后，可以在任务输入框的技能选择器中看到并选择该 skill。
- 执行 `scripts/install_all_workbuddy_skills.sh --force` 后，本地安装 `151` 个 skills；重启 WorkBuddy 后，技能选择器中可搜索到中文名称，例如 `商事合同法务-保密协议审查`。

## 仍需使用者按团队环境配置的内容

- WorkBuddy 官方上传安全检测或插件市场发布配置。
- 公司/律所/团队 playbook。
- 法律检索数据库和 MCP 连接器。
- 合同模板、DPA 模板、员工手册、会议纪要模板、诉讼/仲裁文书模板等。
- 审批人、升级规则、风险等级定义和输出格式。

## 适用边界

本仓库适合作为中国语境法务/合规 WorkBuddy Skills 的起点。它不是中国法律数据库，也不是执业律师替代品。对于具体法律问题，应检索并核验现行有效法律、行政法规、司法解释、监管规则、国家标准、地方规则和裁判规则。
