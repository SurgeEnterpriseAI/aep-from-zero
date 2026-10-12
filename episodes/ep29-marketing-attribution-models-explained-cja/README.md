# Episode 29: Marketing Attribution Models Explained (CJA)

**Watch:** Video coming soon on iTV

[Previous](../ep28-cja-segments-and-calculated-metrics-tutorial/) · [Next](../ep30-fallout-flow-and-cohort-analysis-in-cja/)

## What you will learn

- Explain a **touch**, a **lookback window** and a **container**, and compare attribution models on one worked example
- Apply **First Touch**, **Last Touch** and **Linear** to Priya's illustrative two touches
- Build and read an **Attribution panel**: swing versus rank, openers versus closers, attributed total versus total revenue
- Name the **three places** an attribution model can be set, and who each one affects
- Write an honest recommendation: ranges, a named model and window, and a test that would confirm it

## The story so far

Bloom, a wellness brand with 1.2 million customers, is two weeks into its loyalty relaunch. Rohan Desai, Bloom's analyst, reads its data in Customer Journey Analytics (CJA) through the connection **Bloom 360** and the data view **Bloom Marketing**. In episode 28 Kavya built one shared revenue-per-order metric: Gold members spend $78 per order, Silver $55 and Bronze $38. Now paid search and email both claim the same revenue from the relaunch fortnight (1,240 orders, $66,260), and both teams' bonuses depend on it. Anjali Mehta, the Chief Marketing Officer, needs a referee, not a cheerleader.

## Key ideas

### 1. Attribution is an assumption you choose
**Attribution** shares the credit for one conversion between the channels that touched it. An **attribution model** is the rule for that sharing. No model is true; each answers a different question. Three words set the rules:

| Word | Meaning |
|---|---|
| **Touch** | One contact between a person and a channel, such as an email click |
| **Lookback window** | How many days before the conversion a touch can still earn credit: 14, 30, 60 or 90 Days, Custom Time, or Reporting window (the report's own dates). A touch outside it gets nothing |
| **Container** | Whose touches count together: **Person** (all their visits) or **Session** (only the visit with the conversion). Choosing Session forces the lookback window to the reporting window |

Interview line: *"Attribution models are assumptions, not truths. Name the model and the window every time."*

### 2. The eleven models
| Model | Who gets the credit |
|---|---|
| Last Touch | 100% to the most recent touch before the conversion; typically the default |
| First Touch | 100% to the first touch in the lookback window; used for awareness and acquisition |
| Linear | Equal credit to every touch |
| Participation | 100% to every unique touch, so the column adds up to more than 100% |
| Same Touch | 100% to the event where the conversion happened |
| U Shaped | 40% first, 40% last, 20% shared by the middle |
| J Curve | 60% last, 20% first, 20% shared by the middle |
| Inverse J | 60% first, 20% last, 20% shared by the middle |
| Time Decay | More credit the closer a touch is to the conversion; the half-life defaults to 7 days |
| Custom | Your own weights for first, last and middle, normalised to 100% |
| Algorithmic | Statistical; Adobe says it is based on the Harsanyi Dividend from cooperative game theory |

### 3. Adobe's 50-dollar example
A shopper arrives through a paid search ad (15 September), returns through a friend's social link and fills a cart without buying (18 September), applies a coupon from an email (24 September), then finds another coupon through a display ad and buys for $50.

| Model (Person, 30 days) | Paid search | Social | Email | Display |
|---|---|---|---|---|
| First Touch | $50 | $0 | $0 | $0 |
| Last Touch | $0 | $0 | $0 | $50 |
| Linear | $12.50 | $12.50 | $12.50 | $12.50 |
| U Shaped | $20 | $5 | $5 | $20 |
| J Curve | $10 | $5 | $5 | $30 |
| Inverse J | $30 | $5 | $5 | $10 |

First Touch and Linear are Adobe's published results; the other rows apply the model definitions above. Time Decay gives the most to the two purchase-day touches (email and display) and the least to paid search. With a **Session** container, only the visit with the purchase counts; email came before display in that visit, so **First Touch gives email the whole $50**.

### 4. Priya's two touches (illustrative)
Say, for example, Priya first arrived on her phone from a paid search ad and came back through a Bloom email on her laptop before paying $54 (order BLM-88412). These channels are **illustrative only**; never quote them as Bloom facts.

| Model | Paid search | Email |
|---|---|---|
| First Touch | $54 | $0 |
| Last Touch | $0 | $54 |
| Linear | $27 | $27 |

A model can see both touches only because **Bloom 360** stitches web events (episode 25): until she signed in, her phone rows carried only an anonymous Experience Cloud ID (ECID), and stitching gave those rows her email from the sign-in event. Without stitching, CJA sees two people, and paid search can never earn credit for her order. Cross-device attribution depends on the person ID and stitching, not on the panel.

### 5. Read the swing, not the rank
- **Swing**: how much a channel's credit changes when you change the model.
- **Opener**: earns more under First Touch than Last Touch; it brings people in.
- **Closer**: earns more under Last Touch; it finishes sales other channels started.
- Channels that barely move are steady.

At Bloom, paid search grew under First Touch and email under Last Touch: both teams were partly right.

### 6. Attributed total versus total revenue, and the Channel overlap
- The panel's total is all revenue in the panel's dates ($66,260 for the relaunch fortnight). Each model column adds up to **less**, because orders with no channel touch inside the lookback window earn no credit. It is the same tracking gap as the 520 **No value** orders in episode 27; the amounts differ because the rules differ.
- A freeform table uses the data view's **default** attribution; the panel uses the model and lookback **you chose**. Both are honest. Say which one you used.
- **Channel overlap** is a Venn diagram of the top three channels and how often they take part in the same conversions: the shared money teams fight over.

### 7. Three places to set a model
| Where | How | Who it affects |
|---|---|---|
| One metric column | Column settings icon on the header, **Use non-default attribution model** | Only that column |
| Inside a calculated metric | The gear on the metric in its definition, **Use non-default attribution model** | Everyone who uses that metric |
| Data view default | On the metric in the data view, **Set attribution** | That metric in every report on that data view, for everyone |

Use the smallest place that answers your question. Bloom left the data-view default alone.

### 8. Ranges, not one triumphant number
Give the CMO three sentences: **where the money moves** (a range per channel, lowest model to highest), **the rules** (models, container, lookback window, dates) and **the test** that would confirm it. **Attributed revenue is not incremental revenue**: to learn what a channel really adds, hold back a random group, as the Cart Rescue holdout does, and compare.

## In the product

Labels as of October 2026. Work only in your own project; never change shared settings.

1. **Analysis Workspace**: open your own project. Check the data view in the top right of the panel, and set the panel dates (a new panel opens on **This month**).
2. **Insert**, **Attribution**. The panel has five inputs: **Success metric**, **Channel**, **Included models**, **Container**, **Lookback window**.
3. Drag **Revenue** to Success metric and your channel dimension to Channel. Tick **Last Touch**, **First Touch** and **Linear**. Set Container to **Person** and Lookback window to **30 Days**. Click **Build**.
4. Read the outputs: the total, the comparison bar chart and table (each column header names its model, container and lookback, for example Last Touch, Person, 30 Days), then **Channel overlap** (a Venn), a scatter and a trend.
5. One column only: the **Column settings** icon on a metric header, then **Use non-default attribution model** (the dialog lists Model and Lookback window). The header's right-click menu also offers **Modify attribution model**.
6. Inside a calculated metric: in the builder's definition, the gear on the metric, then **Use non-default attribution model**, with Model, Container and Lookback window, and **Apply**. Left off, Adobe's documentation suggests Last Touch with a 30-day lookback.
7. Data view default (look only): in the data view, select the metric component and open its **Attribution** section to see **Set attribution** (Attribution model, Container, Lookback window). Changing it affects everyone's reports.

## Common mistakes

- Quoting an attributed number without its model, container and lookback window, or comparing numbers that used different ones.
- Picking the model after seeing which one flatters your own channel.
- Ranking the bars instead of reading the swing, then cutting an opener because it looks weak under Last Touch.
- Adding up a Participation column as if it were revenue.
- Expecting the attributed total to equal total revenue; the gap is a tracking problem, not a channel.
- Changing the data-view default to settle an argument.
- Treating attributed revenue as incremental revenue.

## Glossary

| Term | Meaning |
|---|---|
| Attribution model | The rule that splits credit for a conversion across touches |
| Touch | One contact between a person and a channel |
| Lookback window | How many days before a conversion a touch can still earn credit |
| Container (attribution) | Person or Session: whose touches count together |
| U Shaped, J Curve, Inverse J | Models that give fixed shares to the first, last and middle touches |
| Attribution panel | The Workspace panel that compares models side by side |
| Swing | How much a channel's credit changes between models |
| Opener, closer | A channel that starts sales, and one that finishes them |
| Channel overlap | A Venn of the top three channels and their shared conversions |
| Incremental revenue | Revenue that would not have happened without the channel |
| Holdout | A randomly withheld group used to measure what would have happened anyway |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Customer Journey Analytics attribution panel, attribution models and lookback windows, metric attribution in column settings, calculated metric attribution, data view component attribution settings

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
