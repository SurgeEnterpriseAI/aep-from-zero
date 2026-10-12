# Exercise 25: Design Bloom 360 and choose the person ID

You will design Bloom's Customer Journey Analytics (CJA) connection on paper, pick a person ID that joins every dataset, trace Priya with stitching off and on, and explain why Journey Optimizer's reports and CJA rarely show exactly the same number.

## Track A: No Adobe access needed

1. **Design the Bloom 360 connection.** Copy this table and fill every cell. Use these datasets: Bloom Web Events, Bloom Orders, Journey Step Events, Bloom Customers, and the 200-product catalogue.

   | Dataset | Type (event, profile, lookup or summary) | Person ID field | Identity stitching on? | Key and matching key |
   |---|---|---|---|---|
   | | | | | |

   Then answer: does Bloom 360 need a summary dataset? What does Adobe require at minimum?

2. **The capital letter problem.** The order feed sends `Priya.Sharma@example.com` and the customer file sends `priya.sharma@example.com` for the same customer. What does CJA do with these rows, and where would you fix it? Write two or three sentences.

3. **Trace Priya.** Here are three of her rows from the evening of 18 August.

   | Time | Dataset | What happened | Identities on the row |
   |---|---|---|---|
   | 7:44 PM | Bloom Web Events | Add to cart, `BLM-SER-VITC-30` | ECID `38472919862011456743` |
   | Between 7:44 and 7:52 PM | Bloom Web Events | App sign-in | ECID `38472919862011456743` and email `priya.sharma@example.com` |
   | 7:52 PM | Bloom Orders | Order `BLM-88412`, total 54.00 | email `priya.sharma@example.com`, BloomID `BLM-CUST-004217` |

   The web events use the ECID as their person ID and the orders use `orderEmail`. For each case, stitching **off** and stitching **on**, write how many people CJA counts and how many cart abandoners.

4. **Two screens, two numbers.** Journey Optimizer's report shows slightly more sends than CJA for the same morning. Give three legitimate reasons, and say how big Adobe says the normal gap is.

5. **Spot the trap.** A teammate says: "The AJO Enabled Connection already has our sends. Let's compare Gold and Silver opens there, and switch on Use in CJA so we can build on it." Write your reply in three sentences.

## Track B: If you have CJA access (optional)

Safety first:
- This track is **read only**. Look, screenshot, leave.
- Never click **Create new connection**, **Create new data view**, **Edit Connection**, **Refresh**, **Create data view**, **Save** or **Delete**.
- Never switch on **Use in CJA**. Each row then counts toward the organisation's monthly licensed rows, and switching it off still bills the full month.
- Never open or change anyone else's objects.

Steps:
1. Open CJA from the application selector (the nine-dot icon, top right). Note the top menu: Workspace, Data Management, Components, Tools, Labs.
2. Open **Data Management**, **Connections**. Read the columns of the list. Do not click Create new connection.
3. Click the name of one connection you are allowed to see. Read **Records added**, **Records skipped** and **Records deleted**.
4. Scroll to its list of datasets. For each one, note its type and, where your screen shows it, its person ID. If the person ID is only visible inside Edit Connection, ask your administrator to show you instead of opening the form yourself.
5. Write one sentence on what that connection could not tell you (for example, whether it holds any customer profile data).

## Check yourself

1. What does CJA read, and what does it not read?
2. Name the four dataset types. Which one needs no person ID, and what does it need instead?
3. What are the three rules about a person ID?
4. Why did Rohan choose `orderEmail` instead of BloomID on the orders dataset?
5. What does identity stitching do on Bloom Web Events?
6. What does Records skipped count?
7. How much event data does Bloom 360 keep, and how quickly does new data appear?
8. Which connection setting cannot be changed after you save?
9. Why can the AJO Enabled Connection not compare Gold and Silver?
10. Why is Use in CJA never a learner's click?

<details><summary>Check your answers</summary>

**Task 1: the Bloom 360 connection (model answer)**

| Dataset | Type | Person ID field | Identity stitching on? | Key and matching key |
|---|---|---|---|---|
| Bloom Web Events | Event | ECID on the raw rows; stitching gives them the email from the sign-in row | Yes | Not needed |
| Bloom Orders | Event | `orderEmail` | No | Not needed |
| Journey Step Events | Event | The email | No | Not needed |
| Bloom Customers | Profile | The profile's email (`personalEmail.address`) | Not applicable | Not needed |
| Product catalogue | Lookup | None | Not applicable | Key: SKU in the catalogue. Matching key: SKU on each event's product line |

No summary dataset is needed. Adobe requires at least one event or summary dataset in a connection, and Bloom 360 has three event datasets.

**Task 2: the capital letter problem**
The person ID is case sensitive, so CJA treats the two values as **two different people**, and Priya's order and profile never meet. Fix it at the door, before the data lands: a calculated field in Data Prep that lower-cases and trims every email (episode 5). A mapping fix applies to rows that land after it, so agree with the data engineer how older rows will be corrected.

**Task 3: tracing Priya**
- Stitching **off**: **two people**. The ECID person added to cart and signed in but never bought; the email person bought without browsing. **One cart abandoner, and it is false.**
- Stitching **on**: the sign-in row gives the email to the anonymous rows that share its ECID. **One person**, who bought 8 minutes after adding to cart. **Zero abandoners.**

**Task 4: two screens, two numbers**
1. Journey Optimizer's sent counts include retries; CJA's do not.
2. Journey Optimizer reporting is in UTC; a CJA data view can use another time zone.
3. The message feedback dataset arrives in batches up to 2 hours late.

Also accept: CJA latency (within 90 minutes of data reaching Experience Platform, up to 4 hours with stitching). Adobe says the normal gap is typically less than 1-2%, larger for data from the last two hours.

**Task 5: the trap (model reply)**
The AJO Enabled Connection holds only Journey Optimizer's datasets and no customer profile data, so it cannot split opens by Gold and Silver. That needs our own connection with the profile dataset and a person ID that matches the event datasets, which is Bloom 360. And Use in CJA bills every row toward the organisation's licensed rows, so only the owner decides it.

**Track B: what to expect**
A connection's details page shows the record counters and, on the right, Refresh, Create data view and Use in CJA. A system connection named AJO Enabled Connection, owned by Journey Optimizer, may appear for each sandbox. Its datasets are Journey Optimizer's own, such as Journey Step Events and the AJO Email Tracking Experience Event Dataset, so it cannot tell you anything about loyalty tiers.

**Check yourself**
1. Datasets in the AEP data lake, through a connection. It does not read the Real-Time Customer Profile (the profile store).
2. Event, profile, lookup and summary. A lookup needs no person ID; it needs a Key and a Matching key. (A summary dataset is not tied to a person either.)
3. It is case sensitive, rows without it are skipped, and it must match across datasets for them to merge.
4. A person ID must match across datasets, and only the email can reach every Bloom dataset (on web events, through stitching); BloomID never reaches the customer or web datasets as an identity.
5. It gives Priya's anonymous ECID rows and her logged-in rows one person ID, the email from her sign-in row.
6. Rows with no timestamp, or with a missing or invalid person ID.
7. A rolling 13 months. New data appears within 90 minutes of reaching Experience Platform, up to 4 hours with stitching.
8. The sandbox.
9. It holds no customer profile data, so there is no loyalty tier to split by.
10. Each row then counts toward the organisation's monthly licensed rows, and switching it off later still bills the full month. It is the owner's decision.

</details>
