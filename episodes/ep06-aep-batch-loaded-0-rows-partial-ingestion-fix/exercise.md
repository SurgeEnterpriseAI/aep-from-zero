# Exercise 06: The failure lab

You will diagnose Bloom's five broken order rows, do the arithmetic that confuses most teams, and write the checklist you will use before every **Finish**.

Files: `bloom-orders-500.csv` and `bloom-customers-500.csv` from the repo's `/data` folder.

## Track A: No Adobe access needed

1. **Diagnose the five broken rows.** Find these orders in `bloom-orders-500.csv`: `BLM-104200`, `BLM-109100`, `BLM-114700`, `BLM-119300`, `BLM-123800`. For each one, write:
   - a one-line diagnosis (what is wrong with the value)
   - the error family you predict: MAPPER, INGEST, both, or none
   - whether the row was designed to be rejected or to load
2. **Choose a threshold.** A 500-row file has 3 rows that get rejected, and 7 errors are logged.
   - Will a 5 percent error threshold let it land? Will a 1 percent threshold?
   - Which threshold would you accept for a marketing file, and which for a finance reconciliation file?
   - Who should own that decision?
3. **Do the arithmetic.** In three sentences, explain why "497 ingested" plus "7 failed" is not 504 rows, and how many rows were really rejected.
4. **Write your auto-map review checklist.** List what you will check on the mapping screen before every **Finish**. Include the identity, the consent columns, and the extra checks an event file needs.
5. **Describe a good daily feed.** Write three lines, one each for idempotent, quarantined and alerted.
6. **The episode's practice question.** Say, for example, a 500-row file reports 495 ingested and 9 failed. How many rows were really rejected, and which screen proves it?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production, and only objects that carry **your own initials**.
- Load only into **your own** dataset. Never turn on Profile for a schema or dataset that is not yours; enabling a schema for Profile is irreversible.
- Nothing here needs **Activate**, **Publish** or any send. Do not click them.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Go to **Sources**, **Catalog**, **Local system**, **Local file upload**, **Add data**. In **Dataflow detail**, choose your own orders dataset (for example "Bloom Orders" plus your initials). Turn **Error diagnostics** on. Leave **Enable partial ingestion** off.
2. Upload `bloom-orders-500.csv` in **Select data**. On **Mapping**, read the four counters before you change anything. Fix the mapping: delete any text column aimed at an object array, and map `order_id` twice, to `_id` and to the purchase ID field. Click **Validate**, then **Finish**.
3. When the run ends, write down **Status**, **Records ingested** and **Records failed**. Click **Preview error diagnostics**, then **Download** the failure manifest.
4. Create a second dataflow into the **same existing** dataset. This time switch on **Enable partial ingestion** and leave **Error threshold %** at 5. Use the same file and mapping.
5. Write down the new **Records ingested** and **Records failed**. Then open the dataset and read **Total records**. Which number tells you how many rows were rejected?
6. Pick two rows from the failure manifest and write symptom, layer, evidence, fix or route for each.

## Check yourself

1. What do **Required fields** and **Identity fields** tell you that **Mapped fields** does not?
2. Why is partial ingestion off by default, and why is that not a bug?
3. A run shows a MAPPER-3701 error. Where do you look first, and why?
4. Why does one bad row often produce two errors?
5. Why did the order with a price of -20.00 load?
6. What is the difference between a rejected row and a loaded-but-wrong row, and which is more dangerous?
7. What are the four steps of the debugging method?

<details><summary>Check your answers</summary>

**Task 1: the five rows**

| Order | Diagnosis | Error family | Designed to |
|---|---|---|---|
| BLM-104200 | `order_timestamp` is empty; every event needs a timestamp | Both: MAPPER-3707 and INGEST-1555 | Be rejected |
| BLM-109100 | `2026/13/45 25:99` is not a real date (month 13, day 45, hour 25) | Both: MAPPER-3700 and INGEST-1555; the bad date appears word for word in the MAPPER error | Be rejected |
| BLM-114700 | price is the text `N/A` where a number belongs | MAPPER-3701 | Be rejected |
| BLM-119300 | no `bloom_id` and no `email`: no identity, so the order cannot attach to anyone | Both: MAPPER-3707 and INGEST-1555 | Be rejected |
| BLM-123800 | price `-20.00` is a valid number but makes no business sense | None | Load: business validation is Bloom's job |

The first four were designed to fail; in the real run one of these four survived. Only the dataset count (497, so 3 rows rejected) tells you what really happened.

**Task 2: the threshold**
- By rows, 3 of 500 is 0.6 percent, under both 5 percent and 1 percent. Be careful: if you divide the 7 errors instead (1.4 percent), you would predict a failure at 1 percent. Bloom's team never ran a 1 percent threshold, so test a tight threshold in a development sandbox before you rely on it.
- A marketing file can sensibly use 5 percent; a few missing rows means a few customers miss one email. A finance reconciliation file needs a much stricter threshold, or partial ingestion left off so any bad row stops the load.
- The business owner of the data owns the number, in writing. The engineer configures it; they should not choose it alone.

**Task 3: the arithmetic**
"Records failed" counts error instances, not rows. One bad row commonly raises both a MAPPER error and an INGEST error, so the 3 rejected rows produced 6 errors; the seventh was a warning on a row that landed. 500 minus 497 means 3 rows were rejected, and the dataset's Total records (497) is the honest number.

**Task 4: a sample checklist**
- Required fields and Identity fields read "n of n", in green.
- `email` goes to `personalEmail.address` and shows the fingerprint icon.
- Phone goes to `mobilePhone.number`, not a fax field.
- Tier, points and join date go to the `_bloom` loyalty fields, not addresses, coordinates or system fields such as `_repo`.
- `email_consent`, `sms_consent` and `push_consent` go to the `_bloom` consent fields, not status fields.
- City, state and country go to the `homeAddress` fields.
- Event files: `_id` and `timestamp` are mapped (`order_id` can feed `_id` too), and no text column is aimed at an object array.
- Error diagnostics is on, and the partial ingestion setting and threshold have a named owner.
- Wrong mappings are removed bottom-up with the circle-minus.

**Task 5: a good daily feed**
- Idempotent: loading the same day's file twice gives the same result, never duplicate orders.
- Quarantined: bad rows are set aside with their reasons, fixed, and replayed.
- Alerted: a named person hears about a failed run the same day, and every run's dataset row count is compared with the file.

**Task 6: practice question**
500 minus 495 means 5 rows were rejected; "9 failed" counts error instances. Open the dataset and read Total records, then compare it with the file's row count.

**Track B: what to expect**
The first run should end Failed with 0 ingested. The second should land most rows; in Bloom's run it was 497 ingested and 7 failed, with Total records 497 in an empty dataset. Your counts and timings may differ; the first failure took 36 minutes to report in Bloom's run.

**Check yourself**
1. Mapped fields counts columns that found any home. Required fields says whether every required field is mapped (if not, the batch cannot run), and Identity fields says whether rows can attach to a person.
2. The platform will not decide how much bad data your business can accept. That is a business decision for a named owner.
3. Your own mapping and calculated fields first: MAPPER means Data Prep could not convert a value at mapping time. Then look at the actual cell value.
4. It fails once when its value is mapped (MAPPER) and again when the row tries to land without a required field (INGEST).
5. The platform validates types, not business sense, and -20.00 is a valid number.
6. A rejected row never landed and left a reason. A loaded-but-wrong row passed every check, so nothing warns you about it. That makes it the more dangerous of the two.
7. Symptom, layer, evidence, fix or route.

</details>
