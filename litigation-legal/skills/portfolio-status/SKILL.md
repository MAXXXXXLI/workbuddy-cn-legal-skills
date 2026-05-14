---
name: portfolio-status
description: >
  Roll up the portfolio from _log.yaml — risk distribution, upcoming deadlines, stale
  matters, materiality totals, stage distribution, and flagged anomalies. Use when the
  user asks "where do we stand", "how many open matters", or wants a portfolio rollup or
  status across all active matters. WorkBuddy
  中国语境适配：默认中国大陆法域，用于争议解决法务场景下的争议组合状态。中文触发词包括：中国法、中国合规、争议解决法务、争议组合状态、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**争议解决法务**；当前技能：**争议组合状态**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /portfolio-status

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` → risk calibration (defines how to read the `risk:` field).
2. Follow the workflow and reference below.
3. Parse `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml`. Filter closed matters by default (include with `--all`).
4. Produce rollup: risk distribution, deadlines in next 14/30/60 days, matters with no update in >30 days, materiality totals, stage distribution.
5. Flag anomalies — everything marked critical, overdue next_deadline, matters without outside counsel assigned where risk is medium or high.

---

# Portfolio Status

## Purpose

One read that answers: what do I own right now, what needs attention, and what's slipping? Output is scannable — designed for a counsel who has three minutes before their next call.

## Load context

- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml` — source of truth
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` — risk calibration (to interpret risk/materiality fields correctly)

## Flags & filters

Default: active matters only (exclude `status: closed`).

Flags:
- `--all` — include closed
- `--risk=high` (or `critical` / `medium` / `low`) — filter by risk band
- `--stale` — only matters with `last_updated` > 30 days
- `--type=employment` — filter by matter type
- `--owner=[name]` — filter by business/HR/comms owner

## The rollup

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# Portfolio Status — [today]

**Active matters:** [N]
**Closed (ytd):** [N] *(shown only with --all)*

---

## By risk

| Risk | Count | Matters |
|---|---|---|
| Critical | [N] | [slugs] |
| High | [N] | [slugs] |
| Medium | [N] | [count only — expand with `--risk=medium`] |
| Low | [N] | [count only] |

## Upcoming deadlines

| Within | Matters |
|---|---|
| 14 days | [slug — deadline — brief] |
| 15–30 days | [...] |
| 31–60 days | [...] |

*Overdue `next_deadline` flagged separately below.*

## Materiality

| Category | Count | Total exposure (midpoint) |
|---|---|---|
| Reserved | [N] | [$X] |
| Disclosed | [N] | [$X] |
| Monitored | [N] | — |
| None | [N] | — |

## By stage

[table: pleadings / discovery / dispositive motions / trial prep / settlement / appeal]

---

## ⚠️ Anomalies & flags

- **Overdue deadlines:** [list slugs where next_deadline has passed]
- **Stale (>30d no update):** [list]
- **Conflicts unresolved:** [list slugs with `conflicts.status in [pending, not-run]`]
- **Conflicts bypassed (override active):** [list slugs where `conflicts.override.by` is populated — permanent flag until manually cleared]
- **High/critical risk without outside counsel:** [list]
- **Reserved without last_updated in >60d:** [list] — reserve recalibration likely overdue
- **Hold not issued on active litigation:** [list]
- **Missing fields:** [slug → field]

---

## Closing advice

[One or two sentences on what to look at first, if anything stands out. Not boilerplate — only if something truly stands out.]
```

## Anomaly rules

These are the checks that make the skill useful rather than decorative:

1. **Overdue deadline:** `next_deadline < today` and `status != closed`
2. **Stale:** `last_updated < today - 30d` and `status != closed`
3. **Conflicts unresolved:** `conflicts.status in [pending, not-run]` and `status != closed`
3b. **Conflicts override active:** `conflicts.override.by != null` (never auto-clears)
4. **High-risk uncovered:** `risk in [high, critical]` and `outside_counsel.firm == null`
5. **Stale reserve:** `materiality == reserved` and `last_updated < today - 60d`
6. **Hold gap:** `status in [threatened, active, discovery, trial, appeal]` and `legal_hold.issued == false` — preservation duty attaches at reasonable anticipation, so `threatened` matters are in scope.
7. **Missing fields:** any required field null — `risk`, `materiality`, `status`, `opened`, `conflicts.status`

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

If the portfolio has more than ~10 matters, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer for this output — counts by risk tier, a timeline of upcoming deadlines, and a sortable matter ledger with status, conflicts check, and last-touched date.

## What this skill does not do

- Make decisions. It surfaces what needs attention; the user decides priority.
- Pretend precision it doesn't have. Exposure midpoints are rough and should be labeled so.
- Replace a real MMS. This is a working-memory rollup, not a system of record.
