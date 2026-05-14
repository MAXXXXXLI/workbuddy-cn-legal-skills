---
name: "监管合规法务-征求意见跟踪"
description: >
  用于中国大陆监管合规法务场景下的征求意见跟踪。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**监管合规法务**；当前技能：**征求意见跟踪**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /comments

## Purpose

征求意见稿/公开征求意见s have deadlines. The decision to file a comment or not is an attorney
call — but the deadline disappearing without a logged decision is the risk.
This skill surfaces open comment periods and records decisions.

## Load context

`~/.workbuddy/skills/config/workbuddy-cn-legal/regulatory-legal/comment-tracker.yaml` → all tracked 征求意见稿/公开征求意见s and their status.
`~/.workbuddy/skills/config/workbuddy-cn-legal/regulatory-legal/CLAUDE.md` → default comment decision owner.

## Default view — open comment periods

```markdown
## Comment Period Tracker — [date]

### ⏰ Deadline in <14 days

| ID | Regulation | Deadline | Days left | Decision | Owner |
|---|---|---|---|---|---|
| CMT-001 | [name] | [date] | [N] | Undecided | [owner] |

### 🟡 Open (>14 days)

[same table]

### Recently decided

| ID | Regulation | Decision | Rationale |
|---|---|---|---|
| CMT-002 | [name] | Not filing | [reason] |

---

**Total open:** [N]  **Undecided with deadline <30 days:** [N]
```

## Log a decision

```
/regulatory-legal:comments --decide CMT-001
Decision: [filing / not-filing / waived]
Rationale: "[brief — e.g., 'Rule doesn't apply to our model' or 'Filing comment on Section 3']"
```

Updates tracker. If decision is "filing": prompt for filing deadline reminder
(comment deadline minus 5 business days for internal review).

## Notifications

On first detection of an 征求意见稿/公开征求意见 (populated by reg-feed-watcher): 企业微信/飞书/钉钉 DM to
comment decision owner if 企业微信/飞书/钉钉 MCP is configured and `owner_slack` is set.

Reminder at 14 days before deadline if decision is still "undecided."
Reminder at 3 days before deadline if still undecided — elevated urgency.

## Consequential-action gate (submit a regulatory comment / respond to a regulator)

**Before logging a decision as "filing" — and always before producing a comment letter or regulator-response draft for submission:** Read `## Who's using this` in ~/.workbuddy/skills/config/workbuddy-cn-legal/regulatory-legal/CLAUDE.md. If the Role is **Non-lawyer**:

> Submitting a comment or response to a regulator has legal consequences. It's a public statement of the company's position, it's on the record in the rulemaking or enforcement matter, and positions taken here bind the company and can be used against it in subsequent proceedings. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - The rulemaking or inquiry (regulator, docket, deadline)
> - What the proposed comment/response says and on what sections
> - Open questions and what's unresolved
> - What could go wrong (adverse admissions, inconsistent prior positions, coordination-of-comment concerns with trade associations)
> - What to ask the attorney (should we file at all; should we file jointly through a trade group; are there positions we should not take)
>
> If you need to find a lawyer: your professional regulator's referral service is the fastest starting point (司法行政机关/律师协会 in the US; SRA/Bar Standards Board in England & Wales; Law Society in Scotland/NI/Ireland/Canada/Australia; or your jurisdiction's equivalent).

Do not log a "filing" decision or produce a submission-ready draft past this gate without an explicit yes. Tracking views, deadline reminders, and "not-filing / waived" decisions do not require the gate.

---

## What this skill does not do

- Draft the comment letter. That is a separate attorney task.
- Make the filing decision. It tracks the decision; the attorney makes it.
- Monitor post-comment activity. Once a decision is filed, this tracker's job
  is done — follow the rulemaking through `/regulatory-legal:reg-feed-watcher`.

> The `comment-decision` `gap_type` semantics, the per-send 企业微信/飞书/钉钉 confirmation rule, and the comment-tracker.yaml schema live in the **gap-surfacer** reference skill — load it before doing substantive work.
