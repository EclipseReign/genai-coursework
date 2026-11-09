# Research on Generative AI Applications

This report examines four workflows, the value a team could measure, and the engineering work needed before deployment. Implementation examples are based on vendor documentation checked on 9 November 2026. The proposed metrics and controls are evaluation ideas. This report was prepared with AI assistance.

[GenAI vocabulary and frequency counts](vocabulary.md) · [Term-to-use-case graph](vocabulary-graph.png)

## 1. Software development and testing

When a developer describes a missing validation rule, a coding assistant can inspect related files, draft a patch, and run a test. Inline code completion also reduces the effort of writing routine code such as request handlers. The business value is a shorter time from task to reviewed change. A pilot can compare median time to an approved pull request and defects found after merging for similar tasks.

The context window limits how much of a repository the large language model (LLM) can consider, so the prompt should include relevant interfaces, dependencies, and expected failure cases. A plausible patch can use a nonexistent API or pass tests that miss the bug. Keep a human-in-the-loop review step and check boundary cases, dependencies, and security before merging. Give the assistant access only to the repositories it needs.

**Existing implementations**

- GitHub Copilot proposes inline code in supported editors and can work on assigned issues that result in pull requests. [GitHub Docs](https://docs.github.com/en/copilot/get-started/about-github-copilot)
- Cursor Agent searches the codebase, edits related files, and runs commands such as tests from the editor. [Cursor Docs](https://cursor.com/help/ai-features/agent)

## 2. Enterprise knowledge search

An employee asks which expenses require preapproval. Retrieval-augmented generation (RAG) retrieves relevant policy passages and gives them to the model before it writes an answer. Chunking sets the size and boundaries of each passage, and an embedding can help match the question to passages with different wording. The business value is faster access to current rules. A pilot can measure time to a verified answer and the share of answers supported by the current policy.

Grounding depends on the quality of the passages retrieved. A superseded policy can produce a convincing but wrong answer, and a passage can be cut off before a crucial exception. Access control must filter documents before their contents reach the model. Treat retrieved text as data because a document can contain a prompt injection. Return links to the underlying passages so employees can check the evidence and route unanswered questions to the policy owner.

**Existing implementations**

- Microsoft 365 Copilot can ground responses in organizational content through Microsoft Graph, within the signed-in user's permissions. [Microsoft Learn](https://learn.microsoft.com/en-us/copilot/plan/copilot-overview)
- Glean AI Answers uses company documents the user can access and cites them in answers shown in search results. [Glean Docs](https://docs.glean.com/user-guide/assistant/ai-answers)

## 3. Customer support with order lookup

An AI agent retrieves an approved help article and uses it to draft a reply about delivery policy. If the customer wants an update on a specific order, a tool call can look it up after the customer verifies their identity. The business value is faster resolution of routine inquiries and more time for support staff to handle disputes. Track confirmed resolution, repeat contacts, and customer satisfaction alongside response time.

A guardrail should block disclosure when the order belongs to a different account and reject changes that fall outside the support policy. A malicious customer message might tell the agent to ignore those rules. Validate tool arguments and enforce permissions in the service that owns the data. If a write operation times out, check whether it took effect before retrying. Route ambiguous or exceptional requests to a support specialist with the conversation history and any confirmed lookup results.

**Existing implementations**

- Intercom Fin uses support content to answer questions and can run configured Procedures with data connectors and human escalation. [Intercom Help](https://www.intercom.com/help/en/articles/12495167-fin-procedures-explained)
- Salesforce Agentforce Service Agent can use actions to retrieve service data and answer requests in customer conversations. [Salesforce Trailhead](https://trailhead.salesforce.com/content/learn/modules/agentforce-service-agent-quick-look/explore-use-cases-for-agentforce-for-service)

## 4. Marketing image production

A text-to-image workflow can turn a campaign brief into several concept images. The prompt describes the audience, composition, and aspect ratio, while a reference image helps communicate the intended style. The business value is a faster first review and more options to test for different channels. Compare time to an approved asset, approval rate, and hours of editing per published asset with the existing workflow.

Inpainting can replace a selected background while keeping the rest of the composition. Logos, product geometry, and text may still come out wrong, especially across a series of variations. Use source assets with documented rights, add exact logos and typography in the design editor, and have a designer check brand fit, factual accuracy, and usage rights before release.

**Existing implementations**

- Adobe Firefly Generative Fill edits a brushed region of an image using a written description and optional visual references. [Adobe Help](https://helpx.adobe.com/firefly/web/work-with-images/edit-images/generative-fill.html)
- Canva Magic Media generates images from descriptions and lets users add the results to an existing Canva design. [Canva Help Center](https://www.canva.com/help/using-magic-media/)
