# Episode 15: AEP Query Service Tutorial: SQL on the Data Lake

**Watch:** Video coming soon on iTV

[Previous](../ep14-aep-api-tutorial-with-postman-debug-and-rca/) · [Next](../ep16-adobe-journey-optimizer-tutorial-for-beginners/)

## What you will learn

- Explain when **SQL over the data lake** beats the UI, and why Query Service works even without the profile store
- Find a dataset's **table name** and reach nested XDM fields with **dot paths**
- Prove a load with **COUNT(\*)**, then answer business questions with **GROUP BY, SUM, ROUND, YEAR, ORDER BY with LIMIT** and **CASE**
- Explain why an **inner join** silently drops customers who never ordered, and when to use a **LEFT JOIN**
- Explain why Query Service is **append-only**: INSERT INTO only, no UPDATE and no DELETE

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch. In episode 14 Kavya cleared three landmines through the API and wrote five-line root cause analyses. One question was left that the screens, and the one-person-at-a-time Profile Access API, could not answer quickly: across the whole archive, which customers have never ordered at all, and how much did each tier really spend?

## Key ideas

### 1. When SQL over the lake beats the UI (Query Service)
**Query Service** is SQL (structured query language) over the **data lake**, inside AEP. The data lake is the archive: thorough, complete history, not fast. The profile store is the hotel receptionist with perfect memory: one person, right now. Use the screens for one person, one audience rule or one dataflow run. Use SQL for counts, sums and averages by group, joins between datasets, and proving that a load arrived.

Query Service reads datasets in the lake directly, so it works on datasets that are not enabled for Profile. It shows **rows, not merged people**: two rows that share one email are two rows here, even though the profile store folds them into one person.

You will also meet the name **Data Distiller**. This course looks at Query Service and Data Distiller through one lens: SQL over the lake.

### 2. Dataset name to table name, and dots for nested fields
Every dataset is also a table with its own **table name**: lower case, with underscores instead of spaces. `Bloom Customers` becomes `bloom_customers`, `Bloom Orders` becomes `bloom_orders`, and `Bloom Web Events` becomes `bloom_web_events`.

Nested **XDM** (Experience Data Model) fields are reached with **dots**, exactly as in the schema tree: `personalEmail.address`, `person.name.firstName`, and Bloom's own fields under `_bloom`. Copy your paths from your schema tree rather than typing them from memory.

```sql
SELECT personalEmail.address, person.name.firstName
FROM   bloom_customers
LIMIT  5;
```

Table names in these notes carry no initials; your own practice datasets, and so their tables, carry yours.

### 3. Prove the load first: COUNT(*)
The first query is a **proof, not an insight**. Farhan ran these two on the day the 500-row trial files landed in episode 6:

```sql
SELECT COUNT(*) FROM bloom_customers;   -- the 500-row trial file: must say 500
SELECT COUNT(*) FROM bloom_orders;      -- 497: episode 6 rejected 3 rows
```

Bigger loads have landed since (the 10,000-record extract in episode 10). The rule does not change: after every load, compare the count with what you sent.

- **Fewer than expected:** the load is incomplete, and everything built on it is quietly wrong.
- **Double:** the file landed twice. Every successful run **appends** a new batch.
- **Rows are not people.** `COUNT(DISTINCT ...)` on the email counts different addresses, which is smaller on a file with duplicates.

### 4. Business questions in SQL
The examples use the practice CSV column names, so they run in SQLite. In Query Service, use each column's XDM path.

```sql
SELECT loyalty_tier, COUNT(*) AS customers
FROM   bloom_customers
GROUP  BY loyalty_tier
ORDER  BY customers DESC;
```

- **GROUP BY** sorts rows into piles and **COUNT(\*)** counts each pile. **YEAR** pulls the year out of a date, so Priya (joined 2 November 2023) lands in the 2023 pile. **ORDER BY join date DESC LIMIT 5** gives the five newest customers.
- **Revenue per tier** needs a join, because prices live in orders and tiers in customers. Join on **BloomID** (`bloom_id`), not email: the customer file holds duplicate rows on one email, and a key that repeats counts one order twice. **SUM** adds and **ROUND(x, 2)** keeps two decimal places. Total revenue follows headcount; revenue per customer is a different question, so say which one you answer.
- **CASE** is SQL's if-then: when the product is this one, its list price is that number. Comparing each price with it flags defects the platform cannot know about, such as order `BLM-123800` at `-20.00`, which loaded in episode 6 because the platform validates types, not business sense.
- A date that landed in a **text field** can make YEAR come back empty. Types are decided in the schema, so the fix is a correctly typed field and a fresh load, not cleverer SQL.

Adobe documents date functions and joins in Query Service this way; check what your screen shows.

### 5. Inner join versus LEFT JOIN: the zero-order trap
A **join** matches rows from two tables on a shared key. An **inner join** keeps only rows that match on both sides, so a customer with no orders silently disappears. A **LEFT JOIN** keeps every customer and leaves the order columns empty where nothing matched.

Illustrative example: a tier of 100 customers, 40 of whom never ordered, while the other 60 placed 120 orders. The inner join reports 2 orders per customer; the LEFT JOIN reports 1.2. The **ranking of the tiers can change**, and the people who vanished are exactly the ones a retention campaign should reach.

```sql
SELECT COUNT(*) AS never_ordered
FROM   bloom_customers c
LEFT   JOIN bloom_orders o ON o.bloom_id = c.bloom_id
WHERE  o.order_id IS NULL;
```

An inner join can never return these rows, because they have no match. A plain `JOIN` is an inner join; write `LEFT JOIN` to keep the non-buyers.

### 6. Append-only: INSERT INTO, no UPDATE, no DELETE
**Query Service is append-only.** INSERT INTO is the only command that changes a table's rows; there is no UPDATE and no DELETE, in any sandbox. It writes rows into the data lake and never edits a profile. To change data, Adobe's guidance is to insert new records that represent the state you want.

So when the team tried an UPDATE on `personalEmail.address` to fix a wrong email, Query Service refused. The right fix lives upstream: correct the email in the source system and send the corrected record in through the normal dataflow. Handle duplicates in your query (for example with `COUNT(DISTINCT ...)`), not by deleting rows.

### 7. Act One on one whiteboard
Sources (the CRM file, the order history, website clicks), then **Data Prep** cleaning at the door, then **datasets in the lake**, then the **identity graph** (Email, BloomID and ECID resolve to one person), then the **profile store** with its merge policy, then **audiences and destinations** (the agency file carries hashed email and loyalty band only). Around it all: governance, the legal department in the pipes. Side doors: the APIs (episode 14) and Query Service.

### 8. Interview corner: five scenarios that recur

| Scenario | Answer from the build |
|---|---|
| Schema design | Orders are events; loyalty tier is profile |
| A failed dataflow | Three bad rows threw away 497 good orders; partial ingestion set the blast radius |
| Identity design | Email, ECID and BloomID; the sign-in and the order link them |
| Evaluation method | React within minutes? Streaming. If not, batch |
| Governance blocks an export | Contract label C2 on the phone; the policy held |

"Walk me through your identity design" is the most common senior AEP question; answer it from the build.

## In the product

Labels as of October 2026.

1. **Datasets**: open your dataset and copy the value labelled **Table name** from the right rail.
2. **Queries**, then **Create query**. The first time, a notice about query scheduling and a data-governance note may appear; close them.
3. Type the query and run it with **Shift+Enter** or the **Run** (play) button.
4. Results appear under the query, with column headers in capitals.

## Common mistakes

- Typing the display name or someone else's table, and getting "Table or view not found". Copy the Table name from the rail.
- Answering a business question before proving the load with `COUNT(*)`.
- Reading a doubled count as more customers, or rows as people.
- Answering total revenue when the business asked about value per customer.
- Joining on a key that repeats, such as an email shared by duplicate customer rows, so one order is counted twice.
- Using an inner join when the people with nothing are the point.
- Trying to tidy data with UPDATE or DELETE instead of fixing the source.

## Glossary

| Term | Meaning |
|---|---|
| Query Service | SQL over the data lake inside AEP |
| Table name | The SQL name of a dataset, shown in the dataset's right rail |
| Dot path | How SQL reaches a nested XDM field, for example `personalEmail.address` |
| COUNT(*) | Counts every row; the first proof of any load |
| GROUP BY | Sorts rows into piles so each pile can be counted or summed |
| CASE | SQL's if-then, used to apply business rules row by row |
| Join key | The column two tables share, such as BloomID; if it repeats, rows are counted twice |
| Inner join | Keeps only rows that match on both sides; a plain JOIN is an inner join |
| LEFT JOIN | Keeps every row from the left table, matched or not |
| Append-only | Data can be added but never edited or deleted in place |
| INSERT INTO | The only command in Query Service that changes a table's rows |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Query Service SQL syntax (INSERT INTO, append-only): https://experienceleague.adobe.com/en/docs/experience-platform/query/sql/syntax
- Search Experience League for: Query Service overview, Query Editor user guide, Data Distiller

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
