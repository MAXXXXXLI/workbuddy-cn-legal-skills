---
name: demand-received
description: >
  Triage an inbound demand letter — extract fields, cross-check the portfolio, assess
  merit, present response options with a recommendation, and hand off to matter-intake or
  demand-intake if escalation is warranted. Use when the user says "we got a demand
  letter", "triage this demand", or shares an incoming demand to evaluate. WorkBuddy
  中国语境适配：默认中国大陆法域，用于争议解决法务场景下的来函应对。中文触发词包括：中国法、中国合规、争议解决法务、来函应对、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**争议解决法务**；当前技能：**来函应对**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /demand-received

1. Read the incoming document from provided path.
2. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml` for portfolio cross-check.
3. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` → risk calibration, landscape, demand-letter practice.
4. Follow the workflow and reference below.
5. Extract fields; cross-check portfolio; assess merit; present options with recommendation.
6. Write `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/inbound/[slug]/triage.md`. Copy or link incoming to `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/inbound/[slug]/incoming.[ext]`.
7. Hand off per user choice:
   - Create matter → `matter-intake` pre-populated
   - Respond with counter-demand → `demand-intake` pre-populated
   - Link to existing matter → update `related_matters` in log
   - Standalone → no further action

---

# Demand Received

## Purpose

Inbound demand letters are the bread and butter of an in-house litigation practice. A small fraction need escalation; most can be handled with a structured response or a holding letter. The failure mode is treating them all alike. This skill triages, cross-checks the portfolio, and produces options.

## Load context

- The incoming document (user provides path or drops it in-session)
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml` — scan for related matters (same counterparty, overlapping counterparties via entity relationships, or matter type + recent date)
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` → risk calibration (for merit assessment), landscape (is the sender a frequent adversary?), demand-letter practice (house tone and response defaults)

## Workflow

### Step 1: Read the demand

Extract from the incoming:

- **Sender** — entity, signer, counsel (if signed by outside firm)
- **Recipient** — which entity/person at our company
- **Delivery** — certified, email, courier (matters for deadline calculation)
- **Date received** vs. **date signed**
- **Demand type** — payment, breach/cure, C&D, preservation, settlement, other
- **Specific asks** — what they want, by when
- **Facts alleged** — their version of what happened
- **Legal basis** — statutes, contract provisions, theories they cite
- **Threats** — what they say they'll do if we don't comply
- **Settlement-communication framing** — research the settlement-communication protections applicable in the forum (FRE 408 in federal, the state equivalent otherwise). Note whether the demand is marked as a settlement communication, but remember: protection attaches from conduct and context, not merely from labeling. Capture both the label (if any) and a first-pass read of whether the substance is in fact a compromise discussion.

### Step 2: Portfolio cross-check

Search `_log.yaml` for:

- **Direct match** — matter with same counterparty (their slug matches the sender)
- **Type match** — similar matter type with this counterparty in the past (closed matters count — they inform pattern)
- **Subject overlap** — matters where the subject might be the same dispute (e.g., same contract, same product, same project)

Present findings:

- If **direct match + active:** flag as almost certainly the same matter; recommend adding incoming to the existing matter, not opening a new one. Update `related_matters` if it's a tangent.
- If **direct match + closed:** flag — counterparty is back. May be a new dispute (open new matter) or a resurrected one (reopen or amend). User decides.
- If **type match:** note as precedent/context; probably distinct matter but inform the response strategy.
- If **no match:** novel. Treat as fresh.

### Step 3: Merit assessment

Not a legal opinion — a structured read:

- **Facts** — do the alleged facts align with what we know? Where's the disconnect?
- **Legal basis** — are the cited provisions/statutes actually applicable? (Flag cites for user verification — do not attempt to validate law autonomously.)
- **Strength on their side** — if they went to court tomorrow, what's their story?
- **Strength on our side** — what are our likely defenses?
- **Damages demanded vs. likely** — is the ask proportionate to what a court would award if they won?
- **Leverage and pressure** — are they credibly prepared to sue? Do they have capacity? Are they a repeat-litigant adversary per `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md`?

Output a triage rating: **substantial merit / debatable / weak / frivolous**. Be blunt. The user is triaging, not writing the brief.

### Step 4: Response options

Present 3-4 options with tradeoffs:

**Option A — substantive response**
- When: their demand has merit or is at least debatable; a reasoned reply protects the record
- Tradeoff: commits us to a position in writing
- Next step: `/demand-intake` with pre-populated fields for a counter-response letter

**Option B — holding letter**
- When: need time to investigate; don't want to concede anything or trigger their deadline math
- Tradeoff: doesn't resolve anything; buys 2-4 weeks
- Next step: short acknowledgment draft

**Option C — settlement response**
- When: early resolution is cheaper than litigation; willing to discuss without admitting
- Tradeoff: settlement-communication posture required — research the applicable rule (FRE 408 or state equivalent) and structure the response so the substance, not just the label, qualifies as a compromise discussion. Must be careful not to waive claims.
- Next step: `/demand-intake` with `type: settlement-response`

**Option D — ignore + preserve**
- When: demand is frivolous or the deadline doesn't create legal prejudice
- Tradeoff: silence can be used against us in some contexts (e.g., account stated); legal hold still required
- Next step: issue legal hold via `/legal-hold --issue` if not already; log the demand and move on

Recommend one. Be specific about why.

### Step 5: Deadline triage

- **Their stated deadline** — note it, but it doesn't bind us
- **Our internal deadline** — when we must decide (often: stated deadline minus 5 business days to draft + approve)
- **Legal deadlines** — statute of limitations, contractual cure periods, procedural requirements

Flag any legal deadlines that are tight. Calendar them.

**No silent supplement.** If the inbound demand cites rules, cases, or statutes that require verification, and a research query to the configured legal research tool (北大法宝/威科先行/官方法规库, 人民法院案例库/中国裁判文书网, Trellis, Descrybe, or firm platform) returns few or no results for a given authority, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [cite / doctrine]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) leave the `[SME VERIFY]` flag and stop here. Which would you like?" A lawyer decides whether to accept lower-confidence sources; the skill does not decide for them.

**Source attribution.** Tag every citation carried into the triage — including the sender's cited authorities, our response-option rationales, and any research pulled for merit assessment — with where it came from: `[北大法宝/威科先行/官方法规库]`, `[人民法院案例库/中国裁判文书网]`, `[Trellis]`, `[Descrybe]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations supplied in the demand itself. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

### Step 6: Write triage

Output: `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/inbound/[slug]/triage.md`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> **Privilege inheritance.** This triage is derived from the inbound demand and from the portfolio log, and it records our first-pass merit read and response posture. Those internal analyses are attorney-client and/or work-product material. Distributing this triage beyond the privilege circle — including forwarding it to the business lead without marking, sharing with the counterparty, or attaching to an insurance tender without scrubbing — can waive protection over both this document and the reasoning inside it. Store with privileged matter material, mark consistently with house privilege conventions, and make distribution decisions deliberately.

# Demand Received — Triage

> **READ FOR TRIAGE, NOT OPINION.** This document is an intake scan and an options analysis — not a legal merit opinion. The `Triage rating` below is a structured read to support the counsel's decision on how to route the demand. It is not a recommendation on the merits and does not substitute for case-specific legal analysis. Every cited statute, rule, or case is flagged for SME verification; every merit call is the counsel's, not this skill's.

**Slug:** [slug]
**Received:** [YYYY-MM-DD]
**Received by:** [entity / person]
**Incoming file:** [path]

---

## The demand

**Sender:** [entity, signer, counsel]
**Demand type:** [type]
**Specific asks:** [list]
**Their stated deadline:** [date]
**Settlement-communication framing:** [labeled / substantively / neither / ambiguous] — *protection turns on conduct and context, not the label; `[SME VERIFY]` against the forum's applicable rule*

## Facts alleged

[their version, in one paragraph]

## Legal basis cited

[citations — each inline-flagged with `[SME VERIFY: applicability / currency / jurisdiction]` — do not rely on any citation here without independent check]

## Threats / next steps they state

[list]

---

## Portfolio cross-check

**Direct match:** [slug if exists, or "none"]
**Type match / precedent:** [list or "none"]
**Subject overlap:** [list or "none"]
**Recommendation:** [new matter / add to existing / link via related_matters / standalone inbound]

---

## Merit assessment

**Facts:** [alignment with our version; disconnects]
**Legal basis:** [applicability, with flags]
**Their case if litigated:** [one paragraph]
**Our defenses:** [one paragraph]
**Damages proportionality:** [assessment]
**Credibility of threat:** [will they sue? capacity? repeat litigant?]

**Triage rating:** [substantial / debatable / weak / frivolous] — *structured read for routing, not a merit opinion; `[SME VERIFY: counsel to confirm before relying on this]`*

---

## Response options

### A. Substantive response
[Rationale, tradeoffs, next step]

### B. Holding letter
[Rationale, tradeoffs, next step]

### C. Settlement response
[Rationale, tradeoffs, next step]

### D. Ignore + preserve
[Rationale, tradeoffs, next step]

**Recommendation:** [A/B/C/D] — [two sentences why] — `[SME VERIFY: counsel to confirm before executing]`

---

## Deadlines

- **Their stated deadline:** [date]
- **Our internal decision deadline:** [date]
- **Legal deadlines:** [SoL, cure periods, procedural — with dates]

---

## Immediate actions

- [ ] Legal hold issued — [yes/no] — if no, run `/legal-hold [slug] --issue`
- [ ] Matter created in log — [yes/no/TBD]
- [ ] Counsel assigned — [who]
- [ ] Insurance tendered — [yes/no/N-A]
- [ ] Internal escalation (GC/CFO/business lead) — [who/when]
```

### Step 7: Hand off

Based on recommendation and user confirmation:

- Matter creation → hand off to `/matter-intake` with: counterparty, type, `source: demand-letter` (inbound), initial theory framed defensively, pre-populated.
- Counter-response as outbound demand → hand off to `/demand-intake` with: counterparty, context from triage, desired outcome as the response.
- Link to existing matter → update that matter's `related_matters` in `_log.yaml`; append event to its `history.md`.
- Standalone → leave in `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/inbound/`; no portfolio change.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- **Validate cited law.** Flags cites for the user to run through a citator (verify it is good law) or check with outside counsel. Inventing legal analysis on inbound demands is malpractice exposure.
- **Send a response.** Drafts are drafted in `demand-draft`; this skill stops at the triage decision.
- **Decide merit definitively.** The rating is a read for triage; a formal merit opinion lives with outside counsel or more thorough analysis.
- **Make the matter-creation call.** Surfaces the recommendation; user decides.
