---
name: "劳动用工法务-制度/政策起草"
description: >
  用于中国大陆劳动用工法务场景下的制度/政策起草。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Draft an employment policy with state supplements where law differs across the
  jurisdictional footprint. Use when the user says "draft a [topic] policy", "we need a
  policy on", "update our [topic] policy", or names a policy gap. WorkBuddy
  中国语境适配：默认中国大陆法域，用于劳动用工法务场景下的制度/政策起草。中文触发词包括：中国法、中国合规、劳动用工法务、制度/政策起草、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**劳动用工法务**；当前技能：**制度/政策起草**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /policy-drafting

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, handbook location.
2. Use the workflow below.
3. Draft core policy. Check each jurisdiction in footprint for required variants.
4. Output: core policy + state supplements. Flag where law is currently shifting.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A policy that's right for California may be wrong (or unnecessary) in Texas. This skill drafts a core policy and generates state supplements where the footprint requires different rules.

## Load context

`~/.workbuddy/skills/config/workbuddy-cn-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, handbook location and format.

## Workflow

### Step 1: Scope the policy

- What's the policy for? (Remote work, parental leave, social media, etc.)
- Why now? (Legal requirement, incident, growth, gap noticed)
- Who does it apply to? (All employees, certain roles, certain locations)

### Step 2: Jurisdictional scan

For each state/country in the footprint, check: does this jurisdiction have a specific rule on this topic?

**Common topics with jurisdictional variance:**

| Topic | Variance |
|---|---|
| Paid leave | State mandates (CA, NY, CO, WA, etc.) with different accrual rates, uses, carryover |
| Parental leave | State programs layer on top of FMLA (CA PFL, NY PFL, etc.) |
| Meal and rest breaks | CA is the outlier (penalty pay); most states minimal |
| Expense reimbursement | CA requires; most states don't |
| Pay transparency | Growing list of states requiring ranges in postings |
| Non-competes | See hiring-review skill — unenforceable in some states |
| Final pay | Timing varies widely |

If the topic has no jurisdictional variance (dress code, say), skip this step.

### Step 3: Draft the core policy

One policy. Applies everywhere. Clear and readable — employees should understand it without a lawyer.

Structure:
- Purpose (one sentence — why this policy exists)
- Scope (who it applies to)
- The rule (what's required/permitted/prohibited)
- Process (how to request, who approves, what happens if)
- Questions (who to ask)

Avoid: "heretofore," "notwithstanding," nested exceptions. This is a handbook policy, not a contract.

### Step 4: State supplements

For each jurisdiction where the rule differs, a supplement:

```markdown
### [State] Supplement

Employees working in [State] are subject to the following in addition to / instead of the core policy:

- [Specific difference]
- [Cite the state law if helpful]
```

Keep supplements tight. Only what's different — don't repeat the core.

### Step 5: Cross-check

- Does this policy conflict with anything already in the handbook?
- Does it promise more than the company intends to deliver? (A policy is a promise — courts hold employers to handbook promises.)
- Does it inadvertently create a contract? (Some states treat handbook policies as contractual — include the standard "this is not a contract" language if the handbook doesn't already.)

## Output

```markdown
# [Policy Name]

## Core Policy

[Full text]

## State Supplements

### [State 1]
[Supplement]

### [State 2]
[Supplement]

---

## Drafting Notes (internal — remove before handbook insertion)

- **Jurisdictional scan:** [which states checked, which have variance]
- **Conflicts with existing handbook:** [none | list]
- **Law currently shifting:** [any state where this is in flux]
- **Review cadence:** [when to revisit — annual, or when X happens]
```

> **Draft, not a policy in effect.** This is a drafting aid for attorney review, not a policy you can publish. Publishing a handbook policy has legal consequences — in several states it can bind the company as a contractual promise, and wage/leave/accommodation policies are routinely read against the employer. A 执业律师/法务负责人, solicitor, barrister, or other authorised legal professional in your jurisdiction reviews, edits as needed, and takes professional responsibility before the policy is rolled out. Do not publish or distribute this draft unreviewed.

## Handoff

To handbook-updates skill: when this policy is approved, it diffs against the current handbook and flags what changes.

## What this skill does not do

- Approve the policy. It drafts; a human approves.
- Roll out the policy. Communication to employees is an HR workflow.
- Cover every jurisdiction on earth — only the ones in the footprint. If the footprint expands, re-run.
