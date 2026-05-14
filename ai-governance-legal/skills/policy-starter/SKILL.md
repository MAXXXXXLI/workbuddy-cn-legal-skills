---
name: policy-starter
description: >
  Draft a firm AI usage policy from published model policies, adapted to your practice
  profile — a research-and-synthesis tool whose output is a draft for attorney review and
  adoption, not a finished policy. Use when user says "draft an AI policy", "we need an AI
  policy", "build an AI usage policy", "our firm needs a GenAI policy", or similar
  requests to generate a first-cut internal AI policy. WorkBuddy 中国语境适配：默认中国大陆法域，用于AI
  治理法务场景下的AI 政策起草。中文触发词包括：中国法、中国合规、AI 治理法务、AI
  政策起草、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**AI 治理法务**；当前技能：**AI 政策起草**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /policy-starter

1. Read `~/.workbuddy/skills/config/workbuddy-cn-legal/ai-governance-legal/CLAUDE.md`. If the practice profile is unpopulated, stop and direct to `/ai-governance-legal:cold-start-interview`.
2. Use the framework below.
3. Run the scope interview — which sections does the policy need to cover, who's the audience, what's the deployment context. Do not skip to drafting.
4. Web search for the current published model policies and guidance relevant to the deployment context (ABA, 司法行政机关/律师协会s, ILTA, CLOC, NIST, peer-firm / peer-company policies, current state AI laws, EU AI Act, sector regulators as applicable).
5. Draft the selected sections, sourced from the model policies, with `[review]` flags on every choice point and `[review]` open questions at the bottom of each section.
6. Output with the draft header ("DRAFT FOR INTERNAL LEGAL REVIEW — NOT FOR DISTRIBUTION"), the sources block, the reviewer note, and the adoption checklist.
7. Close with the next-steps decision tree.

```
/ai-governance-legal:policy-starter
/ai-governance-legal:policy-starter "we need an AI policy for our 30-lawyer firm"
/ai-governance-legal:policy-starter "update our existing policy for the 2026 state AI laws"
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ai-governance-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.workbuddy/skills/config/workbuddy-cn-legal/ai-governance-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A lot of firms and in-house teams don't have a written AI usage policy yet, or
are running on a 2024-vintage one that doesn't mention the state AI laws, the EU
AI Act implementing acts, the 2025 COPPA amendments, or what they actually ended
up doing with Copilot and WorkBuddy for Work. This skill produces a **draft** policy
to bring to the decision-maker — GC, managing partner, executive committee,
board, head of IT, head of HR — not a finished policy to circulate.

The discipline of this skill:

1. **Source from published model policies, not from invention.** Search for and
   read the ABA AI Toolkit, 司法行政机关/律师协会 guidance, ILTA's model policy, CLOC's
   templates, and peer-firm / peer-company policies that are public. Cite what
   each source says and adapt it — don't generate policy language out of thin
   air.
2. **Decision-tree the scope before drafting.** A policy that tries to cover
   everything covers nothing. Ask the user what sections the policy needs. Let
   them pick. Then build each picked section with `[review]` flags on every
   choice point.
3. **Flag every judgment call.** The output is a draft the attorney reviews and
   adopts; every threshold, every named tool, every disclosure trigger, every
   enforcement consequence is a `[review]` line.
4. **Header signals the scope of the audience.** This output may be read beyond
   legal — by HR, IT, all staff. The header is adapted accordingly.

This skill does NOT finalize, distribute, publish, or even recommend a specific
position on the hard calls. It produces a draft and surfaces the choices.

## Read `~/.workbuddy/skills/config/workbuddy-cn-legal/ai-governance-legal/CLAUDE.md` first

Before drafting, always read the practice profile. The sections that drive the
draft:

- `## Company profile` — AI role (Builder / Deployer / Both), regulatory footprint,
  external commitments, practice setting
- `## Use case registry` — what's already approved, conditional, or a red line
- `## AI policy commitments` — what a prior or current policy already says
- `## Vendor AI governance` — what the team already requires from vendors
- `## Governance team and escalation` — who approves, who escalates
- `## Who's using this` — Role (lawyer / non-lawyer) governs the header and the
  "adopt this" framing

If `## AI policy commitments` is populated, this is an UPDATE, not a new draft —
treat the existing policy as the base and propose changes. If it's empty, this
is a first-cut draft.

## Scope interview (do this BEFORE drafting)

Ask the user which sections the policy should cover. Present as a checklist —
the user picks, you build. Do not pre-decide.

> **What should the AI policy cover? Pick the sections you want in the draft:**
> 1. **Scope** — who the policy applies to (all staff, certain roles, contractors), what tools it covers (GenAI only, all AI, specific vendors), what data is in/out of scope.
> 2. **Permitted and prohibited uses** — the approved categories, the red lines, the "ask first" cases.
> 3. **Approval and review** — who approves a new tool, who approves a new use case, how the review request is filed, what the SLA is.
> 4. **Disclosure** — to clients (for firms), to courts, to counterparties, to employees, to end users of an AI feature.
> 5. **Data handling** — what confidential/client/privileged data can go where, data residency, vendor retention terms, training-on-data posture.
> 6. **Training and certification** — who has to take training, on what cadence, consequences for non-completion.
> 7. **Incidents and reporting** — what counts as an AI incident, how to report, who handles.
> 8. **Enforcement** — what happens when the policy is violated, link to disciplinary framework.
> 9. **Review cadence and ownership** — how often the policy gets updated, who owns updates, how changes are communicated.
> 10. **Glossary** — defined terms (GenAI, approved tool, high-risk use, consequential decision, confidential data, etc.).
>
> Default starter pack for a firm / in-house legal team that's never had a policy: 1, 2, 3, 4, 5, 9. Skip the rest for v1.

After the user picks, ask the second question:

> **Two more inputs before I draft:**
> - **Audience** — who's reading this? (All staff / legal team only / attorneys plus staff / client-facing version also needed) This drives tone and the glossary.
> - **Deployment context** — (a) law firm, (b) in-house legal at a company (policy covers legal or company-wide?), (c) legal aid / clinic, (d) government. This drives which model policies I search.

## Source the model policies

Before drafting, run web searches for the most recent published model AI
policies and guidance.

**Derive the model policy sources from the practice profile's `## Regulatory footprint`.** Don't hardcode US sources for a global user.

| Jurisdiction | Model policy sources |
|---|---|
| US | ABA Formal Opinion 512, 司法行政机关/律师协会 guidance (CA, FL, NY, TX all have published AI guidance), ILTA model policy, CLOC templates, peer firm published AI policies |
| UK | Solicitors Regulation Authority risk outlook, Law Society AI principles, ICO AI guidance, Bar Council guidance |
| EU | EU AI Act compliance framework (Article 4 AI literacy, Article 17 quality management), national DPA AI guidance (CNIL, DSB, Garante, AEPD), EDPB guidelines, EU institutions' AI policies |
| Australia | Law Council of Australia AI guidelines, OAIC AI guidance, state law society guidance, Australian AI Ethics Framework |
| Singapore | PDPC Model AI Governance Framework, MinLaw guidance, MAS AI fairness principles (for financial services) |
| Canada | Law Society of Ontario/BC/Alberta AI guidance, OPC AI guidance, TBS Directive on Automated Decision-Making |
| Multi-jurisdiction | Use all applicable, and note where they diverge (e.g., EU requires human oversight documentation US doesn't; Australia focuses on voluntary ethics frameworks; Singapore focuses on sectoral regulation) |

If the practice profile's footprint is empty or `[PLACEHOLDER]`, ask: "What jurisdiction(s) does your organization operate in? I'll draft from the model policies that match your regulatory environment and professional responsibility framework, not a US-centric template."

For each source the draft uses, **record it in a "Sources" block at the top of
the output** with: name, URL, date accessed, and what the draft took from it.

If a web search can't be run, note in the reviewer note: "Could not run web
search — draft sourced from training knowledge alone, verify against current
versions of the cited sources before adopting." The verification log applies.

## The draft

Output follows a consistent structure. **Every choice point gets a `[review]`
flag.** The user has to decide; the skill presents options.

### Header

```
DRAFT FOR INTERNAL LEGAL REVIEW — NOT FOR DISTRIBUTION
Prepared for: [firm / company name from practice profile]
Date: [today's date]
Prepared by: ai-governance-legal policy-starter skill, adapted from published model policies
Not for adoption, distribution, posting, or reliance until reviewed, adapted, and approved by [attorney / GC / managing partner / executive committee per the governance team section of the practice profile].
```

When the Role in `## Who's using this` is Non-lawyer: add a second line under
the header — "If you are not a 执业律师/法务负责人, solicitor, barrister, or other
authorised legal professional in your jurisdiction, bring this draft to your
attorney contact ([name from practice profile]) before using any of it. This is
a starting draft for their review, not a policy you can adopt."

### Sources block (at the top, under the header)

A table of the model policies / guidance / regulations the draft drew from:

| Source | URL | Accessed | What the draft took from it |
|---|---|---|---|
| 中国法律诊所/法律援助监督要求 | [url] | [date] | Disclosure and competence framing |
| ILTA Model AI Policy v.[X] | [url] | [date] | Approval workflow, data handling |
| [State] Bar Op. [X] | [url] | [date] | Disclosure to clients |
| [peer firm] published AI policy | [url] | [date] | Scope language |
| Colorado SB 24-205 | [url] | [date] | High-risk AI definition |
| EU AI Act, Art. [X] | [url] | [date] | Vendor flow-down |

### Executive summary

Three paragraphs max. What the policy does, who it binds, what the reader has
to do before it takes effect.

### The sections

Only the sections the user picked, in the order above. For each:

- A **header and scope** sentence.
- The **substantive rules**, adapted from the cited model policies. Every
  specific threshold, number, named tool, named vendor, or escalation contact
  is `[review]`. Example: "Confidential client data may not be entered into
  [general-purpose consumer AI tools] `[review — list tools, or reference the
  approved-tools list]`. Use of such data in [approved firm-licensed tools]
  `[review — list tools]` is permitted subject to the data handling section."
- **Source attribution** inline where a rule is adapted from a specific source.
  Example: "Attorneys must verify the accuracy of all AI-generated work product
  before using it in representation of a client `[中国法律诊所/法律援助监督要求]`."
- **Open questions** at the bottom of each section — 2-3 decisions the attorney
  needs to make before the section is ready. These are distinct from inline
  `[review]` flags — these are the "we don't have a position here yet" items,
  not the "fill in the specifics" items.

### Adoption checklist

At the end of the draft, a checklist of the things that have to happen before
the policy is adopted. Don't invent these — pull from the practice profile's
governance team and escalation section. Typical items:

- [ ] Review by GC / managing partner `[review — name]`
- [ ] Review by IT / security `[review — name]`
- [ ] Review by HR (for enforcement / training sections) `[review — name]`
- [ ] Board / executive committee approval (if required) `[review — confirm whether required]`
- [ ] Training materials drafted
- [ ] Announcement drafted
- [ ] Effective date set `[review]`
- [ ] Review cadence calendared `[review — annual is typical]`
- [ ] Add policy to the `## AI policy commitments` section of the practice
      profile once adopted

### Reviewer note

The standard reviewer note above the header, per the `## Outputs` section of
the practice profile. Use the block format:

> **⚠️ Reviewer note**
> - **Sources:** web search ✓ / not connected — cites from training knowledge
> - **Read:** practice profile · [N] published model policies
> - **Flagged for your judgment:** [N] `[review]` items inline · [N] open questions per section
> - **Currency:** searched for developments since [date]
> - **Before relying:** this is a DRAFT — bring to [approver from practice profile], don't distribute until adopted

## Don'ts

- **Don't invent policy language.** Every substantive rule in the draft must be
  traceable to a cited source or flagged `[review — adapted, no direct source]`.
- **Don't pick the hard calls for the attorney.** "Should paralegals be
  permitted to use AI for first-draft work?" is a `[review]`, not a recommended
  position.
- **Don't produce a finished-looking policy.** The header, the reviewer note,
  and the `[review]` flags throughout are the signal that this is a draft. Do
  not soften them.
- **Don't skip the scope interview.** If the user says "just draft a full
  policy," push back: "A policy that tries to cover everything covers nothing.
  Which sections do you want? Here's the checklist." One round of negotiation
  is fine — two is also fine. Drafting without scope is the failure mode.
- **Don't generate section content the user didn't ask for.** If they picked 1,
  2, 3, 4, 5, 9, do those. Don't add section 6 because "a real policy needs
  training."
- **Don't recommend a specific vendor, tool, or consequence.** Flag those
  `[review]` with context on what a typical decision would be, not what the
  user's should be.
- **Don't promise legal sufficiency.** The draft is a starting point for
  attorney review, not a tested policy.

## Handoffs

After the draft is produced, close with the decision tree from the practice
profile. The most common next steps:

1. **Tune the draft** — the user walks through the `[review]` flags and resolves
   them with the attorney; the skill re-runs with the decisions baked in.
2. **Stakeholder summary** — produce a one-page version for the board or
   executive committee explaining what the policy does and doesn't do.
3. **Training materials** — once the policy is adopted, `/ai-governance-legal:aia-generation` can be used to produce per-use-case training notes.
4. **Vendor sweep** — once the policy is adopted, `/ai-governance-legal:vendor-ai-review` should be run against the vendors the policy references to check conformance.
5. **Gap check against new regulation** — pair with `/ai-governance-legal:reg-gap-analysis` to test the draft against a specific regulation or guidance before adoption.

## Output scope reminder

The document this skill produces reaches HR, IT, and the broader business — not
just legal. Keep the language plain enough for non-lawyers to follow. The legal
precision is in the `[review]` flags and the sources, not in jargon.
