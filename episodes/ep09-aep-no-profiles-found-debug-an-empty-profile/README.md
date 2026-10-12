# Episode 09: AEP 'No Profiles Found'? Debug an Empty Profile

**Watch:** Video coming soon on iTV

[Previous](../ep08-aep-real-time-customer-profile-merge-policy/) · [Next](../ep10-aep-segment-builder-tutorial-build-audiences/)

## What you will learn

- Explain why ingestion success says nothing about profile success
- Rule out the cheap explanations in a fixed order, starting with a lookup by a second namespace
- Run the four configuration checks: schema enabled for Profile, identity declared, identity mapped **1 of 1**, dataset enabled and re-ingested
- Read **Monitoring, Batch end-to-end** with the filter cleared, and use the **Records in Profile** and **New profile fragments** columns
- Explain why profile enablement is **not retroactive**, and when to re-ingest
- Know when to stop diagnosing, and write the evidence chain that proves the fault is not in your build

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch. In episode 8 Kavya learned how the Real-Time Customer Profile merges everything known about a person, and how a merge policy decides between Dallas and Austin for Priya's address. Feeling confident, she opened **Profiles**, **Browse**, chose **Default Timebased** and **Email**, typed `priya.sharma@example.com` and pressed **View**. The screen said: **No profiles found**. Both batches had succeeded, both datasets were Profile-enabled, and the customer schema was in the union schema.

## Key ideas

### 1. One file, three destinations, three gates

One ingested file fans out to three different places. Each has its own gate, and a row can pass the first two and never reach the third.

| Destination | Its gate | Where you see it |
|---|---|---|
| Data lake | The row is valid against the schema | The dataset's record count; **Records in dataset** |
| Identity graph | An identity field is declared in the schema and mapped | **Identity records stitched** |
| Profile store (Real-Time Customer Profile) | The schema **and** the dataset are enabled for Profile, and a primary identity resolves | **New profile fragments**, **Records in Profile** |

Seeing identities stitched does not mean a profile exists. The mapping only decides which XDM field receives a value; the **schema** decides whether that value becomes a person key.

### 2. Rule out the cheap explanations, in order

Each check takes about a minute and removes a whole class of cause. Write every result down; the order becomes your evidence.

| Hypothesis | Quick test | Bloom's result |
|---|---|---|
| Wrong namespace or a typo | Repeat the lookup by a **second namespace**: BloomID `BLM-CUST-004217` (the order events' primary identity) | Still **No profiles found**: not a lookup mistake |
| Schema not in Profile | **Profiles**, **Union Schema**, class **XDM Individual Profile** | The customer schema's objects (personalEmail, person, homeAddress, mobilePhone) are listed: ruled out |
| Dataset not Profile-enabled | Start a new dataflow at the dataset; the **Profile dataset** toggle is inherited | Already on: ruled out |
| The batch failed | **Datasets**, the dataset, the batch | 500 received, 500 ingested, 0 failed, **No errors**: ruled out |
| Out of licence capacity | **Administration**, **License usage** | Nothing suggested a capacity problem, but its **Last collected on** date was a week stale, so it is not live evidence |

Seeing your schema in the **union schema** is the cheapest proof it contributes. **Profiles Overview** updates on a daily cycle, so it can lag too.

### 3. The four configuration checks

They catch the usual causes of an empty profile. They are **necessary, but not always sufficient**.

1. **Schema enabled for Profile.** Read the **Enabled for Profile** column in **Schemas**, **Browse**. Saving the Profile switch together with identity edits can silently drop it, so re-read the column after every save.
2. **Schema declares an identity.** Open the schema; the **Identities** section in the left rail must name a field; in the field tree, that field carries a fingerprint icon. Beware `personID`: a stock field whose Identity box is unticked. Mapping a customer number there stores the value and creates no identity.
3. **Identity actually mapped.** On the mapping screen, **Identity fields** must read **1 of 1** before **Finish**.
4. **Dataset enabled, and re-ingested.** The dataset's own Profile toggle must be on, and anything loaded before it was on must be loaded again.

### 4. The screen that answers it

**Monitoring**, **Batch end-to-end** opens filtered to **ONLY INGEST FAILURES: Yes**, which hides every successful batch. Clear that chip, then read the row for your batch:

| Column | What it proves |
|---|---|
| Records in dataset | The data lake has the rows. This is all a green dataflow promises. |
| New profile fragments | How many new profile records this batch created |
| Existing profiles | How many existing profiles it updated |
| Identity records stitched | How many identity links the identity graph formed |
| **Records in Profile** | How many rows are actually queryable in the Real-Time Customer Profile |

Bloom's customers row: **Records in dataset** a green 500, **Identity records stitched** green, **Records in Profile** blank on every batch. The lake had it, the graph had it, the profile store did not.

### 5. Profile enablement is not retroactive

Data loaded before the schema, identity, mapping or dataset toggle was fixed stays in the lake and **never becomes a profile**. The platform does not backfill. The fix is to **re-ingest**; better still, switch the dataset's Profile toggle on **before** you load anything. Enabling a schema for Profile is irreversible, so do it only on a schema you own.

### 6. Diagnosis versus reassurance

Farhan's first guess was "it is just lag". But **Adobe publishes no time for batch data to reach Profile**, so "wait longer" can never be proven wrong. Any waiting limit, such as thirty minutes, is a team's own allowance, not an Adobe figure. A **diagnosis** names a test that could prove you wrong. Bloom's test was a re-ingest of the same file into the now definitely enabled dataset. It ran **500 ingested, 0 failed, Success in 1 min 39 s** (one practice run, not a promise), and **Records in Profile** stayed blank. **Profiles**, **Overview** read "No data is ingested to Profiles" for the whole sandbox. Not lag, and not Bloom's build.

### 7. Stop rebuilding, escalate with an evidence chain

When every layer you control is provably correct and a re-ingest reproduces the fault, stop. It is a sandbox-level condition for whoever owns the platform. Rebuilding a correct build wastes time and muddies the evidence. Bloom's escalation note had five parts: checks in order, the decisive row, what was ruled out, the **batch ID and dataset ID**, and the ask (restore profile ingestion).

**The missing-profile playbook.** The point is not the answer, it is the order. (Bloom's team read the licence page before Monitoring; both are cheap, so that is fine. The re-ingest always comes last.)

| # | Check | Where | If it fails |
|---|---|---|---|
| 1 | Same person by a second namespace | Profiles, Browse | It was a namespace or value error |
| 2 | Schema enabled for Profile | Schemas, Browse | Enable it, then re-ingest |
| 3 | Schema present in the union | Profiles, Union Schema | Check the class and the Profile flag |
| 4 | Dataset Profile flag | Start a dataflow at the dataset | Enable it, then re-ingest |
| 5 | Batch actually succeeded | Datasets, dataset, batch | Read the error diagnostics |
| 6 | **Records in Profile** | Monitoring, Batch end-to-end (filter cleared) | Lake and identity green but Profile blank: profile ingestion, not your build |
| 7 | Licence capacity | Administration, License usage | Check the collection date first |
| 8 | Re-ingest the same file | Sources, existing dataset | Reproduces: escalate with steps 1 to 7 as evidence |

## In the product

Labels as of October 2026.

1. **Profiles**, **Browse**: set **Merge policy** (Default Timebased), **Identity namespace** and **Identity value**, then **View**. The boxes re-arrange as you fill them, so re-read the form after choosing a namespace.
2. **Profiles**, **Union Schema**: set **Class** to **XDM Individual Profile** and look for your schema's objects.
3. **Schemas**, **Browse**: read the **Enabled for Profile** column. Open the schema and read **Identities** in the left rail.
4. **Datasets**, your dataset, the batch: read Records received, ingested and failed, and the status.
5. **Monitoring**, **Batch end-to-end**: clear the **ONLY INGEST FAILURES: Yes** chip, then read the five columns.
6. **Administration**, **License usage**: read **Last collected on** before anything else.
7. **Profiles**, **Overview**: a daily-cycle summary; supporting evidence only.
8. To re-ingest: **Sources**, **Local file upload**, **Add data**, choose **Existing dataset**, confirm the **Profile dataset** toggle is on and inherited, upload the same file, map as before, **Finish**. Then return to Batch end-to-end.

## Common mistakes

- Reading "Success" on a dataflow as proof that profiles exist
- Leaving the default **ONLY INGEST FAILURES** filter on and seeing nothing
- Quoting the License usage page or Profiles Overview as live evidence
- Fixing a setting and never re-ingesting
- Saying "it is just lag" without a test that could prove it wrong
- Deleting and rebuilding a build that is already correct

## Glossary

| Term | Meaning |
|---|---|
| Identity graph | The web of links connecting every record that belongs to one person |
| Real-Time Customer Profile (profile store) | One merged, current record per person, which audiences and journeys read |
| Union schema | The merged view of every Profile-enabled schema of one class |
| Profile dataset toggle | The dataset setting that sends its data to the profile store as well as the lake |
| Batch end-to-end | The Monitoring tab that shows each batch's lake, identity and Profile columns side by side |
| Records in Profile | Rows from a batch that are queryable in the profile store |
| New profile fragments | New profile records a batch created in the profile store |
| Re-ingest | Loading the same file again so the new batch can reach Profile |
| Evidence chain | The ordered list of checks and results that proves where a fault is and is not |
| Escalation | Handing a proven, platform-level fault to whoever owns the platform |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: monitor profile ingestion, monitor batch end-to-end data ingestion, union schema, enable a dataset for Profile

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
