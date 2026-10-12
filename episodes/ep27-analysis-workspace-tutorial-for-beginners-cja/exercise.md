# Exercise 27: Five questions, one project

You will turn Anjali's five questions into table specs, read a channel table the way an analyst does before ranking anything, debug a table of zeros, and write the one sentence of meaning that lets someone read your work without you in the room.

## Track A: No Adobe access needed

1. **Five table specs.** For each of Anjali's five questions, write a table spec with four lines: **rows** (a dimension), **columns** (metrics), **who** (a segment, or "everyone") and **when** (the date range). Then mark any question that one freeform table cannot fully answer, and say what it needs.
   1. Welcome journey entries, completion and conversion to a first repeat order within 14 days.
   2. Cart Rescue recovery rate and recovered revenue.
   3. Revenue by marketing channel, with average order value and orders per person.
   4. Are Gold members actually worth more?
   5. Day-7 repeat-purchase rate for New This Month.
2. **Read before you rank.** Here is Kavya's first channel table for the relaunch fortnight (the Bloom channel sample, `bloom-cja-channels.csv` in the course data folder, has the same rows without the Total). Before you rank anything:
   - a. Find the **No value** row and write one sentence on what it means.
   - b. Find the **duplicate** rows and write one sentence on what they mean.
   - c. What should the `email` row read once the duplicates are merged?
   - d. What will the No value row read after the merge, and why?

   | Channel (raw tag) | Orders |
   |---|---|
   | No value | 520 |
   | email | 150 |
   | Email | 30 |
   | All other channels, combined | 540 |
   | **Total** | **1,240** (revenue $66,260) |

3. **A table of zeros.** A colleague builds a brand-new freeform table and every row reads 0. List three checks, in order, and say why that order.
4. **One sentence of meaning.** Write the sentence you would put above the channel table, and the one above this band table. Each sentence must state the window.

   | Loyalty band | Orders | Revenue |
   |---|---|---|
   | Gold | 300 | $23,400 |
   | Silver | 420 | $23,100 |
   | Bronze | 520 | $19,760 |

5. **Save and share.** In two lines each: why must a new project be saved by hand the first time, and why are board numbers never shared with **Share with anyone**?

## Track B: If you have CJA access (optional)

Safety first:
- Use a **development** sandbox and data view only, never production.
- Create only **one project**, named with your initials (for example `XX - Five questions`). Do not open, save or **Save as** anyone else's project.
- Do not click anything under **Share**, do not **Schedule**, and never **Publish** anything.
- Do not click right-click items that create a segment or an audience: they open builders with Save or Publish.
- Do not edit the data view or create derived fields: a derived field belongs to the whole connection.
- Do not delete anything. In a shared environment: look, screenshot, leave.

Steps:
1. Open **Workspace**, then **Create project**, then **Blank Workspace project**, then **Create**.
2. At the top right of the panel, choose a data view you are allowed to read. Note what the date range says.
3. **Project**, then **Save**. Type your project name in **Name (required)** and click **Save**.
4. Write one question in your notebook first. Then click **Enable table builder**, drag one dimension into the rows and two metrics into the column header, and click **Build**.
5. If the table reads zero, fix the date range (**Apply**) and note what changed. Look for a **No value** row and any duplicate values before you sort.
6. Right-click one row, choose **Breakdown**, then **Dimensions**, and pick a second dimension.
7. Select two or three rows, then **Insert**, then **Line**. Check that the chart and table share a colour.
8. Add your one sentence of meaning with **Edit Description** on the panel's right-click menu.
9. **Project**, then **Save** again before you close the tab.

## Check yourself

1. What are the four lines of a table spec?
2. Which two things does every panel carry for itself?
3. What does auto-save keep, and where?
4. A new panel shows zeros. What do you check first?
5. What does the table builder wait for?
6. Is No value a channel? What is it?
7. Why can `email` and `Email` appear as two rows, and how does Bloom merge them?
8. Why merge duplicates before a breakdown?
9. How can you tell which table a chart is linked to?
10. What makes a project readable without you in the room?

<details><summary>Check your answers</summary>

**Task 1: model table specs**

| # | Rows | Columns | Who | When | One table enough? |
|---|---|---|---|---|---|
| 1 | Journey name | Journey entries, orders | People who entered Bloom Welcome v1 | Relaunch fortnight, plus 14 days after entry | No: completion needs fallout and repeat purchase needs a cohort view (episode 30) |
| 2 | Rescue group versus holdout | Cart adds, orders, revenue | Cart Rescue v1 entrants | Relaunch fortnight | Partly: the recovery rate is a ratio, best as a calculated metric (episode 28) |
| 3 | Marketing channel | Orders, revenue | Everyone | Relaunch fortnight | Partly: average order value and orders per person need calculated metrics (episode 28) |
| 4 | Loyalty band | Orders, revenue | Everyone | Relaunch fortnight | Partly: "worth more per order" needs a revenue-per-order calculated metric (episode 28) |
| 5 | Start week or day | Repeat orders | New This Month customers | Relaunch fortnight, plus 7 days after each first order | No: a cohort view (episode 30) |

Any well-reasoned spec is fine. What matters is that the question is written before the table.

**Task 2: read before you rank**
- a. No value: 520 of 1,240 orders (more than two in five) carried no channel. It is a tracking gap, not a channel. Say it first, and do not rank it or hide it quietly.
- b. `email` and `Email` are one channel typed two ways; CJA treats different casing as different values.
- c. 150 + 30 = **180 orders** in one `email` row (Bloom uses the Marketing channel derived field with its Lowercase rule).
- d. Still **520**. A Lowercase rule merges values that exist; no derived field can invent a channel that was never recorded.

**Task 3: three checks, in order**
1. The panel's **date range**: a new panel opens on This month, so older data reads zero.
2. The panel's **data view**: each panel can use a different one.
3. Only then **the data itself**: compare with the source counts.
The order goes from cheapest and most common to most expensive.

**Task 4: model sentences**
- Channel table: "Relaunch fortnight: 520 of 1,240 orders carried no channel, so channel rankings wait until tracking is fixed."
- Band table: "Relaunch fortnight: Gold placed the fewest orders (300) but brought the most revenue ($23,400); revenue per order follows once we define it as a calculated metric."

**Task 5: save and share**
- Adobe: you must save each new project manually the first time. Auto-save keeps only a local recovery copy (Recovered Projects, last 7 days), not a saved project.
- Share with anyone needs no login at all and gives read-only access to anyone with the link; board numbers should need a login.

**Track B: what to expect**
The new project opens with one Freeform panel and a date range of This month. If your data is older, the table reads zero until you change the dates. A breakdown appears indented under its row, and the line chart sits above the table with a matching colour. Labels as of October 2026; check what your screen shows.

**Check yourself**
1. Rows, columns, who, when.
2. Its own data view and its own date range.
3. A recovery copy every 2 minutes, on your own machine only.
4. The panel's date range (This month), then the data view.
5. Build.
6. No. It is a tracking gap: rows where the dimension was empty.
7. Two teams typed the value in different casing; the Marketing channel derived field's Lowercase rule merges them.
8. Otherwise the breakdown describes only part of the channel (150 of 180 orders).
9. Matching colours: the chart uses that table as its data source.
10. One question per view, a stated window, and one sentence of meaning.

</details>
