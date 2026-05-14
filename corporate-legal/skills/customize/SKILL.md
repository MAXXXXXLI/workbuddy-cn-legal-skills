---
name: customize
description: >
  Guided customization of your corporate practice profile — change one thing without
  re-running the whole cold-start interview. Adjust risk posture, escalation contacts,
  active modules (M&A / Board / Public Company / Entity Management), materiality
  thresholds, disclosure schedule format, consent precedents, or matter workspace paths.
  Use when the user says "change my [thing]", "update my profile", "edit my config", or
  "customize". WorkBuddy
  中国语境适配：默认中国大陆法域，用于公司与交易法务场景下的个性化配置。中文触发词包括：中国法、中国合规、公司与交易法务、个性化配置、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**公司与交易法务**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/corporate-legal:customize`. They want to change something
in their practice profile — a risk posture, an escalation contact, a module
toggle, an output format — without re-running the whole cold-start interview
and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/corporate-legal/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/corporate-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, public
     vs. private, practice setting *(shared across all 12 plugins — changes
     flow through `company-profile.md`)*
   - **Active modules** — which of M&A, Board & Secretary, Public Company,
     Entity Management are on. Turning a module on/off changes which skills
     prompt for setup.
   - **Risk posture** — conservative / middle / aggressive, what each means
     for diligence materiality and disclosure schedule scope
   - **People** — deal team, board secretary, entity management owner,
     escalation chain
   - **M&A module** — materiality thresholds (contract value, headcount,
     revenue), data room platforms trusted, AI bulk-review trust level
     (Luminance / Kira), deal-team briefing cadence
   - **Board & Secretary module** — house consent format, signatory
     preferences, committee structure
   - **Public Company module** — reporting calendar, disclosure controls,
     10-K/10-Q review timing
   - **Entity Management module** — entity table, registered agent, filing
     jurisdictions, annual report calendar
   - **Workflow** — matter workspaces (deal rooms), closing checklist
     location, VDR watcher cadence
   - **Integrations** — 企业网盘/Box / Intralinks / Datasite / CT Corp / 企业微信/飞书/钉钉 status,
     fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Materiality threshold $250K → $500K:* "`/diligence-issue-extraction`
     and `/material-contract-schedule` will now treat $500K as the cutoff.
     Existing findings stay as logged; re-run if you want the new threshold
     applied retroactively."
   - *Turning on the Public Company module:* "I'll prompt you for reporting
     calendar and disclosure controls next time you run anything in that
     area."
   - *AI bulk-review trust "check every row" → "spot-check 10%":* "`/ai-tool-
     handoff` will QA a 10% sample rather than every extraction."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/corporate-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" something, set it
  to `[Not configured]` and explain what that means for the plugin's behavior.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., Public Company module off + "SEC counsel" in
  escalation; or aggressive risk posture + $25K materiality threshold), flag
  the tension.
- **Flag guardrail degradation.** The `[review]` flag, source attribution
  tags on retrieved documents, and `[verify]` tags on cited authorities are
  load-bearing — explain the trade-off before removing.
- **One change at a time.** Don't re-ask the whole interview.
