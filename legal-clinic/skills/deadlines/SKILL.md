---
name: "法律诊所/法律援助-期限管理"
description: >
  用于中国大陆法律诊所/法律援助场景下的期限管理。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Track case deadlines — add, cross-case rollup report, update, complete, close. Warns at
  configurable thresholds (default 14/7/3/1 days); overdue items stay flagged until
  resolved. The operational record for a clinic workload. Use when a student or supervisor
  needs to add a deadline, ask what's due this week, get a deadline report, or update a
  case deadline. WorkBuddy
  中国语境适配：默认中国大陆法域，用于法律诊所/法律援助场景下的期限管理。中文触发词包括：中国法、中国合规、法律诊所/法律援助、期限管理、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**法律诊所/法律援助**；当前技能：**期限管理**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /deadlines

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` → jurisdiction, practice areas, warning-day cadence.
2. Use the workflow below.
3. Route by flag:
   - `--add`: capture case, type, description, due date, source, owner. Write to `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/deadlines.yaml`. Check for duplicates first.
   - `--report` (default): cross-case rollup — overdue, next 3d, next 7d, next 14d; by owner; by practice area; unassigned flags.
   - `--update [id]`: modify fields; log note with date.
   - `--complete [id]`: mark done; confirm with student that work is actually filed/submitted.
   - `--close [id]`: close-without-completing; require rationale in notes.
4. Confirm any write before committing.

---

# Deadlines

## Purpose

A clinic's biggest operational risk is a missed deadline. Students carry multiple cases, work part-time, turn over every semester. Deadlines that live only in individual students' heads get dropped at handoff, get forgotten during finals week, get missed when a student unexpectedly withdraws from the clinic. This skill is the central operational record.

The supervising attorney is on the hook if a deadline is missed. The skill is calibrated to that stakes level — warnings fire early, overdue items stay visible until explicitly resolved, handoffs (via `/semester-handoff`) pull the deadline list forward to the next student.

## Load context

- `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` → jurisdiction, practice areas, deadline warning days (default 14/7/3/1), supervising attorneys
- `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/deadlines.yaml` — the ledger

**Jurisdiction assumption.** Deadline calculations and warning thresholds assume the jurisdiction set in CLAUDE.md. Deadlines, tolling rules, computation-of-time rules, and local court practices vary materially by jurisdiction and by specific court. If a matter involves a different state, a specific court's local rules, or a federal vs. state forum question, confirm the deadline against the governing rule with your supervisor before relying on it.

## Modes

Flag: `--add | --report | --update | --complete | --close` (default: report)

### `--add` — log a new deadline

**Inputs:**
- Case ID + name (which case)
- Practice area
- Type (filing / hearing / statute-of-limitations / discovery / cure-period / response / notice / other)
- Description — one line of what's due
- Due date (and time + timezone if applicable)
- Source — where the deadline came from (court order served 2026-04-20, statute 8 USC § 1229a, cure period in contract §7)
- Owner student — the student responsible

The skill generates an `id` slug automatically: `[case]-[short-desc]-[YYYY-MM]`.

**Extraction from other skills:** when `/client-intake`, `/draft`, or `/status` surface a deadline in their output, they should hand off to this skill with pre-populated fields. Student confirms and adds.

**Pre-add check:** if a deadline with the same case_id + type + due_date already exists, flag as likely duplicate and ask before adding.

**Plausibility sanity band.** After the student enters a due date, do NOT compute or verify — but apply a rough plausibility check against typical ranges for the filing type, and flag the student if the date falls far outside. This is scaffolding to catch gross errors in the student's own math, not an alternative to computing against the rule.

**Bands are jurisdiction-keyed.** Load the band file for this clinic's jurisdiction from `references/plausibility-bands/{state}.md` where `{state}` is the two-letter code from `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` → clinic jurisdiction (and federal always loads alongside). The legal-clinic plugin ships `references/plausibility-bands/CA.md` (fully populated) and `references/plausibility-bands/IL.md` (placeholder structure) as starting points.

**Hard stop at cold-start if the band file is missing.** If `references/plausibility-bands/{state}.md` does not exist for the clinic's jurisdiction, do NOT silently run without plausibility checks. At cold-start, tell the supervisor:

> "I don't have deadline plausibility checks for [state] — the sanity band for this clinic's jurisdiction isn't in the shipped reference files. I can still track deadlines (add, report, update, complete, close), but I cannot sanity-check them against typical ranges. Here's how to build the band file from your state's rules: copy `references/plausibility-bands/IL.md` as a template, fill in one row per deadline type your clinic sees most (typical range, triggering-event handling, computation-of-time rule, short cite), save at `references/plausibility-bands/{state}.md`, and re-run `/legal-clinic:deadlines`. Until then, every deadline I accept will carry `warnings: no-plausibility-band` and your review should treat dates as unchecked."

Do not fall back to the CA table for a non-CA clinic. The silent-degradation case — shipping a California sanity check to an Illinois clinic — is the failure this fix exists to close.

**Sanity check logic:**

1. Load the bands table for this clinic's jurisdiction from `references/plausibility-bands/{state}.md` (plus federal-always).
2. After the student enters `due:`, compare to triggering-event date + typical range for that `type:` (if a typical range exists in the loaded band file for the filing type).
3. If inside the range, write the entry. Say nothing — the band exists to catch errors, not to congratulate correct math.
4. If outside the range by a material margin, stop before writing and say:
   > The date you entered falls outside the typical range for [type] in [jurisdiction]. [Type] deadlines for [filing type] typically fall ~[range] after [triggering event]. Your entry: [date], which is [N] days from [triggering event]. Re-check your calculation against [cited rule from the band file] and the jurisdiction's computation-of-time rule. If your calculation is correct (local rule exception, atypical triggering event, tolling, waiver), confirm and I will add the entry as-is. Otherwise, recompute and re-run `/deadlines --add`.
5. If no band is known for this `type:` (unusual filing, non-standard deadline), do not sanity-check — write the entry and note in the `warnings:` field that no plausibility band applies.
6. If the band file is missing entirely for this jurisdiction, the hard stop above applies at cold-start; in steady-state (supervisor acknowledged the gap and proceeded), every entry is written with `warnings: no-plausibility-band`.

**The skill does not compute.** If the student enters `[VERIFY]` in the `due:` field because they haven't done the math yet, write the entry with `due: [VERIFY]` — the sanity band runs only when the student supplies a concrete date. The computation stays with the student and supervisor.

### `--report` (default) — cross-case rollup

Read `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/deadlines.yaml`. Produce:

```markdown
# Deadline Report — [today]

**Active deadlines:** [N]
**Overdue:** [N] ⚠️
**Due this week (next 7 days):** [N]

---

## ⚠️ Overdue (flagged for immediate attention)

| ID | Case | Type | Due | Owner | Days overdue |
|---|---|---|---|---|---|

## 🔴 Due today / next 3 days

| ID | Case | Type | Due | Owner |
|---|---|---|---|---|

## 🟡 Due in 4-7 days

| ID | Case | Type | Due | Owner |
|---|---|---|---|---|

## 🟢 Due in 8-14 days

[list]

## Beyond 14 days

[count only — expand with `/deadlines --report --horizon=30` for details]

---

## By owner student (workload distribution)

| Student | Overdue | Next 7d | Next 14d | Total active |
|---|---|---|---|---|

## By practice area

[same table, grouped by area]

## Unassigned deadlines

[list — flag if any active deadline has no owner_student]
```

### `--update` — modify an existing deadline

Common updates: due date changed (court continuance), owner changed (reassignment), notes added.

Every update writes a dated note inline; history is visible in the entry.

### `--complete` — mark done

- Sets `status: completed`, `completed_date: [today]`.
- Confirms with the student that the actual work is done and filed/submitted.
- Removes from active reports but stays in the yaml.

### `--close` — close without completing

For deadlines that no longer apply — case settled, motion withdrawn, client dropped the matter. Requires a `notes:` entry explaining why.

## Warning cadence

Per `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` deadline warning days. Default 14, 7, 3, 1.

Warnings don't auto-surface — this plugin has no scheduled/agent behavior. But any time `/deadlines` is invoked (or `/status`, which routes to this skill for deadline checks), the report pulls forward anything hitting a warning threshold.

If a deadline passes its due date without being marked complete, it moves to `status: overdue` and stays there in every report until explicitly resolved. Overdue deadlines do not auto-close.

## Integration

- **`/client-intake`:** when intake surfaces a timeline urgency (eviction notice date, asylum filing deadline, hearing date), offer to `/deadlines --add` with pre-populated fields.
- **`/draft`:** when a filing draft references a deadline (answer due, objection window), offer to add.
- **`/status`:** the status skill reads `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/deadlines.yaml` for the relevant case and includes upcoming deadlines in its output.
- **`/semester-handoff`:** reads deadlines.yaml to identify all active deadlines across departing-student cases; each handoff memo carries the deadlines forward.
- **`/supervisor-review-queue` (if formal review enabled):** deadlines near their cutoff get priority in the review queue.

## What this skill does not do

- **Calculate deadlines from triggering events.** If a complaint was served today and the answer is due in 21 days per local rules, the skill doesn't do that math — the student does, using the rule, and logs the resulting date. (Doing the math autonomously creates a liability the skill shouldn't own; rules vary by jurisdiction and court.)
- **File or serve anything.** The skill tracks dates; filing happens outside the plugin.
- **Auto-notify.** No scheduled notifications. The report surfaces warnings when invoked; it doesn't push. A scheduled cron could be added later but would need explicit professor opt-in per clinic.
- **Override local rules.** If the student logs a due date that contradicts local rules, the skill doesn't catch it. Another reason to calendar with `[VERIFY: confirm against local rule]` for any non-routine deadline.
