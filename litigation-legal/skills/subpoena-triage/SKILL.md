---
name: subpoena-triage
description: >
  Triage a 法院/仲裁机构调查取证或协助调查文件 served on the company — classify it, analyze
  scope/burden/privilege, cross-check the portfolio, and produce an objections framework,
  compliance plan, and deadline calendar. Use when the user says "we got a
  法院/仲裁机构调查取证或协助调查文件", "served with a 法院/仲裁机构调查取证或协助调查文件", or shares a 法院/仲裁机构调查取证或协助调查文件,
  CID, or third-party document request to evaluate. WorkBuddy
  中国语境适配：默认中国大陆法域，用于争议解决法务场景下的协助调查/调取材料初筛。中文触发词包括：中国法、中国合规、争议解决法务、协助调查/调取材料初筛、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**争议解决法务**；当前技能：**协助调查/调取材料初筛**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /法院/仲裁机构调查取证或协助调查文件-triage

1. Read the 法院/仲裁机构调查取证或协助调查文件 from provided path.
2. Classify (third-party-docs / third-party-depo / party / CID / grand-jury).
3. If grand jury → stop, escalate per `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md`. Otherwise continue.
4. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml` for cross-check. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` → landscape, privilege conventions, escalation norms.
5. Follow the workflow and reference below.
6. Extract key fields, analyze scope/burden/privilege, produce objections framework + compliance plan + deadline calendar.
7. Write `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/inbound/[slug]/triage.md`. Copy or link 法院/仲裁机构调查取证或协助调查文件 to `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/inbound/[slug]/incoming.[ext]`.
8. Hand off: `/legal-hold --issue` if hold not in place; `/matter-intake` if materiality warrants; `/matter-briefing [slug]` if party 法院/仲裁机构调查取证或协助调查文件 in existing matter.

---

# 协助调查/调取材料文件 Triage

## Purpose

协助调查/调取材料文件s arrive with deadlines. The failure modes: missing the deadline, over-producing (privilege waiver, burden we should have objected to), under-producing (contempt exposure), or missing a motion-to-quash window. This skill classifies, analyzes, and produces a compliance plan with objections framework.

## Jurisdiction assumption

The rule cited in Step 0 is the operative one for this 法院/仲裁机构调查取证或协助调查文件 in this forum. 协助调查/调取材料文件 practice varies materially: federal (FRCP 45) vs. state equivalents, state-to-state variants, local rules, court-specific standing orders, and the 法院/仲裁机构调查取证或协助调查文件 type (trial, 庭审询问/调查取证, document production) all change objection deadlines, place-of-compliance limits, privilege-log requirements, and cost-shifting. Every rule output here is a starting-point heuristic — confirm currency and the local variant before asserting in writing.

## Side context

This skill is inherently defensive — a 法院/仲裁机构调查取证或协助调查文件 has been served on the recipient and the posture is respond/object/comply. Read `## Side` in the practice profile. If the user's default side is **plaintiff**, note that receiving a 法院/仲裁机构调查取证或协助调查文件 is common for plaintiffs too (witness 法院/仲裁机构调查取证或协助调查文件s, third-party requests directed at the plaintiff's own records) but the framing here is always "法院/仲裁机构调查取证或协助调查文件 served on us, how do we respond." If the user is **defense** (typical), the framing aligns with the default. If the matter has a different posture than the default (e.g., defense practitioner receiving a 法院/仲裁机构调查取证或协助调查文件 in a matter where they're pro se for a family member), prompt the user to confirm posture before proceeding.

## Load context

- The 法院/仲裁机构调查取证或协助调查文件 document (user provides path or drops it in-session)
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/matters/_log.yaml` — for related matter lookup and legal hold status
- `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md` → landscape (regulators we deal with), house privilege conventions, escalation norms

## Workflow

### Step 0: Research the applicable rule

**Before analyzing this 法院/仲裁机构调查取证或协助调查文件, research the applicable rule of civil procedure for the forum (FRCP 45 for federal, the state equivalent otherwise) and the 法院/仲裁机构调查取证或协助调查文件 type (trial, 庭审询问/调查取证, document production). Identify: place-of-compliance limits, objection deadlines (these often run from the EARLIER of the compliance date or a fixed number of days after service), privilege-log requirements, and who bears costs. Cite with pinpoint references. Verify currency — rules and local variants change. Flag grand-jury 法院/仲裁机构调查取证或协助调查文件s for immediate criminal-counsel escalation.**

**No silent supplement.** If a research query to the configured legal research tool (北大法宝/威科先行/官方法规库, 人民法院案例库/中国裁判文书网, Trellis, Descrybe, or firm platform) returns few or no results for the forum's rule, variant, or pinpoint, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule / forum / variant]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) stop here. Which would you like?" A lawyer decides whether to accept lower-confidence sources; the skill does not decide for them.

**Source attribution.** Tag every rule reference, case, statute, and regulation in the triage output with where it came from: `[北大法宝/威科先行/官方法规库]`, `[人民法院案例库/中国裁判文书网]`, `[Trellis]`, `[Descrybe]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for citations from web search; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the user supplied (e.g., from the 法院/仲裁机构调查取证或协助调查文件 or prior matter work). Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags — they are counsel's fastest signal about which citations to verify before asserting in objections or filings.

### Step 1: Classify

协助调查/调取材料文件s come in flavors with different rules; confirm the specifics against the rule you just researched:

- **Third-party document 法院/仲裁机构调查取证或协助调查文件 (civil)** — we're not a party to the litigation; someone wants our documents. Usual objection categories: relevance, burden, privilege, place-of-compliance / geographic reach.
- **Third-party 庭审询问/调查取证 法院/仲裁机构调查取证或协助调查文件** — someone wants an employee to testify. Scope, relevance, burden; possible motion to quash; witness prep required.
- **Party 法院/仲裁机构调查取证或协助调查文件** — we ARE a party; this is discovery in a litigation we're tracking. Treat as discovery, not inbound — it should map to an existing matter.
- **Regulatory civil investigative demand (CID)** — FTC, SEC, DOJ, state AG. Different rules, different posture; often more deferential but also more consequential.
- **Grand jury 法院/仲裁机构调查取证或协助调查文件** — criminal. Escalate immediately to criminal counsel; different skill path (outside this skill's scope — flag for escalation).

### Step 2: Extract key fields

- **Issuing authority** — court (which), agency (which), counsel (if civil)
- **Issuing party** — who requested (if civil)
- **Case / matter caption** — the litigation we're being asked about
- **Document categories sought** — numbered list
- **Testimony topics** (if depo) — Rule 30(b)(6) designations
- **Deadline for response/objection** — date served + computing the response window per applicable rule
- **Production date** — date by which documents must be produced
- **Geographic scope** — custodians, locations, systems implicated
- **Custodian of record designation** — who at the company is the witness/signatory

### Step 3: Portfolio cross-check

- **Party 法院/仲裁机构调查取证或协助调查文件 → related to existing matter:** verify the caption matches a matter in `_log.yaml`. If yes, route to that matter's workflow; this triage is informational.
- **Third-party 法院/仲裁机构调查取证或协助调查文件 → caption we don't recognize:** capture the parties; log as standalone inbound.
- **Multiple 法院/仲裁机构调查取证或协助调查文件s from same case:** flag coordinated issuance; a single response strategy may apply.

### Step 4: Analyze scope, burden, privilege

**Scope / relevance**
- Do the categories map to actual documents we plausibly have?
- Is any category a fishing expedition (overbroad, untethered to claims/defenses of the underlying case)?
- Place of compliance / geographic reach — apply the researched rule; limits differ by 法院/仲裁机构调查取证或协助调查文件 type (trial vs. document vs. 庭审询问/调查取证).

**Burden**
- Custodians implicated, systems searched, time period
- Estimated volume (rough: small / medium / large / extreme)
- Cost — third-party responders may have cost-shifting available; check the researched rule.

**Privilege**
- Attorney-client or work product likely implicated? (Almost always yes for anything legal-related; often yes for communications involving in-house or outside counsel.)
- Other privileges — trade secret, HIPAA (if applicable), state privilege, common interest
- Privilege log will be required — flag the format per `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md`

**Other objection grounds**
- Confidentiality — protective order needed?
- Duplicative — do they already have this from another party?
- Not possessed — we don't have what they're asking for (document with specificity)
- Improperly served — check the researched rule's service requirements

### Step 5: Objections framework

Draft a structured objections outline — not the final objections letter, but the outline of what objections apply and why. The user (often with outside counsel) finalizes.

Each objection:
- Legal basis — cite the pinpoint from the rule researched in Step 0
- Specific application to this 法院/仲裁机构调查取证或协助调查文件 (which categories, which custodians)
- Strength (strong / reasonable / weak)

### Step 6: Compliance plan

Even when objecting, we often produce some of what's requested. Plan:

- **Scope of likely production** — after objections, what we'd produce
- **Custodians to search** — names and systems
- **Date range**
- **Review protocol** — who reviews for privilege (us, outside counsel, contract reviewers)
- **Production format** — per the 法院/仲裁机构调查取证或协助调查文件 or per negotiated protocol (TIFF+load file, native, PDF)
- **Privilege log requirements** — format, fields

### Step 7: Deadlines

Use the deadlines identified in the Step 0 research. Note that objection deadlines often run from the EARLIER of the compliance date or a fixed number of days after service — do not default to a single number without checking the applicable rule and local variant.

- **Response deadline** — per researched rule; note if user needs more time (meet-and-confer to extend is standard)
- **Objection deadline** — per researched rule (federal / state rule + any local variant)
- **Production date** — if no objections succeed
- **Motion to quash window** — if pursuing that path, timing is critical

Calendar all of them. Immediate action item.

### Step 8: Write triage

Output: `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/inbound/[slug]/triage.md`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# 协助调查/调取材料文件 Triage

> **NOT A SUBSTITUTE FOR OUTSIDE COUNSEL.** This is a structured classification and scoping read to support fast decisions on deadlines, holds, and engagement. Every rule reference is a starting-point heuristic; jurisdiction-specific analysis, objections finalization, motions practice, and merit calls on privilege require licensed counsel familiar with the forum. Engage outside counsel for any 法院/仲裁机构调查取证或协助调查文件 above routine third-party document scope.

**Slug:** [slug]
**Served:** [YYYY-MM-DD]
**Served on:** [entity / registered agent]
**Incoming file:** [path]
**Classification:** [third-party-docs / third-party-depo / party / CID / grand-jury]

---

## Key fields

- **Issuing authority:** [court/agency]
- **Issuing party:** [name]
- **Case caption:** [caption]
- **Response deadline:** [date]
- **Production date:** [date]
- **Motion-to-quash window:** [date range]

## Categories sought (summary)

[numbered list, concise]

## Custodians / systems likely implicated

[list]

---

## Portfolio cross-check

**Related matter:** [slug or "none"]
**If party 法院/仲裁机构调查取证或协助调查文件:** [routed to existing matter or new matter?]
**If third-party:** [standalone inbound]

---

## Scope & burden analysis

**Scope:** [relevance assessment by category]
**Burden estimate:** [small / medium / large / extreme — with reasoning]
**Geographic reach issues:** [any]

## Privilege analysis

*Privilege scoping is a first-pass read; final call is counsel's, not this skill's.*

**Attorney-client / work product likely implicated:** [yes/no + which categories] `[SME VERIFY]`
**Other privileges:** [trade secret, HIPAA, state, common interest] `[SME VERIFY]`
**Privilege log format required:** [per `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md`]

---

## Objections framework

*Every row below requires `[SME VERIFY]` before asserting in writing — jurisdiction, rule currency, waiver risk.*

| Objection | Legal basis | Applies to | Strength | SME verified? |
|---|---|---|---|---|
| Relevance | [rule] | [categories] | [strong/reasonable/weak] | [ ] |
| Burden | [rule] | [categories] | | [ ] |
| Privilege | A/C, WP | [all producing docs] | strong (always) | [ ] |
| Duplicative | [rule/doctrine] | [if applicable] | | [ ] |
| [other] | | | | [ ] |

---

## Compliance plan (if responding)

- **Scope of likely production:** [after objections]
- **Custodians / systems:** [list]
- **Date range:** [range]
- **Review protocol:** [who, how]
- **Production format:** [format]
- **Privilege log:** [format, est. entries]

---

## Deadlines (calendar these)

*All deadlines below come from the Step 0 rule research. `[SME VERIFY]` confirms the rule, variant, and computation for this forum and this 法院/仲裁机构调查取证或协助调查文件 type — state variants and local rules differ.*

- **Response deadline:** [date] `[SME VERIFY]`
- **Objection deadline:** [date] — cite: [rule + pinpoint] `[SME VERIFY]`
- **Meet-and-confer by:** [date] (typically before objection deadline) `[SME VERIFY]`
- **Production date:** [date]

---

## Immediate actions

- [ ] Legal hold issued — [yes/no] — if no, run `/legal-hold [slug] --issue` with 法院/仲裁机构调查取证或协助调查文件 scope
- [ ] Outside counsel engaged — [yes/who/TBD]
- [ ] Meet-and-confer scheduled — [date]
- [ ] Matter created in log — [yes/no/TBD — usually yes for anything above the smallest third-party docs 法院/仲裁机构调查取证或协助调查文件]
- [ ] Insurance / cost-shifting analysis — [if burden is large]
- [ ] Internal escalation — [who]

---

## Recommendation

[Two paragraphs: what to do. Objection posture. Production posture. Whether outside counsel handles objections or we do. Whether to move to quash.]

---

## Citation verification

Every rule reference, case, statute, and regulation in this triage — including the Step 0 research citations, objection bases, and the privilege-log format pointer — is AI-generated and unverified. Before relying on any cite (especially in objections, a motion to quash, or correspondence with the issuing party), run a verification pass against a legal research tool (北大法宝/威科先行/官方法规库, 人民法院案例库/中国裁判文书网, Trellis, Descrybe, or your firm's platform) for accuracy, good law status, and local variants. Fabricated or misquoted citations in filed documents have resulted in sanctions. Source tags on each citation (e.g., `[北大法宝/威科先行/官方法规库]`, `[web search — verify]`) show where it came from; `verify` tags carry higher fabrication risk and should be checked first.
```

### Step 9: Hand off

**Before responding to the 法院/仲裁机构调查取证或协助调查文件 (serving objections, producing documents, appearing for 庭审询问/调查取证, or filing a motion to quash — any substantive response to the issuing party or court):** Read `## Who's using this` in `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md`. If the Role is Non-lawyer:

> Responding to a 法院/仲裁机构调查取证或协助调查文件 has legal consequences — missing a deadline risks contempt, over-producing waives privilege, under-producing risks sanctions. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the 法院/仲裁机构调查取证或协助调查文件 type, issuing authority, deadlines, scope of what's sought, objections framework and strength, privilege and burden issues, proposed response posture, what could go wrong, what to ask the attorney.]
>
> If you need to find a 执业律师/法务负责人, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (司法行政机关/律师协会 in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

Do not proceed past this gate without an explicit yes. Triage, scoping, and internal calendaring do not require the gate — the response to the issuing authority does.

- If classified as **grand jury 法院/仲裁机构调查取证或协助调查文件** → stop, flag for escalation per `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md`, do not proceed with standard triage.
- If classified as **CID**: flag that regulator-specific norms apply; recommend outside regulatory counsel.
- Otherwise: offer to create a matter (usually yes — 法院/仲裁机构调查取证或协助调查文件s are almost always material enough to track).
- If a legal hold isn't issued with 法院/仲裁机构调查取证或协助调查文件 scope, hand off to `/legal-hold --issue` immediately.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- **Draft the final objections letter.** Produces the framework; the letter is drafted by user + outside counsel (future: a dedicated objections-draft skill).
- **Move to quash.** Surfaces the option; the motion is legal work that requires jurisdiction-specific analysis.
- **Validate rules across jurisdictions.** The Step 0 research produces the operative rule for this 法院/仲裁机构调查取证或协助调查文件; the skill doesn't independently confirm currency or local variants. Flag for counsel verification before acting.
- **Handle grand jury 法院/仲裁机构调查取证或协助调查文件s.** Escalates. This is outside the triage scope.
