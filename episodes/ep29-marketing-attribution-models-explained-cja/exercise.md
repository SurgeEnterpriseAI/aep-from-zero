# Exercise 29: Referee the revenue

You will re-create Adobe's 50-dollar example under several models, apply three models to Priya's illustrative two touches, read a practice comparison table for its swing, write the three-sentence recommendation for Anjali, and decide who is affected when a model is changed in each of the three places.

## Track A: No Adobe access needed

1. **Adobe's 50-dollar example.** A shopper's touches, in order: a paid search ad (15 September), a friend's social link (18 September), an email with a coupon (24 September), then a display ad, and a purchase of $50. Using a **Person** container and a **30-day** lookback, compute each channel's credit under:
   - a. First Touch
   - b. Last Touch
   - c. Linear
   - d. U Shaped (40% first, 40% last, 20% shared by the middle)
   - e. Bonus: J Curve and Inverse J
   - f. Now switch to a **Session** container. Only the visit with the purchase counts, and in it the email came before the display ad. What does First Touch give now?
2. **Priya's illustrative two touches.** Say, for example, Priya first arrived on her phone from a paid search ad, then came back through a Bloom email on her laptop and paid $54.
   - a. Compute First Touch, Last Touch and Linear.
   - b. U Shaped is defined for a first, a last and a middle touch. What is unclear when there are only two touches, and what should you do before quoting a U Shaped figure?
   - c. In one sentence: why could no model credit paid search if Bloom 360 did not stitch her web events?
3. **Read the swing, then write the recommendation.** These practice numbers are **illustrative, invented for this exercise only, and not Bloom's results**. An attribution panel over two weeks, Person container, 30-day lookback:

   | Channel | Last Touch | First Touch | Linear |
   |---|---|---|---|
   | Email | $16,000 | $11,000 | $13,500 |
   | Paid search | $9,000 | $15,000 | $12,000 |
   | Social | $7,000 | $7,500 | $7,300 |
   | Display | $8,000 | $6,500 | $7,200 |
   | Attributed in total | $40,000 | $40,000 | $40,000 |

   - a. Which channel is the opener, which is the closer, and which barely move?
   - b. The panel's total revenue for the same dates is higher than $40,000. Why do the columns add up to less, and which earlier Bloom finding is the same problem?
   - c. Write the three-sentence recommendation for Anjali: where the money moves (as ranges), the model and window, and the test that would confirm it.
4. **Three places, three audiences.** For each place a model can be set (one metric column, inside a calculated metric, the data-view default), say who is affected if you change it.
5. **The episode's practice question.** In Adobe's 50-dollar example, switch to a **Session** container. Under Linear, how much does email earn, and why?

## Track B: If you have CJA access (optional)

Safety first:
- Use a **development** sandbox and your **own** Workspace project, named with your initials.
- **Do not change any data-view default** (leave **Set attribution** alone), and do not edit anyone else's calculated metrics.
- Do not share, schedule or publish anything, never use **Share with anyone**, and do not create an audience from this panel.
- In a shared environment: look, screenshot, leave.

Steps:
1. Open your own project. Check the panel's data view (top right) and set the panel dates; a new panel opens on **This month**.
2. Choose **Insert**, **Attribution**. Success metric: a revenue metric. Channel: a channel dimension. Included models: **Last Touch**, **First Touch** and **Linear**. Container: **Person**. Lookback window: **30 Days**. Click **Build**.
3. Read the comparison table's column headers. Write down the model, container and lookback window each one shows.
4. Name one opener, one closer and one steady channel, with the numbers that show the swing.
5. Compare the panel's total with one model column, and explain the gap in one sentence.
6. Scroll down to **Channel overlap**. Which two channels overlap most?
7. In a freeform table, open one metric's **Column settings** and look at **Use non-default attribution model** without applying it. Save only your own project.

Labels as of October 2026; check what your screen shows.

## Check yourself

1. What are a touch, a lookback window and a container?
2. What happens to a touch outside the lookback window?
3. What does choosing a Session container do to the lookback window?
4. Which model is typically the default?
5. Why must you never add up a Participation column as revenue?
6. What is the swing, and how does it tell an opener from a closer?
7. Why is the attributed total smaller than total revenue?
8. Why can a freeform table and an attribution panel show different revenue for the same channel?
9. Which of the three places to set a model affects everyone?
10. Why is attributed revenue not incremental revenue, and how do you measure what a channel really adds?

<details><summary>Check your answers</summary>

**Task 1: Adobe's 50-dollar example (Person, 30 days)**

| Model | Paid search | Social | Email | Display |
|---|---|---|---|---|
| a. First Touch | $50 | $0 | $0 | $0 |
| b. Last Touch | $0 | $0 | $0 | $50 |
| c. Linear | $12.50 | $12.50 | $12.50 | $12.50 |
| d. U Shaped | $20 | $5 | $5 | $20 |
| e. J Curve | $10 | $5 | $5 | $30 |
| e. Inverse J | $30 | $5 | $5 | $10 |

- f. Email gets the whole $50. Only the final visit counts, and email came before display in it.

**Task 2: Priya (illustrative)**
- a. First Touch: paid search $54, email $0. Last Touch: email $54, paid search $0. Linear: $27 each.
- b. With two touches there is no middle, and the definition used in this episode does not say where the middle 20% goes. Check Adobe's documentation, or what your own panel shows, before quoting a U Shaped figure.
- c. Without stitching, her anonymous phone visit and her laptop order belong to two different people in CJA, so the paid search touch is never in the same person's path as the order.

**Task 3: practice numbers**
- a. Paid search is the opener: $15,000 under First Touch against $9,000 under Last Touch. Email is the closer: $16,000 under Last Touch against $11,000 under First Touch. Social barely moves ($7,000 to $7,500). Display leans slightly towards closing ($6,500 to $8,000).
- b. Orders with no channel touch inside the 30-day lookback window earn no credit, so they are in the total but in no column. It is the same tracking gap as the 520 **No value** orders in episode 27 (the amounts differ because the rules differ).
- c. Model answer: "Over these two weeks, email earned $11,000 to $16,000 and paid search $9,000 to $15,000 depending on the model; paid search mostly opens sales and email mostly closes them, while social and display barely move. These figures use Last Touch, First Touch and Linear, a Person container and a 30-day lookback, and they are attributed, not incremental. Before we move any budget, we will hold back a random group from email for two weeks and compare their purchases with everyone else's."

**Task 4: three places**
- One metric column: only that column, in your own project.
- Inside a calculated metric: everyone who uses that metric.
- Data-view default: that metric in every report built on that data view, for everyone, including people who never knew it changed.

**Task 5: practice question**
Email earns $25. With a Session container only the final visit counts, and it holds two touches, email and display, so Linear splits the $50 equally between them. (Under a Person container, Linear gave email $12.50.)

**Track B: what to expect**
Each column header in the comparison table names its rules, for example Last Touch, Person, 30 Days. The model columns add up to less than the panel's total. Channel overlap shows a Venn of the top three channels. If your freeform table shows a different number for a channel than the panel, check which model each one uses before you call either one wrong.

**Check yourself**
1. A touch is one contact between a person and a channel. The lookback window is how many days before the conversion a touch can still earn credit. The container (Person or Session) decides whose touches count together.
2. It earns nothing, however important it was.
3. It forces the lookback window to the reporting window, and you cannot change it.
4. Last Touch.
5. Participation gives 100% credit to every unique touch, so the column adds up to more than the real total.
6. The swing is how much a channel's credit changes between models. A channel that gains under First Touch is an opener; one that gains under Last Touch is a closer.
7. Orders with no channel touch inside the lookback window earn no credit.
8. The freeform table uses the data view's default attribution; the panel uses the model and lookback you chose. Both are honest if you say which one you used.
9. The data-view default (Set attribution).
10. Attribution shares out credit for sales that happened; it cannot show what would have happened without the channel. A holdout, a randomly withheld group, measures that.

</details>
