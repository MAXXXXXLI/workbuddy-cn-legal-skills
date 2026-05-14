---
name: "技能治理中心-停用技能"
description: >
  用于中国大陆技能治理中心场景下的停用技能。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**技能治理中心**；当前技能：**停用技能**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /disable

Run the `disable` workflow from the skill-manager reference skill against the
named skill.

What disable does:

- Renames the skill's `SKILL.md` to `SKILL.md.disabled` so WorkBuddy no longer
  discovers it as an active skill. Files, references, templates, and config
  stay in place.
- If the skill ships hooks in `hooks/hooks.json`, also rename that file to
  `hooks.json.disabled` so no automatic triggers fire while the skill is
  disabled.
- Logs the action to
  `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-builder-hub/install-log.yaml`.

Safety rules:

1. **Only disable community skills installed through this hub.** Same check
   as uninstall — consult the install log and CLAUDE.md installed table.
2. **Never disable a first-party plugin's skill.** Off-limits.
3. **Confirm before renaming.** Show the paths, get explicit `yes`.

Re-enable by running the command again with the same skill name — the
skill-manager workflow recognizes a disabled skill and flips the rename back.

> Detailed uninstall, disable, and re-enable workflows live in the
> `skill-manager` reference skill — load it before doing substantive work.
