---
name: "技能治理中心-卸载技能"
description: >
  用于中国大陆技能治理中心场景下的卸载技能。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**技能治理中心**；当前技能：**卸载技能**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /uninstall

Run the `uninstall` workflow from the skill-manager reference skill against
the named skill.

Safety rules:

1. **Only uninstall community skills installed through this hub.** Check
   `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-builder-hub/install-log.yaml`
   and the CLAUDE.md installed starter pack table. If the skill is not recorded
   there, refuse and tell the user.
2. **Never uninstall a first-party plugin's skill.** The 12 core plugins that
   ship with workbuddy-cn-legal are off-limits from this command. If the named
   skill resolves to a path inside one of those plugins, refuse.
3. **Confirm before removing files.** Show the user every path that will be
   deleted. Proceed only on explicit `yes`.
4. **Log the uninstall.** Append to `install-log.yaml` with action `uninstall`
   and timestamp so the audit trail is intact.

If the user wants to stop a skill from running but keep the files (e.g., for
later re-enable, or to preserve configuration), suggest `/legal-builder-hub:disable`
instead.

> Detailed uninstall, disable, and re-enable workflows live in the
> `skill-manager` reference skill — load it before doing substantive work.
