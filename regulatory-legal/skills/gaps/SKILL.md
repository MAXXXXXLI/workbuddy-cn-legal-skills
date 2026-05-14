---
name: gaps
description: >
  Open gaps tracker — what's flagged and not yet closed. Use when the user asks "what gaps
  are open", "gap tracker", "remediation status", or wants to close (--close GAP-ID) or
  risk-accept (--accept GAP-ID) a tracked gap. WorkBuddy
  中国语境适配：默认中国大陆法域，用于监管合规法务场景下的合规缺口台账。中文触发词包括：中国法、中国合规、监管合规法务、合规缺口台账、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**监管合规法务**；当前技能：**合规缺口台账**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /gaps

1. Read the gap tracker at `~/.workbuddy/skills/config/workbuddy-cn-legal/regulatory-legal/gap-tracker.yaml`.
2. If `--close`: mark gap closed with resolution note.
3. If `--accept`: record the risk-acceptance rationale and acceptor, status → risk-accepted.
4. Otherwise: report open gaps by age and materiality.

> Detailed tracker schema, status-report format, owner-notification logic (per-send confirmation, no exceptions), reminder cadence, the close/risk-accept modes, and the consequential-action gate live in the **gap-surfacer** reference skill — load it before doing substantive work.
