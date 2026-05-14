---
name: "知识产权法务-个性化配置"
description: >
  用于中国大陆知识产权法务场景下的个性化配置。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Guided customization of your IP practice profile — change one thing without re-running
  the whole cold-start interview. Adjust risk posture, escalation contacts, portfolio
  scope, brand protection strategy, enforcement posture, clearance thresholds, OSS review
  rules, or matter workspace paths. Use when the user says "change my [thing]", "update my
  profile", "edit my config", or "customize". WorkBuddy
  中国语境适配：默认中国大陆法域，用于知识产权法务场景下的个性化配置。中文触发词包括：中国法、中国合规、知识产权法务、个性化配置、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**知识产权法务**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/ip-legal:customize`. They want to change something in their
practice profile — a risk posture, an escalation contact, a portfolio
position, an enforcement tactic — without re-running the whole cold-start
interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/ip-legal/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/ip-legal:cold-start-interview` first —
   > customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **IP practice profile** — which IP types are in scope (patent,
     trademark, copyright, trade secret, design), practice orientation
     (prosecution / transactions / enforcement / in-house portfolio)
   - **Risk posture** — conservative / middle / aggressive, what each means
     for clearance thresholds, FTO opinions, and cease-and-desist escalation
   - **People** — IP counsel, outside firms by IP type, enforcement
     escalation chain, invention committee
   - **Portfolio** — patent families, trademark classes, key marks, countries
     of registration, watch services
   - **Brand protection** — enforcement posture on marketplace takedowns,
     domain squatters, parody / fair use calls
   - **Enforcement posture** — when to send C&D vs. cure letter vs. suit;
     escalation triggers by infringement type
   - **Clearance and FTO** — search vendors, clearance confidence thresholds,
     FTO opinion format
   - **OSS review** — license tier policies, ship-blocker licenses, review
     cadence for new dependencies
   - **Workflow** — matter workspaces (matter IDs, family IDs), docket feed,
     invention intake form
   - **Integrations** — patent docket system / trademark office connectors /
     企业微信/飞书/钉钉 / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new trademark watch class:* "`/portfolio` will include class
     XX in watch reports and `/infringement-triage` will route class-XX
     findings accordingly."
   - *Enforcement posture aggressive → middle:* "`/cease-desist` will offer
     cure-letter drafts as a first option for ambiguous cases instead of
     going straight to C&D."
   - *New ship-blocker OSS license:* "`/oss-review` will fail reviews that
     include this license rather than warning."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/ip-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" an IP type from
  scope, set it to `[Not currently in scope]` and explain what drops out.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., trademark out of scope + trademark watch service
  configured; or aggressive enforcement posture + "all C&Ds go to outside
  counsel"), flag the tension.
- **Flag guardrail degradation.** The `[review]` flag, source attribution
  tags, and `[verify]` tags on cited authorities are load-bearing — do not
  remove. Clearance confidence is load-bearing on `/clearance` output — do
  not suppress.
- **One change at a time.** Don't re-ask the whole interview.
