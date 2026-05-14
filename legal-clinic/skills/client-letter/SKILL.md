---
name: "法律诊所/法律援助-客户函件"
description: >
  用于中国大陆法律诊所/法律援助场景下的客户函件。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**法律诊所/法律援助**；当前技能：**客户函件**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /client-letter

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` → plain-language standards, supervision style, clinic contact info.
2. Use the templates and workflow below.
3. Match type to template. Plain-language check.
4. Output with AI-assisted label, supervision routing.

Scope: routine only. Substantive advice → `/status client` or a conversation with the professor.

```
/legal-clinic:client-letter appointment
```

```
/legal-clinic:client-letter doc-request
```

---

# Client Letter: Routine Correspondence

## Purpose

Clinics send a lot of routine correspondence: "your appointment is Tuesday at 2pm," "please bring your lease," "we filed your answer." This skill handles those from templates so students aren't typing the same letter every week.

**Scope: routine only.** Substantive advice, bad news, case strategy — those are `/status client` or a conversation, not a template letter.

## Load context

`~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` → plain-language standards, supervision style, clinic contact info.

## Pedagogy check

Read the supervisor guide for this practice area at `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/guides/<practice-area>.md`. Check the `pedagogy_posture` setting:

- **`guide` (default):** Produce the structure and the checklist (required elements, plain-language targets, sign-off per student practice rule). Ask the student to draft each section. Give feedback on their draft (register, reading level, required elements, what they missed). Offer to fill a section only when the student has tried once.
- **`assist`:** Produce the letter. Flag items for student review. The student edits and learns by reviewing.
- **`teach`:** Don't produce the letter. Ask the student to draft it. Give feedback. Ask leading questions when they're stuck. Only show a model paragraph after two attempts, and only the section they're stuck on. Track what they got right and wrong so the supervisor can see progress.

If no guide exists, use `guide`. If the guide exists but doesn't set a posture, use `guide`.

Whatever the posture, the output always includes: "**Pedagogy mode: [assist/guide/teach]** — set by your supervisor's guide. This means I [description of what the student did vs what the skill did]."

## Sign-off and student-attorney disclosure

Check your jurisdiction's student practice rule for required disclosure language in letters signed by a law student. Some jurisdictions require specific forms; most require that the student identify themselves as a law student / certified legal intern and identify the supervising attorney. The templates below use a generic form — conform the sign-off to your rule before sending.

## Letter types

> **Review label goes OUTSIDE the letter.** The `[AI-ASSISTED DRAFT — requires review per plugin config supervision step]` tag is a note to the student, not part of the letter body. Place it above the rendered template (or in a header the student deletes before sending), never inside the fenced letter content. If it ends up in the client-facing copy, the skill has failed.

### Appointment confirmation

*Review label for the student (not for the client — strip before sending):*
`[AI-ASSISTED DRAFT — requires review per plugin config supervision step]`

```markdown
Dear [Client],

This confirms your appointment with [Clinic name]:

**Date:** [date]
**Time:** [time]
**Where:** [address / room / or "by phone at [number]"]
**With:** [student name]

**Please bring:** [documents needed — from case notes or leave as prompt
for student to fill]

If you need to reschedule, call us at [clinic phone] at least 24 hours before.

[Student name]
Law Student, Certified Legal Intern
Under the supervision of [Supervising Attorney]
[Clinic name] | [phone] | [hours]
```

### Document request

*Review label for the student (not for the client — strip before sending):*
`[AI-ASSISTED DRAFT — requires review per plugin config supervision step]`

```markdown
Dear [Client],

To move your case forward, we need the following documents from you:

- [Document 1 — e.g., "Your lease agreement"]
- [Document 2 — e.g., "The notice you received from your landlord"]
- [Document 3]

**How to get them to us:** [drop off at clinic / email to [address] / bring
to next appointment]

**Please send by:** [date — if there's a deadline, say why: "We need these
by [date] so we can file your answer before the court deadline."]

If you don't have some of these or aren't sure what we mean, call us at
[clinic phone] and we can help.

[Student name]
Law Student, Certified Legal Intern
Under the supervision of [Supervising Attorney]
[Clinic name] | [phone] | [hours]
```

### Brief status update

For routine "we filed it" / "we're waiting" updates. (Fuller status updates → `/status client`.)

*Review label for the student (not for the client — strip before sending):*
`[AI-ASSISTED DRAFT — requires review per plugin config supervision step]`

```markdown
Dear [Client],

Quick update: [one-line what happened — "We filed your answer with the court
on [date]" / "We sent the demand letter to your landlord on [date]"].

**What's next:** [one line — "We're waiting for their response" / "The court
will schedule a hearing and let us know the date"].

You don't need to do anything right now. We'll let you know when we do.

[Student name]
Law Student, Certified Legal Intern
Under the supervision of [Supervising Attorney]
[Clinic name] | [phone] | [hours]
```

## Before sending

Sending a letter to a client is a consequential action. This plugin's gate is the supervision workflow described in `## Supervision style` in `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md`, reinforced by the Part 0 role check that confirms a licensed supervising attorney owns the clinic setup. That gate still holds: every letter clears review before it leaves the clinic.

Before sending any of the letters above, confirm:

1. The draft has been reviewed per the supervision protocol in `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` (queue / flag / lighter-touch).
2. All internal review labels (`[AI-ASSISTED DRAFT]`, any `[VERIFY]` or `[FACT NEEDED]` tags) have been removed from the client-facing copy.
3. The sign-off conforms to your jurisdiction's student practice rule for law-student-signed correspondence.

**This is a student draft for supervising-attorney review, not a final letter.** Sending it has legal consequences for the client and may constitute legal advice or communication on the client's behalf. A licensed supervising attorney reviews, edits, and signs off before the letter leaves the clinic. Do not send without supervisor approval.

## Plain-language check

Per `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md` standards. Short sentences. No jargon. Reading level target enforced. If a template above includes a legal term the client might not know, explain it the first time: "We filed your 'answer' — that's the document that tells the court your side of the story."

## Supervision routing

Per `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md`. Routine correspondence may or may not be a flag trigger depending on the supervision style the professor chose. If lighter-touch: these go out after student review without a queue step. If formal queue: even routine letters queue.

## What this skill does NOT do

- **Substantive advice.** If the letter would say "here's what I think about your case" or "here's what you should do," that's not routine — that's `/status client` or a conversation with the professor first.
- **Bad news.** Case closing, adverse ruling, can't-help — those need thought, not a template. Flag for professor.
- **Anything to opposing counsel or a court.** Different audience, different skill (`/draft` or `/status court`).
