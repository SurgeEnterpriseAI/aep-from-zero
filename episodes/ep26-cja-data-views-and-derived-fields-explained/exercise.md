# Exercise 26: Where Bloom's metrics are born

You will decide which Bloom fields become metrics and which become dimensions, write derived-field rules in plain words, work out who a derived-field change affects, and list the checks for a total that does not match its source.

## Track A: No Adobe access needed

1. **Metric or dimension?** For each of these ten Bloom fields, write Metric or Dimension, and one reason.

   | # | Field | Example value |
   |---|---|---|
   | 1 | Order total | 54.00 |
   | 2 | Purchase ID | BLM-88412 |
   | 3 | Product SKU | BLM-SER-VITC-30 |
   | 4 | Product category (from the catalogue lookup) | Skincare |
   | 5 | Loyalty tier | Gold |
   | 6 | Loyalty points | 2,340 |
   | 7 | Email consent | true |
   | 8 | Landing link with UTM tags | a link ending in a medium tag of `Email` |
   | 9 | Journey name (journey step events) | Bloom Welcome v1 |
   | 10 | Add-to-cart event | one row per cart add |

   Then, for the three metrics **Revenue**, **Orders** and **Cart adds**, choose **count values** or **count instances**, and say what Priya's evening of 18 August (one cart add at 7:44 PM, one order of 54.00 at 7:52 PM) adds to each.
2. **Write four derived-field rules in plain words** (no syntax, just clear steps in order):
   - a. **Case When** for the loyalty band: Gold from 1,500 points, Silver from 500, Bronze below 500. Which rule goes first, and what does your Otherwise do?
   - b. **Lowercase** for the channel: what problem does it fix?
   - c. **URL Parse** to read the `utm_campaign` value from a landing link: which option do you choose?
   - d. **Find and Replace** for journey names: turn "Bloom Welcome v1" into "Bloom Welcome".
3. **Who else is affected?** A teammate edits the marketing channel derived field while working in her own data view on Bloom 360. Who else sees the change, and why?
4. **The 2% gap.** Data-view orders for last week are 2% below the source dataset's row count. List your checks, in order, cheapest first.
5. **Sessions.** With a 30-minute session timeout, a customer browses at 8:00 PM, again at 8:20 PM, and again at 9:05 PM. How many sessions is that?

## Track B: If you have CJA access (optional)

Safety first:
- Look only. Never click **Save**, **Create derived field**, **Create data view**, **Create new connection**, **Edit Connection** or **Use in CJA**. Use in CJA bills every row, and a derived field changes every data view on its connection.
- Do not change any value, even a session timeout box that is not greyed out.
- In a shared organisation: look, screenshot, leave.

Steps:
1. Open **Data Management**, then **Data views**, and open a data view you are allowed to read.
2. On **Configure**, note the connection, the time zone and the first day of the week.
3. On **Containers**, note the three containers.
4. On **Components**, use **Search components** to find one metric. Click it and read **Component Settings**: type, format, attribution and behavior (count values or count instances).
5. On **Settings**, read the **Session timeout**. Leave through the **Data views** breadcrumb without saving.

## Check yourself

1. What does a data view decide that a connection does not?
2. Name the four tabs of a data view.
3. What are the three containers, and which one answers "how many customers bought"?
4. What does a 30-minute session timeout mean?
5. What is the difference between count values and count instances?
6. Which component setting applies to dimensions only?
7. Why is a derived field called retroactive?
8. Why must a Case When end with an explicit Otherwise?
9. Who is affected when someone edits a derived field?
10. Name three reasons a data-view total can differ from its source.

<details><summary>Check your answers</summary>

**Task 1: metric or dimension (model answer)**

| # | Field | Answer | Reason |
|---|---|---|---|
| 1 | Order total | Metric | You add it up: it backs Revenue |
| 2 | Purchase ID | Dimension | A label for one order; you do not add IDs up |
| 3 | Product SKU | Dimension | You split revenue by product |
| 4 | Product category | Dimension | Comes from the lookup; you split by it |
| 5 | Loyalty tier | Dimension | A label you compare: Gold against Silver |
| 6 | Loyalty points | Dimension, or the input for the loyalty band | Summing points across orders means little; banding them does |
| 7 | Email consent | Dimension | A true or false label |
| 8 | Landing link with UTM tags | Dimension, and the input for the marketing channel derived field | Nobody reads raw links; you parse them |
| 9 | Journey name | Dimension | You split journey entries by it |
| 10 | Add-to-cart event | Metric | You count it: Cart adds |

Revenue: **count values**; Priya's order adds 54. Orders: **count instances** on the same order total field; her order adds 1. Cart adds: **count instances**; each cart-add row adds 1, so her 7:44 PM cart add adds 1 (her order row adds nothing to Cart adds).

**Task 2: rules in plain words**
- a. Put **Gold** first, the strongest signal (1,500 points and above, Gold), then 500 and above, Silver, then below 500, Bronze. Gold must come first because Priya's 2,340 points are also above 500: with Silver first, she would land in Silver. The **Otherwise** gives a profile with no points its own honest label, so a missing value never hides inside Bronze. These match the thresholds Farhan used at ingestion in episode 5, so the two bands should agree. Check what your own screen offers for comparing numbers in Case When before you build it.
- b. Lowercase merges values typed two ways, such as `email` and `Email`, into one channel.
- c. URL Parse with **Get query string value**, and **Query parameter** set to `utm_campaign`. Adobe prefers URL Parse over Regex Replace for standard parts of a link.
- d. Find and Replace: find " v1" and replace it with nothing. Keep the raw journey name as its own dimension, so anyone can still compare versions. (For messier patterns, Regex Replace is the other cleaning function.)

**Task 3: who else is affected**
Everyone using any data view on Bloom 360, including Bloom Marketing and every report built on it. Derived fields are managed at the connection level, and a change made in any data view on that connection applies across all of them.

**Task 4: the 2% gap, checks in order**
1. Same date range and the same time zone in both counts (AJO reports in UTC; a data view may use another time zone).
2. Late-arriving data: CJA shows new rows within about 90 minutes of reaching AEP, up to 4 hours with stitching.
3. **Records skipped** on the connection: rows with no timestamp or a missing or invalid person ID.
4. Anything in the data view that removes rows: a data-view-wide segment, an exclude rule, metric deduplication.
5. The metric definition itself: count values or count instances, on the right field.
Write the reason for each part of the gap beside the number. Window and timestamp explain most mismatches, which is why they come first; at Bloom, the first check found it (the source query cut the fortnight at midnight in a different time zone).

**Task 5: sessions**
Two. 8:00 and 8:20 PM are 20 minutes apart, one session. 9:05 PM comes 45 minutes after the last activity, so it starts a new session.

**Track B: what to expect**
Configure shows the connection and calendar; on a system-owned data view the fields are greyed out. Containers lists person (People), session and event. Component Settings shows the component type, format and behavior for the metric you clicked. Settings shows the session timeout with a value and a unit.

**Check yourself**
1. Which fields become metrics and dimensions, how they count and give credit, what a session is, and which time zone a day uses.
2. Configure, Containers, Components, Settings.
3. Person, session and event; person answers "how many customers bought".
4. After 30 minutes with no activity, the next event starts a new session.
5. Count values adds the number in the field; count instances adds one per row.
6. Persistence.
7. It is applied at report time, so it changes past data in reports too, with no reload.
8. So the leftover case is a decision, not an accident. For the loyalty band, missing points get their own label instead of hiding in Bronze. For channels, Adobe's guidance is to set the Otherwise to No value, so a later event with no tag never overwrites the channel the customer arrived with.
9. Every data view on the same connection, and every report built on them.
10. Any three of: a different window or time zone, late data, Records skipped, a data-view segment or exclude rule, deduplication, the wrong count setting.

</details>
