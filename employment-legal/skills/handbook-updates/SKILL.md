---
name: handbook-updates
description: >
  Diff a proposed handbook change against the current version, flag ripple effects and
  state supplement impacts. Use when user says "update the handbook", "add this to the
  handbook", "handbook change", or has a policy ready for insertion. WorkBuddy
  中国语境适配：默认中国大陆法域，用于劳动用工法务场景下的员工手册更新。中文触发词包括：中国法、中国合规、劳动用工法务、员工手册更新、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**劳动用工法务**；当前技能：**员工手册更新**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# Handbook Updates

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Handbook changes have ripple effects. Change the PTO policy and you've affected the final pay calculation, the leave policy cross-reference, and three state supplements. This skill finds the ripples before they become inconsistencies.

## Load context

`~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/CLAUDE.md` → handbook location, state supplements list, update cadence.

## Workflow

### Step 1: Get the change

- What section is changing?
- What's the new language?
- Why? (Legal requirement, policy decision, cleanup)

### Step 2: Diff against current

Read the current handbook section. Show the diff:

```diff
- [old language]
+ [new language]
```

### Step 3: Find cross-references

Search the handbook for references to the changed section:

- Other policies that cite this one ("see the PTO policy for accrual rates")
- Defined terms that this section uses or defines
- State supplements that modify this section

Each cross-reference: does it still make sense after the change? Flag any that break.

### Step 4: State supplement impact

For each state supplement in `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/CLAUDE.md`:

- Does this supplement modify the section being changed?
- Does the change make the supplement obsolete, wrong, or incomplete?
- Does the change create a need for a *new* supplement in a state that didn't need one before?

### Step 5: Promise check

Is the change reducing something the old version promised?

If yes: that's a risk. Some states treat handbook policies as contractual. Reducing a benefit may need more than just updating the document — advance notice, consideration, or in some cases it can't be done retroactively.

Flag this. Don't block it — but flag it.

## Output

```markdown
## Handbook Update: [Section name]

### Change

[diff]

### Cross-reference impact

| Section | References changed section | Still accurate? | Fix needed |
|---|---|---|---|
| [name] | [how] | ✅/⚠️ | [what] |

### State supplement impact

| State | Current supplement | After change | Action |
|---|---|---|---|
| [state] | [what it says] | [still valid / obsolete / needs update] | [none / update / new supplement needed] |

### Promise check

[If reducing a benefit: flag + jurisdictional risk note]

### Ready to publish

- [ ] Cross-references updated
- [ ] State supplements updated
- [ ] [If benefit reduction: notice/consideration addressed]
- [ ] Version number and date updated
- [ ] Acknowledgment process (if required)
```

## What this skill does not do

- Approve handbook changes. HR/legal leadership does.
- Communicate changes to employees.
- Track acknowledgments.
