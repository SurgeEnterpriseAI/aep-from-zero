# Exercise 32: The one-page memo

You will build the Adobe Analytics to Customer Journey Analytics (CJA) translation table, write a five-sentence answer to the migration question, list what a migration must rebuild and what it cannot bring across, and tie two CJA-only features to Bloom questions.

## Track A: No Adobe access needed

1. **Fill the translation table.** For each Adobe Analytics term, write the CJA equivalent and one Bloom example.

   | # | Adobe Analytics term | CJA equivalent | Bloom example |
   |---|---|---|---|
   | 1 | Hit | | |
   | 2 | Visit | | |
   | 3 | Visitor | | |
   | 4 | Report suite | | |
   | 5 | eVar | | |
   | 6 | Classification | | |
   | 7 | Customer attribute | | |
   | 8 | Processing rule | | |
   | 9 | Entries | | |
   | 10 | Exits | | |

2. **Write the five-sentence answer** to a client who says: "We run Adobe Analytics. What changes if we move to CJA?" Use the three words person-based, dataset-based and retroactive, give one Bloom example for each, and end with one honest sentence about what must be rebuilt.
3. **Two lists.**
   - a. What a migration must **rebuild** by hand.
   - b. What it **cannot bring across** at all, as of 2026.
4. **Pick two CJA-only features** from this list: Journey canvas, Experimentation analysis, Forecasting, SQL access and the BI Extension. For each, write the Bloom question it would answer and the data it would need.
5. **Data Prep or derived field?** For each rule, choose the layer and give one reason:
   - a. Phone numbers arrive in five shapes and must become `+1XXXXXXXXXX` before journeys use them.
   - b. Marketing channel values `email` and `Email` must be one channel in reports, including last fortnight's orders.
   - c. A client's old Adobe Analytics processing rule copied a campaign code into a custom variable.

## Track B: If you have both products (optional, read only)

Safety first:
- Look only. Never click **Save**, **Create data view**, **Create new connection**, **Edit Connection**, **Use in CJA**, **Publish** or **Activate**. Use in CJA bills every row, and it is the organisation owner's decision.
- Do not edit a report suite, a data view or any component.
- In a shared organisation: look, screenshot, leave.

Steps:
1. In Adobe Analytics, open the component list of one report suite you are allowed to read. Count how many eVars and props are in use, and note three of their names.
2. In CJA, open **Data Management**, **Data views**, and open one data view you are allowed to read. On **Components**, note three dimensions and the schema fields behind them.
3. For each of your three Adobe Analytics variables, write which CJA dimension (if any) holds the same idea.
4. On the data view's **Settings** tab, read the **Session settings**. Leave without saving.

## Check yourself

1. What are the CJA names for hit, visit and visitor?
2. What is the CJA equivalent of a report suite?
3. Why does CJA have no eVars or props, and what takes their place?
4. What does "retroactive" mean for attribution in CJA, and what is the risk?
5. What do classifications and customer attributes become?
6. Which two layers replace processing rules and VISTA rules, and when do you choose each?
7. Can existing Adobe Analytics segments and calculated metrics be migrated?
8. Name two Adobe Analytics features that are not supported in CJA.
9. Why are hourly alerts not available in CJA, and what is available instead?
10. Give the three-word interview answer, with one example per word.

<details><summary>Check your answers</summary>

**Task 1: translation table (model answer)**

| # | Adobe Analytics term | CJA equivalent | Bloom example |
|---|---|---|---|
| 1 | Hit | Event | Priya's order row at 7:52 PM, purchase ID BLM-88412 |
| 2 | Visit | Session | Priya's evening activity; a session ends after 30 minutes of quiet in Bloom Marketing |
| 3 | Visitor | Person | Priya's phone add-to-cart and laptop order, one person through her email in Bloom 360 |
| 4 | Report suite | Data view | Bloom Marketing |
| 5 | eVar | Any schema field, used as a dimension (no eVars in CJA) | Loyalty tier, product SKU, journey name |
| 6 | Classification | Lookup dataset (Key and Matching key) | The 200-product catalogue joined on SKU, so `BLM-SER-VITC-30` shows as Vitamin C Serum 30 ml |
| 7 | Customer attribute | Profile dataset (needs a person ID) | The customer profile in Bloom 360, so Gold compares with Silver |
| 8 | Processing rule | Experience Platform Data Prep, or a derived field | Data Prep cleaned phones and emails; a derived field built the marketing channel |
| 9 | Entries | Session Starts | Where Priya's session began |
| 10 | Exits | Session Ends | Where her session ended |

**Task 2: a model five-sentence answer**

"Customer Journey Analytics is a separate product from Adobe Analytics, and it is person-based, dataset-based and retroactive. Person-based: at Bloom, a customer's phone visit and laptop order are one person, because the connection stitches them on her email. Dataset-based: the Journey Optimizer datasets sit in the same connection as orders and the customer profile, so journeys and revenue are read together. Retroactive: attribution and derived fields apply at report time, so a Lowercase rule merged 'email' and 'Email' (150 and 30 orders) into 180, past data included. The honest part: your segments and calculated metrics must be rebuilt, and Activity Map, Contribution analysis and hourly alerts do not come across."

**Task 3: two lists**
- a. Rebuild: every segment and every calculated metric (Adobe: none of the existing ones are compatible), plus alerts set up again on a daily, weekly or monthly schedule, and every processing rule re-decided as Data Prep or a derived field.
- b. Cannot bring across, as of 2026: Activity Map and Contribution analysis ("No support, not yet planned"), hourly alerts, and project sharing with Analysis Workspace in Adobe Analytics (CJA projects share only between CJA users).

**Task 4: CJA-only features (any two)**
- Journey canvas: how do new customers move between email, app and site before a second order? Needs the web, order and journey step events in one connection, joined on one person ID.
- Experimentation analysis: did Cart Rescue beat its holdout (11.8% recovery against 7.9%)? Needs data view dimensions carrying the context labels Experimentation Experiment and Experimentation Variant; without them the panel has no experiments to work with. Still soft after two weeks.
- Forecasting: what might next fortnight's revenue look like if nothing changes? Needs enough revenue history in the data view.
- SQL access and the BI Extension: can finance report the same revenue definition in its own tool? Needs the data view's revenue metric, defined once.

Bloom has not used these four. Adobe documents them this way; check what your screen shows.

**Task 5: Data Prep or derived field?**
- a. **Data Prep**, at the door: journeys and profiles need the clean phone, not just reports.
- b. **Derived field**: only reporting needs it, and the past must change too. Lowercase merges the two values retroactively.
- c. Decide by use. If only reports need the campaign, a derived field on the schema field that holds the code; if journeys or audiences need it, Data Prep at ingestion. Do not recreate a "custom variable": any schema field can be a dimension.

**Check yourself**
1. Event, session, person.
2. A data view.
3. CJA works on any Experience Platform schema field, so any field can be a dimension or metric, with no fixed count and no unique-value limit.
4. Attribution is applied when the report runs, so a change also rewrites past numbers. Changing a metric's default in the data view changes everyone's numbers, so write down the model and window.
5. Lookup datasets and profile datasets.
6. Data Prep at the door, when journeys and profiles need the clean value; derived fields at report time, when only reports need it or the past must change.
7. Not as they are. Adobe says none of the existing segments or calculated metrics are compatible; rebuild them.
8. Activity Map and Contribution analysis.
9. Adobe gives the timing of data collection as the reason (data arrives within about 90 minutes, up to 4 hours with stitching). Alerts run daily, weekly or monthly.
10. Person-based (phone and laptop, one person), dataset-based (journey datasets beside orders and profile), retroactive (a derived field fixes last fortnight's data).

</details>
