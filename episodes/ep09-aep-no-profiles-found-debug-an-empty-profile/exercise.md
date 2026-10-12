# Exercise 09: The missing-profile investigation

You will put the missing-profile playbook in order, explain the three-destinations model to a colleague, and write the escalation note that proves a fault is not in your build.

## Track A: No Adobe access needed

1. **Put the playbook in order.** Here are Bloom's eight checks, shuffled:
   - Licence capacity
   - **Records in Profile** on the monitoring screen
   - The same person by a second namespace
   - Re-ingest the same file
   - The dataset's Profile flag
   - The schema is present in the union schema
   - The batch actually succeeded
   - The schema is enabled for Profile

   Put them in the order you would run them. For each one, write:
   - the screen you would open
   - what "fail" looks like on that screen
   - what you would do next if it fails
2. **Answer a colleague.** A colleague says: "The batch succeeded, so the profile must be there." Reply in three sentences using the three-destinations model (data lake, identity graph, profile store).
3. **Reassurance or diagnosis?** Label each statement R (reassurance) or D (diagnosis), and rewrite every R as a D:
   - "It is just lag; the profile store catches up on its own schedule."
   - "Records in dataset is 500 and Records in Profile is blank on this batch."
   - "It will probably show up tomorrow."
   - "If a re-ingest into the enabled dataset creates profiles, the first batch arrived too early; if not, it is not our build."
4. **Write the escalation note.** Write five lines to a platform owner:
   - what you checked, in order
   - the decisive Monitoring row
   - what you ruled out
   - the batch and dataset references you would attach
   - what you need from them
5. **The episode's practice question.** A colleague says the batch succeeded, so the profile must be there. Which screen do you open, which filter do you clear, and which column do you read?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production, and only objects that carry **your own initials**.
- Everything below is **read-only**. Do not create, save, delete or re-ingest anything here, and never touch someone else's schema or dataset.
- Never turn on Profile for a schema or dataset that is not yours; enabling a schema for Profile is irreversible.
- Nothing here needs **Activate**, **Publish** or any send. Do not click them.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Open **Monitoring**, **Batch end-to-end**. Find the chip that reads **ONLY INGEST FAILURES: Yes** and clear it.
2. Find a batch that loaded into **your own** dataset. Write down the five columns: **Records in dataset**, **New profile fragments**, **Existing profiles**, **Identity records stitched**, **Records in Profile**.
3. Open **Profiles**, **Union Schema**, set **Class** to **XDM Individual Profile**, and check whether your own schema's objects are listed.
4. Open **Schemas**, **Browse** and read the **Enabled for Profile** column for your own schemas.
5. Open **Profiles**, **Browse**, choose **Default Timebased** and a namespace, and look up one value from your own test data. Re-read the form before you press **View**. Then try a second namespace if your data has one.
6. Write your evidence chain in five lines, as in Task 4. If everything you control is correct and **Records in Profile** is still blank, stop: do not rebuild a correct build while you wait for the platform owner.

## Check yourself

1. Name the three destinations one file fans out to, and the gate for each.
2. Why does "Identity records stitched" not prove that a profile exists?
3. What does the default filter on Batch end-to-end hide, and why does it matter?
4. Which two columns tell you whether a batch reached the profile store?
5. Why is a lookup by a second namespace the first check?
6. Why can the License usage page rule out a capacity problem but not serve as live evidence?
7. What happens to data loaded before a dataset was enabled for Profile, and what is the fix?
8. When do you stop diagnosing and escalate?

<details><summary>Check your answers</summary>

**Task 1: the playbook in order**

| # | Check | Screen | What fail looks like | Next step |
|---|---|---|---|---|
| 1 | Same person by a second namespace | Profiles, Browse | One namespace finds the person and another does not | It was a namespace or value error; fix the lookup |
| 2 | Schema enabled for Profile | Schemas, Browse, Enabled for Profile column | The column does not read Enabled | Enable it (your own schema only), then re-ingest |
| 3 | Schema present in the union | Profiles, Union Schema | Your schema's objects are missing | Check the class and the Profile flag |
| 4 | Dataset Profile flag | Start a dataflow at the dataset; the Profile dataset toggle is inherited | The toggle is off | Enable it on the dataset, then re-ingest |
| 5 | Batch actually succeeded | Datasets, the dataset, the batch | Failed rows or a failed status | Read the error diagnostics; fix the mapping or the data |
| 6 | Records in Profile | Monitoring, Batch end-to-end, filter cleared | Lake and identity green, Records in Profile blank | This is the decisive one: profile ingestion, not your build |
| 7 | Licence capacity | Administration, License usage | A capacity problem, or a stale Last collected on date | Check the collection date before believing the page |
| 8 | Re-ingest the same file | Sources, Local file upload, existing dataset | Records in Profile still blank | Escalate to the platform owner with steps 1 to 7 as evidence |

The point is the order: each step is cheap and removes a whole class of cause. Bloom's team happened to read the licence page before Monitoring; swapping two cheap checks is fine. What matters is that the re-ingest comes last, after every cheap check has passed.

**Task 2: a model reply**
"Success means the rows reached the data lake, which is only one of three destinations; the identity graph and the profile store each have their own gate. The profile store also needs the schema and the dataset enabled for Profile and a primary identity that resolves, and data loaded before that is never promoted. So let's open Monitoring, Batch end-to-end, clear the failures-only filter, and read Records in Profile for that batch."

**Task 3: reassurance or diagnosis**
- "It is just lag" is R. As a D: "Adobe publishes no time for batch data to reach Profile, so we will re-ingest into the enabled dataset and read Records in Profile on the new batch."
- "Records in dataset is 500 and Records in Profile is blank" is D: it is a fact you can show.
- "It will probably show up tomorrow" is R. As a D: "We will read Records in Profile for this batch on Batch end-to-end now; if it is blank, we will re-ingest once into the enabled dataset and read the new row."
- The re-ingest statement is D: it names a test, and either result teaches you something.

**Task 4: a model escalation note**
1. Checked, in order: lookup by Email and by BloomID, schema Enabled for Profile, schema in the union schema, dataset Profile toggle (on, inherited), batch status, licence page, then a re-ingest of the same file.
2. Decisive row: Monitoring, Batch end-to-end, filter cleared: Records in dataset 500 (green), Identity records stitched (green), Records in Profile blank, on the original batch and on the re-ingest.
3. Ruled out: namespace or typo, schema not contributing, dataset not enabled, failed batch, licence capacity, and an early load (the re-ingest reproduced it). Profiles Overview reads "No data is ingested to Profiles" for the whole sandbox.
4. References: batch ID `<batch ID>` and dataset ID `<dataset ID>` for both batches.
5. Ask: profile ingestion does not appear to be running in this development sandbox; please investigate and restore it, and tell us when to re-ingest.

**Task 5: practice question**
Open Monitoring, Batch end-to-end. Clear the ONLY INGEST FAILURES: Yes chip. Read Records in Profile (and New profile fragments) for that batch, not just Records in dataset.

**Track B: what to expect**
In a healthy sandbox, a batch into a Profile-enabled dataset shows New profile fragments above zero, and the lookup finds the person. Adobe publishes no time for batch data to reach Profile, so any waiting allowance is your own. If Records in Profile stays blank after every check passes, that is evidence for the platform owner, not a reason to rebuild.

**Check yourself**
1. The data lake (the row is valid), the identity graph (an identity is declared and mapped), and the profile store (schema and dataset enabled for Profile, and a primary identity resolves).
2. The identity graph and the profile store are separate destinations with separate gates; a number from one is not evidence about the other.
3. It hides every successful batch, and the successful batch is the one whose Profile columns you need to read.
4. New profile fragments and Records in Profile.
5. It is the cheapest test, and it rules out a typo or a wrong namespace before you suspect the platform.
6. Its Last collected on date can be days old. A stale page can still show there is no capacity problem, but it cannot tell you what is happening today.
7. It stays in the data lake and never becomes a profile, because enablement is not retroactive. Re-ingest it.
8. When every layer you control is provably correct and a re-ingest of the same file reproduces the fault.

</details>
