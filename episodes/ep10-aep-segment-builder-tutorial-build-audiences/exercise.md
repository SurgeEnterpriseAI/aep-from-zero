# Exercise 10: The relaunch five

You will build Bloom's five relaunch audiences on paper, refuse the trap conditions, turn a vague brief into decisions, and read the rule language the Segment Builder writes for you.

No files are needed for Track A. Everything you need is on this page.

## Track A: No Adobe access needed

1. **Build the relaunch five.** For each audience below, write:
   - the rule in one plain sentence
   - which conditions from its list belong (some are traps)
   - one reason why each trap condition is wrong
   - which of the four kinds of logic it uses: attribute, event with a time window, sequential, exclusion

   | Audience | Candidate conditions |
   |---|---|
   | High-Value Loyalists | (a) Loyalty band is Gold · (b) 3+ orders in the last 12 months · (c) Email opens 3 or more · (d) Home city is Dallas · (e) Has an ECID |
   | Cart Abandoners 24h | (a) Add-to-cart event occurred · (b) NOT followed by a purchase within 24 hours · (c) Cart total is over $50 · (d) Loyalty band is Gold · (e) Product views 5 or more |
   | Lapsed 90 | (a) Last order more than 90 days ago · (b) Email consent is true · (c) No orders ever · (d) Loyalty points below 500 · (e) SMS consent is true |
   | New This Month | (a) First-ever order within the last 30 days · (b) Has placed any order, ever · (c) Profile created in the last 30 days · (d) Loyalty band is Bronze |
   | Window Shoppers | (a) Product views 5 or more in the last 30 days · (b) Zero orders ever · (c) Add-to-cart at least once · (d) Loyalty band is Gold · (e) Last order more than 90 days ago |

2. **Find the four decisions.** Anjali asks for "our good customers in Texas". Rewrite her request as four decisions someone must own: *good*, *customers*, *in Texas* and the unsaid one, *consent*. For each, list the options and suggest who at Bloom should own it.
3. **Write the PQL.** The rule "lives in Texas" reads `homeAddress.stateProvince = "TX"`. Order events carry a purchase ID at `commerce.order.purchaseID`. Write the PQL for "lives in Texas **and** has at least one order".
4. **Explain Ananya.** In three sentences, explain why Ananya, who never gave email consent, can never be in the win-back file. Then say what would go wrong if the three consent columns had stayed in the email and phone status fields where auto-map first put them.
5. **The episode's practice question.** Which kind of logic does Cart Abandoners need, what is its time window, and why does Priya never qualify? (She added a Vitamin C Serum to her cart on her phone at 7:44 PM and bought on her laptop at 7:52 PM.)

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production, and put **your own initials** on everything you create.
- Save **drafts only**. Do not click **Publish** or **Activate**, and do not add your audience to any journey, campaign or destination.
- Never edit or delete an audience that is not yours. In a shared sandbox: look, screenshot, leave.

Steps:
1. Go to **Customer**, **Audiences**, then **Create audience**. Read both options, choose **Build rule**, and click **Create**.
2. Before you build anything, write down what the three panels hold: the **Fields** tabs on the left, the canvas in the centre, and **Audience properties** on the right.
3. In **Attributes**, expand **XDM Individual Profile**, then `homeAddress`, and drag `stateProvince` onto the canvas. Set the operator to **equals** and the value to `TX`.
4. Name it **Texas customers** followed by your initials. Leave **Evaluation method** on **Batch**.
5. Open **Code view** and copy the PQL into your notes. Compare it with your answer to Track A, task 3.
6. Optionally, switch to **Events**, add an order event condition, and read **Code view** again to see how the rule grows.
7. Read **Qualified profiles** and **Estimated profiles**. If the estimate reads about 0 with "Last updated: Not available", that is expected until profile data exists; it does not prove your rule is wrong (episode 11 explains estimates).
8. Click **Save as draft**, and stop there.

## Check yourself

1. What is the difference between a list and an audience, and why does it matter commercially?
2. Why do audience rules only become trustworthy after identity stitching?
3. When would you choose **Compose audience** instead of **Build rule**?
4. Name the three tabs in the Segment Builder's **Fields** panel and the question each one answers.
5. Write the cart-abandoner rule in words. What two things does it need that a spreadsheet cannot express?
6. Why is "Email opens 3 or more" a trap condition for High-Value Loyalists right now?
7. Why does High-Value Loyalists depend on episode 5's calculated field?
8. Where does Bloom enforce consent for the win-back, and what earlier fix makes that possible?

<details><summary>Check your answers</summary>

**Task 1: the relaunch five**

| Audience | Rule in one sentence | Keep | Traps and why | Logic |
|---|---|---|---|---|
| High-Value Loyalists | Loyalty band is Gold and 3+ orders in the last 12 months | a, b | (c) the platform holds no email opens yet, so it would match nobody; (d) geography says nothing about value; (e) anyone who opens the Bloom app or website gets an ECID, so it says nothing about value | Attribute plus event with a time window |
| Cart Abandoners 24h | Added to cart, not followed by a purchase within 24 hours | a, b | (c) Bloom chases all abandoned value, not just big carts; (d) abandoners come from every tier; (e) heavy browsing is a different audience, Window Shoppers | Sequential, with a time window |
| Lapsed 90 | Last order more than 90 days ago and email consent true | a, b | (c) never-buyers are not lapsed, they never started; (d) points do not define lapsed, recency does; (e) the win-back is an email, so SMS consent is irrelevant | Event with a time window plus attribute |
| New This Month | First-ever order within the last 30 days | a | (b) nearly every customer has ordered at some point in 18 months; you want the first order; (c) a CRM row is not a purchase; (d) tier does not mean new | Event with a time window |
| Window Shoppers | 5+ product views in 30 days and zero orders ever | a, b | (c) a cart is the abandoner's territory, window shoppers only look; (d) window shoppers are mostly not loyalty members at all, and a tier says nothing about browsing; (e) they have zero orders, so this contradicts the audience | Event with a time window plus exclusion |

**Task 2: the four decisions**
- *Good*: loyalty band, lifetime spend or order count, and over what period. A business owner decides; at Bloom that is Anjali.
- *Customers*: anyone with a profile, or only people who have purchased. Marketing decides, with the data team confirming what the data can support.
- *In Texas*: home address, billing address, or the shipping address of the last order. They can differ, so the data owner (Farhan) says which field is reliable and marketing chooses.
- *Consent*: do we hold valid marketing consent for this person? If not, nothing else matters. Legal and privacy own the rule; the audience must include it.

**Task 3: the PQL**
```
homeAddress.stateProvince = "TX"
  AND
xEvent[ commerce.order.purchaseID != null ].count() >= 1
```
The second part counts order events that carry a purchase ID and checks there is at least one. A real Code view may print it slightly differently (for example, a lower-case `and`), so compare the meaning, not the exact spelling.

**Task 4: Ananya**
Lapsed 90 requires email consent to be true, and Ananya never gave it, so she never qualifies. Because the win-back file is built from Lapsed 90, she can never appear in it, whoever exports it and whenever. If the consent columns had stayed in the email and phone status fields, which describe delivery rather than permission, the rule would have had no real consent field to read, so consent would fall back to a manual check that someone can forget.

**Task 5: practice question**
Sequential logic: an add-to-cart event not followed by a purchase, with a 24-hour window. Priya's add-to-cart at 7:44 PM was followed by a purchase at 7:52 PM, so she never qualifies. That is only true because identity stitching joined her phone and her laptop into one profile; unstitched, her phone fragment would look abandoned.

**Track B: what to expect**
Code view should show `homeAddress.stateProvince = "TX"` for the attribute rule. Your estimate may read about 0 in a sandbox with little profile data. Your saved draft appears under **Audiences**, **Browse** with your initials in the name and an evaluation method of Batch.

**Check yourself**
1. A list is a snapshot that starts rotting on export; an audience is a rule the platform keeps re-evaluating. Commercially: no more two-day list pulls, and no more messages to people who no longer qualify.
2. Rules read the merged profile. On unstitched fragments, one person's browsing and buying look like different people, so rules are silently wrong.
3. When you already have audiences and want to combine them: union, exclusion or splits.
4. Attributes (what is true about this person?), Events (what did this person do, and when?), Audiences (who is already in another audience?).
5. Add-to-cart not followed by a purchase within 24 hours. It needs event ordering and a clock.
6. Nothing has been sent through the new platform yet, so it holds no email opens; the condition would match nobody and empty the audience. It only becomes meaningful once Journey Optimizer starts sending.
7. It reads the derived loyalty band, which that calculated field produces from points. If the band breaks, the audience quietly thins (episode 14).
8. Inside the Lapsed 90 rule (email consent is true). It works because episode 6 re-mapped the consent columns to the `_bloom` consent fields.

</details>
