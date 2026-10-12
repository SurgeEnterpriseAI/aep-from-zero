# Exercise 31: The flywheel, live

You will draw Bloom's flywheel and mark where each part was built, write the spec for the audience the analysis found, write the expected effect of the journey before it goes live, and design the four-tile exec scorecard and its sharing rules.

## Track A: No Adobe access needed

1. **Draw the flywheel.** Draw Bloom's loop as a circle with five parts: data, audience, journey, measurement, better audience. Beside each part write:
   - a. Where it happens (AEP, Journey Optimizer or CJA).
   - b. The episode range of this series that built it.
   - c. One Bloom object that belongs to it (for example a schema, an audience, a journey, a connection or a data view).
   - d. In one sentence: what proves the loop is closed?
2. **Write the audience spec** for **Checkout Leakers - Mobile**. Include:
   - a. **Source**: which visualisation and step it comes from, and the menu item you use.
   - b. **Refresh frequency**: choose one of One time, Every 4 hours, Daily, Weekly, Monthly, and say why.
   - c. **Lookback**: how many days, and the maximum allowed.
   - d. **The consent rule** it must obey, and who at Bloom must never receive the email.
   - e. **Two limits** you checked before publishing.
   - f. How Journey Optimizer will use it, and why not Audience qualification.
3. **Write the expected effect** of the **Checkout Rescue** journey before it goes live, in this shape: "We expect ___ to ___ within ___, measured by ___, against ___." Then name one vanity metric you will **not** use to judge it, and say why.
4. **Sketch the mobile scorecard.** Draw four tiles at phone width: revenue by channel, journey performance, recovery and day-seven retention. For each tile, write the one number Anjali reads and the baseline or caveat printed beside it, using Bloom's figures:
   - Revenue in the relaunch fortnight: $66,260 from 1,240 orders; "No value" channel: 520 orders
   - Fallout: 2,000 journey entries; 132 purchases
   - Cart Rescue: 11.8% recovery for the journey group, 7.9% for the holdout, two weeks of data
   - Day-seven retention: New This Month by first-order week (no fixed figure; write what the tile shows)

   Then write **who may see it** and **how it is shared**, and the one sharing option you will never use, with the reason.
5. **Run the loop next month.** Name an owner for each step, a cadence and two review triggers.
6. **The episode's practice question.** Kavya adds her revenue per order calculated metric to the audience filter, to keep only small carts, and publishes. What does the published audience actually contain, and how could she have caught it before publishing?

## Track B: If you have CJA access (optional)

Safety first:
- Use a **development** sandbox and your **own** project only.
- This track is **read-only**. Never click **Publish** on the Create audience screen: a published audience lands in Experience Platform for the whole sandbox, and a recurring one keeps refreshing.
- Never use **Share with anyone**, **Schedule** or anything else under **Share**.
- Never publish an audience in a shared organisation. Look, screenshot, leave.

Steps:
1. In Customer Journey Analytics, open **Components**, then **Published audiences**. Read the list only. Note the columns you see and whether any audience refreshes on a schedule.
2. Do not open, create or edit any audience. If the list shows columns such as refresh frequency, note what they say, then leave.
3. Optional: in **Experience Platform**, open **Customer**, **Audiences**, **Browse**, and filter **Origin** for "Customer Journey Analytics". Note whether any audience names carry a CJA audience ID at the end.
4. In Workspace, open the **Project** menu and find **Create mobile scorecard**. Do not create or share anything; just confirm the label your screen shows.

## Check yourself

1. Name two ways to start a CJA audience.
2. What are the five refresh frequency choices?
3. What is the longest refresh lookback window?
4. What is the largest audience CJA can publish?
5. What happens to a calculated metric you add to an audience filter?
6. Does an audience published from CJA escape consent rules? What does Adobe say happens to governance labels at publish?
7. Through which journey entry does Bloom use a CJA audience, and what must be true of that step?
8. When must the expected effect be written down, and why?
9. What proves the loop is closed?
10. Why is Share with anyone never used for board numbers?

<details><summary>Check your answers</summary>

**Task 1: the flywheel (model answer)**

| Part | Where | Episodes | Bloom object |
|---|---|---|---|
| Data | AEP datasets, identity, Real-Time Customer Profile | 3 to 9 | Bloom Customer Profile schema; Bloom Orders dataset |
| Audience | AEP Segment Builder | 10 to 12 | Lapsed 90; Cart Abandoners 24h |
| Journey | Journey Optimizer | 16 to 24 | Bloom Welcome v1; Cart Rescue v1 |
| Measurement | CJA | 25 to 30 | Bloom 360 connection; Bloom Marketing data view |
| Better audience | Published from CJA to AEP | 31 | Checkout Leakers - Mobile |

d. One concrete thing in the next campaign changed because of what the last measurement showed. For Bloom, that is the Checkout Rescue journey.

**Task 2: audience spec (model answer)**
- a. Source: the fallout from journey entry to purchase, broken down to mobile, non-Gold; right-click the add to cart step and choose **Create audience from selection** (or Components, Published audiences, Create audience). Then read the pre-filled filter until it says mobile, not Gold, added to cart, no purchase.
- b. **Daily**, so new leakers join each day and the journey can read fresh people. One time would freeze a snapshot.
- c. 14 days (Bloom's choice); the maximum is **90 days**.
- d. The same consent rules as any other audience: **email consent true** in the filter, as in Lapsed 90, read from the customer profile dataset in Bloom 360. Ananya never gave email consent, so she must never receive Checkout Rescue. Send only through the Marketing channel configuration.
- e. Any two of: at most 20 million people; lookback at most 90 days; no calculated metrics; only a limited number of audiences can refresh on a schedule, depending on the package; up to 20 segments in the filter.
- f. Through **Read audience** as the first step of Checkout Rescue, on a Daily schedule with **Incremental read**, so later runs pick up only newly qualified people. Adobe recommends Audience qualification for real-time needs, but we found no Adobe page confirming a CJA audience can drive it.

**Task 3: expected effect (model answer)**
"We expect more checkout leakers who receive Checkout Rescue to complete a purchase within 7 days of entry, measured by purchase rate, against a random holdout who qualify but are sent nothing." Vanity metric to avoid: open rate. It can look healthy even when nobody buys, and choosing it after seeing the result is how programmes lie to themselves.

**Task 4: the scorecard (model answer)**

| Tile | Number | Baseline or caveat |
|---|---|---|
| Revenue by channel | $66,260 from 1,240 orders | "No value" (520 orders) flagged as a tracking gap, not a channel |
| Journey performance | 2,000 entries to 132 purchases | The checkout step marked as the leak |
| Recovery | 11.8% | Against 7.9% for the holdout; soft, two weeks of data |
| Day-seven retention | New This Month by first-order week | Read the diagonal before crediting a journey |

Who may see it: Anjali and a short list of named people. How: shared with named Workspace users, and a scheduled delivery on Monday at 8:00 AM to a named, reviewed recipient list. Never: **Share with anyone**, because it needs no login, so a forwarded link exposes the numbers.

**Task 5: running the loop (model answer)**
Owners: Rohan (audience and scorecard), Divya (Checkout Rescue), Tara (consent check and sharing list). Cadence: the Monday scorecard at stand-up. Review triggers: the journey group does not beat its holdout after four weeks; the audience size jumps or drops sharply overnight.

**Task 6: practice question**
Audiences cannot include calculated metrics; Adobe says one you add is not included in the definition. So the audience contains every mobile non-Gold leaker, big carts and small carts alike: bigger than Kavya believed. She could have caught it by reading the limits before publishing and checking the Data Preview's total people against what she expected. Testing the confounder belongs in the measurement anyway.

**Track B: what to expect**
Published audiences may be empty in a practice sandbox. In Experience Platform, an audience published from CJA shows Origin "Customer Journey Analytics" with the CJA audience ID appended to its name. Labels as of October 2026; check what your screen shows.

**Check yourself**
1. Right-click in Workspace (fallout, freeform table, flow, cohort table) and choose Create audience from selection; or Components, Published audiences, Create audience.
2. One time, Every 4 hours, Daily, Weekly, Monthly.
3. 90 days.
4. 20 million people.
5. It is not included in the audience definition.
6. No. It obeys the same consent rules as any other audience. The data governance labels and policies on the fields it uses are recorded at publish.
7. Read audience. It must be the first step, a journey can have only one, and only profiles with Realized status enter.
8. Before go-live, because choosing the metric after seeing the result lets you pick the number that flatters you.
9. One concrete change in the next campaign caused by what the measurement showed.
10. It needs no login, so anyone holding the link can open the numbers.

</details>
