---
name: "争议解决法务-案件/事项简报"
description: >
  用于中国大陆争议解决法务场景下的案件/事项简报。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**争议解决法务**；当前技能：**案件/事项简报**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /matter-briefing

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` → risk calibration + relevant stakeholders.
2. Follow the workflow and reference below.
3. Read `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/[slug]/matter.md` + `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/[slug]/history.md` + log row from `_log.yaml`.
4. Produce briefing: current posture, what's changed since last update, next deadline, open questions, risk re-assessment check ("does the `risk:` field still reflect reality?").
5. Flag staleness: if `last_updated` > 30 days, say so.

---

# Matter Briefing

## Purpose

Give the counsel a clean read on one matter in the time it takes to walk to a conference room. Current posture, what's changed, what's next, what's worth reconsidering.

## Load context

- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml` — structured row
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/[slug]/matter.md` — narrative intake
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/[slug]/history.md` — event log
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` — risk calibration (so "risk: high" means something specific, not generic)

**Conflicts gate — unbypassable.** Before briefing, check `_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't build a briefing on a matter that hasn't been intaken — the conflicts check is the gate."

## Input

Slug (required). If ambiguous or missing, ask the user to pick from a list of active matters.

## The briefing

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# [Matter Name] — Briefing as of [today]

**Status:** [status / stage]
**Risk:** [rating] ([severity] × [likelihood])
**Materiality:** [category]
**Outside counsel:** [firm — lead]
**Last updated:** [date] [flag ⚠️ STALE if >30d]
**Conflicts:** [status — flag ⚠️ if `pending` or `not-run`]

---

## One-paragraph summary

[Current posture. What are we doing and why. Name the pivot fact if one is captured.]

## What's changed recently

[Last 3-5 entries from history.md, most recent first. If history is thin, say so.]

## What's next

- **Immediate deadline:** [next_deadline + what it is]
- **Upcoming milestones:** [anything dated in matter.md or recent history]
- **Decisions pending:** [open questions flagged in matter.md]

## Exposure

[Range + any change since intake. If reserved, current reserve + whether recalibration is overdue.]

## Internal owners

[Who's looped in; whether anyone should be looped in and isn't]

## Risk re-assessment check

*A prompt, not an answer.*

- Does `risk: [rating]` still feel right, or has the case moved?
- Does `materiality: [category]` still match? (New facts might push toward reserve or disclosure.)
- Any new stakeholder the matter needs (e.g., CISO becomes relevant after a discovery development)?

## Open questions

[From matter.md and anything unresolved in history]

## For the conversation

[If user specified a purpose — "brief me before the call with outside counsel" — tailor the final section: questions to ask, decisions to get, updates to extract. If no purpose given, omit this section.]
```

## Staleness

If `last_updated > 30 days ago`: flag at the top AND suggest running `/litigation-legal:matter-update [slug]` after the meeting to capture whatever's discussed.

## Tone

This is not marketing. Say what's known; flag what's not. If a matter has thin history and was just opened, the briefing is short — and that's correct. Don't pad.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- Predict outcomes. Risk rating is a captured judgment, not a forecast.
- Recommend strategy. Surfaces questions; the counsel answers them.
- Re-triage. If the user wants to re-triage, that's an `/matter-update` with field changes — this skill reads, doesn't write.
