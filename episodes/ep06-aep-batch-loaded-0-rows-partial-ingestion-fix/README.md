# Episode 06: AEP Batch Loaded 0 Rows? Partial Ingestion Fix

**Watch:** Video coming soon on iTV

[Previous](../ep05-aep-data-ingestion-tutorial-batch-vs-streaming/) · [Next](../ep07-aep-identity-stitching-identity-graph/)

## What you will learn

- Read the **Required fields** and **Identity fields** counters, and never trust **Mapped fields** alone
- Explain why partial ingestion is off by default, and choose an error threshold as a business decision
- Read error diagnostics and tell **MAPPER-37xx** errors from **INGEST-1555** errors
- Use the dataset's row count, not **Records failed**, to count rejected rows
- Tell a rejected row from a row that loaded but is wrong, and apply the method: symptom, layer, evidence, fix or route

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch. Farhan, the data engineer, and Kavya, the new marketing technologist, built three schemas in episode 4. In episode 5 they started loading two 500-row trial files and reached the mapping screen, where a full green bar said **Mapped fields 14 of 14**. Kavya's cursor was on Finish. Farhan said: "Read the counters next to it."

## Key ideas

### 1. Mapped is not correct (the mapping counters)
Auto-map matches source columns to schema fields by **name similarity**. It is deterministic, so the same file gets the same guesses every time. **Mapped fields** counts columns that found *a* home, not whether the home makes sense. The real gates are **Required fields** and **Identity fields**. On Bloom's customer file they read **0 of 1** and **0 of 1**, and the platform blocked the run with "The following unmapped paths are required: personalEmail.address".

What auto-map did with the customer file, and where each column belongs:

| CSV column | Auto-map chose | Corrected target |
|---|---|---|
| email | personalEmail.label | personalEmail.address (primary identity, Email) |
| phone | faxPhone.number | mobilePhone.number |
| loyalty_tier | billingAddress.stateProvince | the `_bloom` loyalty tier field |
| loyalty_points | billingAddress._schema.longitude | the `_bloom` loyalty points field |
| join_date | _repo.createDate (a system field) | the `_bloom` loyalty join date field |
| email_consent | personalEmail.status | the `_bloom` email consent field |
| sms_consent | billingAddressPhone.status | the `_bloom` SMS consent field |
| push_consent | billingAddressPhone.statusReason | the `_bloom` push consent field |
| city, state, country | billingAddress.city, shippingAddress.state, homeAddress.country | homeAddress.city, homeAddress.stateProvince, homeAddress.countryCode |

`bloom_id` stays a plain attribute here: auto-map sent it to the stock `personID` field, which carries no identity, and Bloom Customer Profile declares one identity, Email. Consent matters now: the Lapsed 90 win-back audience (episode 10) needs email consent true, so Ananya, who never consented, is excluded only if her consent lands in a field a rule can read.

After the fixes the customer run read **Records ingested 500, Records failed 0, Status Success**.

### 2. The orders file fails differently
Because the episode 4 schema named its custom fields after the CSV columns, auto-map got both order identities right: `bloom_id` to `_bloom.bloomId` (primary, BloomID) and `email` to `_bloom.orderEmail` (Email). It still blocked the run with **Required fields 2 of 3, Errors 1**:
- "STRING cannot be mapped to the destination field of type OBJECT": `product_name` was aimed at `productListItems`, an array of objects. Delete that mapping.
- "The following unmapped paths are required: _id": map `order_id` a second time. One source column can feed two targets, `_id` and `commerce.order.purchaseID`.

### 3. All-or-nothing batch
**Partial ingestion is off by default.** Without it a batch is **all-or-nothing**: one bad row can fail the whole file. Bloom's first orders run took 36 minutes to report **Status Failed, Records ingested 0**, with the banner "Successfully ingested 0 rows, failed to ingest 7 rows". Three rejected rows threw away 497 good orders.

### 4. Partial ingestion and the error threshold
Switching on **Enable partial ingestion** lets good rows land while bad rows are set aside. It reveals a hidden control, **Error threshold %**, which defaults to **5**: the batch fails only if more than that share is bad. Bloom's re-run, into the same dataset, read **Records ingested 497, Records failed 7, Status Success** in 3 min 14 s. Partial ingestion is not "ignore errors"; it is **"set the blast radius"**. The threshold is a **business decision** with a named owner: 5 percent can suit a marketing file and be far too loose for a finance reconciliation file. (Timings are from one practice run, not promises.)

### 5. MAPPER-37xx versus INGEST-1555
| Code family | Raised when | Usually whose fault |
|---|---|---|
| MAPPER-37xx | Data Prep could not convert a value at mapping time: text in a number field, an impossible date, a null source field | Your mapping |
| INGEST-1555 | A required XDM field arrived missing or null when the row tried to land | The data |

One row can raise both.

### 6. Error instances versus rows
**Records failed counts error instances, not rows.** 497 ingested plus 7 failed is 504, more than the 500 rows in the file. 500 minus 497 means **3 rows** were rejected (6 errors; the 7th was a warning on a row that landed). The dataset's **Total records** is the honest number.

### 7. Type validation versus business validation
The platform validates **types, not business sense**. `BLM-123800` had a price of `-20.00`, a valid number, so it loaded. A **rejected** row failed validation, never landed and left a reason. A **loaded-but-wrong** row passed every check, so nothing warns you; it is the more dangerous of the two. Business validation, such as flagging negative prices, is Bloom's job. Of the four rows designed to fail, one survived the real run: another reason to count rows in the dataset.

### 8. The debugging method and daily feeds
**Symptom, layer, evidence, fix or route:** read what the run reports literally; find the layer (source, Data Prep, validation); look at the actual cell value; then fix and re-run, or quarantine the bad data and record why. A good daily feed is **idempotent** (loading the same file twice never duplicates orders), **quarantined** (bad rows set aside with reasons) and **alerted** (a person hears about a failed run the same day).

## In the product

Labels as of October 2026.

1. Go to **Sources**, **Catalog**, choose the category **Local system**, and on the **Local file upload** card click **Add data**. This opens the workflow **Map CSV to XDM schema**, with three steps: **Dataflow detail**, **Select data**, **Mapping**. Local file upload takes CSV only, up to 1 GB.
2. On **Dataflow detail**, choose a new or existing dataset (an existing dataset brings its own schema). The **Profile dataset** toggle appears only after you choose a Profile-enabled schema. Turn on **Error diagnostics**, or a failed run gives you no failure detail. Decide on **Enable partial ingestion**; switching it on reveals **Error threshold %** (default 5).
3. On **Select data**, upload the CSV and read the preview before you go on.
4. On **Mapping**, read **Mapped fields**, **Required fields**, **Identity fields** and **Errors**. Identity rows carry a fingerprint icon. Remove a wrong mapping with the circle-minus button at the right of its row, working **bottom-up** because rows reflow; clearing the target text does not remove it. Click **Validate**, then **Finish**.
5. On the dataflow run, read **Records ingested**, **Records failed** and **Status**. On a failed run click **Preview error diagnostics**; **Download** gives the full failure manifest.
6. Open the dataset under **Data Management**, **Datasets**, and read **Total records** and **Failed batches**. This is your source of truth.

## Common mistakes

- Clicking **Finish** because the bar is green, without reading Required fields and Identity fields.
- Leaving consent columns in delivery status fields. Consent is permission; status is delivery.
- Re-running a failed all-or-nothing batch unchanged.
- Raising the error threshold until the run goes green.
- Reporting **Records failed** as a row count.
- Blaming the source data for every error. MAPPER codes usually point at your own mapping.
- Assuming that "loaded" means "right".

## Glossary

| Term | Meaning |
|---|---|
| Auto-map | The mapping step's automatic guess of a target field for each column, by name similarity |
| Required fields, Identity fields | The counters that decide whether a batch may run and whether rows can reach a person |
| All-or-nothing batch | A batch with partial ingestion off: one bad row fails the whole file |
| Partial ingestion | A setting that lets good rows load while bad rows are set aside, up to an error threshold |
| Error threshold | The share of bad data allowed before the whole batch fails; default 5 percent |
| Error diagnostics | The per-row failure detail for a dataflow run, with error codes |
| Failure manifest | The downloadable list of failed rows from a run |
| MAPPER-37xx | Data Prep could not convert a value at mapping time |
| INGEST-1555 | A required field arrived missing or null at ingestion time |
| Error instance | One error raised; one row can raise several |
| Type validation | The platform's check that a value fits the field's data type |
| Business validation | Your own check that a valid value makes business sense |
| Idempotent feed | A feed that gives the same result when the same file is loaded twice |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Local file upload source: https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/local-system/local-file-upload
- Data Prep mapping: https://experienceleague.adobe.com/en/docs/experience-platform/data-prep/ui/mapping
- Monitor sources dataflows: https://experienceleague.adobe.com/en/docs/experience-platform/dataflows/ui/monitor-sources
- Search Experience League for: partial batch ingestion error threshold, dataflow error diagnostics

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
