# Episode 11: Batch vs Streaming vs Edge Segmentation in AEP

**Watch:** [Watch episode 11 on YouTube](https://youtu.be/PJGA2T45FcU)

[Previous](../ep10-aep-segment-builder-tutorial-build-audiences/) · [Next](../ep12-adobe-web-sdk-datastreams-aep-destinations/)

## What you will learn

- Choose **batch**, **streaming** or **edge** evaluation for each audience with one question: will a journey need to react within minutes?
- Explain why "make everything streaming to be safe" is a mistake, including the 2026 change for rules built only on profile attributes
- Use the audience **estimate** as a quality gate, and diagnose the 9,930 "New This Month" bug
- Tell **Qualified** from **Estimated** profiles, and read a zero estimate correctly
- Catch the overlap trap between Window Shoppers and New This Month
- Place **Schedule all audiences**, audience composition, externally generated audiences and Federated Audience Composition in the toolkit

## The story so far

Bloom, a direct-to-consumer wellness brand, is rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch. In episode 10, Kavya built the relaunch five in the Segment Builder, each one a living rule on the merged profile, and Divya claimed Lapsed 90 as her win-back list. Nobody had yet decided how fast each audience must update. Then Farhan put the previous consultants' draft estimates on her desk, with one number circled in red: 9,930.

## Key ideas

### 1. The evaluation method
Every audience has an **evaluation method**: how often the platform re-checks who belongs. It sits in the Segment Builder's right-hand panel, **Audience properties**, and it defaults to **Batch**. Leaving it alone is still a choice. Do not confuse it with episode 5: there, batch and streaming described how data *arrives* (ingestion); here they describe how often an audience is *re-checked*.

| Method | Rhythm | Use it for |
|---|---|---|
| Batch | Evaluated once every 24 hours | Groups that change slowly: loyalists, the lapsed, window shoppers |
| Streaming | Updates in near real time as streamed data arrives (Adobe gives no minutes figure); batch-loaded data waits for the daily run | Moments a journey must react to: a cart left behind, a first order |
| Edge | Evaluated on the Edge Network, on the same page load | On-site personalisation, such as a homepage banner |

### 2. The "react within minutes?" rule
Ask of every audience: **"Will a journey need to react within minutes? If yes, streaming. If not, batch."** At Bloom exactly two of the five pass.

| Audience | Rule | Method | Why |
|---|---|---|---|
| High-Value Loyalists | Loyalty band Gold AND 3+ orders in last 12 months | Batch | Value changes slowly |
| Cart Abandoners 24h | Add-to-cart NOT followed by purchase within 24 hours | Streaming | The rescue journey has hours, not days |
| Lapsed 90 | Last order more than 90 days ago AND email consent true | Batch | Someone becomes lapsed at most once a day |
| New This Month | First-ever order within the last 30 days | Streaming | Bloom's target is a welcome within a minute of the first order (a business target, not a platform promise) |
| Window Shoppers | 5+ product views in 30 days AND zero orders ever | Batch | A nurture email can wait a day |

Write the reason beside each method, not just the method.

### 3. Why not stream everything
Streaming and edge are not a "better batch". They **consume more of the licence entitlement** and **constrain what a rule may contain**, and for slow-moving groups they buy nothing. Streaming is also only fast for data that streams in: batch-loaded data, such as a nightly order file, still waits for the daily run. Choose batch unless somebody can name the business moment that fails without freshness.

### 4. 2026: no Streaming for new attribute-only rules
**Adobe no longer offers Streaming for new rules that use only profile attributes** (facts stored on the person, such as a home state, tier or consent flag). Older attribute-only audiences may still show Streaming from their older definition; treat them as history, not a template, and never save someone else's audience to tidy it. Bloom's two streaming choices rest on events, but streaming is the design, not a promise. If the builder won't offer Streaming for your rule, the platform is telling you something: rewrite the rule, or agree a slower rhythm with the journey owner.

### 5. The estimate as a quality gate: the 9,930 trap
The **estimate** is the predicted number of people who qualify, shown while you build. Against Bloom's 10,000-customer extract: High-Value Loyalists 1,180, Cart Abandoners 24h 214, Lapsed 90 3,890, Window Shoppers 640, and New This Month 9,930 in the old draft, about 480 once fixed.

The old draft's rule said **any order, ever** instead of **first-ever order within the last 30 days**. One word reversed its meaning, and fed to the welcome journey it would have welcomed loyal customers like Priya, Gold since 2023, as strangers. Kavya debugged it with **symptom, layer, evidence, fix**: the symptom was the estimate, the layer was the rule, the evidence was in the draft's **Code view** (the rule in Profile Query Language, PQL), and **Refresh estimate** on her own correct New This Month verified the fix. The old draft was never edited or reused. An audience of 99 percent is almost never right, and neither is an audience of zero on a sandbox full of profiles. Record every estimate with its date, so you notice when one moves.

### 6. Qualified versus estimated; a zero on an empty store
- **Qualified**: the actual number of profiles that matched at the **last evaluation job**.
- **Estimated**: an approximate figure from a **sample job**. **Refresh estimate** and **Last updated** belong to the estimate.

The two can describe different moments: for a batch audience, Qualified can be most of a day old. When they disagree, ask which is older before you ask which is wrong.

An estimate of about 0 with **Last updated: Not available** is expected until profile data exists. It does not prove a wrong rule. Read Last updated, press Refresh estimate, and check that profile data exists before you suspect the rule.

### 7. The overlap trap
Window Shoppers (zero orders ever) and New This Month (a first-ever order) look separate on paper. At the boundary they are not: a shopper who browsed all month and ordered today joins the streaming New This Month in near real time once her order streams in, but stays in the batch Window Shoppers until its next daily run. A later edit that drops "zero orders ever" would put every new customer who browsed in both. Kavya wrote the exclusion in explicitly (the **Audiences** tab lets a rule build on an existing audience) and recorded that the welcome wins.

### 8. The rest of the toolkit (place it, don't master it)
- **Schedule all audiences**: a sandbox-wide toggle on the audience list. It switches scheduled evaluation for every audience, and streaming audiences depend on it too. Never touch it.
- **Compose audience**: builds audiences out of existing ones (split, rank, exclude).
- **Externally generated audiences**: audiences built outside the platform and brought in.
- **Federated Audience Composition**: query the company's own data warehouse (outside Adobe), land the audience in AEP.

## In the product

Labels as of October 2026.

1. Go to **Customer**, **Audiences**, **Browse**. Note the **Schedule all audiences** toggle at the top of the list and do not touch it.
2. Click **Create audience**. You are offered **Build rule** (the Segment Builder) or **Compose audience** (a workflow over existing audiences). Choose **Build rule**, then **Create**.
3. In the Segment Builder, the left panel has the **Attributes**, **Events** and **Audiences** tabs; the centre is the rule canvas.
4. The right panel, **Audience properties**, shows qualified and estimated profiles, **Refresh estimate**, **View profiles**, **Code view**, Name, Description, Tags and **Evaluation method** (default **Batch**).
5. Read the **Last updated** line under the estimate and press **Refresh estimate** before you judge any number.
6. Open **Code view** to read the rule in PQL.
7. Practise only on your own draft in a development sandbox. Do not save other people's audiences, and do not activate anything.

## Common mistakes

- Setting every audience to streaming "to be safe", or promising a minutes figure for it. Adobe gives none.
- Copying an old attribute-only audience that still shows Streaming.
- Expecting a streaming audience to react fast to data that arrives in a nightly batch file.
- Trusting a rule because it saved without errors.
- Quoting the estimate as if it were the real membership.
- Rewriting a correct rule because the estimate reads zero on an empty profile store.
- Checking each audience alone, never against the audiences next to it.
- Touching **Schedule all audiences** in a shared sandbox.

## Glossary

| Term | Meaning |
|---|---|
| Evaluation method | How often audience membership is re-checked: batch, streaming or edge |
| Profile attribute | A fact stored on the person, such as home state, loyalty tier or consent |
| Estimate | The predicted count of qualifying profiles, shown while you build; your first quality gate |
| Qualified profiles | Profiles that matched the rule at the last evaluation job |
| Estimated profiles | An approximate count from a sample job, with Refresh estimate and Last updated |
| Code view | The Segment Builder view that shows the rule in PQL |
| Profile Query Language (PQL) | The rule language the Segment Builder writes for you |
| Overlap | One person qualifying for two audiences meant to be separate |
| Schedule all audiences | A sandbox-wide toggle for scheduled evaluation of every audience |
| Audience composition | Building audiences out of existing audiences: split, rank, exclude |
| Externally generated audience | An audience built outside the platform and brought in |
| Federated Audience Composition | Query your company's own data warehouse, land the audience in AEP |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Audience Portal overview: https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/overview
- Segment Builder UI guide: https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder
- Streaming segmentation: https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/methods/streaming-segmentation
- Search Experience League for: edge segmentation, audience composition, Federated Audience Composition, externally generated audiences

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
