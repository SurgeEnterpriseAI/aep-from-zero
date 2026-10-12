# Episode 25: Customer Journey Analytics Tutorial: Person ID

**Watch:** Video coming soon on iTV

[Previous](../ep24-ajo-journey-not-sending-triage-with-step-events/) · [Next](../ep26-cja-data-views-and-derived-fields-explained/)

## What you will learn

- Explain what **Customer Journey Analytics (CJA)** is, what it reads, and why its numbers can legitimately differ from Adobe Experience Platform (AEP) profiles
- Explain **person-based, dataset-based and retroactive**, with one Bloom example each
- Design a **connection**: event, profile and lookup datasets, a person ID per dataset, identity stitching and the data window
- Choose a **person ID** that matches across datasets, and trace Priya with and without stitching
- Explain **Records skipped**, latency, why Adobe Journey Optimizer (AJO) reports and CJA differ slightly, and why **Use in CJA** is a billing decision

## The story so far

Bloom, a direct-to-consumer wellness brand with 1.2 million customers, is two weeks into its loyalty relaunch. In episode 24 Kavya triaged a broken journey with Journey Step Events and delivered Bloom's first ops readout. Then three teams brought Anjali three different answers to one question: how many orders did the relaunch bring? Act Three opens, led by Rohan, Bloom's analyst.

## Key ideas

### 1. CJA reads the lake through a connection, not the profile store
CJA is a **separate application**, not a reporting tab inside AEP. It reads **datasets from the data lake** (the archive) through a **connection**, not the Real-Time Customer Profile (the receptionist). Every number travels the same path: **dataset, connection, data view, Workspace**. A data view (episode 26) turns fields into metrics and dimensions; Workspace (episode 27) shows them.

**Profile stitching serves activation; analytical stitching serves measurement.** The profile store joins identities through the identity graph and a merge policy, to act on a person now. CJA joins rows through the connection's person ID, over the history in its window. So their counts can differ for defensible reasons.

### 2. Person-based, dataset-based, retroactive

| Word | Bloom example |
|---|---|
| Person-based: counts people, not devices or rows | Priya's phone browsing and laptop order are one customer |
| Dataset-based: any lake dataset can join | Web events, orders, journey step events and the catalogue side by side |
| Retroactive: definitions apply at report time | Fix a definition and the whole relaunch fortnight reports the new way, with no reload |

### 3. Bloom 360: four kinds of dataset
A connection holds **event**, **profile**, **lookup** and **summary** datasets, and needs at least one event or summary dataset.

| Dataset | Type in Bloom 360 | Needs a person ID? |
|---|---|---|
| Bloom Web Events | Event | Yes |
| Bloom Orders | Event | Yes |
| Journey Step Events | Event | Yes |
| Bloom Customers | Profile: a person's attributes, applied to their events | Yes |
| Product catalogue (200 products) | Lookup | No: a key and a matching key |

A **profile dataset** is a dataset in the lake, not the profile store: one ingest, two worlds. A **summary dataset** holds totals not tied to a person; Bloom 360 has none.

Why Bloom needs its own connection: with CJA reporting on for Journey Optimizer, Adobe creates an **AJO Enabled Connection** and **AJO Enabled Data View** per sandbox, and AJO's reports are "powered by Customer Journey Analytics". That connection holds only Journey Optimizer's datasets, with no profile data, so it cannot split opens by Gold versus Silver.

### 4. The lookup: key and matching key
Farhan loaded the 200-product catalogue as a batch dataset. As a **lookup** it needs no person ID. The **Key** is the SKU column in the catalogue; the **Matching key** is the SKU on each event's product line. Matching rows gain product names and categories, so `BLM-SER-VITC-30` reads as Vitamin C Serum 30 ml.

### 5. The person ID
The **person ID** is the field CJA uses to decide that rows belong to one human, chosen per dataset from the identities in its schema.
- It is **case sensitive**: `abc123` and `ABC123` are two people.
- A row with no value for it is **skipped**.
- Datasets merge into one person **only when their person IDs match**.

Bloom's choice is **the email on every dataset**:

| Dataset | Person ID in Bloom 360 |
|---|---|
| Bloom Orders | `orderEmail` (the primary identity is BloomID, but only the email can reach every dataset) |
| Bloom Customers | The profile's email; Bloom Customer Profile declares one identity, Email |
| Journey Step Events | The email |
| Bloom Web Events | Most rows carry only an ECID; **identity stitching** gives them the email from the sign-in row |

The repo's sample file `sample-profile-priya.json` lists BloomID in its identityMap as a teaching shape; in the build, the customer schema's only identity is Email. And because episode 5 lower-cases and trims emails as they land, `Priya.Sharma@example.com` and `priya.sharma@example.com` never become two people.

### 6. Tracing Priya: stitching off and on

| Priya's evening, 18 August | Stitching off | Stitching on |
|---|---|---|
| 7:44 PM add-to-cart in the app (ECID only) | An anonymous person | Priya, by email |
| App sign-in (ECID and email together) | The same anonymous person | The linking row |
| 7:52 PM order on her laptop (email) | A second person | Priya, by email |
| People counted | Two | One |
| Cart abandoners | One, and it is false | None: she bought 8 minutes later |

### 7. Records skipped, the window and latency
- The details page shows **Records added**, **Records skipped**, **Records deleted** and **Batches added**. Records skipped counts rows with no timestamp or a missing or invalid person ID.
- **Enable rolling data window** was ticked at **13 months**.
- New data appears **within 90 minutes** of reaching Experience Platform, **up to 4 hours with stitching**. Small backfills take up to 7 days, large ones up to 30.
- The **sandbox cannot be changed** once a connection is saved.
- Rohan's episode 7 question, "how many customers do we actually have?", gets an honest unit: **people**, each email counted once.

### 8. Why AJO reports and CJA differ
Adobe says the gap is "typically less than 1-2%", larger for the last two hours of data:
- **Retries:** AJO counts them; CJA does not, so CJA shows lower.
- **Time zone:** AJO reports in UTC; a data view can use another zone. Midnight UTC is 5:30 AM in India.
- **Late data:** the message feedback dataset arrives in batches up to 2 hours late.

When reports disagree, check the window and the timestamp definition first.

### 9. Use in CJA is a billing decision
On the AJO Enabled Connection's details page, the right panel holds **Refresh**, **Create data view** and **Use in CJA**. Adobe: once enabled, "each row counts toward your monthly licensed rows", and removing it later still bills the full month. It is the organisation owner's decision.

Interview lines: *"CJA is person-based, dataset-based and retroactive."* *"A connection with the wrong person ID produces confident, wrong numbers."*

## In the product

Labels as of October 2026. Read only: look, screenshot, leave.

1. Open CJA from the application selector (the nine-dot icon, top right). The menu reads **Workspace**, **Data Management**, **Components**, **Tools**, **Labs**.
2. **Data Management**, **Connections**: tabs **List** and **Usage**; columns Name, Connection type, Datasets, Sandbox, Owner, Import new data, Date created. Do not click **Create new connection**.
3. Click a connection's name. Read **Records added**, **Records skipped**, **Records deleted**, **Batches added**. Click none of **Refresh**, **Create data view**, **Use in CJA**.
4. **Edit Connection** is a live form: **Connection settings** (Connection name, Tags, Connection description, Primary ID) and **Data settings** (Enable rolling data window, Select number of months, Sandbox, Average number of daily events). If an administrator shows it to you, leave with **Cancel**.
5. Creating a connection (Adobe documents it this way; check what your screen shows): **Create new connection**, then **Add datasets** in three steps: **Select datasets**, **Datasets settings**, **Datasets preview**. Per event dataset: **Person ID**, **Timestamp**, **Data source type**, optional identity stitching. Per lookup: **Key** and **Matching key**. Per dataset: **Import new data** and a backfill. Only a CJA product administrator who also holds Platform permissions can create one.
6. In Journey Optimizer, **Journey Management**, **Reports** names its data view at the top right.

## Common mistakes

- Calling CJA "reporting in AEP" and expecting a profile's live values.
- Reading "profile dataset" as the Real-Time Customer Profile.
- BloomID on one dataset and the email on another, expecting one person.
- Mixed-case emails, so one customer becomes two people.
- Stitching off on anonymous web events, creating false abandons.
- Ignoring Records skipped because Records added looks healthy.
- Chasing a one or two percent AJO-versus-CJA gap as if it were a bug.
- Clicking **Use in CJA** "to see what it does".

## Glossary

| Term | Meaning |
|---|---|
| Customer Journey Analytics (CJA) | Adobe's separate application for person-based analysis of lake datasets |
| Connection | Brings datasets into CJA and names the person ID |
| Person ID | The field that decides rows belong to one human; case sensitive |
| Event dataset | Time-stamped rows such as page views, orders or journey steps |
| Profile dataset | A person's attributes, applied to their events; a lake dataset |
| Lookup dataset | Reference data joined to events through a key and a matching key |
| Identity stitching (CJA) | Gives a person's anonymous and logged-in rows in one event dataset one person ID |
| Records skipped | Rows dropped for no timestamp or a missing or invalid person ID |
| Rolling data window | Months of event data a connection keeps (13 in Bloom 360) |
| AJO Enabled Connection | Adobe's system connection for Journey Optimizer reporting; no profile data |
| Use in CJA | Bills every row toward licensed rows; the owner's decision |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

Search Experience League for: Customer Journey Analytics connections overview, create a connection, dataset types (event, profile, lookup, summary), person ID, identity stitching in Customer Journey Analytics, data latency, Use in CJA licensed rows, Journey Optimizer reporting in Customer Journey Analytics.

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
