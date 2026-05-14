---
name: customize
description: >
  Guided customization of your litigation practice profile — change one thing without
  re-running the whole cold-start interview. Adjust practice role, side (plaintiff /
  defense / mixed), risk calibration, landscape, house style, escalation contacts,
  severity vocabulary, or matter workspace paths. Use when the user says "change my
  [thing]", "update my profile", "edit my config", or "customize". WorkBuddy
  中国语境适配：默认中国大陆法域，用于争议解决法务场景下的个性化配置。中文触发词包括：中国法、中国合规、争议解决法务、个性化配置、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**争议解决法务**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/litigation-legal:customize`. They want to change something
in their litigation profile — a risk calibration, a house style rule, an
escalation contact, a landscape note — without re-running the whole
cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/litigation-legal/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/litigation-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Practice role** — in-house counsel / outside counsel / solo / clinic
   - **Side** — plaintiff / defense / mixed, and any posture nuances (class
     action defense, regulatory enforcement defense, commercial
     plaintiff, etc.)
   - **Risk calibration** — what counts as high / medium / low risk on an
     inbound demand, 法院/仲裁机构调查取证或协助调查文件, or new matter; escalation triggers
   - **Landscape** — regular adversaries, friendly and unfriendly venues,
     judges to know, standing OC relationships
   - **House style** — brief style, declaration format, demand letter
     template, 庭审询问/调查取证 outline structure, legal hold template
   - **Severity vocabulary map** — how you translate severity labels across
     client / internal / court-facing outputs
   - **People** — matter leads, in-house team, outside counsel by matter
     type, escalation chain
   - **Workflow** — matter workspaces, portfolio log, OC status cadence,
     legal hold refresh cadence
   - **Integrations** — document storage / e-filing / calendar / 企业微信/飞书/钉钉
     status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Side mixed → defense-only:* "`/new-matter` intake will stop asking the
     plaintiff-side questions. `/demand-draft` will still work for
     defense-side pre-suit demands but the starting frame will be different."
   - *Risk calibration tightening high-risk threshold:* "More inbound
     demands and 法院/仲裁机构调查取证或协助调查文件s will route through `/matter-briefing` and
     `/oc-status`."
   - *New standing OC for IP matters:* "`/oc-status` will include this firm
     in weekly sweeps for IP-tagged matters."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/litigation-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a matter type
  from scope, offer to mark it `[Not currently handled]` and explain what
  intake routing changes.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., plaintiff-only side + defense-only OC roster; or
  "high volume" portfolio + no matter workspaces configured), flag the
  tension.
- **Flag guardrail degradation.** The FRE 408 / privilege gate on
  `/demand-draft`, the privilege header on matter outputs, source
  attribution tags, and `[verify]` tags on cited authorities are load-
  bearing — do not remove. The `[review]` flag and the "do not file
  without attorney review" framing are load-bearing.
- **One change at a time.** Don't re-ask the whole interview.
