# Exercise 14: Three landmines, one API

You will diagnose three incidents with symptom, layer, evidence, fix, write a five-line RCA, and learn the four headers that scope every Adobe Experience Platform (AEP) API call.

## Track A: No Adobe access needed

1. **Work each landmine.** For each of the three landmines below, write four lines: symptom, layer, evidence, fix.
   - **Landmine 1.** Marketing says the High-Value Loyalists file looks thinner every day. A Gold profile ingested last week shows `"tier": "Gold", "band": "Gold"`. A Gold profile ingested yesterday shows `"tier": "Gold", "band": null`. The dataflow history says the mapping was last edited three days ago.
   - **Landmine 2.** The identity graph has started linking strangers. A test profile's identity map shows a BloomID value under `Email`. Asking the Profile Access API for that value with `entityIdNS=email` returns a profile. A test dataset ingested last week mapped `bloom_id` into the Email namespace.
   - **Landmine 3.** Lapsed 90's estimate is 7,240 against a recorded 3,890. The rule reads "last order more than 30 days ago and email consent true". The audit log shows an update to Lapsed 90, with the account and the time.
2. **Write a full RCA for landmine 1** in five lines: symptom, cause, fix, verification, prevention. Make the prevention line a detection net plus a process gate.
3. **Wrong answers.** Explain in two or three sentences each why "reset the sandbox" (landmine 2) and "lock the platform" (landmine 3) are wrong answers.
4. **The four headers.** Write the four headers of an AEP API call, say what each one answers, and say what happens if you forget the sandbox one.
5. **Strangers.** Explain in two sentences how reused test IDs filed in the wrong namespace can link strangers.
6. **The episode's practice question.** Say, for example, the Window Shoppers audience suddenly shrinks overnight. Which layers would you check, and what evidence would you gather first?

## Track B: If you have a development sandbox and API credentials (optional)

Safety first:
- Use a **development** sandbox only. Never point the collection at a production sandbox.
- Use **your own** credentials. Never paste a real token or key into a shared file, a chat or a repository.
- Send **read requests only** (the Profile Access API lookup). Do not send anything that creates, updates or deletes.
- Use a **test profile** you created yourself, never a real customer.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. In Postman, import the course collection, `bloom-aep-postman-collection.json` from the course data folder, and fill the four placeholders, `{{ACCESS_TOKEN}}`, `{{API_KEY}}`, `{{IMS_ORG}}` and `{{SANDBOX_NAME}}`, with your own development values. Read the sandbox name aloud.
2. Call the Profile Access API for your test profile by email, using the request in the notes: `GET /access/entities?schema.name=_xdm.context.profile&entityId=<your test profile's @example.com address>&entityIdNS=email`.
3. Call it again by your custom namespace: set `entityId` to the test profile's customer number and `entityIdNS` to your custom namespace's symbol (the short code you gave it when you created it, not its display name).
4. Compare the two responses. Is it the same profile? How many identities does each response list?
5. Open **Sources**, then **Dataflows**; then open **Datasets**, your dataset, and **Dataset activity**. Write down the total records and any failed batches. Do not edit any mapping.

## Check yourself

1. What four pieces of context does every Platform API call carry?
2. What can go wrong if you forget the sandbox header, and why is it dangerous?
3. What two things does the Profile Access API need to find one person?
4. Why does fetching the same person by two namespaces prove the identity design?
5. Name the five layers you can translate a symptom into.
6. Why is the fault for a null loyalty band usually in Data Prep, not in the audience?
7. What does "replay the window" mean?
8. What does quarantine mean, and how is it different from deleting?
9. What are the five lines of an RCA?
10. What makes a prevention line credible?

<details><summary>Check your answers</summary>

**Task 1: the three landmines**

| | Landmine 1 | Landmine 2 | Landmine 3 |
|---|---|---|---|
| Symptom | Loyalist file thinner every day | Identity graph links strangers | Win-back audience nearly double the recorded estimate |
| Layer | Ingestion (the Data Prep calculated field), though it shows in the audience | Ingestion (a test dataset's mapping), though it shows in the identity graph | Audience (the rule itself), though it shows in the campaign's size |
| Evidence | Old rows have a band, new rows have null; the mapping was edited three days ago, exactly when nulls began | A BloomID value under Email; a lookup in the Email namespace returns a profile; the test dataset's mapping sent `bloom_id` to Email | The rule says 30, not 90; the estimate is 7,240 against 3,890 (about 1.86 times); the audit log names who changed it and when |
| Fix | Restore the calculated field in the mapping; re-run only the batches from the broken window | Quarantine: take the polluting batches out, keep the file, batch details and affected-profile list, fix the mapping before any re-ingest | Restore 90 days, Refresh estimate, confirm about 3,890, record the change and its author in the incident note |

**Task 2: a model RCA for landmine 1**
- **Symptom:** the High-Value Loyalists file looked thinner every day.
- **Cause:** a mapping edit three days earlier broke the calculated field that derives the loyalty band, so new records landed with a null band, and High-Value Loyalists reads the band.
- **Fix:** restored the calculated field in the dataflow mapping and re-ran only the batches from those three days.
- **Verification:** newly ingested profiles, fetched through the Profile Access API, read band Gold; the audience estimate recovered to a little under the 1,180 recorded at the build, because episode 13 added an email consent condition.
- **Prevention:** detection net, monitor null rates on key fields such as the loyalty band after any mapping change; process gate, dataflow edits need a review before they run.

**Task 3: wrong answers**
- **Reset the sandbox** destroys every schema, dataflow and audience the team built in order to fix one dataset. The fault is one test dataset's mapping, so the repair should touch only that dataset's batches and mapping.
- **Lock the platform** confuses a freeze with prevention. No edits ever means no operations: nobody could fix the next real problem either. Prevention is a detection net plus a process gate, such as a named reviewer for rule changes.

**Task 4: the four headers**
`Authorization: Bearer` (who you are), `x-api-key` (which application), `x-gw-ims-org-id` (which organisation) and `x-sandbox-name` (which sandbox). Forget the sandbox header and you can query production while believing you are in development, with no warning, because the response looks normal.

**Task 5: strangers**
A test file reused a few BloomIDs across different test customers, and its mapping filed those values in the Email namespace. Every record carrying the same "email" value was treated as the same person, so the identity graph joined strangers into one profile.

**Task 6: practice question (one good answer)**
Start with the symptom and list the layers. Check the audience layer first because it is cheap: read the rule and look in the audit log for an edit. Then check ingestion: are web events and orders still landing, according to the Dataflows page under Sources and each dataset's Dataset activity? Then identity: does a sample person still resolve as one profile through the Profile Access API? Fix only where the evidence points.

**Check yourself**
1. A Bearer token (who), an API key (which application), the IMS org ID (which organisation) and the sandbox name (which sandbox).
2. The call can land in production while you believe you are in development. Nothing warns you, so reads mislead and writes put test data among real customers.
3. An identity value and the namespace it belongs to (`entityId` and `entityIdNS`).
4. Two different identifiers returning one profile proves the graph really links the systems that hold them. If they return different people or nothing, the design is broken.
5. Schema, ingestion, identity, audience and activation.
6. The band is a calculated field that Data Prep derives as records land. Old rows are fine and new rows are not, so the break happened at ingestion time.
7. Re-running only the batches that were ingested while the fault was live, through the corrected mapping, instead of re-ingesting everything.
8. Setting bad records aside deliberately, recorded and recoverable. Deleting quietly loses the evidence and the ability to explain or reverse the clean-up.
9. Symptom, cause, fix, verification, prevention.
10. It pairs a detection net (a check that catches the fault quickly next time) with a process gate (a step that stops it happening), and it never relies on "be more careful", a freeze or blame.

</details>
