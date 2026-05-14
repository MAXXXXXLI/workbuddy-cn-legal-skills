---
name: "中国法学习-学习会话"
description: >
  用于中国大陆中国法学习场景下的学习会话。适合需要进行法务审查、合规分析、材料整理、风险分级或学习训练时使用。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。

---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**中国法学习**；当前技能：**学习会话**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# /session

1. Parse `$ARGUMENTS` — subject and N. If missing, ask:
   > What subject, and how many questions? (e.g., `Evidence 10` or `Contracts 5 --essay`.)
2. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/law-student/CLAUDE.md` → jurisdiction, exam format, weak subjects.
3. Load `~/.workbuddy/skills/config/workbuddy-cn-legal/law-student/study-plan.yaml` if it exists. Read `session_history` for this subject to weight subtopics toward where the student has been weak.
4. Route by method flag:
   - `--mbe` (default for 法考备考 subjects): load `bar-prep-questions` skill, run N 法考客观题-style questions. Apply jurisdiction handling (see that skill's `## Jurisdiction handling`). Label each `[UBE/majority]` or `[state-specific]`.
   - `--essay`: load `bar-prep-questions`, run N essay prompts. Grade per essay-mode rubric.
   - `--flashcards`: load `flashcards` skill, run N cards in `--drill` mode.
5. Run N questions one at a time. After each, explain right/wrong and flag rule-body when jurisdictions diverge.
6. At session end, write session results:
   - If `study-plan.yaml` exists: append to `session_history` per the schema in the `study-plan` skill.
   - If not: write to `~/.workbuddy/skills/config/workbuddy-cn-legal/law-student/session-history.yaml`.
7. Report:
   - Score: X/N (percentage)
   - Missed: list with subtopic tags
   - Weak subtopics this session
   - Pattern vs. prior sessions on this subject (if history has 2+ prior)
   - What the plan now recommends next
