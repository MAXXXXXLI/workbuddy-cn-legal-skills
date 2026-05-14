---
name: "产品合规法务-个性化配置"
description: >
  用于中国大陆产品合规法务场景下的个性化配置。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**产品合规法务**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/product-legal:customize`. They want to change something
in their product counsel profile — a risk calibration threshold, an
escalation contact, a framework section — without re-running the whole
cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/product-legal/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/product-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting, product surface area *(shared across all 12 plugins — changes
     flow through `company-profile.md`)*
   - **Launch review process** — intake (Jira / Linear / Asana / doc),
     review SLA, launch tiering, PRD location
   - **Review framework** — the categories you review launches against
     (privacy, IP, safety, claims, regulatory, accessibility, security,
     etc.) and the depth you go on each
   - **Risk calibration** — what's P0 blocker / needs a real look / fine at
     your company, with examples that anchor the labels
   - **Marketing claims** — posture on puffery vs. substantiated, comparative
     claims framing, superlatives, house rules for AI-feature claims
   - **People** — product partners by surface, escalation chain (your
     manager, GC, risk committee), marketing counterpart
   - **Workflow** — matter workspaces, launch-radar watcher cadence, launch
     review template
   - **Integrations** — Jira / Linear / Asana / 企业微信/飞书/钉钉 / document storage
     status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Risk calibration tightening "fine" → "needs a real look" for a
     pattern:* "`/triage` and `/launch-review` will start flagging this
     pattern. Existing reviews stay as written; re-run if you want the new
     posture applied."
   - *New launch-review category:* "`/launch-review` will add a section for
     this category. `/is-this-a-problem` will pattern-match it in triage."
   - *Marketing claims posture tightening:* "`/check-claims` will flag more
     language as needing substantiation or reframing."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/product-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a review
  category, offer to mark it `[Not in scope — route elsewhere]` and name
  the plugin / team that picks it up.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., AI-feature claims scrutiny on + no AI policy
  commitments set in `/ai-governance-legal`; or "fast SLA" + "every
  launch requires GC sign-off"), flag the tension.
- **Flag guardrail degradation.** The `[review]` flag, source attribution
  tags, and `[verify]` tags on cited regulations are load-bearing — do not
  remove. The substantiation requirement on claims is the thing `/check-
  claims` exists for; weakening it defeats the skill.
- **One change at a time.** Don't re-ask the whole interview.
