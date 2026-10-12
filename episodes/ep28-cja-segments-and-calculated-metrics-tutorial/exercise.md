# Exercise 28: Is Gold worth more?

You will choose the right segment container for three Bloom questions, explain "segments explain; audiences act" in your own words, compute revenue per order by loyalty band (and then deliberately divide the wrong way), and write the honest sentence a Chief Marketing Officer can repeat to a board.

## Track A: No Adobe access needed

1. **Choose the container.** For each Bloom question, choose **Person**, **Session** or **Event**, and write one sentence on why.
   - a. Across the relaunch fortnight, which product categories do Gold-band customers buy?
   - b. How much revenue came from visits that started with a click in a Bloom email, and not from those customers' other visits?
   - c. How many add-to-cart events were for the Vitamin C Serum (`BLM-SER-VITC-30`)?
2. **Segments explain; audiences act.** In two or three sentences, explain the line using a Bloom example. Then answer Divya, who asks: "Can I send a thank-you email to your *Gold band customers* segment?"
3. **Quick or saved?** For each case, choose a quick segment or a saved segment, and say why.
   - a. Kavya wants to glance at Gold customers for five minutes in her own project.
   - b. Rohan wants every analyst's project to use the same definition of "Gold band customers".
   - c. Rohan needs "clicked an email, then bought within 7 days", which is a sequence.
4. **Revenue per order in a spreadsheet.** Use the repo's Bloom band sample, `bloom-cja-bands.csv` in the data folder (relaunch fortnight, fictional data):

   | Band | Orders | Revenue |
   |---|---|---|
   | Gold | 300 | $23,400 |
   | Silver | 420 | $23,100 |
   | Bronze | 520 | $19,760 |

   - a. Compute revenue per order for each band, and for all three bands together.
   - b. Now deliberately divide the wrong way: orders divided by revenue. Format the cells as currency with two decimal places. What do you see?
   - c. Write two ways you would spot the mistake, even if you never looked at the formula.
5. **The honest sentence.** Write one sentence on why a higher Gold average order value does not prove the loyalty programme caused it. Name one possible confounder and one test that could prove cause.
6. **The episode's practice question.** You want the revenue from visits that started with a Bloom email, not everything those customers ever bought. Which container do you choose, and what goes wrong if you pick Person instead?

## Track B: If you have CJA access (optional)

Safety first:
- Work only in **your own** Workspace project, named with your initials, on development or practice data.
- Do not **Share**, **Schedule** or **Publish** anything, and never click **Create audience from segment** or **Create audience from selection**.
- Do not open, edit or **Save** a segment, metric or data view that is not yours, and never change a data view or a derived field.
- In a shared organisation, do not click **Make available to all projects and add to your component list**: that turns your quick segment into a component other people see.
- In a shared environment: look, screenshot, leave.

Steps:
1. Open your own project, or create one and **save it by hand** the first time. Set the panel's date range to a period that has data.
2. Build a freeform table: one dimension down the side, with **Orders** and **Revenue** as columns (use whatever your data view offers).
3. Build one **quick segment**: select the segment icon at the top of the panel, choose **Include**, set the scope to **Person**, and write one rule. Note how the table's totals change. Then remove the segment (hover over it and select the **x**), so later numbers count everyone again.
4. Build one **calculated metric**: **Components**, **Create metric**. **Title** `XX - Revenue per order` with your initials. **External ID** in lower case with your initials, for example `xx_revenue_per_order`. **Format** Currency, **Decimal places** 2, **Show upward trend as** Good (Green). Drag **Revenue** into **Definition**, then **Orders** just below it. Read **Summary** and **Preview**, then **Save**.
5. Drag your metric into the table next to Revenue. Check one row by hand: does Revenue divided by Orders match?
6. Look at the order of your two metric columns. Without clicking anything, predict the name of the column that **Create metric from selection**, **Divide** would create.

## Check yourself

1. When did CJA rename filters to segments, and what is still called a filter?
2. What does a Person container keep that a Session container does not?
3. Why should revenue under an event-level "cart add" segment read zero?
4. Name the three limits of a quick segment.
5. How do you turn a quick segment into a regular segment?
6. Finish the line: segments explain; ...
7. Which two fields does the calculated metric builder require besides the definition?
8. How many days does the calculated metric Preview cover?
9. What decides the direction of division in Create metric from selection?
10. Why does Gold's higher average order value not prove the programme works?

<details><summary>Check your answers</summary>

**Task 1: containers**
- a. **Person.** Loyalty band describes a customer, and you want everything those customers bought across the whole fortnight, so you keep every session and event of the people who qualify.
- b. **Session.** You want only the visits that started from an email. A Person container would also keep every other visit by those customers.
- c. **Event.** You are counting single add-to-cart events for one SKU, not people or visits.

**Task 2: model answer**
"A CJA segment narrows a report so we can understand a group, for example how Gold-band customers behave. It sends nothing. An AEP audience, such as High-Value Loyalists, is a living rule that Journey Optimizer reads to send messages." Reply to Divya: "Not from the segment. Segments explain; audiences act. Use an AEP audience such as High-Value Loyalists, which the Bloom Gold Thank-You campaign already uses. Publishing a CJA audience to AEP is a separate, deliberate step (episode 31)."

**Task 3: quick or saved**
- a. **Quick segment.** One condition, one project, short-lived exploration.
- b. **Saved segment.** A quick segment stays in its project and cannot be shared; a shared definition must be saved to the component list.
- c. **Saved segment** in the Segment Builder. Quick segments allow no sequences or nested containers; a sequential segment joins the steps with **Then**.

**Task 4: the numbers**
- a. Gold $78.00, Silver $55.00, Bronze $38.00. All bands: $66,260 ÷ 1,240 = about $53.44.
- b. Gold 0.0128, Silver 0.0182, Bronze 0.0263, all bands 0.0187. As currency with two decimals they show **$0.01**, **$0.02** and **$0.03**; rounded to whole numbers they all show 0, which matches what Kavya saw: zero on every row.
- c. Any two of: the column's **name** reads Orders / Revenue; the values are absurdly small for a price; the **ranking is reversed** (Bronze looks best, Gold worst); the result does not survive a sanity check against one order you know, such as Priya's 54-dollar order.

**Task 5: model sentence**
"Gold orders averaged 78 dollars against 38 for Bronze in the relaunch fortnight; that is association, and to know whether the programme causes it we would need a fair comparison or a test with a holdout group." A possible confounder: customers who already buy bigger baskets earn points faster, so they reach Gold sooner.

**Task 6: practice question**
**Session.** With a Person container, every visit by anyone who ever arrived from an email is counted too, before and after, including visits that never touched an email, so email revenue looks far bigger than it is.

**Track B: what to expect**
The quick segment changes every table and chart in the panel at once, and its name fills itself in from the rule. Your metric's Summary should read Revenue ÷ Orders. Preview covers the last 90 days, so it will not match a shorter panel date range exactly. For step 6: with Orders to the left of Revenue, the shortcut would create **Orders / Revenue**, whatever order you click in. Labels as of October 2026; check what your screen shows.

**Check yourself**

1. April 2025, to match Adobe Analytics. Search filters are still called filters.
2. Every session and event of the people who qualify, not only the sessions where the rule was true.
3. An Event container keeps only the add-to-cart events, and those events carry no revenue.
4. At most 3 conditions; no nested containers or sequences; it stays in its project and cannot be shared.
5. Hover over it, select the info icon, choose **Make available to all projects and add to your component list**, name it and **Save**.
6. ...audiences act.
7. **Title** and **External ID**.
8. The last 90 days.
9. The order of the columns in the table, not the order of your clicks.
10. It shows association. A confounder, such as big spenders reaching Gold faster, could explain it; proving cause needs a fair comparison or a test.

</details>
