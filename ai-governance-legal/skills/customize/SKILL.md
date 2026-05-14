---
name: "AI 治理法务-个性化配置"
description: >
  用于中国大陆AI 治理法务场景下的个性化配置。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Guided customization of your AI governance practice profile — change one thing without
  re-running the whole cold-start interview. Adjust risk posture, escalation contacts,
  use-case registry entries, vendor AI positions, AI policy commitments, impact-assessment
  house style, or matter workspace paths. Use when the user says "change my [thing]",
  "update my profile", "edit my config", "tune my playbook", or "customize". WorkBuddy
  中国语境适配：默认中国大陆法域，用于AI 治理法务场景下的个性化配置。中文触发词包括：中国法、中国合规、AI
  治理法务、个性化配置、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**AI 治理法务**；当前技能：**个性化配置**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /customize

## When this runs

The user typed `/ai-governance-legal:customize`. They want to change something
in their practice profile — a risk posture, an escalation contact, a playbook
position, a jurisdiction, an output format — without re-running the whole
cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.workbuddy/skills/config/workbuddy-cn-legal/ai-governance-legal/CLAUDE.md`
   (and `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/ai-governance-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Regulatory footprint** — EU AI Act, state AI laws, sector regulators in
     scope
   - **Risk posture** — conservative / middle / aggressive, what each means for
     triage and AIA output
   - **People** — governance team, AI risk owner, escalation chain, approvers
   - **Use case registry** — approved / conditional / never entries, and
     conditions attached to each
   - **AI system inventory** — per-system role (provider / deployer / etc.) and
     tier under the EU AI Act. Run `/ai-governance-legal:ai-inventory` for
     the dedicated editor.
   - **Vendor AI governance** — training-on-data, liability, model-change
     notice, and other positions in your vendor AI playbook
   - **AI policy commitments** — the public or internal commitments your AI
     policy has made, that the plugin cross-checks against
   - **Impact assessment house style** — AIA section order, risk scoring
     format, stakeholder framing
   - **Workflow** — intake path, output format, matter workspace paths, review
     cadence for the policy monitor
   - **Integrations** — what's connected (企业微信/飞书/钉钉, document storage,
     scheduled-tasks), what falls back

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples of downstream explanation:
   - *Risk posture middle → conservative:* "I'll flag more use cases as
     conditional rather than approved, surface more AIA follow-ups, and
     recommend more conservative vendor AI redlines."
   - *Adding an escalation contact:* "Every skill that routes escalations
     (`/triage`, `/review-vendor-ai`, `/gap-check`) will now include this
     contact on the relevant risk bands."
   - *New use case registry entry:* "`/triage` will match against this entry
     on its next run. Existing AIAs aren't rewritten — re-run them if you want
     the new posture reflected."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.workbuddy/skills/config/workbuddy-cn-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/ai-governance-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" something, set it
  to `[Not configured]` and explain what that means for the plugin's behavior.
  ("Removing your escalation chain means `/triage` will flag escalation-worthy
  items but won't route them to a specific person.")
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., risk posture aggressive + escalation "everything goes to
  the GC"; or "EU AI Act in scope" + "no systems flagged for the EU"), flag
  the tension and ask which one they want.
- **Flag guardrail degradation.** If the user asks to turn off a guardrail
  ("stop adding the `[review]` flag," "drop the citations warning," "skip the
  privilege header"), explain what the guardrail protects against and confirm
  they understand the trade-off. Most guardrails are adjustable — a few are
  structural:
  - The `[review]` flag mechanism (tells the user when legal judgment is
    needed rather than a confident wrong answer) — load-bearing, don't
    remove.
  - Source attribution tags on retrieved content — load-bearing, don't remove.
  - `[verify]` tags on cited statutes/regulations — load-bearing, don't
    remove.
- **One change at a time.** Don't re-ask the whole interview. If the user
  wants multiple changes, handle them sequentially and confirm each before
  moving on.
