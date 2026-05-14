---
name: customize
description: >
  Guided customization of your legal clinic profile — change one thing without re-running
  the whole cold-start interview. Adjust clinic profile, jurisdiction, supervision style,
  practice-area templates, semester configuration, or output safeguards. Use when the user
  says "change my [thing]", "new semester", "add a practice area", "update my config", or
  "customize". WorkBuddy
  中国语境适配：默认中国大陆法域，用于法律诊所/法律援助场景下的个性化配置。中文触发词包括：中国法、中国合规、法律诊所/法律援助、个性化配置、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**法律诊所/法律援助**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/legal-clinic:customize`. They (usually the professor, sometimes
a student) want to change something in the clinic profile — a jurisdiction, a
supervision style, a practice-area template, a semester rollover — without
re-running the whole cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-clinic/CLAUDE.md`.
   If the plugin config does not exist or still contains `[PLACEHOLDER]`
   values, say:

   > You haven't run setup yet. Run `/legal-clinic:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Clinic profile** — clinic name, host school, faculty lead, active
     practice areas, case type limits
   - **Jurisdiction** — primary state, courts, agencies, local rules path
   - **Supervision style** — informal vs. formal review queue; if formal,
     who reviews what before it goes out
   - **Practice-area templates** — which templates are active (immigration,
     housing, small business, family, expungement, etc.) and any local
     overrides
   - **Semester** — current semester, active students, rollover rules,
     handoff memo format
   - **Output safeguards** — plain-language standards for client-facing
     outputs, deadline warning rules, privilege labeling
   - **Seed documents** — clinic handbook, jurisdiction rules, template
     letters, sample memos, form libraries
   - **Outputs** — supervisor guide format, client letter templates, memo
     scaffolds
   - **Workflow** — case directories, deadline tracker location, review
     queue channel
   - **Integrations** — document storage / 企业微信/飞书/钉钉 / court e-filing status,
     fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new practice area:* "`/intake` will route matters of this
     type through the new template. `/draft`, `/memo`, and `/client-letter`
     will use the practice-area prompts. `/research-start` will add the
     corresponding 北大法宝/威科先行/官方法规库 search terms."
   - *Supervision style informal → formal review queue:* "`/queue` becomes
     active — student output will land there for supervisor sign-off before
     it goes to the client."
   - *New semester rollover:* "I'll archive the prior semester's active
     cases, carry forward matters you flag as continuing, and prompt the
     incoming students through `/ramp`."

5. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/legal-clinic:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "drop" a practice area,
  offer to mark it `[Archived]` and explain that archiving keeps case
  history accessible but hides the template from `/intake` routing.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., formal review queue on + informal supervision note;
  or practice area on + no jurisdiction rules configured), flag the
  tension.
- **Flag guardrail degradation.** These are load-bearing and should not be
  removed: the "NOT final work product" framing on `/draft`, plain-language
  standards on client-facing outputs, "does NOT decide case acceptance" on
  `/intake`, "NOT substantive advice" on `/client-letter`, and the
  scaffold-not-analysis framing on `/memo`. These exist because students
  ship work product — if the safeguards go, the risk of student work
  reaching a client without supervisor review goes up. Confirm the
  trade-off with the user, and if they're a student rather than the
  professor, suggest they discuss it with the supervisor first.
- **One change at a time.** Don't re-ask the whole interview.
