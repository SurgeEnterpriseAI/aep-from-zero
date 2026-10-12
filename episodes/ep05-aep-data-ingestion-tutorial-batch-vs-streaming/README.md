# Episode 05: AEP Data Ingestion Tutorial: Batch vs Streaming

**Watch:** Video coming soon on iTV

Part 1: Know your customer (AEP and Real-Time CDP) · [Previous](../ep04-aep-schema-tutorial-identities-and-profile/) · [Next](../ep06-aep-batch-loaded-0-rows-partial-ingestion-fix/)

## What you will learn

- Choose **batch** or **streaming** for any feed: history and bulk go by batch; anything a journey must react to goes by streaming
- Trace one row through **source, Data Prep, dataset and profile**, and name the fifth outcome: **rejection**
- Map CSV columns to XDM fields, including the three consent columns, and explain why the **identity columns** matter most
- Write **calculated-field** logic that normalises phones, lower-cases and trims emails, and derives a loyalty band
- Describe how an **HTTP API streaming source** and **Postman** send live events

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch.
In episode 4, Farhan (data engineer) and Kavya (new marketing technologist) built three schemas, chose email as the primary identity, and confirmed in **Schemas, Browse** that all three read **Enabled** for Profile. They were still empty.
On Monday the ops team drops two messy CSV files on Farhan's desk, and the web team can only send live events to a web address.

## Key ideas

### 1. Two roads in: batch and streaming
**Ingestion** means getting data into the platform. The difference between the two roads is rhythm, not difficulty, and real projects use both.

| | Batch ingestion | Streaming ingestion |
|---|---|---|
| What moves | Files, on a schedule | Events, one at a time, as they happen |
| Good for | History and bulk | Anything a journey must react to |
| Typical sources | Cloud storage, CRM connectors, file uploads | An HTTP API endpoint, or the Web SDK (episode 12) |
| Bloom example | 18 months of orders | Tonight's add-to-cart |

The test for any feed: **who needs to react, and how fast?** Tonight's order goes by streaming if a welcome email must react to it, and by batch if it only feeds next month's revenue report.

### 2. Sources, dataflows and runs
- **Source connector:** a pre-built link from an outside system into AEP, such as cloud storage, a CRM system, an HTTP API for live events, or **Local file upload** (CSV only, up to 1 GB).
- **Dataflow:** a configured pipeline from a source, through Data Prep, into a dataset.
- **Dataflow run:** one execution of a dataflow, with counts of what landed and what failed. When something breaks, open the run first.

### 3. One row's path, and the fifth ending
1. **Source:** the row leaves the CSV, or arrives at the streaming endpoint.
2. **Data Prep:** its columns are mapped to XDM fields and dirty values can be cleaned.
3. **Dataset:** it lands in the data lake, the archive of complete history.
4. **Profile:** if the dataset is enabled for Profile, it also folds into that person's live record. One ingest, two worlds.
5. **Rejected:** if it fails validation (a missing timestamp, a price that is text, no identity), it never reaches the dataset, and the dataflow records why.

### 4. Data Prep mapping, and the consent columns
**Data Prep** sits between source and dataset and does two jobs: **mapping** (a line from each source column to its XDM field) and **calculated fields** (clean or derive values on the way in). Kavya's plan for the 14 columns of `bloom-customers-500.csv`:

| CSV column | Planned XDM home |
|---|---|
| `email` | `personalEmail.address`, the primary identity (Email) |
| `bloom_id` | a plain attribute, **not** an identity on this schema |
| `first_name`, `last_name` | `person.name.firstName`, `person.name.lastName` |
| `phone` | `mobilePhone.number` |
| `loyalty_tier`, `loyalty_points`, `join_date` | the `_bloom` loyalty fields, for example `_bloom.loyalty.tier` |
| `city`, `state`, `country` | `homeAddress.city`, `homeAddress.stateProvince`, `homeAddress.countryCode` |
| `email_consent`, `sms_consent`, `push_consent` | the `_bloom` consent fields, one per channel |

Consent must land where an audience rule can read it. The Lapsed 90 win-back audience (episode 10) needs email consent true, so Ananya, who never consented, is excluded only if her value lands in a `_bloom` consent field.

### 5. Why the identity columns matter most
Every other column is an attribute. The identity columns decide **which person** a row belongs to.

| File | `bloom_id` | `email` |
|---|---|---|
| Customer file | Plain attribute | Primary identity (Email) |
| Order file | Primary identity (BloomID) | Second identity (Email) |

A wrong loyalty tier is a small, fixable error. A row with **no identity is an orphan**: no profile, audience or journey will ever find it. Map the identity columns first, and map them right.

### 6. Calculated fields: three clean-ups at the door
"Never ingest dirt you can clean at the door." A **calculated field** cleans or derives a value as each row lands, so nobody edits the source file by hand.

- **Phone to one shape.** Phones arrive as `(469) 555-0142`, `469.555.0142`, `4695550142`, `1-469-555-0142` and `+1-469-555-0142`. Strip every non-digit; if eleven digits remain and the first is `1`, drop it; then put `+1` in front. Every shape becomes `+14695550142`. Skip the middle step and numbers that already start with `1` become `+114695550142`.
- **Email lower-cased and trimmed.** ` Priya.Sharma@Example.com ` becomes `priya.sharma@example.com`. Software compares text exactly, so one person must always carry exactly the same identity value. In episode 25, the person ID in Customer Journey Analytics (CJA) is case sensitive, so two spellings would be two people. Duplicate customers are handled in episode 8.
- **Loyalty band from points.** Bronze is below 500, Silver is 500 to 1,499, Gold is 1,500 and above. Ask the bigger question first:

```
loyalty_band = iif(points >= 1500, "Gold", iif(points >= 500, "Silver", "Bronze"))
```

Priya (2,340 points) is Gold; the High-Value Loyalists audience (episode 10) reads this band. The phone and email logic is written as steps, not exact syntax: test every shape in the editor.

### 7. The three switches on Dataflow detail
- **Profile dataset:** appears only after you choose a Profile-enabled schema. Switch it on **before** loading; rows loaded while it is off do not flow into the profile later.
- **Error diagnostics:** turn it on, or a failed run gives no failure detail.
- **Enable partial ingestion:** decides whether the good rows in a file may still load when some rows are bad. It is off by default. Farhan leaves it at the default for the trial; episode 6 shows the cost.

### 8. The streaming road: HTTP API and Postman (documented route)
The **HTTP API** source generates a **streaming endpoint**, an address that accepts events one at a time. Each event is a JSON message shaped like the **Bloom Web Event** schema, carrying an ECID, meant to land in the **Bloom Web Events** dataset. Bloom's **Postman** collection sends three web events to the endpoint by hand. It ships with placeholders only (for example `{{SANDBOX_NAME}}`); never commit real keys. Adobe documents this route this way; check what your own screen shows.

## In the product

Labels as of October 2026.

1. Go to **Sources**, **Catalog**, choose the category **Local system**, and on the **Local file upload** card click **Add data**. This opens **Map CSV to XDM schema**: **Dataflow detail**, **Select data**, **Mapping**.
2. On **Dataflow detail**, choose **New dataset** (for example "Bloom Customers" plus your initials) and your own Profile-enabled schema. Set the three switches as above, name the dataflow, and click **Next**.
3. On **Select data**, upload `bloom-customers-500.csv` and read the preview. Row one is Priya Sharma, `BLM-CUST-004217`, Gold, 2,340 points.
4. On **Mapping**, recognised columns are already auto-mapped. Add a clean-up from the **New field type** menu, **Add calculated field**; build the expression, save it, and map its output to a target. Do not click **Finish** until you have read every row and every counter (episode 6).
5. For live events: **Sources**, **Catalog**, the **Streaming** category, **HTTP API**, which generates the streaming endpoint.

## Common mistakes

- Uploading everything first and planning to clean it later.
- Streaming everything, or batching an event a journey must react to.
- Mapping the identity columns last, or wrongly, and creating orphan rows.
- Leaving consent columns where no audience rule reads them.
- Adding `+1` to a number that already starts with `1`.
- Testing "500 or more" before "1,500 or more".
- Switching on Profile dataset after loading, or leaving Error diagnostics off.
- Trusting a full green **Mapped fields 14 of 14** bar (episode 6).

## Glossary

| Term | Meaning |
|---|---|
| Batch ingestion | Loading data as files on a schedule; right for history and bulk |
| Streaming ingestion | Loading events one at a time as they happen; right when a journey must react |
| Source connector | A pre-built link from a source system into AEP |
| Dataflow | A configured pipeline from a source, through Data Prep, into a dataset |
| Data Prep | The stage that maps source columns to XDM fields and can clean values on the way in |
| Calculated field | A Data Prep expression that cleans or derives a value as it lands |
| Identity column | A source column mapped to an identity field; how a row finds its person |
| Rejected row | A row that failed validation, never landed, and has a logged reason |
| Postman | A tool for sending web requests by hand, used to fire test events |
| JSON | JavaScript Object Notation, a plain text format for structured data |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Local file upload source (batch ingest a CSV): https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/local-system/local-file-upload
- Data Prep, map fields to XDM: https://experienceleague.adobe.com/en/docs/experience-platform/data-prep/ui/mapping
- Monitor sources dataflows: https://experienceleague.adobe.com/en/docs/experience-platform/dataflows/ui/monitor-sources
- Search Experience League for: HTTP API streaming connection, Data Prep calculated fields

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
