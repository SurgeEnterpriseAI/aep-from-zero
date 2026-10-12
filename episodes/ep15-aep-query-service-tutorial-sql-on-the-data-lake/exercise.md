# Exercise 15: Ask the archive

You will load Bloom's two trial files into a free SQL tool, prove the load, answer Bloom's business questions, fall into the join trap on purpose, and explain why Query Service will not let you edit a row.

## Track A: No Adobe access needed

You need `bloom-customers-500.csv` and `bloom-orders-500.csv` from the course's `data` folder, and any SQL tool. SQLite works (DB Browser for SQLite, or the `sqlite3` command line).

1. **Load the files.** Create two tables named `bloom_customers` and `bloom_orders`, one per file. In the `sqlite3` command line:
   ```
   .mode csv
   .import bloom-customers-500.csv bloom_customers
   .import bloom-orders-500.csv bloom_orders
   ```
2. **Prove the load.** Run `SELECT COUNT(*)` on both tables. Then answer: why does `bloom_orders` give a different count here from the Bloom Orders dataset in the episode?
3. **Rows or people?** Count the rows in `bloom_customers`, then count the distinct email addresses. Explain the difference in one sentence.
4. **Customers per loyalty tier**, biggest tier first.
5. **Revenue per tier.** Join orders to customers on `bloom_id` and write two queries: total revenue per tier, and revenue per customer per tier, both with `ROUND(..., 2)`. In this file, `price` is the line total for the row. Which question does each query answer? Bonus: count the rows of the join on `bloom_id`, then the same join on `email`. Why does the email join return more rows than there are matching orders?
6. **New customers by join year.** SQLite has no `YEAR()` function, so use `strftime('%Y', join_date)`.
7. **The five newest customers**: first name, last name, email and join date.
8. **Below list price.** Use these practice list prices (illustrative, taken from the single-unit prices in the sample file) in a `CASE`, and list every order row whose `price / quantity` is below its list price. Which orders turn up, and why did the platform load one of them in episode 6?

   | SKU | List price (USD) |
   |---|---|
   | BLM-CLN-GEL-150 | 16 |
   | BLM-LIP-BALM-08 | 9 |
   | BLM-MOIST-HYA-50 | 20 |
   | BLM-MSK-CLAY-100 | 24 |
   | BLM-SER-RET-30 | 42 |
   | BLM-SER-VITC-30 | 34 |
   | BLM-SPF-MIN-50 | 26 |
   | BLM-SUP-COLL-30 | 38 |
   | BLM-SUP-MULTI-90 | 22 |
   | BLM-SUP-OMG3-60 | 28 |

9. **The join trap.** Write orders per customer, by loyalty tier, twice: once with `JOIN` and once with `LEFT JOIN`. Compare the two rankings. Then count the customers who never ordered, using `LEFT JOIN ... WHERE o.order_id IS NULL`, and try the same count with an inner join.
10. **Append-only.** In two or three sentences, explain why an `UPDATE` cannot fix a wrong email in Query Service, and what you would do instead.
11. **Interview drill.** Pick one of the five recurring AEP scenarios (schema design, a failed dataflow, identity design, choosing an evaluation method, governance blocking an export) and answer it aloud in under a minute, using something you built or followed in this series.
12. **The episode's practice question.** Anjali wants to know how many Gold customers have never placed an order. Which join do you use, and what would an inner join return?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- Run **read-only** queries: `SELECT` only. Never run `INSERT INTO`, and never query or change another person's datasets.
- Query only a dataset you created yourself, named with your own initials.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Open **Datasets**, open your own dataset, and copy the value labelled **Table name** from the right rail.
2. Open **Queries**, then **Create query**. If a notice about query scheduling or data governance appears, read it and close it.
3. Type `SELECT COUNT(*) FROM your_table_name;` using the table name you copied, and run it with **Shift+Enter** or the **Run** button.
4. Compare the count with the number of rows in the file you loaded. Note the column header: it shows in capitals.
5. Copy one nested field path from your schema tree (for example `personalEmail.address`) and run a warm-up: `SELECT personalEmail.address FROM your_table_name LIMIT 5;`

## Check yourself

1. When does SQL over the data lake beat the UI? Give two examples.
2. Why does Query Service still work when profile ingestion is not running?
3. How do you find a dataset's table name, and what does `Bloom Web Events` become?
4. What should the first query on any new dataset be, and what do "fewer" and "double" tell you?
5. Why is total revenue per tier not the same question as revenue per customer per tier?
6. Why can an inner join never list customers who never ordered?
7. What is the only data-changing command in Query Service?
8. Name the five recurring AEP interview scenarios.

<details><summary>Check your answers</summary>

**Task 1.** With `.mode csv`, `.import` creates each table and uses the first row of the file as column names.

**Task 2.** Both tables say **500** in SQLite. The Bloom Orders dataset in AEP held **497** after the episode 6 trial load, because AEP validated the rows and rejected three of the planted bad ones. SQLite checks nothing, so every row loads, broken ones included. The honest count is always the count of what actually landed.

**Task 3.** There are fewer distinct emails than rows (with the course files, 500 rows and 488 distinct emails), because the CRM extract contains duplicate rows on one email. `COUNT(*)` counts rows, not people. In AEP, the profile store would fold those duplicates into one person; the lake keeps both rows.

**Task 4.**
```sql
SELECT loyalty_tier, COUNT(*) AS customers
FROM   bloom_customers
GROUP  BY loyalty_tier
ORDER  BY customers DESC;
```
You should see three piles that add up to 500. With the course files: Bronze 279, Silver 150, Gold 71.

**Task 5.**
```sql
-- Total revenue per tier
SELECT c.loyalty_tier, ROUND(SUM(o.price), 2) AS revenue
FROM   bloom_customers c
JOIN   bloom_orders o ON o.bloom_id = c.bloom_id
GROUP  BY c.loyalty_tier
ORDER  BY revenue DESC;

-- Revenue per customer per tier (every customer counted)
SELECT c.loyalty_tier,
       ROUND(SUM(o.price) / COUNT(DISTINCT c.bloom_id), 2) AS revenue_per_customer
FROM   bloom_customers c
LEFT   JOIN bloom_orders o ON o.bloom_id = c.bloom_id
GROUP  BY c.loyalty_tier
ORDER  BY revenue_per_customer DESC;
```
The first answers "which tier brings in the most money", which mostly follows headcount. The second answers "is a customer in this tier worth more". Label each one.

Bonus: the join on `bloom_id` returns one row per matching order. The join on `email` returns more rows than there are matching orders, because some emails appear on two customer rows, so those orders match twice and would be counted twice. A join key that repeats on the side you join to inflates every count and sum built on it.

**Task 6.**
```sql
SELECT strftime('%Y', join_date) AS join_year, COUNT(*) AS customers
FROM   bloom_customers
GROUP  BY join_year
ORDER  BY join_year;
```
In Query Service the same idea is written with `YEAR(...)` on the join date field.

**Task 7.**
```sql
SELECT first_name, last_name, email, join_date
FROM   bloom_customers
ORDER  BY join_date DESC
LIMIT  5;
```
Look at the emails and dates you get back. Some raw emails carry capital letters, which is why Bloom cleans emails at the door. And if any join date is later than the day you run the query, treat it as a data defect to raise, not a customer: the platform would load it, because it is a valid date.

**Task 8.**
```sql
SELECT order_id, sku, quantity, price
FROM   bloom_orders
WHERE  price / quantity < CASE sku
         WHEN 'BLM-CLN-GEL-150'  THEN 16
         WHEN 'BLM-LIP-BALM-08'  THEN 9
         WHEN 'BLM-MOIST-HYA-50' THEN 20
         WHEN 'BLM-MSK-CLAY-100' THEN 24
         WHEN 'BLM-SER-RET-30'   THEN 42
         WHEN 'BLM-SER-VITC-30'  THEN 34
         WHEN 'BLM-SPF-MIN-50'   THEN 26
         WHEN 'BLM-SUP-COLL-30'  THEN 38
         WHEN 'BLM-SUP-MULTI-90' THEN 22
         WHEN 'BLM-SUP-OMG3-60'  THEN 28
       END;
```
Expect **BLM-123800** at `-20.00`. In episode 6 it loaded, because minus 20 is a valid number: the platform validates types, not business sense, and business validation is Bloom's job. In SQLite you will probably also see **BLM-114700**, whose price is `N/A`: SQLite treats that text as zero in arithmetic. In AEP that row never landed (MAPPER-3701).

**Task 9.**
```sql
-- Inner join: only customers who ordered
SELECT c.loyalty_tier,
       ROUND(COUNT(o.order_id) * 1.0 / COUNT(DISTINCT c.bloom_id), 2) AS orders_per_customer
FROM   bloom_customers c
JOIN   bloom_orders o ON o.bloom_id = c.bloom_id
GROUP  BY c.loyalty_tier
ORDER  BY orders_per_customer DESC;
-- LEFT JOIN: change JOIN to LEFT JOIN and run it again

SELECT COUNT(*) AS never_ordered
FROM   bloom_customers c
LEFT   JOIN bloom_orders o ON o.bloom_id = c.bloom_id
WHERE  o.order_id IS NULL;
```
Every tier's average drops with the LEFT JOIN, and with the course files the order of the tiers changes between the two versions. The never-ordered count is **188** with the LEFT JOIN and **0** with an inner join, because an inner join cannot return rows that have no match. Self-check: customers with at least one order (312) plus customers who never ordered (188) must add up to 500.

**Task 10.** Query Service is append-only: INSERT INTO is the only command that changes a table's rows, and there is no UPDATE and no DELETE, in any sandbox. It writes rows to the data lake and never edits a profile. Fix the email at the source, in the CRM, and send the corrected record in through the normal dataflow, so the fix happens at the layer where the fault began.

**Task 11.** A strong answer names the decision, the reason and the evidence from the build. For example, identity design: "Email is the primary identity on the customer profile, the ECID marks anonymous web events, and BloomID, a custom cross-device namespace, is primary on orders. Priya's app sign-in links her ECID to her email, her order links her email to her BloomID, and she resolves to one profile with three identities." "Walk me through your identity design" is the most common senior AEP question.

**Task 12.** A LEFT JOIN from customers to orders, filtered to `loyalty_tier = 'Gold'` and `o.order_id IS NULL`. With the course files that is **31** of the 71 Gold customers. An inner join returns zero, because it can only see customers who ordered.

**Track B: what to expect**
The dataset's right rail shows a Table name in lower case with underscores. The count comes back under a header in capitals. If the count is higher than your file, you loaded it more than once: every successful run appends a batch. If you see "Table or view not found", copy the table name again from the rail.

**Check yourself**
1. For questions across the whole history: counts, sums and averages by group, joins between datasets, and proving that a load arrived.
2. It reads datasets in the data lake directly and never asks the profile store anything.
3. Datasets, open the dataset, copy Table name from the right rail. `Bloom Web Events` becomes `bloom_web_events`.
4. `SELECT COUNT(*)`. Fewer means the load is incomplete; double means the file landed twice.
5. Total revenue follows headcount; revenue per customer divides by the number of customers, so it answers whether a customer in that tier is worth more.
6. An inner join keeps only rows that match on both sides, and a customer with no orders has no match.
7. INSERT INTO.
8. Schema design, a failed dataflow, identity design, choosing an evaluation method, and governance blocking an export.

</details>
