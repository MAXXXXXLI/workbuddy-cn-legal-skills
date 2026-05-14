---
name: "商事合同法务-个性化配置"
description: >
  用于中国大陆商事合同法务场景下的个性化配置。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**商事合同法务**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/commercial-legal:customize`. They want to change something
in their practice profile — a risk posture, an escalation contact, a playbook
position, a jurisdiction, an output format — without re-running the whole
cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/commercial-legal/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/commercial-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting, sales-side vs. purchasing-side orientation *(shared across all
     12 plugins — changes flow through `company-profile.md`)*
   - **Risk posture** — conservative / middle / aggressive, what each means
     for fallback positions and escalation triggers
   - **People** — escalation chain, approvers by dollar threshold and by
     clause type
   - **Playbook positions** — the substantive contract positions: liability
     caps, indemnity scope, IP ownership, data protection, termination,
     auto-renewal, price escalation, and the fallbacks for each
   - **NDA triage preferences** — what green / yellow / red looks like for
     inbound NDAs
   - **Review preferences** — redline style, explanation depth, whether to
     produce a stakeholder summary by default
   - **House style** — document format, signature block, renewal-alert
     channel, deviation-log format
   - **Workflow** — matter workspace paths, intake path, renewal watcher
     cadence
   - **Integrations** — Ironclad / 上上签/法大大/e签宝/DocuSign / 企业微信/飞书/钉钉 / document storage
     status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Liability cap fallback 12 months → 6 months:* "`/review` will now flag
     anything above 6 months as a deviation; existing deal-debrief entries
     stay as logged."
   - *New escalation approver:* "Any redline exceeding your own authority
     will now route to this approver — `/escalate` will include them by
     default for the matching risk band."
   - *Risk posture middle → aggressive:* "I'll accept more vendor-friendly
     positions without flagging them and shift the `[review]` bar higher."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/commercial-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" something, set it
  to `[Not configured]` and explain what that means for the plugin's behavior.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., risk posture aggressive + "every redline needs GC
  approval"; or "sales-side" + a purchasing-side playbook position), flag the
  tension and ask which one they want.
- **Flag guardrail degradation.** If the user asks to turn off a guardrail
  (drop the `[review]` flag, skip the privilege header, remove `[verify]`
  tags), explain what the guardrail protects against and confirm they
  understand the trade-off. The `[review]` flag, source attribution tags, and
  `[verify]` tags on cited statutes are load-bearing and should not be
  removed.
- **One change at a time.** Don't re-ask the whole interview.
