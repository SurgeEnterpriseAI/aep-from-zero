# Exercise 30: Find the real leak

You will read Bloom's fallout step by step, test the fallout settings on three shoppers, name confounders before a cause, explain why a flow is not a head count, read a cohort table along its diagonal, and write the honest sentence for the Cart Rescue holdout.

## Track A: No Adobe access needed

1. **Read the fallout.** Bloom's fallout over the relaunch fortnight counts people: journey entry **2,000**, email click **620**, site visit **540**, add to cart **300**, purchase **132** (also in `bloom-cja-fallout.csv` in the course data folder). For each of the four steps, work out:
   - a. how many people continued, as a percentage of the step before
   - b. how many people dropped
   - c. which drop is the biggest in absolute terms, and whether it is normal
   - d. which drop is the interesting one, and why
2. **Test the settings.** Imagine a short fallout with just two touchpoints: add to cart, then purchase. Three shoppers each add to cart and later buy:
   - Shopper A adds to cart, and the very next event is the purchase, in the same visit.
   - Shopper B adds to cart, views two more product pages, then buys, in the same visit.
   - Shopper C adds to cart on Monday evening, then comes back in a new visit on Wednesday morning, opens the cart page and buys.

   Which of them count at the purchase step under: (i) Eventual path with the Person container, (ii) Next event with the Person container, (iii) Eventual path with the Session container?
3. **The container error.** Kavya drags a Person-level segment called "Email click" onto a Person fallout as a touchpoint and gets **Invalid container within segment**. In two sentences, explain the rule and the fix.
4. **Name two confounders.** The breakdown says mobile non-Gold shoppers leak at checkout. Name two possible confounders, and for each, the comparison or test that would rule it out.
5. **Flow is not a head count.** A colleague pastes a flow node's number into the board slides as "customers who went to the product page after the email". Explain in two or three sentences why that number is not a count of people, and what you would use instead.
6. **Read the cohort table.** Use this illustrative table (practice numbers, not Bloom results; also in `bloom-cja-cohort-repeat.csv` in the course data folder). Rows are first-time buyers grouped by the week of their first order. Cells are the percentage who bought again in that period. Bloom Welcome v1 went live at the start of week 3.

   | First order in | First 7 days | Second week | Third week |
   |---|---|---|---|
   | Week 2 (before relaunch) | 6% | 9% | 4% |
   | Week 3 (relaunch) | 10% | 4% | |
   | Week 4 (relaunch) | 7% | | |

   - a. Which cells sit on the diagonal for calendar week 3?
   - b. Write one sentence about day-seven repeat purchase that reads the first column **and** the diagonal.
7. **The holdout sentence.** Cart Rescue v1 recovered **11.8%** of the journey group and **7.9%** of the 10% holdout over two weeks. Write the honest sentence for Anjali: the delta, the window, and why it is soft.
8. **The episode's practice question.** Of 540 people who visited the site, 300 added to cart and 132 bought. Which step would you investigate, and what is one possible confounder?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox and a Workspace project that carries **your own initials**. Never edit someone else's project or data view.
- Do not change any data view, connection or derived field.
- Never use **Create audience from selection**, **Create segment from touchpoint** or **Create a segment for this path**, and never **Publish** anything.
- Do not share or schedule the project. In a shared organisation: look, screenshot, leave.

Steps:
1. Create your own project and **save it manually** the first time. Set the panel's date range to a period that has data (a new panel opens on "This month").
2. Click the **+** inside the panel and choose **Fallout**. Build three or four touchpoints using **dimension items** (open a dimension's items with the **>** in the left panel) and one metric such as orders.
3. Note each touchpoint's count. Switch one touchpoint from **Eventual path** to **Next event** and write down what changes. Then switch the container from **Person** to **Session** and note the change.
4. Right-click a touchpoint and choose **Breakdown fallout at this touchpoint** with any dimension. Write one sentence about where the drop concentrates, and one possible confounder.
5. Optional: add a **Flow** with one item in **Contains**. Open **Show advanced settings**, leave **Include repeat instances** off and set **Flow container** to Person, then **Build**. Hover a node and note its path views, Entries and Exits. Compare the node's number with the fallout's count of people for the same item.

## Check yourself

1. What does a fallout count?
2. What is the difference between Eventual path and Next event?
3. Which container is the default for a fallout, and what does Session change?
4. When do you see Invalid container within segment, and what is the quickest fix?
5. Why is the biggest absolute drop often not the interesting one?
6. What must be held constant in a segment comparison?
7. What is a confounder? Give one for Bloom's checkout leak.
8. What does a flow node count?
9. What does a diagonal in a cohort table show?
10. Why is the Cart Rescue holdout result called soft?

<details><summary>Check your answers</summary>

**Task 1: read the fallout**

| Step | Continued | Dropped | Dropped (share of step before) |
|---|---|---|---|
| Entry to email click | 620 of 2,000 = 31% | 1,380 | 69% |
| Click to site visit | 540 of 620 = 87% | 80 | 13% |
| Site visit to add to cart | 300 of 540 = 56% | 240 | 44% |
| Add to cart to purchase | 132 of 300 = 44% | 168 | 56% |

- c. The biggest absolute drop is entry to email click (1,380 people). It is the normal shape of email: most people who receive a marketing email never click it.
- d. The interesting drop is add to cart to purchase. More than half of the people who had already chosen products did not buy, and the breakdown shows the drop is much worse for one group (mobile, non-Gold) than for others. Overall, 132 of 2,000 entrants (6.6%) bought.

**Task 2: test the settings**
- (i) Eventual path, Person: **A, B and C** all count. The purchase happens any time later, and the Person container joins visits and days.
- (ii) Next event, Person: **only A**. For B, the next event after add to cart was a product page; for C, the next event was the Wednesday cart page view.
- (iii) Eventual path, Session: **A and B**. C bought in a different visit, so the purchase falls outside the session.

**Task 3: the container error (model answer)**
A segment used as a touchpoint must use a container at a lower level than the fallout's own, and a Person segment inside a Person fallout is the same level. Drag the dimension item called "Email click" instead (or use a segment built on a lower container).

**Task 4: two confounders (any two well-argued ones)**
- **Customer tenure and cart size:** mobile shoppers may be newer customers with smaller carts, who abandon more on any device. Test: compare new customers with similar carts on mobile and on desktop, in the same window.
- **Intent or entry channel:** mobile shoppers may arrive from an email tap while browsing, with less intent to buy. Test: compare mobile and desktop within the same entry channel.
- **Time of day:** mobile sessions may cluster late at night. Test: compare the same hours on both devices.
- The strongest test is a randomised one: fix mobile checkout for a random half of shoppers and measure both halves.

**Task 5: flow is not a head count (model answer)**
A flow node counts path views, not people: one shopper who walked the same path in two visits can be counted twice. The number is therefore larger than, or at best equal to, the number of people. For a count of people, use a fallout (or a people metric) and say what you counted.

**Task 6: the cohort table**
- a. Calendar week 3 is the diagonal: Week 2 cohort, second week (9%), and Week 3 cohort, first 7 days (10%).
- b. Model sentence: "Day-seven repeat rose from 6% before the relaunch to 10% in relaunch week, but the older cohort, which bought before Bloom Welcome v1 went live, also rose to 9% that same week, so most of the jump looks like a calendar effect; the second relaunch cohort's 7% suggests Welcome v1 adds a little at most, and two weeks is too soon to say how much."

**Task 7: the holdout sentence (model answer)**
"Over the two-week relaunch fortnight, 11.8% of abandoners who received Cart Rescue v1 were recovered, against 7.9% of the holdout, about 4 more recoveries per 100 abandoners. That is soft because it rests on only two weeks of data, so we will keep the holdout running and re-read it before we quote any revenue."

**Task 8: practice question**
Investigate add to cart to purchase: 168 of 300 people with a cart did not buy (56%), against 240 of 540 (44%) at the step before. One possible confounder: newer customers with smaller carts (or entry channel, or time of day). Break the step down by device and loyalty band, then compare like with like.

**Track B: what to expect**
Next event usually lowers the later touchpoints, because other events often happen in between. Session usually lowers them too, because steps spread over several visits are cut off. A flow node's path views can be higher than the fallout's count of people for the same item. Labels as of October 2026; check what your screen shows.

**Check yourself**
1. People.
2. Eventual path counts a step any time later; Next event counts it only if it is the very next event.
3. Person is the default; Session requires every step inside one visit.
4. When a touchpoint segment's container is equal to or higher than the fallout's container; use the dimension item instead.
5. Some steps always lose many people (most email is never clicked). Interesting drops are worse than expected, or worse for one group than another.
6. The date range, the steps and the settings; only the group should differ.
7. A third factor that explains an apparent relationship. For example, mobile shoppers may be newer customers with smaller carts.
8. Path views, not people.
9. One calendar week across every cohort, so it reveals calendar effects such as a sale, a big send or an outage.
10. It rests on only two weeks of data, so one unusual week could move either rate.

</details>
