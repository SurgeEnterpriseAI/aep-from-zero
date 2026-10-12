# Episode 31: Publish CJA Audiences to AEP: Close the Loop

**Watch:** Video coming soon on iTV

[Previous](../ep30-fallout-flow-and-cohort-analysis-in-cja/) · [Next](../ep32-adobe-analytics-vs-customer-journey-analytics/)

## What you will learn

- Publish an audience from **Customer Journey Analytics (CJA)** to **Adobe Experience Platform (AEP)** with **Create audience from selection**, and know its options and limits
- Feed a CJA-born audience into an **Adobe Journey Optimizer (AJO)** journey through **Read audience**, with consent and governance intact
- Draw the **flywheel** and prove a loop is closed by what changes next
- Build an exec dashboard as a **mobile scorecard**, schedule it, and share it safely
- Read the **decisioning report** for offers, and explain how AJO reports relate to CJA

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, in week five of its programme, two weeks into the loyalty relaunch. In episode 30, Rohan Desai, Bloom's analyst, built a fallout from journey entry to purchase and found the real leak: **checkout, on mobile, among non-Gold customers**. He named a confounder, proposed a test, and read the Cart Rescue holdout (11.8% against 7.9%) honestly as soft. Old Bloom would have written a report. Today the team acts on those people instead.

## Key ideas

### 1. Create audience from selection
A group found in analysis can be published back to AEP as an ordinary audience. **Measurement becomes targeting.**
- Right-click in a fallout, freeform table, flow or cohort table and choose the create-audience item (on a fallout touchpoint it reads **Create audience from selection**). Adobe says this pre-fills the audience builder with the dimension or dimension item you selected, so read the filter before you publish.
- The other way in: **Components**, **Published audiences**, **Create audience**.
- Rohan named the audience **Checkout Leakers - Mobile**, checked the filter, used **View sample IDs**, then clicked **Publish**.
- Adobe: it shows up in Experience Platform in "only a minute or two", with **Origin** "Customer Journey Analytics" and the CJA audience ID appended to the name.

Adobe documents the publish step this way; check what your screen shows.

### 2. Options and limits
| Setting or limit | What Adobe says | Bloom's choice |
|---|---|---|
| Refresh frequency | One time, Every 4 hours, Daily, Weekly, Monthly | Daily |
| Refresh lookback window | Days back from today the rule is evaluated; **90 days at most** | 14 days |
| Expiration date | When it stops refreshing; default 1 year from creation | Default, with a review date |
| Filter | Up to 20 segments, joined by And or Or | Mobile, not Gold, added to cart, no purchase, email consent true |
| Size | **At most 20 million people** | Bloom has 1.2 million customers |
| Calculated metrics | **Cannot be included**; one you add is not included in the definition | None |
| Scheduled refresh | Only a limited number of audiences, depending on your package | One recurring audience |

**One time** publishes a frozen snapshot; any other frequency makes the audience recurring. Kavya's revenue per order calculated metric (episode 28) would not be included, so a "small carts only" audience would publish bigger than she believed. Test the confounder in the measurement, not the audience.

### 3. Same consent, same governance
- **An audience published from CJA still has to obey the same consent rules.**
- Bloom's filter for Checkout Leakers - Mobile carries the same condition as Lapsed 90: **email consent is true**, read from the customer profile dataset in Bloom 360. Ananya, who never gave email consent, must never receive Checkout Rescue. The journey also sends only through the **Marketing** channel configuration, which respects opt-outs.
- Adobe: when you publish, the **data governance labels and policies** attached to the fields used in the audience **are recorded**. Adobe says only "recorded", so a person still reads the labels before activation.
- Administrators get **Audience Publishing** automatically. Keep publishing rights to few people.

### 4. Read audience into Checkout Rescue
Divya's **Checkout Rescue** journey starts with **Read audience** on Checkout Leakers - Mobile. Adobe documents this route; check what your screen shows.
- One Read audience per journey, as the first step; only profiles with **Realized** status (currently qualified) enter.
- Schedule: Once, Daily, Weekly or Monthly. Bloom uses Daily with **Incremental read**, so later runs pick up only newly qualified people.
- Adobe says to use **Audience qualification** for real-time needs, but **we found no Adobe page confirming a CJA audience can drive it**, so Bloom promises no real-time rescue.
- The message is **helpful, not discount-led**: nobody yet knows that price was the reason.
- A random holdout is sent nothing, as on Cart Rescue v1. Bloom's two-a-week cap lives in the **global rule set**, so it covers this journey too.

**Write the expected effect before go-live.** More leakers who receive Checkout Rescue buy within 7 days than a random holdout who are sent nothing. Measure the change you made, not the metric that flatters you (such as opens).

### 5. The flywheel
| Part | Where at Bloom | Built in episodes |
|---|---|---|
| Data | AEP datasets, identity, profile | 3 to 9 |
| Audience | AEP Segment Builder | 10 to 12 |
| Journey | Journey Optimizer | 16 to 24 |
| Measurement | CJA: Bloom 360, Bloom Marketing | 25 to 30 |
| Better audience | Published from CJA | 31 |

The proof that a loop is closed is not a dashboard or a published audience. It is **one concrete thing in the next campaign that changed because of the last measurement**. For Bloom, that is Checkout Rescue.

Interview line: *"Closing the loop means the next campaign changes. Otherwise it is just a report."*

### 6. The exec dashboard as a mobile scorecard
- **Project** menu, **Create mobile scorecard** (the Create project dialog also offers **Blank mobile scorecard**). The builder steps are not covered here; check what your screen shows.
- Four tiles, readable at phone width: **revenue by channel** ($66,260 over the fortnight, with "No value" flagged as a tracking gap), **journey performance** (2,000 entries to 132 purchases), **recovery** (11.8% against 7.9% for the holdout, marked soft) and **day-seven retention** (New This Month by first-order week).
- Scheduled to arrive **Monday at 8:00 AM**. Adobe lists scheduled file exports under the **Share** menu.
- **Share with anyone needs no login**, so it is never the way to share board numbers. Share with named Workspace users; keep scheduled recipients short and reviewed.

### 7. Offer reporting and AJO reports
- **Decisioning reporting** shows Total items, Total displays, Total clicks and the **Fallback rate** (instances where no selection strategy qualified and a generic option showed). It needs a live decision and real impressions. Bloom Win-Back goes to Lapsed 90, the people the Comeback offer is built for, so a high fallback rate (Free Shipping) is a question about eligibility.
- AJO all-time reports are **"powered by Customer Journey Analytics"**. **Analyze in CJA** needs a CJA licence; with several connections, the data view must reference the connection flagged **Use in CJA**, or the button may be disabled. Use in CJA bills every row: an owner's decision.
- Audiences created from an AJO report: 25 published per organisation, 5 per user per hour, 20 per user per day.

### 8. Operationalise
A loop that only works while its builder is in the room is not a loop. Name an **owner** per step (Rohan: audience and scorecard; Divya: Checkout Rescue; Tara: consent and the sharing list), a **cadence** (the Monday scorecard at stand-up) and a **review trigger** (no lift over the holdout after four weeks, or the audience size jumping overnight).

## In the product

Labels as of October 2026. Read only in any shared organisation.

1. **Customer Journey Analytics**, **Workspace**: right-click a fallout touchpoint, **Create audience from selection**. The **Create audience** screen shows Name, Tags, Description, **Refresh frequency**, the segments, **Data Preview** (total people, identity namespaces), and **View Sample IDs**, **Cancel**, **Publish**. In a shared organisation, click **Cancel**.
2. **Components**, **Published audiences**: the list of audiences published from CJA, and **Create audience**.
3. **Experience Platform**, **Customer**, **Audiences**, **Browse**: filter the **Origin** column for "Customer Journey Analytics".
4. **Journey Optimizer**, a journey's first step: **Read audience** (Orchestration), with a schedule of Once, Daily, Weekly or Monthly; recurring runs offer **Incremental read**.
5. **Workspace**, **Project** menu: **Create mobile scorecard**. **Share** menu: share with Workspace users, share links, scheduled file exports.
6. **Journey Optimizer**, a campaign, **Reports**, **View all time report**, **Decisioning reporting**; **Analyze in CJA** on reports.

## Common mistakes

- Treating **Publish** as a harmless test: the audience lands in AEP for the whole sandbox.
- Adding a **calculated metric** to an audience filter and trusting the count.
- Assuming an audience from analytics escapes **consent** rules.
- Promising real-time entry: nothing we found confirms CJA audiences can drive **Audience qualification**.
- A daily Read audience without **Incremental read**, which re-reads the same shoppers every run.
- Choosing the success metric **after** seeing the result.
- Sharing board numbers with **Share with anyone**, which needs no login.

## Glossary

| Term | Meaning |
|---|---|
| Published audience | An audience built in CJA and sent to AEP for activation |
| Refresh frequency | How often a CJA audience is re-evaluated: One time, Every 4 hours, Daily, Weekly, Monthly |
| Refresh lookback window | How many days back the rule is evaluated; 90 at most |
| Read audience | A journey entry that reads everyone in an audience, once or on a schedule |
| Flywheel | The loop of data, audience, journey, measurement and a better audience |
| Expected effect | What should change, written with its metric and baseline before go-live |
| Vanity metric | A number that flatters without informing a decision |
| Mobile scorecard | A CJA project layout made for phones |
| Fallback rate | How often no selection strategy qualified and a generic option was shown |
| Operationalise | Assign owners, cadence and a review trigger so a process runs without its designer |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Customer Journey Analytics publish audiences, CJA audiences overview, Journey Optimizer Read audience, CJA mobile scorecard, share Workspace projects, Journey Optimizer decisioning reports, Analyze in CJA

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
