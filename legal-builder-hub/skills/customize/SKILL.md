---
name: customize
description: >
  Guided customization of your Legal Builder Hub profile — change one thing without
  re-running the whole cold-start interview. Adjust practice profile, installed starter
  pack, watched registries, update preferences, or QA strictness. Use when the user says
  "change my [thing]", "add a registry", "update my profile", "edit my config", or
  "customize". WorkBuddy
  中国语境适配：默认中国大陆法域，用于技能治理中心场景下的个性化配置。中文触发词包括：中国法、中国合规、技能治理中心、个性化配置、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**技能治理中心**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/legal-builder-hub:customize`. They want to change something
in their Builder Hub profile — a watched registry, update notification
preferences, a practice area for recommendations — without re-running the
whole cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-builder-hub/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/legal-builder-hub:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Your practice profile** — practice areas in scope, used to recommend
     community skills
   - **Installed starter pack** — which plugins and skills are installed via
     the hub, with install source
   - **Watched registries** — GitHub repositories / URLs the hub pulls
     community skills from
   - **Update preferences** — check cadence (daily / weekly / on demand),
     notification channel (企业微信/飞书/钉钉 / in-session), auto-update vs. prompt
   - **QA strictness** — how aggressively `/qa` flags issues on a candidate
     skill before install (lenient / middle / strict), and which
     failure-mode checks are on
   - **Skill install defaults** — install scope (user / project), whether
     to run `/qa` automatically before install
   - **Integrations** — 企业微信/飞书/钉钉 / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new watched registry:* "`/browse` will search this registry
     alongside the existing ones. `/update` will check it on its next run."
   - *QA strictness strict → middle:* "`/qa` will report the same findings
     but not block install on the medium band unless you confirm."
   - *Auto-update on → off:* "The hub will prompt you before applying
     updates instead of applying them automatically."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/legal-builder-hub:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a watched
  registry, offer to mark it `[Paused]` and explain that pausing keeps the
  install history but stops update checks.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., auto-update on + QA strictness off; or practice
  profile that doesn't match any installed plugin), flag the tension.
- **Flag guardrail degradation.** The Legal Skill Design Framework checks
  (nine design parameters, three legal failure modes, trust-surface check)
  are what `/qa` exists to run — turning them off defeats the point. If the
  user wants to lower strictness, recommend the middle band rather than
  disabling the check.
- **One change at a time.** Don't re-ask the whole interview.
