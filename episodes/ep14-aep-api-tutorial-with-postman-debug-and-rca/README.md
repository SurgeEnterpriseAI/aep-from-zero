# Episode 14: AEP API Tutorial With Postman: Debug and RCA

**Watch:** [Watch episode 14 on YouTube](https://youtu.be/wnEOmQsoghE)

[Previous](../ep13-aep-data-governance-dule-labels-policies/) · [Next](../ep15-aep-query-service-tutorial-sql-on-the-data-lake/)

## What you will learn

- Name the **four pieces of context** on every Adobe Experience Platform (AEP) API call, and the risk of a missing **sandbox header**
- Read one person with the **Profile Access API**, by identity value and namespace
- Apply **symptom, layer, evidence, fix** to three real-shaped incidents
- Choose **surgical remediation** (fix the mapping, replay the window, quarantine polluting batches) over rebuilds
- Write a **five-line root cause analysis (RCA)** with a verification line and a credible prevention line

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on AEP before its loyalty relaunch. In episode 13, governance held: the phone field carried contract label C2, the matching policy was switched on, and the agency activation went out with hashed email and loyalty band only. A week before the relaunch, Bloom's chief technology officer (CTO) forwarded three complaints that traced back to landmines left by the previous consultants, and asked for proof that the foundation holds, through the API and not through screenshots.

## Key ideas

### 1. Why the API, when you have a UI
An API (application programming interface) lets one program ask another for data, with no screens. The interface shows you what Adobe decided to show you; the API shows you the object as it actually is. So the honest answer to "is this customer's data correct?" is the object, not a screenshot.

The team works in **Postman**, a tool for sending API requests and saving them as a collection. Bloom's collection holds placeholders only, never real secrets.

### 2. Four pieces of context on every call
Every Platform API call carries four **headers**, labelled lines of context sent with the request. Each answers one question:

| Question | Header | Placeholder in Bloom's collection |
|---|---|---|
| Who are you? | `Authorization: Bearer ...` (an access token) | `{{ACCESS_TOKEN}}` |
| Which application is asking? | `x-api-key` | `{{API_KEY}}` |
| Which organisation? | `x-gw-ims-org-id` (the IMS org ID; IMS = Identity Management System) | `{{IMS_ORG}}` |
| Which sandbox? | `x-sandbox-name` | `{{SANDBOX_NAME}}` |

**The missing sandbox header.** Forget `x-sandbox-name` and you can query production while believing you are in development, and nothing warns you. Keep the sandbox name in one clearly labelled place, read it aloud before anything that writes, and never point a practice collection at production.

### 3. The Profile Access API: one person by identity
To read one person from the Real-Time Customer Profile, ask for an **entity by identity**: a value plus the **namespace** that value belongs to.

```
GET /access/entities?schema.name=_xdm.context.profile&entityId=priya.sharma@example.com&entityIdNS=email
Authorization: Bearer {{ACCESS_TOKEN}}
x-api-key: {{API_KEY}}
x-gw-ims-org-id: {{IMS_ORG}}
x-sandbox-name: {{SANDBOX_NAME}}
```

- `entityId` holds the value; `entityIdNS` holds the namespace.
- The response is the **merged profile**: the person as the profile store holds her right now, with attributes and her identity map.
- **Same person, two namespaces.** Fetched by email and then by BloomID (`BLM-CUST-004217`), Priya returns the same profile with three identities: Email, BloomID and ECID. That is the cheapest proof the identity design links Bloom's systems.
- A value sent in the wrong namespace (a customer number asked for as an email) should find nobody. If it finds someone, your identity data is polluted.

### 4. Symptom, layer, evidence, fix
Problems arrive as **symptoms** ("the loyalist file is shrinking"). Translate the symptom into a **layer**: schema, ingestion, identity, audience or activation. Gather **evidence** at that layer before touching anything. Then **fix** where the fault lives, which is often not where the symptom appeared. A null loyalty band shows up in an audience but is almost always caused in Data Prep. Loosening the audience rule would make the count look normal while the data stays broken.

### 5. The three landmines

| | 1. The vanishing loyalty band | 2. Polluted identities | 3. The audience that grew |
|---|---|---|---|
| Symptom | High-Value Loyalists file thinner every day | The identity graph links strangers | Lapsed 90 estimate jumps from 3,890 to 7,240 (nearly double, about 1.86 times) |
| Evidence | Older Gold profiles have band Gold; yesterday's read band null. The dataflow mapping was edited three days ago, when the nulls began | A BloomID value sits under Email in a test profile's identity map; asking for it in the Email namespace returns a profile. A test dataset mapped `bloom_id` into the Email namespace | The rule reads "more than 30 days". The audit log names who changed it and when |
| Layer | Ingestion: the calculated field in Data Prep | Ingestion: a test dataset's mapping | Audience: the rule itself |
| Fix | Restore the calculated field, re-run only the batches from the broken window | Quarantine the polluting batches, keep the evidence, fix the mapping | Restore 90 days, Refresh estimate, confirm about 3,890, record the change |

**Why strangers linked.** The test file reused a handful of BloomIDs across different test customers. Because those values were filed as emails, every record sharing one of them was joined into one graph. The graph did its job: it linked what it was told.

### 6. Quarantine, do not delete: surgical remediation
**Quarantine** means setting bad records aside deliberately, recorded and recoverable, never quietly deleted. Taking a polluting batch out is fine; doing it silently, with no record, is not. For landmine two, take the polluting batches out (bad identity data can be removed with the batches that brought it in), keep the original file, the batch details and the list of affected profiles, and fix the mapping before anything is re-ingested.

Wrong answers: **reset the sandbox** (destroys everything to fix one dataset), **rename the Email namespace** (impossible; namespaces cannot be renamed or deleted), **lock the platform** (no edits means no operations), and **leave the 30-day audience** (burns margin discounting people who lapsed only weeks ago).

### 7. The five-line RCA
Symptom, cause, fix, **verification**, **prevention**. Verification is the line most people skip; prevention separates senior from junior. Prevention is never "be more careful", a freeze, or a blame line. It is a **detection net** plus a **process gate**.

The episode walks through landmine one (your exercise). Here is landmine three in the same shape:

| Line | Landmine three |
|---|---|
| Symptom | Lapsed 90's estimate jumped from 3,890 to 7,240 overnight |
| Cause | The rule was edited from 90 to 30 days; the audit log names who and when |
| Fix | Restored 90 days |
| Verification | Refresh estimate returned about 3,890 |
| Prevention | Net: a daily check of each relaunch audience's estimate against its recorded value. Gate: a named reviewer for rule changes |

**Handover.** A foundation is finished when someone else can run it: named datasets with owners, a documented identity design, merge policies with their business reason written down, and a list of known-bad rows you chose to live with (for example the order priced at -20.00, which loaded because it is a valid number).

Interview line: *"An RCA has five lines: symptom, cause, fix, verification, prevention. Prevention is a detection net plus a process gate."*

## In the product

Labels as of October 2026.

1. **Sources**, then **Dataflows**, lists every dataflow run and its errors. Open the dataflow that feeds the dataset in question.
2. **Datasets**, then your dataset, then **Dataset activity**, shows total records and failed batches. That row count is the honest evidence of what landed.
3. Open the audience in **Segment Builder** to read its rule. The **Audience properties** panel on the right shows Estimated profiles and **Refresh estimate**.
4. **Postman:** import the course collection, fill the four placeholders with your own development values, and send the Profile Access API request above. Read the sandbox name before every send.

## Common mistakes

- Forgetting `x-sandbox-name`, so a call lands in production while you believe you are in development.
- Pasting a real token into a shared collection.
- Testing a profile with only one identity, which proves the lookup but not the links.
- Fixing where the symptom appeared, for example loosening an audience rule, instead of where the fault lives.
- Quietly deleting bad data instead of quarantining and documenting it.
- Writing an RCA without a verification line, or with "be more careful" as prevention.

## Glossary

| Term | Meaning |
|---|---|
| API (application programming interface) | A doorway that lets one program ask another for data, with no screens |
| Postman | A tool for sending API requests and saving them as a reusable collection |
| Header | A labelled line of context sent with every API request |
| Bearer token | The access token that says who is calling, sent in the Authorization header |
| IMS org ID | The identifier for your Adobe organisation; IMS = Identity Management System |
| x-sandbox-name | The header that decides which sandbox a call talks to |
| Profile Access API | The read API for the Real-Time Customer Profile: one person by identity value plus namespace |
| entityId / entityIdNS | The request parameters that carry the identity value and its namespace |
| Identity pollution | False identities in the graph, usually from a wrong namespace mapping |
| Quarantine | Setting bad records aside deliberately, recorded and recoverable, rather than deleting them |
| Replay the window | Re-running only the batches ingested while a fault was live |
| Audit log | The record of who changed an object, and when |
| Root cause analysis (RCA) | Five lines: symptom, cause, fix, verification, prevention |
| Detection net | A check that catches a fault quickly next time, such as a null-rate monitor |
| Process gate | A step that stops a fault happening, such as a review before dataflow edits |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Profile Access API entities, Experience Platform API authentication, sandbox header x-sandbox-name
- Search Experience League for: dataflow monitoring, dataset activity, audit logs overview

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
