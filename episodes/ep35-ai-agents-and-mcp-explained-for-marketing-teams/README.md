# Episode 35: AI Agents and MCP Explained for Marketing Teams

**Watch:** Video coming soon on iTV

Part 4: Multiply the team (AI) · [Previous](../ep34-rag-explained-simply-ai-chatbot-on-your-data/) · [Next](../ep36-aep-ajo-and-cja-capstone-project-demo-day/)

## What you will learn

- Tell an **AI assistant** from an **AI agent**, and explain why autonomy needs limits
- Explain **tools**, **tool calling** and the **Model Context Protocol (MCP)** in plain words
- Trace an agent's tool calls in a **run log**, add a **frequency-guardrail tool**, and test it in **dry-run mode**
- Design **permissions**, **blast radius**, **stopping conditions** and **failure behaviour**
- Place **human approval gates** and an **audit trail**, and write a one-page **agent governance note**

## The story so far

Bloom, a direct-to-consumer wellness brand with 1.2 million customers, is in the last week of its Adobe programme, and Demo Day is days away. In episode 34, Vikram, the solution architect, and Kavya built an honest assistant with retrieval-augmented generation (RAG). Re-chunking by headings fixed a fluent but wrong answer, and the second run passed at least 8 of 10 with citations. But the assistant only answers, and every Monday Divya still drafts the campaign brief by hand.

## Key ideas

### 1. Assistant versus agent
An **assistant** answers when you ask. An **agent** is given a goal: it **plans**, **acts** with tools, **observes** each result and **continues** until the goal is met or a limit is hit. That autonomy is the value and the risk in the same sentence, so judge an agent by what it may do and what stops it, not by how clever its writing sounds.

### 2. The loop and a definition of done
Plan, act, observe, continue. An agent knows it has finished only if you write down what done looks like. For Bloom's brief: an audience, an offer, a recommendation, and every check logged. The **definition of done** is the first **stopping condition**.

### 3. Tools, tool calling and MCP
A **tool** is a capability an agent may invoke: a query, a call to another system, a file write. In **tool calling**, the model never runs the tool itself: it asks for a named tool with inputs, the software around the model runs it, and the result goes back to the model. The **Model Context Protocol (MCP)** is a standard way to describe tools (a name, a plain description of the job, the inputs) so any agent that speaks it can discover and call them. A program that offers tools this way is an **MCP server**. A standard tool is not automatically a safe tool: which tools an agent may use is still your decision.

### 4. Bloom's campaign-brief agent and its run log
The agent comes as a coding notebook (a page of runnable code) in the asset pack and runs outside the Adobe screens. Goal: **"win back lapsed Gold members"**.

| Tool | What it does | Access |
|---|---|---|
| Audience-count lookup | Counts **Lapsed 90** (estimate 3,890 of the 10,000-customer extract) and **Gold Members** | Read-only |
| Offer-library check | **20% Comeback** (Lapsed 90 only) ranks above **Early Access Drop** (Gold only); **Free Shipping** is the fallback | Read-only |
| Brief writer | Saves the draft into one drafts folder | Write, one folder |

The **run log** lists every call with its inputs and outputs. The first run made two calls and proposed a Comeback email for the next morning, and Kavya nearly posted it as finished. Nothing asked what Lapsed 90 had received recently, because no tool could. **An agent can only check what it has a tool for.**

### 5. The frequency-guardrail tool
Divya's rule, written as a contract before any code:

| Part | Frequency-guardrail check |
|---|---|
| Input | The audience name and a 48-hour window |
| Check | Bloom's send log: which message went to which audience, and when |
| Output | Clear, or a warning naming the last message and its time |
| Effect on the draft | On a warning, recommend waiting before any new send |

Journey Optimizer's business rule (at most 2 marketing emails per profile per week, episode 23) acts at send time, and it allows two a week, so a second email could still pass a day after the first. The guardrail catches the clash at planning time. Both belong.

### 6. Dry-run mode, and the trip
In the agent's **dry-run mode** it plans, calls its read-only tools and reports, but changes nothing. It is not Journey Optimizer's **Dry run** (episode 18), which counts how many profiles would take each path of a journey.

The re-run made three calls, and the guardrail **tripped**: **Bloom Win-Back went to Lapsed 90 yesterday afternoon**, and every lapsed Gold member is in Lapsed 90. The brief dropped the next-morning send and recommended waiting. The team then made the code run the guardrail before any brief that recommends a send, because a brake the model may skip is not a brake.

### 7. Build the brake before the engine
- **Narrow permissions**: the narrowest access that still lets the agent finish. Read-only wherever possible; write access scoped to one sandbox, one dataset, one action.
- **Blast radius**: ask "what is the worst thing this could do if it misunderstands?" With Kavya's own full access, a confused agent could publish a journey. With Bloom's design, the worst case is a bad draft.
- **Stopping conditions**: maximum steps, maximum spend on model calls, a timeout and a definition of done. An agent without one is an incident waiting for a trigger.
- **Failure behaviour**: **stop and report** ("offer library unreachable, brief incomplete, here is the log") beats retrying forever, and never guess.

### 8. Approval gates without approval fatigue
Put the human where the decision is **irreversible**: before a send, a delete or an export. Not at every step: people who approve everything soon approve nothing carefully (**approval fatigue**). At Bloom, reading and drafting need no approval; a send needs Divya's decision, and the agent has no send tool at all.

### 9. Audit trail and the governance note
Log what the agent did, why, and with what inputs. If you cannot reconstruct a decision, you cannot defend it to a client or a regulator, or improve the agent. Kavya's one-page **governance note** covers what the agent may do alone, what needs approval and whose, dry-run as the default, stopping conditions, failure behaviour, and who reads the log.

### 10. The 2026 landscape, honestly
Adobe's 2026 agent features include Agent Orchestrator (a reasoning engine with specialised agents and conversation memory). Partners announce agents too, and some of it is still marketing. Adobe's documentation suggests Coworker Chat, part of CX Enterprise Coworker (episode 33), is reachable through an MCP icon and a Customer Journey Analytics (CJA) MCP server, and the October 2026 release notes appear to list a read-only permission for that server. What your own login shows is the fact.

**Interview line:** *"Put the human approval where the action is irreversible."* Back it with your build: a 48-hour guardrail that tripped in dry-run mode and changed the brief.

## In the product

Labels as of October 2026. Bloom's agent runs outside the Adobe screens; these are the screens a person uses for the same checks. Look only.

1. **Adobe Experience Platform**: **Customer**, **Audiences**, **Browse** tab: audience counts.
2. **Journey Optimizer**: **Decisioning**, **Catalogs**: offers and their eligibility.
3. **Journey Optimizer**: **Journey Management**, **Reports**, **Campaigns**: recent sends. Default period **Last 7 full days**; reporting is in UTC.
4. **CX Enterprise Coworker**: Adobe's documentation suggests Coworker Chat reaches CJA data through an **MCP icon** in its left rail. Check what your own login shows.

## Common mistakes

- Judging an agent by its writing instead of its permissions and stopping conditions.
- Trusting a polished draft without reading the run log.
- Leaving a guardrail for the model to call "if it remembers".
- Believing MCP makes a tool safe.
- Connecting an agent with your own full access, or adding a send tool "just in case".
- No stopping condition, retrying forever, or guessing when a tool fails.
- Approval at every step, or no gate before a send, a delete or an export.
- Confusing the agent's dry-run mode with Journey Optimizer's Dry run.
- Pasting customer data into an AI service that has not been cleared for it.

## Glossary

| Term | Meaning |
|---|---|
| Agent | AI that plans, acts with tools, checks results and continues towards a goal |
| Tool | A capability an agent may invoke: a query, a call to another system, a file write |
| Tool calling | The model asks for a named tool with inputs; the software around it runs the tool and returns the result |
| Model Context Protocol (MCP) | A standard way to describe tools so an agent can discover and call them |
| MCP server | A program that offers tools to agents in the MCP format |
| Run log | Every tool call in a run, with inputs and outputs |
| Dry-run mode | The agent plans and reports but changes nothing |
| Blast radius | The maximum damage an action could cause if it goes wrong |
| Stopping condition | The limit that ends a run: steps, time, spend, or goal met |
| Approval gate | A required human decision before an irreversible action |
| Approval fatigue | So many approvals that people approve without reading |
| Audit trail | The log of what an agent did, why, and with what inputs |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

Search Experience League for: Agent Orchestrator, AI Assistant in Customer Journey Analytics, Customer Journey Analytics MCP server, Journey Optimizer business rules, Journey Optimizer dry run.

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
