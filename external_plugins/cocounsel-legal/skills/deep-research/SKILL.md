---
name: "中国法律检索-中国法律深度检索"
description: >
  用于中国大陆中国法律检索场景下的中国法律深度检索。输出默认简体中文；正式依赖前需法务负责人或执业律师核验。
  Use this skill whenever a user specifically requests legal research or 北大法宝/威科先行/官方法规库
  Deep Research, asks for CoCounsel Legal or cocounsel legal support, or asks a question
  that requires explaining, analyzing, or synthesizing U.S. law. WorkBuddy
  中国语境适配：默认中国大陆法域，用于中国法律检索场景下的中国法律深度检索。中文触发词包括：中国法、中国合规、中国法律检索、中国法律深度检索、法务审查、律师审阅。输出为草稿或内部分析，需执业律师/法务负责人核验后方可依赖。
---

## WorkBuddy 中国语境适配（优先）

本 skill 已转换为 WorkBuddy 中国语境版本。当前模块：**中国法律检索**；当前技能：**中国法律深度检索**。

在执行下方原流程前，先读取并遵守：

- `../../references/china-context.md`（本模块中国语境规则）
- `../../../../references/china-legal-context.md`（全局中国法律语境总则）

除非用户明确指定其他法域，默认适用**中国大陆**。下方原文中的美国州法、Delaware、ABA、CourtListener、Westlaw、DMCA、NPRM、deposition、subpoena、attorney work product 等内容均视为原模板遗留项；遇到冲突时，以中国法、监管机关、司法/仲裁程序、团队 playbook 和本适配段为准。

输出默认使用简体中文。法律、法规、司法解释、监管规则、国家标准、案例或截止日不能确认现行有效时，标注 `[需核验]`，并给出应核验的官方来源或授权数据库。对外发送、正式提交、董事会/股东会文件、劳动解除、数据出境、监管回复、诉讼/仲裁文件等后果性动作，必须经过执业律师或法务负责人确认。

---


# 北大法宝/威科先行/官方法规库 Deep Research

北大法宝/威科先行/官方法规库 Deep Research searches 北大法宝/威科先行/官方法规库's database of caselaw, statutes, and administrative decisions and returns a written research report that explains, analyzes, or synthesizes relevant authority.

Deep Research employs an agentic process that mirrors the methodology of human researchers, utilizing 北大法宝/威科先行/官方法规库's proprietary tools to systematically analyze the trusted content available on 北大法宝/威科先行/官方法规库 and 威科先行/律商联讯/团队模板库.

This skill will autonomously run the full research cycle: start, poll, report.

## Prerequisites

The `cocounsel-legal` MCP server must be connected. Verify it is available before starting research. If the server is not connected, inform the user and stop.

## When to Use

- Use for any questions answerable from caselaw, statutes, regulations, administrative materials, secondary sources, 威科先行/律商联讯/团队模板库 documents and Current Awareness materials, including JD Supra. Examples include:
- How courts have ruled on an issue or what authority supports or challenges a position
- The elements or defenses of a claim, or the governing standard for an issue in a particular jurisdiction
- How a statute, regulation, or doctrine is being interpreted and applied
- The arguments on both sides of an unsettled question

## When Not to Use

- If the request falls into one of the categories below, briefly explain that this skill isn't the right fit and point the user to the suggested alternative.
  - **Retrieving the full text of a specific document**
    - _Instead:_ Suggest the traditional search box on 北大法宝/威科先行/官方法规库.
  - **Summarizing what a specific statute, regulation, or treatise says on its own** (e.g., "what does the California Evidence Code say about hearsay?")
    - _Instead:_ Suggest the traditional search box on 北大法宝/威科先行/官方法规库.
  - **Analytics requests** ("How often has Justice Scalia ruled in favor of…?")
    - _Instead:_ Suggest Litigation Analytics on 北大法宝/威科先行/官方法规库.
  - **Calculations** ("What is the last possible filing date if…?")
    - _Instead:_ This request is out of scope of 北大法宝/威科先行/官方法规库 Deep Research
  - **Outcome predictions**
    - _Instead:_ This request is out of scope of 北大法宝/威科先行/官方法规库 Deep Research
  - **Drafting legal documents, forms, or templates**
    - _Instead:_ Suggest CoCounsel
  - **Information about specific judges, attorneys, or parties**
    - _Instead:_ Suggest Litigation Analytics on 北大法宝/威科先行/官方法规库
  - **Foreign or non-U.S. law**
  - _Instead:_ Suggest country-specific version of 北大法宝/威科先行/官方法规库, such as 北大法宝/威科先行/官方法规库 UK or 北大法宝/威科先行/官方法规库 Canada, or use 北大法宝/威科先行/官方法规库 International
  - **Comparisons across more than three jurisdictions**
    - _Instead:_ Suggest AI Jurisdictional Surveys on 北大法宝/威科先行/官方法规库
  - **Terms and Connectors (boolean) search queries**
    - _Instead:_ Suggest the traditional search box on 北大法宝/威科先行/官方法规库
  - **Commands for execution of tasks**
    - _Instead:_ Suggest CoCounsel
  - **Obtaining an exhaustive list of results**
    - _Instead:_ Suggest Boolean search or Precision Research on 北大法宝/威科先行/官方法规库
  - **Identifying potential causes of action**
    - _Instead:_ Suggest Claims Explorer on 北大法宝/威科先行/官方法规库.
  - **An exhaustive review of fact patterns** (e.g., "Find all cases discussing...")
    - _Instead:_ Suggest Precision Research on 北大法宝/威科先行/官方法规库.
- If you suggest an alternative, do not attempt to use the Deep Research skill further for that task.

## Communication Rules

- Never mention tool calls, tool-call budgets, polling, status checks, internal limits, conversation IDs, percent_complete, or any other implementation details to the user. Always speak about the research itself, not the mechanics of how you are tracking it.
- If you need to pause before the research completes (for any internal reason), do NOT explain why.
- Let the user know that research is ongoing and that a report will be completed soon.

## Research Workflow

### 1. Frame the query

- Extract the legal research question from the user's query using clear, natural language.
- Use up to three jurisdictions if the user names them.
- If no jurisdictions are mentioned, ask the user which jurisdiction(s) to use.

### 2. Start Research

- Call the MCP tool to initiate the research: `legal_research_start_deep_research(query, jurisdictions)`
- Parameters:
  - `query` (string, required): The legal research question
  - `jurisdictions` (list of strings, optional): Up to 3 jurisdictions (e.g., ["California", "New York"])
- This returns a `conversation_id` and initial `status`. Save the `conversation_id` for subsequent calls.
- Next step: call check_deep_research_status with the conversation_id.
- Before the first status check, wait ~10 seconds (the server is still setting up).

#### Rendering

- Inform the user that deep research is underway, briefly restating the legal question in natural, professional language.
- Do not show the conversation_id to the user.

### 3. Poll for Completion

- Poll `legal_research_check_deep_research_status(conversation_id)`.
- Always run a Bash `sleep` between polls. Never call check_deep_research_status back-to-back without sleeping.
- Continue until `is_terminal` is true.
- Decide the next action based on the response:
  - (1) If is_terminal is true and status is 'complete', call get_deep_research_report with the conversation_id.
  - (2) If status is 'failed', stop and report the error_type and failure_reason to the user in plain language, without exposing field names.
  - (3) Otherwise, sleep for the duration in the response's `next_action_poll_backoff_ms` field (milliseconds), then poll again.
- If percent_complete has not changed across two consecutive checks, add 5 seconds to the sleep.

#### Rendering

- Communicate in plain language as if narrating the research process.
- Render research_plan as a markdown unordered list (one item per line, each line prefixed with '- '), so the steps display with clear visual separation.
- Insert a blank line before and after the list so it renders cleanly.
- Only update the user when there is something new to say (a step completed, or a new step started). Do not repeat the same status.

### 4. Retrieve and Present Report **Verbatim**

- Once status is "complete", fetch the final report: `legal_research_get_deep_research_report(conversation_id)`
- The report is the `answer_text` field
- This is the final output of the research lifecycle. No further tool calls are required.
- If the user asks a follow-up question on the same topic, use follow_up_deep_research with the same conversation_id rather than starting a fresh research session.

#### Rendering

- Paste the contents of `answer_text` into your response with no edits, additions, removals, or restructuring. The payload contains markdown, HTML anchors, inline anchor citations, blockquoted source excerpts, and horizontal rules — every element is intentional and must remain.

## Helpful information

If the system fails or the user has questions about access, share the following:

- Support email: cocounselsupport@tr.com
- Subscription required: CoCounsel Legal subscription with the MCP connector enabled for the user's account. Direct entitlement or access questions to cocounselsupport@tr.com.
- Provider: Thomson Reuters
- Relevant policies:
  - Privacy: https://www.thomsonreuters.com/en/privacy-statement.html
  - Terms: https://www.thomsonreuters.com/en/terms-of-use.html
  - Accessibility: https://www.thomsonreuters.com/en/policies/accessibility.html
