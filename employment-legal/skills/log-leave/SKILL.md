---
name: "劳动用工法务-记录休假事项"
description: >
  用于中国大陆劳动用工法务场景下的记录休假事项。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Add a new leave to the leave register with the minimum information needed to start
  tracking deadlines. Use when an employee goes on leave and you want the tracker to watch
  designation, certification, and exhaustion clocks from day one. WorkBuddy
  中国语境适配：默认中国大陆法域，用于劳动用工法务场景下的记录休假事项。中文触发词包括：中国法、中国合规、劳动用工法务、记录休假事项、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**劳动用工法务**；当前技能：**记录休假事项**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /log-leave

Adds a new leave entry to `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/leave-register.yaml` with the minimum
information needed to start tracking deadlines. Use when an employee goes on
leave and you want the tracker to watch the clocks from day one.

## Instructions

1. Read `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/CLAUDE.md` → jurisdiction table and Systems section.

2. Ask all of the following in a single prompt — do not drip them one at a time:

   > A few quick questions to set up leave tracking:
   >
   > - Employee name or role (anonymized is fine)
   > - Where do they work? (State — this determines which rules apply)
   > - Leave type: FMLA / state leave (which state) / USERRA / ADA accommodation
   > - Leave start date
   > - Is this intermittent leave?
   > - Expected return date (if known — leave blank if not)
   > - Has the designation notice been sent? If yes, when?
   > - Has medical certification been requested? If yes, when?

3. Using the jurisdiction table in `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/CLAUDE.md`, look up the applicable leave
   entitlement (hours/weeks) for this leave type in this jurisdiction.

4. Compute the first upcoming deadline based on the information provided:
   - Designation not yet sent → deadline is 5 business days from leave start
   - Med cert requested but not received → deadline is 15 days from request date
   - Both sent and received → next deadline is at 75% exhaustion

5. Write a new entry to `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/leave-register.yaml` using the leave register
   format from the leave-tracker agent. If the file doesn't exist, create it.

6. Confirm with a single line:
   > "Logged. [Employee/Role] — [Leave type] — [Jurisdiction] — started [date].
   > First deadline: [what it is and when]. Leave tracker will alert automatically."

## Examples

```
/employment-legal:log-leave
```

```
/employment-legal:log-leave
Sarah (Sr. Engineer, works in California) just started FMLA today for a
serious health condition. Intermittent. No designation sent yet.
```
