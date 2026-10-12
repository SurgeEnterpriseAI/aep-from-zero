# Episode 01: What Is Adobe Experience Platform? CDP Explained

**Watch:** [Watch episode 1 on YouTube](https://youtu.be/5ddhP_wBBG0)

Part 1: Know your customer (AEP and Real-Time CDP) · Previous: none, this is episode 1 · [Next](../ep02-aep-architecture-data-lake-vs-profile-store/)

## What you will learn

- Explain in one sentence what a Customer Data Platform (CDP) does.
- Name the four parts of the stack (AEP, AJO, CJA and the AI layer) and what each hands to the next.
- Explain why Real-Time CDP is the commercial name for AEP's profile, audience and activation capabilities, not separate software.
- Describe Bloom's problem in business terms.
- Name the four acts of the programme, what Bloom gains in each, and who on the team leads each one.

## The story so far

The story starts here. Kavya Menon, a marketing technologist who has never opened Adobe, joins Bloom, a direct-to-consumer skincare and supplements brand.
Bloom has 1.2 million customers spread across three systems that do not talk to each other, so everyone gets the same email, twice a week, with the same 20% discount.
At the Monday stand-up, Anjali Mehta (CMO) sets the clock: the loyalty relaunch goes live in two weeks, and the board sees results on Demo Day.
Vikram Joshi, the solution architect, picks up a marker and draws the map.

## Key ideas

### 1. Bloom's problem: three systems that never talk

Bloom's customer data sits in three tools, bought at different times by different teams:

| System | What it holds | What it cannot tell you |
|---|---|---|
| E-commerce platform | Orders | Who the buyer really is |
| CRM export (customer relationship management) | Names, emails, loyalty points | What they bought last night |
| Email tool | Who opened what | Whether opens became orders |

Bloom can say how many orders happened yesterday, but not whether yesterday's buyer is the person who complained last week. What it costs:

- **Money:** a 20% discount for people who would have paid full price.
- **Time:** a "not bought in 90 days" list takes two days of Excel matching.
- **Customers:** the welcome email is a Tuesday batch job, so new customers wait up to six days.
- **Revenue:** thousands of rupees of product abandoned in carts every night.
- **Direction:** nobody can say which campaigns make money.

**Technical term:** fragmented (siloed) customer data. **Plain version:** you know your transactions, not your customers.

### 2. Customer Data Platform (CDP)

**A Customer Data Platform collects the fragments, joins them into one person, and makes that person usable in real time.**

- **Collect:** bring every fragment (an order, a loyalty record, an email open) into one place, in one shared format.
- **Join:** recognise that those fragments belong to the same human being.
- **Usable in real time:** the joined person is ready when a message, a website, a report or an AI tool needs her.

Storing data is the easy part; the value is in joining and using. Episode 2 defines "real time" layer by layer.

### 3. One customer, many keys

Each system knows the same customer by a different key. Take Priya Sharma, a Gold member with 2,340 points:

| Where Priya shows up | What it knows her by |
|---|---|
| CRM export | Her email, tier and points |
| E-commerce platform | Orders carrying her email and her BloomID (Bloom's own customer number) |
| Bloom app on her phone, before she signs in | Only an anonymous app ID |
| Email tool | Her address and what she opened |

A CDP joins these using the **identifiers** each record carries, such as an email address. Episode 7 shows how her anonymous app activity gets linked to her.

### 4. The Adobe Experience Cloud map

**Adobe Experience Cloud** is Adobe's family of marketing and customer-experience products that share one data foundation. Four parts matter in this course:

| Part | Think of it as | What it does |
|---|---|---|
| Adobe Experience Platform (AEP) | The memory | Collects data from everywhere; keeps one live profile per person |
| Adobe Journey Optimizer (AJO) | The voice | Decides when and how to talk to each person (email, SMS, push, in-app); reads the memory first |
| Customer Journey Analytics (CJA) | The eyes | Looks back across every channel and answers "what worked?" |
| The AI layer | The colleague | Answers questions, drafts content, does routine work through agents |

**What each hands to the next:**

1. AEP hands AJO a profile for each person and **audiences** (groups of people defined by a rule). AJO reads those audiences directly.
2. Every message AJO sends, and every journey step a customer takes, leaves a record.
3. CJA reads those records alongside orders and website visits, and answers which journey earned money.
4. CJA's answers flow back into AEP as new audiences for the next message.
5. The AI layer helps at every step.

Adobe Experience Manager (AEM) manages websites and content. It is part of the same family, but this course does not cover it.

### 5. Real-Time CDP is a commercial name, not separate software

**Real-Time Customer Data Platform (Real-Time CDP, often written RT-CDP)** is the commercial name for three capabilities inside AEP:

- **Profiles:** the joined, current record of each person.
- **Audiences:** groups of people defined by a rule, such as "Gold members with no order in 90 days".
- **Activation:** sending an audience out to where it is used, such as an email system, an ad platform or cloud storage.

When a job post asks for "RT-CDP experience", it means: can you work with profiles, audiences and activation inside AEP?

### 6. Four acts, four gains, four leads

The programme runs in four acts over about six weeks. The build carries forward: nothing is a throwaway.

| Act | Product | What Bloom gains | Lead voice |
|---|---|---|---|
| I. Know your customer | AEP and Real-Time CDP | Three disconnected databases become one real-time profile with governed audiences | Farhan |
| II. Speak to your customer | Adobe Journey Optimizer | Twice-a-week blasts become event-driven, personalised journeys with guardrails | Divya |
| III. Prove what worked | Customer Journey Analytics | Every journey seen end to end; answers fed back into activation | Rohan |
| IV. Multiply the team | AI and capstone | AI takes over repetitive work; the team presents on Demo Day | Vikram |

### 7. The team and the clock

| Name | Role | In one line |
|---|---|---|
| Anjali Mehta | Chief Marketing Officer | Funded the programme; asks business questions |
| Farhan Qureshi | Data engineer | "Show me the row." Distrusts green ticks |
| Divya Nair | CRM and journeys lead | Guards the customer's inbox |
| Rohan Desai | Analyst | "Which model? Which window?" |
| Tara Joseph | Legal and privacy counsel | "Nothing moves without consent, and nothing restricted leaves the building." |
| Vikram Joshi | Solution architect and mentor | "Say it in one sentence." |
| Kavya Menon | New marketing technologist | "Wait, say that again slowly." She is you |

The clock: the loyalty relaunch goes live in two weeks; Demo Day is about six weeks away. The goal is one customer Bloom truly knows.

## In the product

Labels as of October 2026.

1. Sign in to Adobe Experience Cloud at `experience.adobe.com`.
2. Open the **App switcher**, the nine-dot icon at the top right.
3. Choose **Experience Platform**.
4. Different logins see different applications. Whatever your own screen shows is the fact.

On a first visit, look, screenshot, leave. Episode 2 explains the Experience Platform left menu.

## Common mistakes

- **Treating Real-Time CDP and AEP as two products.** Same software; never list them on a CV as two tools.
- **Calling CJA "Adobe Analytics".** Adobe Analytics is a different, older product (episode 32 compares them).
- **Thinking a CDP is just a bigger database.** Storage is the easy part; joining and using are the job.
- **Matching customers by name.** Two customers called Priya Sharma can be two different people. Join on identifiers.
- **Thinking AJO needs its own customer list.** It reads audiences from AEP.
- **Starting with the tool.** Name the business pain first, then the product.
- **Rushing to journeys under a deadline.** Act II stands on Act I's foundation.

## Glossary

| Term | Meaning |
|---|---|
| Customer Data Platform (CDP) | Software that collects customer data from many systems, joins it into one person, and makes it usable in real time. |
| Adobe Experience Cloud | Adobe's family of marketing and customer-experience products that share one data foundation. |
| Adobe Experience Platform (AEP) | The data foundation: ingestion, datasets, profiles, audiences, governance. "The memory." |
| Real-Time Customer Data Platform (Real-Time CDP) | The commercial name for AEP's profile, audience and activation capabilities. |
| Adobe Journey Optimizer (AJO) | Builds and runs customer journeys and campaigns across email, SMS, push and in-app. "The voice." |
| Customer Journey Analytics (CJA) | Cross-channel, person-based analytics over AEP datasets. "The eyes." |
| AI layer | Assistants and agents across the stack that answer, draft and do routine work. "The colleague." |
| Adobe Experience Manager (AEM) | Adobe's website and content product; part of the family, not covered in this series. |
| Audience | A group of profiles defined by a rule that the platform keeps re-evaluating. |
| Activation | Sending an audience to a destination with a mapping of which fields go along. |
| Journey | A path one person moves through, with steps, decisions and waits. |
| Schema | The blueprint for one kind of record. Episode 3 explains it. |
| App switcher | The nine-dot icon, top right, listing the applications your login can open. |

## Exercise

Do the tasks in [exercise.md](exercise.md): paper-only by default, with an optional look-only track if you have Adobe access.

## Further reading

- [Getting around the Platform UI](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-ui/ui-guide)
- Search Experience League for: Real-Time Customer Data Platform overview
- Search Experience League for: Adobe Journey Optimizer overview
- Search Experience League for: Customer Journey Analytics overview

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
