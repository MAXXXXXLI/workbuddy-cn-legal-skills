---
name: outline-builder
description: >
  Build or extend a course outline in your format, from class notes and casebook.
  Scaffolds — it does not write the outline for you. Use when the user says "outline
  [subject]", "add to my outline", "build an outline from", or points at class materials.
  WorkBuddy
  中国语境适配：默认中国大陆法域，用于中国法学习场景下的课程大纲。中文触发词包括：中国法、中国合规、中国法学习、课程大纲、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**中国法学习**；当前技能：**课程大纲**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /outline-builder

1. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/law-student/CLAUDE.md` → outline preferences, existing outlines.
2. Apply the workflow below.
3. Build in student's format. If extending an existing outline, match its structure exactly.

---

## Purpose

The outline is the thing you study from. **Building it is half the studying** — that's a literal claim, not a throwaway. An outline you didn't build is an outline you won't know on the exam. This skill helps you build — it does not build for you.

## The "don't write it for me" rule (hard rule)

This is a learning-mode skill. Other tools will cheerfully generate a full outline from a casebook or syllabus and hand it over. This one refuses.

**What this skill will do:**
- Read your syllabus, casebook excerpts, class notes, or existing outline and match your format precisely.
- Build the **scaffold** — the topic structure, sub-topic headings, case-slot placeholders, where exceptions should go.
- Ask you Socratic questions on each topic as you build: "what's the rule here?", "which case did the professor use?", "what's the exception the casebook hinted at?"
- Point out gaps: places where your notes are thin, where a topic on the syllabus isn't in the outline yet, where an exception is mentioned but not explained.
- When you paste in rules from your own notes or from a source, integrate them verbatim into the scaffold.
- Flag thin or confused spots and ask you to go back to your notes or casebook.

**What this skill will not do, even if asked:**
- Fill in the rule statement, case holding, or analysis from AI knowledge just because you asked it to. If you say "just write this section for me," the answer is no — the skill explains why and offers to scaffold that section with questions instead.
- Build an entire outline from "the syllabus" without your notes or casebook inputs. A scaffolded topic tree, yes. Populated rules and cases, no — that's the learning work.
- Invent rules to avoid leaving a gap. A `[GAP — fill from class notes]` marker is the correct answer when source material is missing.

**Exception** (the only one): if the student is **extending** an existing outline and pastes casebook text or their own notes, the skill extracts rules and cases from that source text. That is not writing-for-you; that is formatting what you provided.

If the student asks the skill to cross the line, respond:

> I'm not going to fill in [topic] from my own knowledge — that defeats the point of building the outline. Two options:
>
> 1. **Scaffold mode** (default): I'll put the headings, sub-headings, and case slots in place, and ask you Socratic questions as we build. You write the rules.
> 2. **Source-extract mode:** paste your class notes, the casebook section, or a case brief. I'll extract the rule from that text and slot it in.
>
> Which one?

## Confidence discipline

An outline is a rule library. Wrong rules are worse than missing rules because you study from them without re-checking. The rule for this skill:

- **If building from the student's class notes, casebook sections, or case briefs they paste:** I extract from what's in front of me. Confident. Rules stated in the source are the rules I write.
- **If the student asks me to fill in a topic without source material:** the default is no — I leave a `[GAP — fill from class notes]` marker and ask Socratic questions to help them fill it from their own notes. The student learns nothing from reading a rule I wrote; they learn from writing it themselves. Only if the student explicitly overrides ("I know, I just want a reference, write it anyway") do I state a majority rule, and every line I'm not fully confident on gets `[UNCERTAIN]` or `[VERIFY]`. Default to the gap.
- **Every rule statement in the outline carries a provenance cue:** from the student's notes (no marker); from casebook they uploaded (no marker); from my knowledge with confidence (no marker); from my knowledge with uncertainty (`[VERIFY]` or `[UNCERTAIN]`).

The outline is only as trustworthy as what's in it. Err toward gaps over guesses.

**Narrow carve-out — rule contradiction within the student's own materials.** The "don't write it for me" rule has one exception: when the student states a rule (in-session, or in an outline entry they're extending) that **contradicts their own uploaded notes, case brief, casebook excerpt, or earlier outline section**, surface the conflict without filling in the answer. Say:

> "That doesn't match what you wrote at [file / outline section / case brief]. Your earlier note says [exact quote]. Which is right?"

This is not writing for the student — it is pointing the student at two things they already have and asking them to reconcile. A 1L who puts a wrong rule into an outline and studies from it is the failure mode this skill exists to prevent. Apply this only when:

1. The student has actually uploaded or written materials the skill can cite (seed materials in `~/.workbuddy/skills/config/workbuddy-cn-legal/law-student/CLAUDE.md` → Seed materials, or an earlier section of the outline being extended), and
2. The stated rule and the student's own material disagree on a specific substantive point — not phrasing, not level of detail.

Do not volunteer the correction from your own knowledge. Do not cite the casebook unless the student uploaded it. Only quote the student's own materials back to them. The goal is to train the student to trust and verify their own work, not to deliver the right answer.

## Load context

`~/.workbuddy/skills/config/workbuddy-cn-legal/law-student/CLAUDE.md` → outline preferences (format, depth, existing outlines location).

If existing outlines exist: read one. Match its structure exactly. Headings, depth, how cases are integrated, whether there are hypos.

## Workflow

### Step 1: Inputs

What are we building from?
- Class notes
- Casebook sections
- Case briefs (from case-brief skill or the student's own)
- Syllabus (for structure)
- Existing partial outline (extending, not starting fresh)

### Step 2: Structure

Syllabus gives the structure. Major topics → subtopics → rules → cases illustrating rules.

If extending: match the existing outline's structure precisely. Don't impose a different organization.

### Step 3: Build — scaffold first, content from sources

**The scaffold gets built from the syllabus and any existing outline.** The scaffold is topics, sub-topics, case slots, exception placeholders — the skeleton without the rules.

**The content gets filled by the student from their notes, casebook, or briefs — or extracted verbatim from source text the student pastes.** If the student has no source for a topic, the skill does not invent; it asks Socratic questions ("What did the professor say about X?", "Which case illustrates this rule?") and leaves a `[GAP]` marker.

Never skip the scaffold step and just generate a populated outline. That is the failure mode this skill exists to prevent.

Per the student's format. Common formats:

**Traditional outline:**
```
I. [Major topic]
   A. [Subtopic]
      1. Rule: [statement]
         a. [Case name]: [how it illustrates the rule]
         b. [Exception or limitation]
      2. [Next rule]
```

**Rules-only (法考备考 style):**
```
## [Topic]
- [Rule]. [Case cite].
- Exception: [rule]. [Case cite].
```

**Flowchart-adjacent:**
```
[Topic] → Is [element 1] met?
  YES → Is [element 2] met?
    YES → [Result]
    NO → [Different result]
  NO → [No claim]
```

Match theirs.

### Step 4: Gaps

Mark where the outline is thin:
- `[NEEDS CASES — rule stated but no illustrating case]`
- `[CHECK CLASS NOTES — professor may have emphasized something here]`
- `[EXCEPTION UNCLEAR — casebook mentions an exception, find the rule]`

## Citation check

Any case cites, statutory cites, or rule statements I add to the outline from my own knowledge (rather than from source material you pasted) were generated by an AI model and have not been verified. Before you study from the outline, look up each case and statute on 北大法宝/威科先行/官方法规库, Fastcase, 人民法院案例库/中国裁判文书网, or your casebook. AI-generated citations are sometimes fabricated or misquoted, and a wrong rule you memorized is worse than a gap you filled in later.

## Drill-me integration

In drill-me mode, after building a section: "Okay, close the outline. [Subject] question: [hypo]." Test whether the outline got into their head or just onto paper.

## What this skill does not do

- Replace the student's own synthesis. An outline you didn't build is an outline you won't know. This skill *helps* build — the student should be driving.
- Guarantee exam coverage. Outline the whole syllabus; the professor will test whatever they want.
- **Invent rules to fill gaps.** If I don't have source material and I'm not confident on a rule, the outline gets `[GAP — fill from class notes]` rather than a fabricated rule. Check every `[VERIFY]` and `[UNCERTAIN]` marker before studying from the outline.
