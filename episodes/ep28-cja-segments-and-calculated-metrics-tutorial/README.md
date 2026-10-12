# Episode 28: CJA Segments and Calculated Metrics Tutorial

**Watch:** Video coming soon on iTV

[Previous](../ep27-analysis-workspace-tutorial-for-beginners-cja/) · [Next](../ep29-marketing-attribution-models-explained-cja/)

## What you will learn

- Use **segments** in Customer Journey Analytics (CJA), called filters before April 2025, with the right **container**: person, session or event
- Choose between a **quick segment** and a **saved segment**
- Explain **"segments explain; audiences act"** with a Bloom example
- Build a **calculated metric** for revenue per order with a **Title**, an **External ID**, a **Format** and a **Preview**
- Avoid the column-order trap in **Create metric from selection** by reading the column name

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers. It is week five of its Adobe programme, two weeks after the loyalty relaunch went live. In episode 27 Kavya built her first Analysis Workspace project: saved by hand, a table that read zero until she fixed the date range, and a channel report whose biggest row, "No value", turned out to be a tracking gap. Now Anjali Mehta, the Chief Marketing Officer, wants question four answered before the board update: **are Gold members actually worth more?** Kavya's table shows orders and revenue by loyalty band, but revenue alone makes Gold and Silver look tied.

## Key ideas

### 1. Filters became segments
In **April 2025** Adobe renamed CJA's **filters** to **segments**, to match Adobe Analytics. Older pages and videos still say filters; both words mean one feature. Adobe notes one exception: **search filters** are still called filters. The old word also survives in a panel's drop zone, which reads *Drop a component to filter or break down the data*.

A **segment** is a rule that narrows analysis to certain people, sessions or events. Drop one onto a panel and every table and chart in it counts only what the segment keeps. Nothing is sent anywhere.

### 2. The container decides what a segment keeps
| Container | What it keeps when the rule is true |
|---|---|
| **Person** | "Every session and every event for the persons that qualify" (Adobe) |
| **Session** | Only the sessions (visits) in which the rule was true |
| **Event** | Only the single events that match the rule |

Priya's evening, with one rule, "a cart add exists":
- **Person:** Priya qualifies, so all her visits come along, including her 54-dollar order `BLM-88412`.
- **Session:** only the visits that contained a cart add.
- **Event:** only the add-to-cart event itself. It carries no money, so revenue under this segment should read zero.

Choose the container from the question: people, visits, or moments. A Person container on "came from a Bloom email" keeps every visit those people ever made, so email looks more valuable than it is.

### 3. Quick segment or saved segment
| | Quick segment | Saved (regular) segment |
|---|---|---|
| Conditions | At most 3 | One or more, joined by **And** or **Or** |
| Nested containers, sequences | Not allowed | Allowed (sequential segments use **Then**) |
| Who can use it | Only the project it was made in; cannot be shared | Your component list, reusable across projects |
| Where you build it | The segment icon at the top of a panel | The Segment Builder |

Explore with a quick segment. Save a proper segment the moment someone else depends on the definition. Kavya's quick segment was **loyalty band equals Gold**, scope **Person**, using the loyalty band derived field from episode 26. Her saved version is titled *Gold band customers*.

### 4. Segments explain; audiences act
| | CJA segment | AEP audience |
|---|---|---|
| Lives in | Customer Journey Analytics | Adobe Experience Platform (AEP) |
| Job | Narrows a report | A living rule that journeys and destinations act on |
| Sends anything? | Never | Yes, through Adobe Journey Optimizer (AJO) or activation |
| Bloom example | Gold band customers | High-Value Loyalists (episode 10), used by the Bloom Gold Thank-You campaign |

The bridge is deliberate: the Segment Builder has a **Create audience from segment** button, which Adobe describes as creating and sharing the audience with Experience Platform. Episode 31 crosses that bridge. Adobe also says CJA audiences **cannot include calculated metrics**.

### 5. Calculated metrics: one shared definition
A **calculated metric** is a saved formula built from other metrics, such as **revenue per order** (average order value). Ratios that people quote belong in calculated metrics, so every team uses one definition. A typed rate breaks the first time someone segments it; a calculated metric divides again in every row, segment and breakdown.

The builder needs a **Title** and an **External ID** (Adobe: "the name of the calculated metric when using an external BI tool and the BI extension"; if you do not override it, it is filled with `undefined_` plus characters). **Preview** covers the **last 90 days**, so it will not match a fortnight table exactly. Inside a metric's definition, a gear on each metric can also set an attribution model (episode 29).

### 6. The column-order trap
**Create metric from selection** follows the **order of the columns in the table**, not the order of your clicks. Kavya's table had Orders, then Revenue. She clicked Revenue first and chose Divide, and the new column was named **Orders / Revenue**, reading zero on every row. Adobe notes that a metric made by picking a function from this menu is **project-only**. Read the column name before you trust any number in it.

### 7. Bloom's answer to question four
| Band | Orders | Revenue | Revenue per order | Wrong way (Orders / Revenue) |
|---|---|---|---|---|
| Gold | 300 | $23,400 | $78 | about 0.013 |
| Silver | 420 | $23,100 | $55 | about 0.018 |
| Bronze | 520 | $19,760 | $38 | about 0.026 |
| All | 1,240 | $66,260 | about $53 | about 0.019 |

Relaunch fortnight, Bloom's fictional sample data (US storefront, dollars). The wrong-way column would rank Bronze top and Gold bottom: the exact opposite of the truth.

**The honest caveat.** Gold spends more per order. That is **association, not proof** that the loyalty programme caused it. Say, for example, customers who buy bigger baskets earn points faster and so reach Gold sooner: a **confounder** (episode 30). Proving cause needs a comparison that holds everything else constant, and ideally a test with a holdout group.

## In the product

Labels as of October 2026. Practise only in your own project, on objects carrying your initials.

1. **Quick segment:** select the segment icon at the top of a panel. The **Quick segment** builder offers **Include** or **Exclude**, a scope of **Event**, **Session** or **Person**, and the rule. The name fills itself in from the definition.
2. **Keep a quick segment:** hover over it, select the info icon, choose **Make available to all projects and add to your component list**, name it, select **Save**. It becomes a regular segment.
3. **Saved segment:** **Components**, **Segments**, then **Add** in the Segment manager, or **Components**, **Create segment**. Adobe's documentation suggests the dialog is **New segment**, with **Title** and **Definition** required and **Description** and **Tags** optional; check what your screen shows. Each container is Include or Exclude with a level; rules join with **And**, **Or** or **Then**. Buttons: **Save**, **Save As**, **Delete**, **Cancel**, **Create audience from segment**.
4. **Calculated metric:** **Components**, **Create metric** (or the add icon next to **Metrics** in the left panel). The dialog is **New calculated metric**. Set **Title**, **External ID** (the screen label reads "External Id"), **Format** Currency, **Decimal places** 2, **Show upward trend as** Good (Green). Drag **Revenue** into **Definition**, then drop **Orders** just below it; the operator defaults to divide, and **Summary** reads Revenue ÷ Orders. Read **Preview** and **Product compatibility**, then **Save**. The metric joins your component list; sharing it with your team is a separate, deliberate step.
5. **The shortcut:** click one metric header, Ctrl-click a second, right-click, **Create metric from selection**: **Divide**, **Subtract**, **Add**, **Multiply**, **Percent change**, **Open in Calculated Metric Builder**. Check the new column's name. To remove a column, hover over its header and select the **x**.

## Common mistakes

- Thinking an old tutorial about "filters" describes a retired feature.
- Calling a CJA segment an audience, or promising a client you will target a CJA segment directly.
- Using a Person container for a visit question, so every visit those people made counts too.
- Forgetting a segment is still on the panel, so every later number counts only that group.
- Rebuilding the same quick segment in five projects, each slightly different.
- Leaving the External ID as the default `undefined_` value.
- Trusting a **Create metric from selection** column without reading its name.
- Saying "Gold members are worth more because of the programme" when the data shows only association.

## Glossary

| Term | Meaning |
|---|---|
| Segment (CJA) | A rule that narrows analysis to certain people, sessions or events; it explains, it does not activate |
| Filter | CJA's name for a segment before April 2025; search filters keep the name |
| Container | The level a segment keeps when its rule is true: Person, Session or Event |
| Quick segment | A segment built at the top of a panel; at most 3 conditions, no nesting, project-only |
| Segment Builder | The dialog for saved segments: Title, Definition, containers, And, Or, Then |
| Sequential segment | A segment whose steps are joined with Then, for things done in order |
| Audience (AEP) | A living rule in Experience Platform that journeys and destinations act on |
| Calculated metric | A shared formula, such as revenue per order, so everyone uses one definition |
| External ID | The required name a calculated metric uses in external BI tools |
| Create metric from selection | A right-click shortcut that builds a metric from selected columns, in column order |
| Confounder | A third factor that explains an apparent relationship between two things |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Customer Journey Analytics segments, segment containers, quick segments, Segment Builder, calculated metric builder, create metric from selection, terminology change filters to segments

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
