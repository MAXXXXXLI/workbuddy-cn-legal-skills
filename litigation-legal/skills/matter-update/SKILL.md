---
name: matter-update
description: >
  Append a dated event to a matter's history file and refresh the log row — captures new
  developments, status changes, risk re-assessments, deadline shifts, and settlement
  authority changes. Use when the user wants to log an update on a matter, note a
  development, or record a status change against the portfolio. WorkBuddy
  中国语境适配：默认中国大陆法域，用于争议解决法务场景下的事项更新。中文触发词包括：中国法、中国合规、争议解决法务、事项更新、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**争议解决法务**；当前技能：**事项更新**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /matter-update

1. Follow the workflow and reference below.
2. Confirm slug exists in `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/` and `_log.yaml`.
3. Prompt for event type, date (default today), summary, and any log field updates (risk change, status change, next deadline shift, materiality reclassification).
4. Append dated entry to `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/[slug]/history.md`.
5. Update `_log.yaml` — set `last_updated` to today, apply any field updates.
6. Confirm.

---

# Matter Update

## Purpose

The portfolio only stays useful if it stays current. This skill makes logging an update cheap — two minutes of structured capture, no freeform drift.

## Load context

- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml` — find the row
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/[slug]/history.md` — append target
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/[slug]/matter.md` — reference (don't rewrite)
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` — risk calibration (if re-assessing risk)

**Conflicts gate — unbypassable.** Before logging an update, check `_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace exists. I won't append history to an unmanaged matter — the conflicts check is the gate, and there's no `history.md` to append to until the matter is intaken."

## Input

Slug (required). If not provided, ask — with a short list of recently updated matters to pick from.

## The update

### 1. Event type

Offer categories:

- **Procedural** — motion filed/received, order issued, hearing held, deadline set
- **Discovery** — production made/received, 庭审询问/调查取证s taken, 法院/仲裁机构调查取证或协助调查文件 served
- **Substantive** — new facts, key document surfaced, ruling on merits
- **Strategy** — posture shift, settlement offer made/received, authority update
- **Risk re-assessment** — severity or likelihood changed
- **Stakeholder** — new person looped in, outside counsel change
- **Administrative** — engagement letter executed, budget adjusted, hold refreshed

Or freeform if none fits.

### 2. Date

Default today. Accept an override (e.g., capturing an event from last week).

### 3. Summary

One-paragraph narrative. What happened, what it means, any immediate implication.

### 4. Log field changes

Walk through potentially affected fields:

- `status:` — has the stage shifted (e.g., pleadings → fact discovery)?
- `stage:` — substage update
- `risk:` — reassessment required?
- `materiality:` — any change (new facts might trigger reserve or disclosure)?
- `exposure_range:` — revise if new information
- `next_deadline:` — new upcoming date, if any
- `outside_counsel:` — change?
- `internal_owners:` — anyone new or removed?
- `legal_hold:` — refreshed, expanded, released?

Only prompt for fields likely affected by the event type. Procedural updates usually touch `stage` and `next_deadline` only; a settlement offer might touch `materiality`, `exposure_range`, `status`.

### 4pre. Settlement-acceptance gate

If the Strategy update is a **settlement acceptance** (the company is accepting a settlement offer, executing a settlement agreement, or authorizing acceptance in principle — not merely logging an offer made or received): Read `## Who's using this` in `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md`. If the Role is Non-lawyer:

> Accepting a settlement has legal consequences — it resolves claims, typically requires a release, and can affect insurance, tax, and related matters. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the matter, proposed settlement terms (dollar, structural, release scope, confidentiality, non-disparagement), exposure at stake, authority ladder status (see `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` settlement authority), what could go wrong, what to ask the attorney before accepting.]
>
> If you need to find a 执业律师/法务负责人, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (司法行政机关/律师协会 in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

Do not log the acceptance or flip materiality on acceptance basis without an explicit yes. Logging offers or counters does not require the gate — acceptance does.

### 4a. Materiality trigger — explicit prompt

Certain event types force a materiality re-check. When the event type is in this list, **always prompt** — don't let the user move on without an explicit answer:

| Event type | Materiality trigger prompt |
|---|---|
| Substantive (new facts, key document, merits ruling) | "This event is substantive. Does it push `materiality`? Current: `[current]`. Options: `reserved / disclosed / monitored / none`. Change?" |
| Strategy (posture shift, settlement offer made or received) | "Settlement activity often triggers materiality reclassification. Current: `[current]`. If the offer, counter, or acceptance moves exposure or shifts from contested to probable-and-estimable, reclassify." |
| Risk re-assessment (severity or likelihood changed) | "Risk moved. Materiality should track. Current: `[current]`. Reclassify?" |
| Regulatory / enforcement development | "Regulator action (法院/仲裁机构调查取证或协助调查文件, CID, enforcement notice) usually triggers disclosure analysis. Current: `[current]`. Change?" |

Acceptable answers include `no change` — but `no change` must be explicit, not implied by silence. Capture in the history entry:

```markdown
**Materiality check:** [no change / changed from X to Y]
**Reasoning:** [one sentence]
```

If materiality moves to `reserved` or `disclosed`, and the matter did not previously carry a reserve or disclosure, flag the event as requiring finance / audit-committee notification per `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` materiality thresholds.

### 5. Seed doc prompt (optional)

If the update references a document (order, filing, correspondence), ask if there's a path to link. Not pushy.

## Writing

### Append to `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/[slug]/history.md`

Most recent at top, directly under the `---` that follows the header.

```markdown
## [YYYY-MM-DD] — [Event type]: [short title]

[Paragraph summary.]

**Fields changed:**
- [field]: [old → new]
- [field]: [old → new]

**Related doc:** [path, if provided]
```

If no fields changed, omit the "Fields changed" block.

### Update `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml`

- Apply any field changes.
- Set `last_updated: [today]` (or the event date if the user overrode — the log tracks when the record was last touched).

## Confirm

Show the user the history entry and the yaml diff before writing:

> Here's what I'll append and update. Good to commit?

## What this skill does not do

- Edit past history entries. Corrections are new entries that reference and correct prior ones.
- Silently change the log. Every field change is shown to the user before write.
- Decide whether a new development warrants reserve/disclosure. It surfaces the question ("this might push materiality — want to reclassify?"), the user answers.
