# Episode 36: AEP, AJO and CJA Capstone Project: Demo Day

**Watch:** Video coming soon on iTV

Part 4: Multiply the team (capstone) · [Previous](../ep35-ai-agents-and-mcp-explained-for-marketing-teams/) · [Next](../ep37-aep-ajo-and-cja-interview-questions-answers/)

## What you will learn

- How to run a **12-point capstone checklist** across Adobe Experience Platform (AEP), Adobe Journey Optimizer (AJO), Customer Journey Analytics (CJA) and the AI layer, where green means evidence
- Why a journey's branches are proven with **Dry run path counts**, not Test mode
- How to structure a **seven-minute technical story** around one customer
- **Demo hygiene:** stable test profiles, ready event payloads, screenshot fallbacks
- How to present **numbers honestly**, with a window, a model and a baseline
- How to answer panel questions with **trade-offs**, and **score peers** against a published rubric

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers. Over six weeks its team built one real-time customer profile, governed audiences, personalised journeys, offer decisioning, cross-channel analytics and an AI layer. In episode 35, Kavya extended the campaign-brief agent with a 48-hour frequency guardrail and wrote its governance note. Tomorrow the board sees everything: Demo Day.

## Key ideas

### 1. The 12-point capstone checklist

The day before Demo Day, the team checks every **seam**, each place where one part of the build hands over to the next. Every point gets a colour: **green** (evidence attached: a row, a count or a screenshot), **amber** (a written caveat) or **red** (fix it today).

| # | Point | Bloom's evidence |
|---|---|---|
| 1 | Schemas | **Enabled for Profile** column in Schemas, Browse (one Save can drop the flag silently) |
| 2 | Ingestion | **Records in Profile** in Monitoring, Batch end-to-end: lake success is not profile success |
| 3 | Identity | Priya by email and by BloomID: one profile, three identities |
| 4 | Audiences | Five relaunch audiences; Lapsed 90 still says 90 days, not 30 |
| 5 | Activation | Mapping is hashed email and loyalty band only. **Amber:** a mapping, not a delivered file |
| 6 | Welcome journey | Was **red** (Test mode evidence); fixed with Dry run path counts |
| 7 | Cart rescue | Exits on any purchase; re-entry at most once in 7 days; 10% holdout |
| 8 | Decisioning | Three offers signed off and approved; Free Shipping fallback |
| 9 | Guardrails | 2 marketing emails per profile per week, in the global rule set |
| 10 | Data view | Bloom Marketing on the stitched person ID; No value labelled a tracking gap |
| 11 | Closed loop | Checkout Leakers - Mobile feeds Checkout Rescue through Read audience |
| 12 | AI evidence | Evidence sheet, golden-set run (at least 8 of 10), agent dry-run log |

Result: eleven green, one amber with its reason written beside it.

### 2. Prove branches with Dry run, not Test mode

Point six was first marked red because its only evidence was a Test mode run. **Test mode** sends real emails to test profiles, and in our testing the **top branch of a split was always taken**. Kavya's Gold seat and Rohan's Silver seat both went down the Gold Members path: the email was proven, the split was not. **Dry run** (the journey's own button, not the agent's dry-run mode from episode 35) shows how many real profiles would take each path and contacts nobody. Divya's Dry run before relaunch Monday showed people on both paths, and those dated counts became the evidence.

### 3. The seven-minute arc

| Part | Suggested time | What to show |
|---|---|---|
| Problem | About 1 minute | What the business could not do, in one sentence |
| Architecture | About 1 minute | AEP the memory, AJO the voice, CJA the eyes, AI the colleague |
| Walkthrough | About 3 minutes | The build working, through one person |
| Numbers | About 1 minute | Each figure with its baseline |
| AI layer | About 1 minute | What the AI does, and how it is checked |

The times are a guide. The rule is: **tell it through a person, not a box diagram.** A component appears only where it moves that person forward. For a shorter slot, use the **five-minute spine**: the problem, four beats (identity, audience, journey, measurement), one number, one thing you would do differently. A first timed run usually takes about twice as long as planned.

### 4. Tell it through Priya: six beats

| Beat | What happens | Artefact |
|---|---|---|
| 1. Anonymous visit | 7:44 PM: a phone in the Bloom app adds a Vitamin C Serum to a cart, ECID only | The web event |
| 2. Stitched identity | Sign-in links the ECID and her email; 7:52 PM laptop order | One profile, three identities |
| 3. Audiences | Gold tier puts her in Gold Members; Cart Abandoners leaves her out (she bought 8 minutes later) | The two rules |
| 4. Journey | The abandon event takes her into Cart Rescue v1 at 7:44; her 7:52 purchase lets her exit before any email | Her journey step events |
| 5. Measurement | In CJA, with stitching, add-to-cart and order are one person, not a false abandon | Bloom 360 and Bloom Marketing |
| 6. The change | Non-Gold mobile shoppers leaked at checkout; the Checkout Rescue journey now sends them a helpful email, not a discount | Checkout Leakers - Mobile, Checkout Rescue |

### 5. Demo hygiene

- **Stable test profiles** staged the day before (a Gold seat and a Silver seat), each with the team member's own inbox.
- **A ready event:** the cart-abandon payload in Postman, aimed only at your own seat. Adobe documents this streaming route; check what your screen shows.
- **Screens loaded** before the panel arrives.
- **The failure path:** a screenshot of every screen, in order, two clicks away. Rehearse the switch.
- **Rehearse in the real sandbox** at the time of day you will present; performance varies.
- **Never click Activate, Publish or Send proof** in a demo. Looking is safe; sending is not.

### 6. Numbers with a window, a model and a baseline

Bloom's figures (fictional sample data, relaunch fortnight, US dollars):

| Number | Window and model | Honest note |
|---|---|---|
| 1,240 orders, $66,260 | Relaunch fortnight | A count, not a result: say what you would compare it with |
| Revenue by channel | Last Touch, 30-day lookback | 520 orders are No value: a tracking gap |
| Average order: Gold $78, Silver $55, Bronze $38 | Relaunch fortnight | An association, not proof |
| Cart Rescue recovery 11.8% | Relaunch fortnight, against a 10% holdout at 7.9% | **Soft:** two weeks. Say so first |

The value is the **gap** against the baseline. With no real baseline, say what you would measure and how.

### 7. Trade-offs and "I don't know"

Write down the **three questions you fear** and answer them on paper; they are almost always about a shortcut. Kavya's: *"Can you look up any Bloom customer by their BloomID?"* Not yet, only customers who have ordered: the customer profile declares one identity, Email, and the BloomID column landed in a plain field, so BloomID becomes an identity through the order event. The trade-off: in week one the team kept the customer schema to one identity, Email, and did not reopen it before the relaunch. Differently: settle the identity design for every customer number on day one, before any data lands.

When you do not know: *"I don't know, but here is how I would find out."* Adobe publishes no time for batch data to reach the profile store, so measure your own batches in Monitoring.

### 8. The rubric and peer scoring

| Criterion | Points | Full marks |
|---|---|---|
| Architecture story | 20 | Survives a "why this design?" challenge |
| Live walkthrough | 30 | Works live; fallbacks used gracefully |
| Business value | 20 | Every capability tied to a number or benefit |
| Panel questions | 20 | Direct, honest, no bluffing |
| Clarity and time | 10 | Seven minutes; anyone could follow |

The panel marks **judgement**, not coverage: is the business better off, can you explain your decisions, would you be safe in front of a client? **Every team member scores two others**, with one written strength and one improvement, because judging a build is a job skill. Keep your **war stories**, such as the batch that loaded nothing and the 9,930 estimate.

Interview line: *"I don't know, but here is how I would find out."*

## In the product

Labels as of October 2026. Read-only checks for your own development sandbox; check what your screen shows.

1. **Schemas**, **Browse**: read the **Enabled for Profile** column.
2. **Monitoring**, **Batch end-to-end**: clear "ONLY INGEST FAILURES: Yes", then read **Records in Profile**.
3. Journey toolbar: **Alerts**, **Simulate** (offers Test mode) and **Dry run** (path counts, contacts nobody; it holds an active-journey slot, so return the journey to Draft afterwards).
4. CJA Workspace, **Project** menu, **Create mobile scorecard**: the exec view.

## Common mistakes

- Marking a point green because a screen looked green.
- Treating an arrived Test mode email as proof that every branch works.
- Opening with the architecture slide, or touring every screen.
- Quoting a big number with no window, model or baseline, or hiding a soft one.
- Bluffing instead of saying how you would find out.
- Scoring a peer with a number but no strength or improvement.

## Glossary

| Term | Meaning |
|---|---|
| Capstone | The end-to-end build, presented and defended |
| Seam | A place where one part of the build hands over to another |
| Spine | The fixed narrative order of a demo |
| Failure path | The prepared fallback when the live system does not cooperate |
| Baseline | The comparison that gives a number meaning |
| Holdout | A randomly withheld group that shows what would have happened anyway |
| Trade-off | A deliberate compromise you can explain and defend |
| War story | A concrete problem you hit, diagnosed and fixed |
| Rubric | The published scoring sheet: 100 points, five criteria |
| Dry run | Counts how many real profiles take each journey path; contacts nobody |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Journey Optimizer dry run, test your journey, Monitoring dataflows end-to-end, Real-Time Customer Profile, Customer Journey Analytics attribution, Customer Journey Analytics mobile scorecard

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
