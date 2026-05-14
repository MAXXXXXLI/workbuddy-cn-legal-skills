---
name: review-proposals
description: >
  Review and approve (or reject) pending playbook update proposals from the
  playbook-monitor agent and apply approved changes to the practice profile. Use when the
  playbook-monitor agent has surfaced proposals, when the user says "review playbook
  proposals", "what playbook updates are pending", or wants to step through
  deviation-driven playbook changes. WorkBuddy
  中国语境适配：默认中国大陆法域，用于商事合同法务场景下的审查意见管理。中文触发词包括：中国法、中国合规、商事合同法务、审查意见管理、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**商事合同法务**；当前技能：**审查意见管理**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /review-proposals

Steps through pending playbook update proposals from the monitor agent and applies approved changes to `~/.workbuddy/skills/config/workbuddy-cn-legal/commercial-legal/CLAUDE.md`.

## Instructions

1. **Load the playbook-monitor agent** and run Step 5 (review and approval flow).

2. **If no proposals file exists** or it is empty: respond *"No pending proposals. Playbook is up to date."* Do not proceed further.

3. **Present proposals one at a time.** For each, show the full proposal block and offer four options: Accept, Reject, Edit, Defer.

4. **For Accept or Edit:** show the exact diff to `~/.workbuddy/skills/config/workbuddy-cn-legal/commercial-legal/CLAUDE.md` before writing. Only apply after the attorney explicitly confirms.

5. **For Reject or Defer:** log the decision. Do not modify `~/.workbuddy/skills/config/workbuddy-cn-legal/commercial-legal/CLAUDE.md`.

6. **After all proposals are resolved:** show a summary of what changed, then archive the proposals file.

## Examples

```
/commercial-legal:review-proposals
```

```
/commercial-legal:review-proposals
(runs automatically after playbook-monitor notifies you)
```
