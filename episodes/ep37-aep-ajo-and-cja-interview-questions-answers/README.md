# Episode 37: AEP, AJO and CJA Interview Questions & Answers

**Watch:** Video coming soon on iTV

[Previous](../ep36-aep-ajo-and-cja-capstone-project-demo-day/) · [Series home](../../) · [Start again from episode 1](../ep01-what-is-adobe-experience-platform-cdp-explained/)

## What you will learn

- The **answer pattern** strong candidates use: claim, example, trade-off, verification
- The recurring **AEP**, **AJO**, **CJA** and **AI** interview questions, answered from one real build
- How to tell **war stories**, and write **five evidence-backed resume bullets** and a **90-second architecture story**
- What this course did **not** cover, and where to go next

## The story so far

Over six weeks, the team at Bloom, a wellness brand, built one real-time customer profile in Adobe Experience Platform (AEP), journeys in Adobe Journey Optimizer (AJO), measurement in Customer Journey Analytics (CJA), and an AI layer. In episode 36, Kavya Menon presented it all on Demo Day in seven minutes, through one customer, Priya. Then a recruiter called, and Vikram Joshi, the solution architect, offered to play the hiring panel.

## Key ideas

### 1. What a panel is really marking
A panel is quietly asking: is the business measurably better off, can you explain and defend your decisions, and would you be safe in front of a client? **Coverage is not the goal. Judgement is.**

### 2. The answer pattern

| Part | What it sounds like |
|---|---|
| Claim | One sentence that answers the question directly |
| Example | Something you built, with its real names and numbers |
| Trade-off | What your choice cost, and why it was still right |
| Verification | The screen, row or count that proved it, not the green tick |

Keep each answer to about a minute. Naming your trade-off signals seniority.

### 3. AEP questions

| Question | Claim | Bloom evidence |
|---|---|---|
| AEP or Real-Time CDP? | Not separate software: the commercial name for AEP's profile, audience and activation capabilities. | One profile per customer; five audiences; two activated |
| Why are orders events? | Orders never change. Loyalty tier changes in place, so it is profile. | Enabled for Profile checked in Schemas, Browse |
| Walk me through your identity design | Identity stitching turns anonymous traffic into known customers at the moment they authenticate. | Email, ECID and a custom BloomID: one Priya, three identities |
| An ingestion failure | 14 of 14 mapped is not 14 of 14 correct. Partial ingestion sets the blast radius. | Three rows rejected, seven errors logged, 497 good orders lost; 497 loaded at a 5% threshold |
| Green everywhere, empty profile | The lake received it, the identity graph received it, the profile store did not. Here is the row that proves it. | Records in Profile blank in Batch end-to-end; re-ingest, then escalate |
| Sources disagree | The merge policy is a business decision, not a technical default. | Dallas (2023 record) versus Austin (2026 app update) |
| Batch or streaming? | Will a journey need to react within minutes? If yes, streaming. If not, batch. | Two of five audiences designed as streaming (Cart Abandoners 24h, New This Month); three batch |
| Governance | Consent is a profile attribute enforced by the platform, not a process document enforced by goodwill. | Ananya never enters Lapsed 90; phone labelled C2 |

**Identity design is the most common senior question.** Walk it through Priya: a 7:44 PM add-to-cart carrying only an ECID; an app sign-in carrying the ECID and her email together (the **linking event**); a 7:52 PM laptop order carrying her email and BloomID. Trade-off: BloomID became an identity only through orders, so a customer who never ordered cannot yet be found by it. Risk: a shared family tablet can merge two relatives. Verification: by email or by BloomID, the same person returns. (`sample-profile-priya.json` lists BloomID in its identityMap only as a teaching shape.)

**Honesty rule:** tell a story such as "the policy blocked the export" only once it is true in your own sandbox.

### 4. AJO questions
- **Journeys versus campaigns versus decisioning:** "A campaign answers what do we send. A journey answers what happens to this customer next." Bloom Gold Thank-You is a campaign; Bloom Welcome v1 and Cart Rescue v1 are journeys. Decisioning chooses the offer inside Bloom Win-Back's email: "A library is not a decision."
- **Whiteboarding:** practise drawing both journeys from memory.
- **Testing:** "Test mode, Simulation and Send proof can reach a real inbox. Dry run never does." Bloom proved its split with Dry run path counts, because Test mode only ever took the top branch.
- **Triage:** read the step events in order: entry, qualification, wait, action, delivery. No action row means no message was attempted, so it was never the cap.
- **Capping:** "Frequency capping applied per journey is not frequency capping." Bloom's two marketing emails per profile per week sit in the global rule set; a Draft rule set protects nobody.

### 5. CJA questions
- **Adobe Analytics versus CJA:** "CJA is person-based, dataset-based and retroactive." One example each, then the honest part: segments and calculated metrics must be rebuilt, Activity Map and Contribution analysis are not supported, and alerts are not hourly.
- **Person ID:** "A connection with the wrong person ID produces confident, wrong numbers." It is case sensitive.
- **Derived fields:** report-time and retroactive. A Lowercase rule merged "email" (150 orders) and "Email" (30) into 180.
- **Attribution:** "Attribution models are assumptions, not truths. Name the model and the window every time." Give ranges, not a winner.
- **A defensible number:** Cart Rescue recovered 11.8% against 7.9% for a 10% holdout. Call it soft (two weeks) before anyone else does.
- **The closed loop:** "Closing the loop means the next campaign changes." Checkout Leakers - Mobile feeds Checkout Rescue, with the expected effect and baseline written first.

### 6. AI questions
- **Governing AI work:** "AI may draft. A human approves, and the approver is accountable." Log prompt, output, verdict and correction.
- **Where RAG fails:** "Fluent but wrong almost always means the right source never reached the model." Re-chunking by headings and sections took Bloom's assistant to at least 8 of 10.
- **Where an agent stops:** "Put the human approval where the action is irreversible." Bloom's 48-hour guardrail tripped in dry-run mode.

### 7. War stories
A **war story** is a concrete problem you hit, diagnosed and fixed. Tell it as **symptom, layer, evidence, fix, prevention**. Your own mistakes are the best material. Kavya's column-order story: **symptom**, a new revenue-per-order column read zero; **layer**, the calculated metric; **evidence**, its name said Orders over Revenue; **fix**, a calculated metric of revenue divided by orders; **prevention**, read every column name first. Describe the fault, never blame people.

### 8. Five resume bullets and the 90-second story
Each bullet is a strong verb, what you built, a number or named object, and an **artefact** someone could ask to see. Kavya's five cover the identity design, the recovered batch, the five audiences, two journeys with a holdout, and the closed loop. Label course work as a **practice project**, never as client experience, and write only what you did yourself.

The 90-second architecture story is the Demo Day spine squeezed: the problem in one sentence; four beats through one customer (identity, audience, journey, measurement); one number with its baseline; one thing you would do differently. Kavya's lesson, as on Demo Day: settle the identity design for every customer number on day one.

### 9. "I don't know, but here is how I would find out"
On the Demo Day rubric, panel questions carry 20 of 100 points; full marks mean direct answers, no bluffing. Say the line, then name how: the documentation, a test in a development sandbox, and the owner you would ask.

**Not covered in this course:** advanced Data Distiller (deeper SQL on the data lake than episode 15), the B2B (business-to-business) edition, CJA administration at enterprise scale, and Adobe Experience Manager (AEM).

## In the product: where your evidence lives

Labels as of October 2026. Look and screenshot; change nothing.

1. **Schemas, Browse:** the **Enabled for Profile** column.
2. **Monitoring, Batch end-to-end:** clear the **ONLY INGEST FAILURES** filter, then read **Records in Profile**.
3. **Segment Builder, Audience properties:** **Estimated profiles** and **Evaluation method**.
4. **Journey canvas:** **Alerts**, and **Dry run** path counts on journeys you own.
5. **CJA, Data Management, Connections:** person ID per dataset and **Records skipped**.

## Common mistakes

- Reciting a definition, or dropping the trade-off.
- Claiming a result you did not see yourself.
- Quoting a number without its model, window or baseline, or hiding that it is soft.
- Resume bullets with no artefact behind them ("familiar with AEP").
- Bluffing past the edge of your knowledge, or blaming people in a war story.

## Glossary

| Term | Meaning |
|---|---|
| Answer pattern | Claim, example, trade-off, verification |
| Trade-off | A deliberate compromise you can explain and defend |
| War story | A concrete problem you hit, diagnosed and fixed |
| Artefact | Reusable evidence of what you built |
| Defensible number | A figure whose model, window and source you can state |
| Baseline | The comparison that gives a number meaning |
| Rubric | The published scoring sheet a panel marks against |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Real-Time Customer Data Platform overview, identity graph, partial batch ingestion, merge policies, Journey Optimizer journeys and campaigns, Journey Optimizer dry run, Customer Journey Analytics compared with Adobe Analytics

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
