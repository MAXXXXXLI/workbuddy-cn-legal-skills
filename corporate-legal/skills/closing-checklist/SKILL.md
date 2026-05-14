---
name: closing-checklist
description: >
  What's blocking close — maintain the closing checklist with status, critical path, and
  days to close. Self-updating: ingests new items from diligence findings and schedule
  builds, tracks status, surfaces what's blocking. Use when user says "closing checklist",
  "what's left to close", "checklist status", "add to the checklist", or on a scheduled
  status pull. WorkBuddy
  中国语境适配：默认中国大陆法域，用于公司与交易法务场景下的交割清单。中文触发词包括：中国法、中国合规、公司与交易法务、交割清单、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**公司与交易法务**；当前技能：**交割清单**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /closing-checklist

1. Read `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/deals/[code]/closing-checklist.yaml` and use the modes below.
2. If status update provided: Mode 3 (update item).
3. Otherwise Mode 4: blocking items, critical path, days to close.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Deals close when the checklist is done. Everything on it, done. Nothing missing. This skill maintains the list, ingests new items as they surface from diligence, and tells the team what's blocking.

## The checklist

Lives at `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/deals/[code]/closing-checklist.yaml`. Structure:

```yaml
deal_code: "Project Falcon"
target_close: [DATE]
signing_date: [DATE]
last_updated: [DATE]

conditions_precedent:
  - id: CP-001
    item: "HSR waiting period expiration"
    category: "Regulatory"
    responsible: "Buyer counsel"
    due: 2026-04-15
    status: "Filed 2026-03-01, waiting period runs"
    blocking: true
    source: "Purchase Agreement §7.1(a)"

  - id: CP-002
    item: "Acme Corp consent to assignment"
    category: "Third-party consents"
    responsible: "Target — Jane Doe"
    due: 2026-04-20
    status: "Request sent 2026-03-10, no response"
    blocking: true
    source: "Schedule 3.12(a)(4); Acme MSA §14.2"

closing_deliverables:
  - id: CD-001
    item: "Certificate of good standing — Target (DE)"
    category: "Corporate"
    responsible: "Target counsel"
    due: 2026-04-28
    status: "Not started"
    blocking: true
    source: "Purchase Agreement §2.3(b)(iv)"

  # ... etc
```

## Modes

### Mode 1: Initialize from the purchase agreement

Read the signed (or near-final) purchase agreement. Extract:

- Every condition precedent (location varies by agreement — read the actual section headings)
- Every closing deliverable (closing deliverables schedule or corresponding section)
- Every covenant with a pre-closing deadline

Each becomes a checklist item with a source cite to the agreement section.

**Research obligations before populating regulatory/approval items.** Antitrust, foreign-investment, and sector-specific approvals (for example, HSR-style filings, CFIUS, industry regulators) have jurisdiction-specific mechanics, thresholds, and timing windows that change. Extract the name of each regulatory condition from the PA, then research the currently operative mechanics (who files, when, what triggers a second request, what the waiting period is). Cite primary sources and verify currency. Do not populate a timing assumption from memory.

**Material-adverse-effect / material-adverse-change closing conditions.** Pull the defined term from the PA — MAC/MAE framing is negotiated, not a standard. Research the governing-law interpretation of the specific language used (公司注册地/章程约定地（中国公司须按《公司法》和章程核验）, New York, and other jurisdictions treat carve-outs and quantitative tests differently) before flagging an event as a potential MAC trigger.

**Consent-requirement extraction from material contracts** depends on governing-law default rules and the specific anti-assignment language in each contract. Research the applicable rule per contract rather than assuming a default.

### Mode 2: Ingest from diligence (the "self-updating" part)

Mode 2 is triggered when an upstream skill produces a finding with a pre-closing action. The upstream skills and output types this mode ingests:

- **`diligence-issue-extraction` findings** — any finding flagged for a closing action (consent, shareholder vote, board resolution, regulatory filing, release, escrow mechanic, pay-off letter). Not just "consents" — see the extraction skill's Handoffs section for the full list.
- **`material-contract-schedule` CoC / assignment items** — change-of-control provisions, anti-assignment clauses, MFN triggers surfaced during schedule build.
- **`deal-team-summary` output** — the exec-tier brief aggregates extraction findings and sometimes surfaces a closing-action item that a mechanical read of the individual extraction memos would miss (e.g., a §280G cleansing vote rolled up across multiple employment agreements, or a composite consent package). Mode 2 reads the latest deal-team-summary in the deal folder and reconciles its closing-action items against the checklist. Anything flagged by deal-team-summary as requiring pre-closing action that is not already on the checklist is appended.

The handoff schema covers the full range of pre-closing actions, not just consents:

```yaml
handoff:
  # Required fields
  item: "[Counterparty or action, one line]"
  category: "[Third-party consents | Shareholder / board action | Regulatory filing | Release / termination | Escrow / holdback | Closing deliverable]"
  source: "[Contract name / statutory section / VDR path + Bates]"
  blocking: true  # unless the agreement has a materiality qualifier
  severity: "[🔴 / 🟠 / 🟡 / 🟢 — carried from upstream, see severity-floor rule in CLAUDE.md]"

  # Consent / third-party action fields
  counterparty: "[e.g., Dunmore Holdings LLC]"
  guarantor: "[e.g., Buyer parent guaranty required, or N/A]"
  conditions: "[any substantive condition the counterparty attached — e.g., 'replacement guaranty from buyer parent required before consent effective']"
  notice_deadline: "[e.g., 30 days prior to closing, or specific date]"

  # Corporate action fields
  approval_body: "[Shareholders | Board | Committee | Regulator]"
  approval_threshold: "[e.g., 75% disinterested stockholder vote for §280G cleansing]"
  statutory_or_charter_source: "[e.g., IRC §280G(b)(5)(B); Charter Art. IV §2]"

  # Timing
  estimated_time_to_complete: "[e.g., 30 days]"
  must_occur_before: "[e.g., closing | signing | end of hiatus period]"
```

Preserve every field the upstream skill populated. A "Dunmore consent required, with replacement guaranty condition and 30-day notice" should surface on the checklist with all three elements (consent, guarantor, notice), not collapse to "Dunmore consent to change of control." When the upstream skill provides a severity, carry it — see the cross-skill severity floor rule in `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/CLAUDE.md`.

Append to the checklist. De-dupe on (counterparty + action type), not on the freeform item name — a Dunmore consent and a Dunmore release are different items even though both name Dunmore. When de-duping, merge fields rather than overwrite: if one handoff populated `guarantor` and a later handoff populated `notice_deadline`, the checklist row carries both.

### Mode 3: Status update

User (or dataroom-watcher agent) provides a status update. Find the item, update status and last-updated.

```
/corporate-legal:closing-checklist
CP-002: Acme responded, consent form attached, needs countersignature
```

### Mode 4: What's blocking

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> This status report is derived from the purchase agreement, diligence findings, and internal deal records. It inherits their privilege and confidentiality status — distribution beyond the privilege circle (counterparty, broader business teams) can waive privilege. Confirm the distribution list before sending.

## Closing Checklist Status — [Deal code] — [date]

**Target close:** [date] ([N] days out)
**Items:** [N] total — [N] done, [N] in progress, [N] not started

### 🔴 Blocking and at risk

| ID | Item | Due | Status | Days to due |
|---|---|---|---|---|
| [CP-XXX] | [item] | [date] | [status] | **[N]** |

### 🟡 Blocking, on track

[same table]

### ✅ Complete

[N] items — [collapsed list]

### Not blocking (post-closing, informational)

[N] items

---

**Critical path:** [The item(s) that, if they slip, push the close date]
```

## Critical path analysis

Not all blocking items are equal. A consent that takes 30 days to get is critical path. A good-standing certificate that takes 2 days is not, even though both are blocking.

For each blocking item, estimate time-to-complete. The ones where `(due date - today) < estimated time` are at risk. Those go at the top of every status report.

If the checklist has more than ~10 items, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer for this output — counts by status (done / in progress / not started / at risk), a critical-path view grouped by workstream, and a sortable grid with item, owner, due date, and days-to-due.

## Integration: dataroom-watcher agent

The agent checks the checklist daily, pulls any status updates from email/企业微信/飞书/钉钉 if connected, and posts the "what's blocking" report to the deal team channel. Mode 4 is the agent's output.

## Consequential-action gate (certify closing)

**Before producing a "ready to close / all CPs satisfied" certification or closing memo:** Read `## Who's using this` in `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Certifying that closing conditions have been satisfied (or producing a closing memo asserting this) has legal consequences — it's the signal that drives funds flow and post-closing obligations. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - The full CP list with status (what's done, what's in progress, what's not started)
> - Anything where evidence of completion is weak or missing
> - Any waivers or side letters needed for items that won't close in time
> - Open questions (counterparty consents still pending, any MAC/bring-down risk)
> - What to ask the attorney (is this ready to call closed; are any conditions being walked past that shouldn't be; what needs to go on a schedule of exceptions)
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (司法行政机关/律师协会 in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service.

Do not produce a final "ready to close" certification past this gate without an explicit yes. Status tracking and "what's blocking" reports do not require the gate.

---

## What this skill does not do

- It doesn't obtain consents, file forms, or draft documents. It tracks that they need to happen.
- It doesn't decide what's blocking — the purchase agreement decides that. This skill reads the agreement.
- It doesn't close the deal. It tells you when you can.
