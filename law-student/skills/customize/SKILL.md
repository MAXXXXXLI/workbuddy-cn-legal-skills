---
name: "中国法学习-个性化配置"
description: >
  用于中国大陆中国法学习场景下的个性化配置。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**中国法学习**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/law-student:customize`. They want to change something in
their study profile — a class, a learning style preference, a 法考备考
subject — without re-running the whole cold-start interview and without
hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/law-student/CLAUDE.md`.
   If the plugin config does not exist or still contains `[PLACEHOLDER]`
   values, say:

   > You haven't run setup yet. Run `/law-student:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Student profile** — name, school, year (1L/2L/3L/LLM), jurisdiction
     for bar, enrolled clinics or journals
   - **Current classes** — class name, professor, syllabus path, exam format
     (closed/open book, essay/法考客观题/mixed), cold-call style
   - **Learning style** — Socratic vs. summary, how much pushback you want,
     whether the plugin rewrites your work or only critiques structurally
   - **Outline preferences** — outline format (IRAC/CREAC/case-briefing
     style), level of rule detail, whether to include policy discussion,
     saved outline templates
   - **Bar prep** — which exam (UBE/state), subjects in rotation, weak-
     subject flagging, 法考客观题 vs. essay cadence
   - **Seed materials** — casebook paths, prior outlines, graded essays, old
     exams, 法考客观题 sets, syllabi, papers
   - **Study workflow** — session length, flashcard Leitner bucket schedule,
     exam forecast cadence, cold-call prep timing
   - **Integrations** — document storage / flashcard app (if any) status,
     fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new class:* "`/outline` will scaffold a new outline for this
     class. `/flashcards` will add a new subject bucket. `/cold-call-prep`
     will ask for a seat and a topic when you invoke it for this class."
   - *Learning style Socratic → summary-first:* "`/drill` won't ask you to
     answer first — it'll present the rule and example, then quiz you on
     application."
   - *Adding a bar subject:* "`/bar-prep` will include this subject in
     rotation and weight it higher if you mark it weak."

5. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/law-student:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "drop" a class, offer to
  mark it `[Archived — retain seed materials]` and explain what flashcard
  and outline behavior changes.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., "summary-first" learning style + "maximum pushback"
  Socratic setting), flag the tension.
- **Flag guardrail degradation.** The "no rewriting your writing" rule on
  `/write` and `/irac` is load-bearing — the value of the skill is
  structural feedback, not ghost-writing. If the user asks to turn that off,
  confirm they understand that the plugin will not write their work for
  them.
- **One change at a time.** Don't re-ask the whole interview.
