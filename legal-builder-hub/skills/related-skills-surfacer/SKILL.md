---
name: "技能治理中心-相关技能推荐"
description: >
  用于中国大陆技能治理中心场景下的相关技能推荐。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Suggest community skills based on recent activity in other plugins. Checks whether the
  community has built something relevant to a task and mentions it once, non-intrusively.
  Use when the user says "is there a community skill for this", "what else is out there",
  or asks for skill recommendations; also runs passively as part of other plugins'
  workflows. WorkBuddy
  中国语境适配：默认中国大陆法域，用于技能治理中心场景下的相关技能推荐。中文触发词包括：中国法、中国合规、技能治理中心、相关技能推荐、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**技能治理中心**；当前技能：**相关技能推荐**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /related-skills-surfacer

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-builder-hub/CLAUDE.md` → practice profile.
2. Use the workflow below.
3. Check what other plugins have been doing. Match against registry.
4. Suggest: "You've been doing X — community has a skill for Y that's related."

---

## Purpose

The community might have built the thing you're about to build. This skill notices and mentions it — once, briefly, non-annoyingly.

## How it runs

This skill surfaces related community skills after a task. It can be invoked directly by the user ("what else is out there for X?") or wired into other plugins via a Stop hook — the hook-based pattern requires each sibling plugin to declare a Stop hook that calls this skill, which is not wired by default. Without the hook wiring, invoke it directly.

Other plugins can include a light check at the end of a task:
> "The legal-builder-hub found a community skill that might help with this kind of thing: [name] — [one-line]. Want to take a look?"

## Load context

`~/.workbuddy/skills/config/workbuddy-cn-legal/legal-builder-hub/CLAUDE.md` → practice profile, installed skills (don't suggest what's already installed).
Registry cache from registry-browser.

## The match

Given a task description (what the user was just doing), find registry skills that match:

- Keyword overlap between the task and skill descriptions
- Practice profile fit (don't suggest litigation skills to a transactional lawyer)
- Not already installed

**Threshold:** Only surface if the match is strong. Weak matches are noise. Better to surface nothing than to annoy.

## Output

If strong match:
> 💡 The community has a skill for this: **[name]** from [registry] — "[description]". `/legal-builder-hub:skill-installer [name]` to try it.

If no strong match: silent. No output. Don't announce "I found nothing."

## Frequency limit

Don't surface the same skill twice. If the user didn't install it the first time, they saw it and decided no. Track dismissals in `references/surfaced.json`.

## User control

Per `~/.workbuddy/skills/config/workbuddy-cn-legal/legal-builder-hub/CLAUDE.md` → new skill notifications:
- **All:** Surface any match
- **Matching practice profile:** Filter by profile (default)
- **None:** This skill is off

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- Install anything.
- Interrupt a task in progress. Surfacing happens at the *end* of a task, not in the middle.
- Nag. One mention per skill, ever.
