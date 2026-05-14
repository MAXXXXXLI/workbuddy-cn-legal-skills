---
name: status
description: >
  Case status summary by audience — client-facing (plain language), internal (for the
  professor), or court-ready (formal caption format per local rules). Same facts,
  different framing and depth. Use when a student needs to update the client, brief the
  professor, or prepare a court status report. WorkBuddy
  中国语境适配：默认中国大陆法域，用于法律诊所/法律援助场景下的状态汇报。中文触发词包括：中国法、中国合规、法律诊所/法律援助、状态汇报、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**法律诊所/法律援助**；当前技能：**状态汇报**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /status

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` → supervision style, plain-language standards, jurisdiction.
2. Use the workflow below. Read case notes.
3. Generate for the specified audience:
   - `client` — plain language, what happened/next/you do/reach us
   - `internal` — procedural posture, done since last check-in, upcoming, needs professor input, student's assessment
   - `court` — formal status report in caption format per local rules
4. Supervision routing per audience (client-facing and court-ready usually flag).

```
/legal-clinic:status client
```

```
/legal-clinic:status internal
```

```
/legal-clinic:status court
```

---

# Status: Audience-Aware Case Summaries

## Purpose

Clinics generate enormous numbers of status updates — to clients, to professors, to co-counsel, to courts. Same case, same facts, completely different documents. This skill takes the case notes and produces the right summary for the right reader.

## Load context

`~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` → supervision style, plain-language standards (for client-facing), jurisdiction.
Case notes for facts.

## Audience modes

### Client-facing

**Reader:** The client. Probably stressed. Possibly unfamiliar with legal process. Reading level per `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` plain-language standards (default 6th grade).

**Include:**
- What's happened since they last heard from the clinic
- What's happening next and when
- What (if anything) they need to do
- How to reach the clinic

**Don't include:**
- Legal analysis (they don't need to know the IRAC)
- Weaknesses in their case (unless it's time to have that conversation — and that's a call for the professor, not a status update)
- Jargon

*Review label for the student (not for the client — strip before sending):*
`[AI-ASSISTED DRAFT — requires student review and supervision step per plugin config]`

Check your jurisdiction's student practice rule for required law-student sign-off language; some jurisdictions require specific forms.

```markdown
Dear [Client],

I wanted to update you on your case.

**What's happened:** [Plain English. "We filed your answer with the court on
[date]" not "The responsive pleading was submitted."]

**What's next:** [What and when. "The court scheduled a hearing for [date] at
[time]. You need to be there." Or: "We're waiting for the landlord's lawyer
to respond. That could take a few weeks."]

**What you need to do:** [Specific and clear. Or: "Nothing right now — we'll
let you know when we need something from you."]

**How to reach us:** [Clinic phone, hours, student name]

[Student name]
Law Student, Certified Legal Intern
Under the supervision of [Supervising Attorney]
[Clinic name]
```

**Before sending:** sending a client status update is a consequential action. The gate is the supervision workflow in `## Supervision style` in `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md`, reinforced by the Part 0 role check confirming a licensed supervising attorney owns the setup. Confirm the draft has been reviewed per the supervision protocol (queue / flag / lighter-touch) and all internal review labels (`[AI-ASSISTED DRAFT]`, `[VERIFY]`, etc.) have been removed from the client-facing copy.

### Internal (for the professor)

**Reader:** The supervising professor. Knows the law. Wants to know where the case stands and what the student needs from them.

**Include:**
- Procedural status (where in the life of the case)
- What's been done since last check-in
- What's coming up (deadlines, hearings)
- Issues needing professor input
- Student's assessment (how it's going, concerns)

```markdown
# Status: [Client] — [Matter] — [date]

**Student:** [name] | **Procedural posture:** [pre-filing / answer filed /
discovery / motion pending / etc.]

## Since last check-in

- [What's been done]

## Upcoming

| Date | What | Action needed by |
|---|---|---|
| [date] | [deadline/hearing] | [date] |

## Needs professor input

- [Question or decision point — specific]

## Student's assessment

[How it's going. Strengths, concerns, strategic questions. This is where the
student's thinking shows.]

---
[AI-ASSISTED DRAFT — student should revise the assessment section especially;
that's your thinking, not a summary of notes]
```

### Court-ready

**Reader:** A judge or clerk. Formal. Specific to what the court needs (often a status report ordered by the court, or a statement in advance of a status conference).

**Include:**
- Procedural history (briefly)
- Current status of discovery/motions/settlement
- What's outstanding
- Proposed next steps or scheduling

**Format:** Per local rules. Caption, signature block, certificate of service if filed.

```markdown
═══════════════════════════════════════════════════════════════════════
  AI-ASSISTED DRAFT — requires student analysis and attorney review
  Court filings ALWAYS require professor review before filing
═══════════════════════════════════════════════════════════════════════

[Caption per jurisdiction — VERIFY against current local rules]

STATUS REPORT

[Party] respectfully submits this status report pursuant to [the court's
order of [date] / local rule [X] / in advance of the status conference
scheduled for [date]].

1. Procedural history: [brief]

2. Current status: [discovery status / motion status / settlement status]

3. Outstanding matters: [what's pending]

4. Proposed next steps: [scheduling, if the court wants input]

[Signature block — student attorney under supervision of [Professor]]

[Certificate of service if filing]

---

[VERIFY: caption format, local status report requirements, service
requirements — per current [Court] rules]
```

## Supervision routing

Per `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md`:
- Client-facing → usually a flag trigger (client communication)
- Internal → no flag (it's going to the professor anyway)
- Court-ready → always flagged if formal queue enabled (court filings)

## What this skill does NOT do

- **Decide what to tell the client.** Especially on bad news or case weaknesses — that's a conversation for the student and professor to have, then the student to have with the client. Status updates are status, not strategic advice.
- **File anything with a court.** Drafts the document; professor reviews; filing per clinic procedure.
- **Replace the student's assessment in internal status.** The "student's assessment" section is the student's thinking — the draft can scaffold it but can't write it.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

