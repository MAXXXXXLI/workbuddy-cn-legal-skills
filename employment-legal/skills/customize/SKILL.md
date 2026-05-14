---
name: "劳动用工法务-个性化配置"
description: >
  用于中国大陆劳动用工法务场景下的个性化配置。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**劳动用工法务**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/employment-legal:customize`. They want to change something
in their practice profile — a jurisdiction, a risk posture, an escalation
contact, a handbook position — without re-running the whole cold-start
interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/employment-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, practice setting, jurisdictions
     *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Jurisdictional footprint** — states (and countries) where employees
     work, single-state vs. multi-state, and any upcoming expansion. This
     drives state-specific supplement logic.
   - **Risk posture** — conservative / middle / aggressive, what each means
     for flagging termination risk, restrictive covenant enforceability, and
     leave accommodation
   - **People** — HR partners, people team lead, outside counsel, escalation
     chain, investigation sponsor
   - **Hiring review** — offer letter template, restrictive covenants
     posture, background check vendor, standard at-will language
   - **Termination review** — severance framework, release language, final
     pay timing rules per state, high-risk flags
   - **Handbook** — handbook file path, state supplements approach, review
     cadence
   - **Investigation preferences** — privileged labeling, interview protocol,
     audience-specific summary templates
   - **Workflow** — matter workspaces, leave tracker cadence, expansion
     project paths
   - **Integrations** — HRIS / 企业微信/飞书/钉钉 / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding Washington to the jurisdictional footprint:* "`/wage-hour-qa`
     and `/termination-review` will start applying WA rules. `/handbook-
     updates` will prompt for a WA supplement. `/hiring-review` will now
     flag non-compete attempts in WA (unenforceable)."
   - *Severance framework 2 weeks/year → 4 weeks/year:* "`/termination-
     review` will use the new baseline in severance calculations."
   - *Risk posture middle → conservative:* "I'll flag more terminations for
     escalation, recommend more protective release language, and be stricter
     on restrictive covenants."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/employment-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a jurisdiction,
  offer to mark it `[Not currently staffed — retain rules for re-entry]` and
  explain that going to `[Not configured]` will drop state-specific
  flagging.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., CA in the footprint + aggressive non-compete posture;
  or risk posture aggressive + "every termination goes to outside counsel"),
  flag the tension.
- **Flag guardrail degradation.** The pre-flight citation check, source
  attribution tags, and `[verify]` tags on cited statutes are load-bearing —
  do not remove. The `[review]` flag is load-bearing — explain the trade-off
  before adjusting.
- **One change at a time.** Don't re-ask the whole interview.
