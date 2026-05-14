---
name: "劳动用工法务-扩张事项更新"
description: >
  用于中国大陆劳动用工法务场景下的扩张事项更新。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Update the status of an in-progress international expansion project — recalculates what
  is now unblocked, flags anything overdue, and surfaces the next priorities. Use when
  work has happened since the last session and the expansion tracker needs to reflect the
  current state. WorkBuddy
  中国语境适配：默认中国大陆法域，用于劳动用工法务场景下的扩张事项更新。中文触发词包括：中国法、中国合规、劳动用工法务、扩张事项更新、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**劳动用工法务**；当前技能：**扩张事项更新**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /expansion-update

Returns to an open expansion tracker and updates item status based on what
has happened since the last session. Recalculates what is now unblocked,
flags anything overdue, and surfaces the next priorities.

## Instructions

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/CLAUDE.md`.

2. Identify the tracker file: `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/expansion-[slug].yaml`. If it doesn't
   exist, respond: "No expansion tracker found for [country]. Run
   `/employment-legal:expansion-kickoff [country]` to start one."

3. Read the tracker. Show the current state:

```
[Country] Expansion — last updated [date]
Open: [N] | In progress: [N] | Done: [N] | Blocked: [N]

Next priorities (open items with earliest due dates or highest-dependency):
  [item] — owner: [owner]
  [item] — owner: [owner]
  [item] — owner: [owner]
```

4. Ask for updates in a single prompt — do not ask about each item one by one:

   > Which items have moved since we last looked? Tell me what's changed
   > (e.g., "EOR decision made — going with Deel", "outside counsel engaged —
   > call scheduled for Thursday", "PE analysis still open, waiting on tax").
   > You can also add new items or change due dates.

5. Apply updates to the tracker file. For any item newly marked `done`,
   check whether it unblocks other items and flag those as now actionable.

6. If any item has a due date that has passed and is still `open` or
   `in-progress`, flag it:

```
⚠️ Overdue: [item] — was due [date], owner: [owner]
```

7. Write the updated tracker. Confirm:

```
Tracker updated — [N] items closed, [N] still open.
Next priority: [top open item].
```

## Examples

```
/employment-legal:expansion-update Germany
```

```
/employment-legal:expansion-update
(will ask which country if multiple trackers exist)
```

> Detailed tracker schema, item-status rules, and dependency logic live in the
> `international-expansion` reference skill — load it before doing substantive
> work.
