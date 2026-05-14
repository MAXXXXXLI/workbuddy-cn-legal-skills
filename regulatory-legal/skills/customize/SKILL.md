---
name: "监管合规法务-个性化配置"
description: >
  用于中国大陆监管合规法务场景下的个性化配置。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Guided customization of your regulatory practice profile — change one thing without
  re-running the whole cold-start interview. Adjust watched regulators, policy library
  index, materiality threshold, gap response process, feed configuration, or matter
  workspace paths. Use when the user says "change my [thing]", "add a regulator", "update
  my watchlist", "edit my threshold", or "customize". WorkBuddy
  中国语境适配：默认中国大陆法域，用于监管合规法务场景下的个性化配置。中文触发词包括：中国法、中国合规、监管合规法务、个性化配置、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**监管合规法务**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/regulatory-legal:customize`. They want to change something
in their regulatory profile — a watched regulator, a materiality threshold,
a feed source — without re-running the whole cold-start interview and
without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/regulatory-legal/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/regulatory-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Regulators we watch** — agencies / bodies / SROs / state regulators
     in scope, and which are "leading" (most likely to drive policy
     impact) vs. "monitor"
   - **Policy library** — the internal policies the library indexes, path
     to each, owner per policy
   - **Materiality threshold** — when a regulatory change rises to
     "notable" vs. "report" vs. "digest only"; how this threshold filters
     `/watch` output
   - **Gap response process** — who triages, SLA per severity, downstream
     owners (policy, product, training)
   - **Feed configuration** — regulator feeds, Thomson Reuters
     connectors, cadence of the `/watch` sweep, digest channel
   - **People** — regulatory counsel, policy owners, comment drafter,
     escalation chain
   - **Workflow** — matter workspaces, open gaps tracker, comment deadline
     tracker, digest publication cadence
   - **Integrations** — Thomson Reuters / 企业微信/飞书/钉钉 / document
     storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a regulator to the watchlist:* "`/watch` will sweep this
     regulator on its next run. `/diff` will accept inputs from this
     regulator's rulemaking feed."
   - *Tightening materiality threshold:* "`/watch` digest will be
     shorter — items below the new threshold will drop from the weekly
     digest but stay searchable."
   - *New policy added to the library:* "`/diff` will include this policy
     when matching new rules against the library. The comment tracker
     will tag comments affecting this policy."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/regulatory-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "drop" a regulator,
  offer to mark it `[Monitor only]` and explain that monitoring keeps the
  feed in the archive but pulls it out of the active digest.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., regulator in scope + no jurisdiction in the footprint
  that the regulator covers; or "weekly digest" + materiality threshold
  that yields fewer than one item a quarter), flag the tension.
- **Flag guardrail degradation.** `[verify]` tags on cited regulations,
  source attribution on feed pulls, and the `[review]` flag on gap triage
  are load-bearing — do not remove. Materiality threshold can be adjusted,
  but lowering it below the point where the digest becomes noise is the
  point — warn if that's the direction.
- **One change at a time.** Don't re-ask the whole interview.
