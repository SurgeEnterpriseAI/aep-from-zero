# Episode 27: Analysis Workspace Tutorial for Beginners (CJA)

**Watch:** Video coming soon on iTV

[Previous](../ep26-cja-data-views-and-derived-fields-explained/) · [Next](../ep28-cja-segments-and-calculated-metrics-tutorial/)

## What you will learn

- Build an **Analysis Workspace** project in Customer Journey Analytics (CJA): a **panel**, a **data view**, a **date range**, a **freeform table**, a **breakdown** and a **linked visualization**
- Start every table from a **written question**, turned into a table spec
- Spot **No value** and **duplicate values** (such as `email` and `Email`) before you rank anything
- Save a new project correctly the first time, and escape the **This month** zero trap
- Present a project someone else can read: **one question per view, a stated window, one sentence of meaning**

## The story so far

Bloom, a direct-to-consumer wellness brand, is two weeks past its loyalty relaunch. In episode 25 Rohan Desai, the analyst, built the CJA connection **Bloom 360** with the email as the person ID on every dataset. In episode 26 he and Kavya Menon built the data view **Bloom Marketing**: trusted metric names, a 30-minute session and five derived fields, including a Marketing channel field whose Lowercase rule merges `email` and `Email`. Now Anjali Mehta, the Chief Marketing Officer, has sent five questions she must answer before the board update.

## Key ideas

### 1. Question first, then the table
A freeform table answers a question; it never asks one for you. Rohan's rule: **write the question first, then build the table.** Each question becomes a **table spec** with four lines:

| Line | Means | Example (question 3) |
|---|---|---|
| Rows | A dimension: the labels you split by | Marketing channel |
| Columns | Metrics: the numbers you count | Orders, Revenue |
| Who | A segment that narrows the people (episode 28) | Everyone |
| When | The date range | The relaunch fortnight |

Anjali's five questions: (1) welcome entries, completion and a first repeat order within 14 days; (2) Cart Rescue recovery rate and recovered revenue; (3) revenue by marketing channel, with average order value and orders per person; (4) are Gold members actually worth more?; (5) Day-7 repeat-purchase rate for New This Month. Writing the specs shows what one table cannot do: completion needs a fallout chart and repeat purchases need a cohort table (episode 30), and per-order value needs a calculated metric (episode 28).

### 2. Workspace in one picture
| Part | What it is | Guardrail (Adobe, as of 2026) |
|---|---|---|
| **Project** | One file of analysis: you save, name and share it | Up to 15 panels |
| **Panel** | A frame with its **own data view and own date range** | Up to 25 visualizations |
| **Visualization** | A table or chart inside a panel | 400 rows per dimension before pagination; 5 dimension columns per freeform table |
| **Component** | What you drag in: dimensions, metrics, segments, date ranges | |

One value of a dimension, such as `email` in Marketing channel, is a **dimension item**. **Guided analysis** and **annotations** also exist; this episode leaves them for later.

### 3. Save a new project by hand
Adobe: "you must save each new project manually the first time." Auto-save runs every 2 minutes, but it only keeps a **recovery copy on your own machine** (unsaved projects appear in **Recovered Projects (Last 7 Days)** on the landing page). Save by hand again before you leave.

### 4. The This month zero trap
A new panel opens on **This month**. If your data sits in an earlier month (Bloom's relaunch fortnight did), every cell reads zero. Check **(1) the panel's date range, (2) the panel's data view, and only then (3) the data itself** against the source counts.

### 5. Freeform tables and the table builder
A **freeform table** puts a dimension down the side (rows) and metrics across the top (columns). With **Enable table builder**, you place several components first and the table **updates only after you select Build**.

### 6. No value is a tracking gap, not a channel
**No value** collects every row where the chosen dimension was empty. Bloom's channel table for the relaunch fortnight held 1,240 orders and $66,260, and its biggest row was **No value: 520 orders**, more than two in every five. Two opposite mistakes: ranking it as a channel, or hiding it quietly and ranking the rest as the whole business. Size it, say it first, then find the cause (the channel may sit on an earlier visit, or links went out without campaign tags).

Interview line: *"'No value' is a tracking gap, not a channel."*

### 7. Duplicates hide in casing
Kavya's first table used a raw channel tag and showed `email` (150 orders) and `Email` (30): one channel typed two ways, counted as two values. The **Marketing channel** derived field (episode 26, with its Lowercase rule) gave one `email` row of **180 orders**; No value stayed at 520. Scan for casing, spelling and spacing twins, and pick the curated component.

### 8. Breakdowns
A **breakdown** splits one row by a second dimension: right-click the row, choose **Breakdown**, then **Dimensions**, **Metrics**, **Segments** or **Date ranges** (or search). Bloom broke the `email` row down by **Product category** (from the 200-product catalogue lookup). A table shows up to 400 breakdowns. Merge duplicates **before** you break down, or the breakdown describes only part of the channel.

### 9. Linked visualizations
Select rows, then **Insert**, then **Line**. Adobe: a simple visualization such as Line or Bar uses the **closest freeform table** as its data source, and "matching colors mean that visualizations are based on the same data source." In the chart's data source settings, **Lock Selection** (Selected Items or Selected Positions) lets you choose what the chart keeps when rankings or filters change. Choose the question, then the chart.

### 10. Question four, laid out (not yet answered)
| Loyalty band | Orders | Revenue |
|---|---|---|
| Gold | 300 | $23,400 |
| Silver | 420 | $23,100 |
| Bronze | 520 | $19,760 |
| **Total** | **1,240** | **$66,260** |

Gold placed the fewest orders but brought the most revenue. "Worth more per order" needs one shared definition of revenue per order: a calculated metric, built in episode 28. The split works because Bloom 360 includes the customer profile dataset.

*Bloom's figures are fictional sample-storefront data in US dollars, used throughout Act III.*

### 11. One question, one window, one sentence
Each view answers **one question**, states its **window**, and carries **one sentence of meaning**, for example: "Relaunch fortnight: 520 of 1,240 orders carried no channel, so channel rankings wait until tracking is fixed." The test: a colleague opens the project and understands it without you in the room.

**Share carefully.** The Share menu offers **Share with Workspace users** (needs a CJA login), **Share with anyone** (no login needed, read-only) and **Get project link**. Board numbers never travel by Share with anyone, and while you practise you share nothing.

## In the product

Labels as of October 2026. Practise only in your own project, named with your initials.

1. In Customer Journey Analytics, open **Workspace**, then **Create project**. Choose **Blank Workspace project** and click **Create**. (The dialog also offers **Blank mobile scorecard** and **Guided analysis** tiles.)
2. A new project opens with one **Freeform** panel. At the top right of the panel, open the data view list and choose your data view (Bloom's is **Bloom Marketing**).
3. Click the date range (it says **This month**). In the panel calendar use **Preset**, or set the start and end, then **Apply** (this panel) or **Apply to all panels**.
4. **Project**, then **Save**. Fill in **Name (required)**; **Description**, **Tags**, **Folder** and **Version notes** are optional. Click **Save**.
5. In the empty freeform table (or the **+** inside the panel, then **Freeform table**), click **Enable table builder**. Drag a dimension into the rows and metrics into the column header, then click **Build**.
6. Sort with the **Sort** icon on a column header. The column's **Filter** icon has an **Include "No value"** option.
7. Right-click a row, then **Breakdown**, then **Dimensions** (Bloom: **Product category**).
8. Select rows, then **Insert**, then **Line**.
9. A new panel (the **+** below the last panel, or **Insert**) opens on This month again.
10. Write the sentence of meaning with **Edit Description** on the panel's right-click menu, or a **Text** visualization. Then **Project**, **Save** again.

## Common mistakes

- Opening Workspace and dragging fields around before writing the question.
- Building for an hour and never doing the first manual save.
- Raising a data incident for a table of zeros before reading the panel's date range.
- Ranking channels before reading the No value row, or hiding No value without saying so.
- Grabbing the first component a search returns instead of the curated derived field, so `email` and `Email` stay split.
- Breaking down a row before its duplicates are merged.
- Using **Share with anyone** for numbers that should need a login.

## Glossary

| Term | Meaning |
|---|---|
| Analysis Workspace | CJA's analysis canvas of projects, panels, tables and charts |
| Project | One saved file of analysis in Workspace |
| Panel | A frame in a project with its own data view and date range |
| Freeform table | The core Workspace table: dimensions as rows, metrics as columns |
| Table builder | A mode where components are placed first and the table runs only after Build |
| Dimension item | One value of a dimension, such as `email` in Marketing channel |
| No value | The row collecting events where the dimension was empty; a tracking gap |
| Breakdown | Splitting one table row by a second dimension, metric, segment or date range |
| Linked visualization | A chart that uses a freeform table as its data source; matching colours show the link |
| Table spec | Rows, columns, who and when, written before building |
| Share with anyone | A sharing option that needs no login; never for board numbers |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Customer Journey Analytics create projects, save projects, freeform table, table builder, breakdown dimensions, filter and sort freeform tables, linked visualizations, share projects, Analysis Workspace guardrails

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
