# Episode 07: AEP Identity Stitching and the Identity Graph

**Watch:** [Watch episode 7 on YouTube](https://youtu.be/iEQupG9yHMc)

[Previous](../ep06-aep-batch-loaded-0-rows-partial-ingestion-fix/) · [Next](../ep08-aep-real-time-customer-profile-merge-policy/)

## What you will learn

- Say when Adobe Experience Platform (AEP) treats two records as the same person, directly or through a chain
- Identify the **linking event** and explain why it closes the graph
- Trace Priya's five fragments into one identity graph and leave the decoys out
- Use **Graph Simulation** to model stitching with no ingested data, and know its namespace limit
- Name the ways stitching goes wrong, including the shared-tablet over-link, and how teams guard against them

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on AEP before its loyalty relaunch. In episode 6 the failure lab ended well: 500 customers and 497 orders landed in the data lake. Then Rohan Desai, the analyst, asked how many customers Bloom actually has. The CRM (customer relationship management) export, the order system and the website each gave a different answer, and nobody could say which records were the same people.

## Key ideas

### 1. An identity is a pair: passport, driving licence and gym card
Your passport, driving licence and gym card carry three different numbers that all point to one you. In AEP every identity is a pair: an **identity namespace** (the kind of ID) and a **value**. Each record lists the identities it carries in its **identityMap**.

| Namespace | Type | What it identifies at Bloom |
|---|---|---|
| Email | standard | The person. Bloom's primary identity |
| BloomID | custom (Individual cross-device ID) | Bloom's own customer number |
| ECID (Experience Cloud ID) | standard | A browser or app install, not yet a person |

### 2. The stitching rule: share a value, same person; links chain
**Two records that share an identity value are treated as the same person.** The capability that does this is **Identity Service**. Stitching is **deterministic**: it links on identical values, never on similar names, cities or products. And **links chain**: if record A shares an ECID with record B, and B shares an email with record C, then A, B and C are one person, even though A and C have nothing in common directly.

### 3. Priya's five fragments
On the evening of 18 August, Priya browsed the Bloom app on her phone, added a Vitamin C Serum to her cart at 7:44 PM without signing in, signed in on the app, and bought on her laptop at 7:52 PM (order `BLM-88412`, 54.00 dollars).

| # | Record | Identities it carries |
|---|---|---|
| F1 | Product view in the app | ECID `3847…` |
| F2 | Add to cart, 7:44 PM | ECID `3847…` |
| F3 | App sign-in (**the linking event**) | ECID `3847…` and Email |
| F4 | Order `BLM-88412`, 7:52 PM | Email and BloomID |
| F5 | CRM loyalty record | Email |

The chain: **F1 and F2** join **F3** through the shared ECID, and F3 joins **F4 and F5** through the shared email. Priya's full ECID is `38472919862011456743`.

Why does F5 carry only one identity? Bloom Customer Profile declares one identity, Email, so the `bloom_id` column landed as a plain attribute. Priya's BloomID becomes an identity through F4, the order, whose schema declares BloomID as primary and the order email as a second identity. (The episode 4 sample file `sample-profile-priya.json` lists BloomID in its identityMap only as a teaching shape.)

### 4. The identity graph
The **identity graph** is the web of links connecting every record that belongs to one person. Think of dots and lines: each dot (node) is an identity value; a line (edge) is drawn when one record carries two values together. Priya's graph has three nodes (her ECID, her email, her BloomID) and two edges (the sign-in and the order). One connected graph is one person. Once stitched, Priya is one profile with **three identities**, and looking her up by email or by BloomID returns the same person. You will try that lookup in episode 8.

### 5. The linking event closes the graph
A **linking event** is one record that carries an anonymous ID and a known ID together. In real life it is almost always a sign-in, a login or a form submission.

| Before the linking event | After it |
|---|---|
| Browsing is anonymous | The ECID is bound to the person |
| Retargeting is blind | Earlier anonymous browsing attaches to them retroactively |
| Personalisation is impossible | Personalisation becomes possible |

Pull F3 out and the graph snaps in half: F1 and F2 float away as an anonymous device with no owner. An ECID-only profile like that is **pseudonymous**: treat it as anonymous for privacy until it is stitched to a known identity.

### 6. The decoys that must never join
Two records sit in the same sandbox: a web event with **ECID `9021…`**, and an order from **Arjun Patel** under his own email. Neither shares any identity value with Priya's five records, so neither joins her graph. Recognising who does not belong is half the skill.

### 7. Graph Simulation: stitching with no ingested data
**Graph Simulation** draws the graph that results from **activities** you type in. An activity is a set of identities seen together in one event, such as a sign-in. It works with **no ingested data**, so you can learn stitching whatever state your sandbox is in, and it ingests nothing. Its limit: the namespace list offers only the **16 standard namespaces**, so custom namespaces such as BloomID cannot be simulated.

### 8. Over-linking and the guardrails
A missing link splits one person into two. A **shared device over-links**: one family tablet's ECID, seen with two relatives' sign-ins, chains two emails into one graph, so two people become one. In the episode, Kavya finds one in Bloom's identity-links file; the exercise shows how to check the sample file for the same pattern. The opposite pattern, one email seen with several ECIDs, is expected: one person on several devices or browsers. The guardrails:

| Risk | Guard |
|---|---|
| Shared family devices | Watch login patterns; limit how aggressively one device can link people; review any device seen with more than one person's sign-in |
| Runaway identities (a test account or support login used by everyone) | Find them and keep them out; they can balloon one graph to thousands of people |
| Pseudonymous (ECID-only) profiles | Treat them as anonymous until stitched |
| Weak primary identity | Use email, not a device. Devices are shared and recycled; a weak primary identity makes the whole graph untrustworthy |

Rohan's question, "how many customers do we have?", gets its honest, person-based answer in episode 25.

## In the product

Labels as of October 2026.

1. In Adobe Experience Platform, open **Identities**. It has four tabs: **Overview**, **Namespaces**, **Graph Viewer** and **Graph Simulation**.
2. Open the **Graph Simulation** tab and click **Add activity**.
3. Row 1: namespace **Email**, value `priya.sharma@example.com`.
4. Click **+** to add a second row. An activity needs at least two identities.
5. Row 2: namespace **ECID**, value `38472919862011456743`. Check both rows, then click **Save**.
6. Add a second activity: **Email** `priya.sharma@example.com` and **ECID** `99887766554433221100` (Priya on a second device). **Save**.
7. Scroll down and click **Simulate**.
8. Check: **three nodes and two edges**, with the Email node in the middle joined to two ECID nodes. Each edge carries the number of the activity that created it (1 and 2). Disconnected nodes mean your two activities did not share an identical email value.

Watch out:
- The namespace list offers only the 16 standard namespaces: CORE, ECID, Email, Phone, Windows AID, TNTID, Adobe Analytics (Legacy ID), Emails (SHA256), AAMSegment, AAMTrait, Phone (SHA256), AEPSegments, Phone (E.164), Phone (SHA256_E.164), MLAudiences and CJA Audiences. **BloomID is not there**; do not go hunting for it.
- The namespace dropdown belongs to the row whose arrow you clicked, and choosing a value can overwrite a **different** row. Set one row, check it, then set the next.
- **Graph Viewer** is where you look at a real person's graph once data has landed. Graph Simulation is for learning the mechanism.

## Common mistakes

- Expecting every record to carry the same identity. The platform only needs overlapping pairs.
- Assuming an ECID-only record can never be joined. It can, through a linking event.
- Designing events where the ECID and the email never travel in the same record.
- Linking records because they look alike (same product, same evening, similar name). Only shared identity values link.
- Hunting for a custom namespace in Graph Simulation's dropdown.
- Saving an activity without re-checking every row.
- Celebrating a very large graph. It is often the first sign of an over-link.
- Choosing a device ID as the primary identity.

## Glossary

| Term | Meaning |
|---|---|
| Identity namespace | A kind of identifier, such as Email, ECID or a custom one like BloomID |
| identityMap | The part of a record that lists the identity values it carries |
| Experience Cloud ID (ECID) | The anonymous ID a browser or app install receives automatically |
| Identity Service | The AEP capability that links records sharing an identity into one identity graph |
| Identity stitching | Linking records that share an identity so fragments resolve to one person |
| Deterministic stitching | Linking only on identical identity values, never on guesses |
| Identity graph | The web of links connecting every record that belongs to one person |
| Linking event | One record carrying an anonymous ID and a known ID together, usually a sign-in |
| Pseudonymous profile | An anonymous, ECID-only profile not yet stitched to a known identity |
| Graph Simulation | The Identities tab that models a graph from typed activities, with no ingested data |
| Activity (Graph Simulation) | A set of identities seen together in one event |
| Over-linking | Wrongly merging different people, for example through a shared device |
| Primary identity | The identity a schema treats as the main key for the person |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Identity Graph viewer: https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/identity-graph-viewer
- Search Experience League for: identity graph simulation, Identity Service overview, identity namespaces

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
