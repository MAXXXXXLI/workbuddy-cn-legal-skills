---
name: "公司与交易法务-交易团队摘要"
description: >
  用于中国大陆公司与交易法务场景下的交易团队摘要。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**公司与交易法务**；当前技能：**交易团队摘要**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# Deal Team Summary

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The deal lead doesn't read 200 findings. They read: what's material, what changed since last brief, what needs a decision. This skill compresses the diligence output to the right level for the reader.

## Load context

- `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/CLAUDE.md` → Deal team briefing (cadence, format, what the business reads)
- `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/deals/[code]/deal-context.md` → deal lead, timeline
- Current findings from diligence-issue-extraction output

## Audience tiers

Per `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/CLAUDE.md` — what the business reads vs. what's for the file. Default tiers:

| Audience | Gets | Doesn't get |
|---|---|---|
| **Board / exec sponsor** | Top 3-5 material issues, price/structure impact, decision items | Category detail, green findings, process |
| **Deal lead** | All reds, all yellows, progress, decision items, next steps | Green finding detail |
| **Working team** | Everything — full findings, status by category, gaps | Nothing withheld |

Ask which tier if not obvious.

## The summary

### Exec tier

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> This brief aggregates privileged diligence findings and inherits the sources' privilege and confidentiality status. Distribution beyond the privilege circle (including to broader business teams) can waive privilege — confirm the distribution list matches the privilege circle before sending.

# [Deal code] — Diligence Brief — [date]

**Status:** [On track / Issues identified / Material findings]
**Coverage:** [X]% of VDR reviewed

## Material findings

[3-5 max. One paragraph each. What it is, why it matters to the deal, what
we're doing about it.]

## Decisions needed

- [ ] [Specific decision — price adjustment, indemnity ask, walk-away trigger]
  — [who decides] — [by when]

## Since last brief

[What changed. New findings, findings resolved, coverage progress.]
```

### Deal lead tier

Same as above plus:

```markdown
## All open issues by category

### 🔴 Red
[Finding title + one-line — link to full finding for detail]

### 🟡 Yellow
[same]

## Progress

| Category | Docs reviewed | Coverage | Reds | Yellows | Status |
|---|---|---|---|---|---|
| [name] | [N/M] | [%] | [N] | [N] | [Complete / In progress / Blocked] |

## Gaps and follow-ups

- [Supplemental request items outstanding]
- [Questions to management]

## Next 72 hours

[What's getting reviewed, what briefings are scheduled]
```

### Working team tier

Full finding detail. Same structure as above but every finding gets its full house-format block, not a one-liner.

## Deltas

If this is a recurring brief (per `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/CLAUDE.md` cadence), lead with what changed:

- New findings since last brief
- Findings upgraded/downgraded in severity
- Findings resolved (consent obtained, issue clarified away)
- Coverage movement

Deal leads care more about movement than state. "Still 12 yellows" is less useful than "2 new yellows, 3 resolved."

## Handoffs

- **From diligence-issue-extraction:** This skill reads the accumulated findings.
- **To closing-checklist:** Any "decision needed" items that resolve into closing conditions go on the checklist.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't make the materiality call — it reports the calls that were made at extraction time.
- It doesn't decide what the deal team does about a finding — it surfaces the decision.
- It doesn't distribute the brief — drafts it, human sends.
