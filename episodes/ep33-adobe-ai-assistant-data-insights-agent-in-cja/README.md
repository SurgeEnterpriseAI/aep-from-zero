# Episode 33: Adobe AI Assistant & Data Insights Agent in CJA

**Watch:** Video coming soon on iTV

Part 4: Multiply the team (AI) · [Previous](../ep32-adobe-analytics-vs-customer-journey-analytics/) · [Next](../ep34-rag-explained-simply-ai-chatbot-on-your-data/)

## What you will learn

- What built-in AI assistants are **good at** and **bad at**, and the **verification habit** that goes with them
- How to ask an assistant about **your own build** (schema usage, audience overlap, journey status) and **score every answer** against a truth you wrote down first
- The honest **2026 naming tangle**: AI Assistant, Data Insights Agent, Ask Coworker, CX Enterprise Coworker
- How to use **generated content** safely: brand checks, written rejection reasons, human approval
- The **data boundaries** and governance rules for work done with AI

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers. In episode 32, Rohan Desai, the analyst, answered the board's Adobe Analytics question in one memo, and Act Three closed. Now it is Monday of week six. Bloom's team of five is doing the work of twenty, and Vikram Joshi, the solution architect, brings the stack's newest colleague: an AI that answers questions in plain language, and is sometimes confidently wrong.

## Key ideas

### 1. A fast colleague with imperfect recall
An **in-product assistant** is AI built into the Adobe applications. It is good at tedious work: explaining an object, drafting a query, summarising what changed, suggesting a starting point. It accelerates people who know what good looks like, and **accelerates mistakes** for people who do not. A **hallucination** is a fluent, confident, wrong answer.

There are two kinds of question:
- **Product knowledge:** how does something work? ("What does a merge policy do?")
- **Operational:** what is true about *your* objects? ("Which schemas use the BloomID namespace?")

### 2. Write the truth first: ten questions about your own build
Before her first prompt, Kavya wrote ten questions about Bloom's build (four on schema usage, three on audience overlap, three on journey status), each with the true answer and where it lives. **Prompting** matters (give context, constraints and the shape of the answer you want), but the valuable skill is **knowing which question needs answering**.

| Kind | Example question | True answer (Bloom's build) |
|---|---|---|
| Schema usage | Which schemas use the BloomID namespace? | Bloom Order Event only, as its primary identity |
| Audience overlap | How many people are in both Lapsed 90 and Window Shoppers? | None: zero orders ever versus a last order more than 90 days ago |
| Journey status | What state is Bloom Welcome v1 in? | Live since relaunch Monday; read-only, so a change means a new version |

All ten, with answers, are in the exercise. Note: the repo's `sample-profile-priya.json` lists BloomID in its identityMap as a teaching shape; in Bloom's real build the customer profile schema declares only Email.

### 3. Score: right, incomplete or wrong
Ask, copy the answer word for word, compare it with the **build itself**, give a **verdict**, write the **correction**. Kavya's results: most right, two incomplete, one confidently wrong.

| Question | Assistant said | Verdict | Correction |
|---|---|---|---|
| Which schemas use BloomID? | Customer profile and order event | **Wrong** | Order event only, as primary identity (Schemas, Browse confirms) |
| What state is Bloom Welcome v1 in? | Live, and nothing more | **Incomplete** | Right, but left out that a live journey is read-only; changes need a new version |
| Lapsed 90 and Window Shoppers overlap? | Explained how overlap works | **Incomplete** | A product-knowledge answer to an operational question; no count |

Why it mattered: a customer who has never ordered has no BloomID identity to look up.

### 4. One specialised-agent flow
As this series frames it, **Agent Orchestrator** is a reasoning engine, specialised agents (data engineering, audiences, journeys) and conversation memory. Vikram ran one overlap check on Lapsed 90 and Window Shoppers: no overlap, which matches the rules. Kavya recorded **what it did on her behalf**: what it read, compared and changed (nothing). An **agent** is AI that takes steps with tools towards a goal; agents are episode 35.

### 5. AI Assistant in CJA, the Data Insights Agent, and the naming tangle
- **AI Assistant** in Customer Journey Analytics (CJA) has two parts: **Product Knowledge** and the **Data Insights Agent**. Adobe says it is available to all CJA tiers, with an Admin Console permission and the organisation's acceptance of generative AI legal terms.
- The **Data Insights Agent** answers data questions by building visualisations in a Workspace panel.

| Builds | Does not build |
|---|---|
| Line, Multi-line, Freeform table, Bar, Donut, Summary number | Flow, Fallout, Cohort table, attribution (and others) |

- **The tangle (October 2026):** Adobe's pages give Data Insights Agent access "through February 28, 2026" and "through March 31, 2026"; both have passed, and Adobe points to licensing Agent Orchestrator. **CX Enterprise Coworker** went generally available on 10 June 2026, standalone or as an add-on. In Bloom's login, the CJA header icon says **Ask Coworker**, and a banner calls Coworker "an evolution of AI Assistant". Adobe does not say whether Coworker replaces AI Assistant or the Data Insights Agent.
- **The rule:** what your own login shows is the fact. Screenshot it, with the date.

### 6. Generated subject lines: keep two, explain three
In Adobe Journey Optimizer (AJO), generative AI drafts subject-line and copy variants, with brand kits and guardrails steering generation. Kavya generated five lines for the next Bloom Win-Back send:

| Line | Verdict | Reason |
|---|---|---|
| Your skin has missed you, and so have we | Keep | Warm and true |
| A little something to welcome you back | Keep | True: every Lapsed 90 customer is eligible for the 20% Comeback |
| 30% off, today only | Reject | An offer that does not exist at Bloom |
| Clear skin in 7 days, guaranteed | Reject | A result no wellness brand can honestly promise |
| LAST CHANCE (in capitals) | Reject | Shouting breaks the brand sheet's tone rules; the urgency is false |

Divya, not the tool, approved the two kept lines.

### 7. Intelligent captions: check the unit
**Intelligent captions** summarise a CJA chart in words. They work on Line, Bar, Horizontal bar, Area, Donut, Fallout and Flow (at least 3 data points), in CJA only. Illustrative example: a Flow's email node holds 600 path views, and a caption says the top path into email "accounts for 48 People" (8%). 48 ÷ 600 = 8%, so the base is **path views**. Correct it to "48 of 600 paths through email came from that channel".

### 8. Data boundaries
- **Never paste customer data** into a tool that has not been approved for it. It is often a contractual and legal requirement.
- **Accepting generative AI terms is the organisation's decision**, not one person's click.
- **AI may draft; a human approves, and the approver is accountable** (a **human in the loop**).
- Know which tools in your stack are cleared for which data.
- Log every check in the **AI evidence sheet**: prompt, output, verdict, correction.

Interview line: *"AI may draft. A human approves, and the approver is accountable."*

## In the product

Labels as of October 2026. Availability depends on licences and permissions; check what your screen shows.

1. **Experience Platform:** AI Assistant appears inside the Experience Platform interface. Availability varies by entitlement and sandbox.
2. **CJA header:** the icon just left of **Help** shows the tooltip **Ask Coworker**. Its card says "Tell CX Enterprise Coworker your goal and let it handle the execution" and offers **Try now**. Do not click it: it may start a trial or ask the organisation to accept AI terms. The **Create project** banner calls Coworker "an evolution of AI Assistant".
3. **Data Insights Agent set-up (administrators):** Admin Console permissions **AI Assistant: Product Knowledge** and **Data Insights Agent**; data views are enabled under **Data Management**, **Data views**, **Enable for Data Insights Agent**.
4. **Intelligent captions:** click the **Intelligent captions** icon at the top right of a visualisation. Step through every caption with **<** and **>**. Rate with **Good response**, **Bad response** or **Report**. The **Intelligent Captions** permission and generative AI terms are required.
5. **Journey Optimizer:** no menu path is given here for generative AI; check what your screen shows. Practise only on a message you own, in a development sandbox, and never click Activate, Publish or Send proof.

## Common mistakes

- Treating a fluent answer as a checked answer, or asking first and judging afterwards.
- Checking only the answers that look odd; the dangerous ones look normal.
- Asking the Data Insights Agent for a fallout or a flow.
- Choosing the subject line that sounds best without checking that it is true.
- Pasting a caption into a board slide without checking its unit.
- Pasting customer data into a free AI tool.

## Glossary

| Term | Meaning |
|---|---|
| In-product assistant | AI features built into the Adobe applications themselves |
| AI Assistant | Adobe's in-product assistant for product questions and, in CJA, data questions |
| Product knowledge question | A question about how the product works |
| Operational question | A question about your own objects: schemas, audiences, journeys |
| Data Insights Agent | The part of CJA's AI Assistant that answers data questions with charts |
| CX Enterprise Coworker | Adobe's 2026 AI offering that CJA calls "an evolution of AI Assistant" |
| Agent Orchestrator | As this series frames it: a reasoning engine, specialised agents and conversation memory |
| Intelligent captions | Summaries of a CJA chart written by AI; check every number |
| Hallucination | A fluent, confident, wrong answer |
| Human in the loop | A named person who reviews and is accountable for AI output |
| AI evidence sheet | A log of prompt, output, verdict and correction for every AI answer you check |
| Path view | One pass along a path in a flow; one person can produce several |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: AI Assistant in Customer Journey Analytics, Data Insights Agent, Intelligent captions, CX Enterprise Coworker, Agent Orchestrator, AI Assistant in Experience Platform, generative AI in Journey Optimizer

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
