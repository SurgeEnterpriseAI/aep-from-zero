# Episode 08: AEP Real-Time Customer Profile & Merge Policy

**Watch:** [Watch episode 8 on YouTube](https://youtu.be/05wGgS9nRIM)

[Previous](../ep07-aep-identity-stitching-identity-graph/) · [Next](../ep09-aep-no-profiles-found-debug-an-empty-profile/)

## What you will learn

- Explain what the **Real-Time Customer Profile** is, and why journeys and audiences read it instead of datasets
- Use the **union schema** as the cheapest proof that a schema contributes to Profile
- Compare **timestamp-ordered** and **dataset precedence** merge policies with the Dallas and Austin example
- Explain how duplicate CRM rows on one email become one profile, and what the merge policy decides
- Explain why a merge policy is a **business decision** that needs a named owner

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch. In episode 7, Kavya traced Priya's five fragments from the evening of 18 August into one identity graph: the app sign-in was the linking event, and the two decoys stayed out. But two of Priya's records disagree. Her CRM record from 2023 says she lives in **Dallas**; an update she made in the Bloom app in 2026 says **Austin**. Anjali, the CMO, asks which city the single customer view will show, and who chose it.

## Key ideas

### 1. The Real-Time Customer Profile
The **Real-Time Customer Profile** (the profile store) is one merged, current view of a person: the **union** of every attribute and event known about them, across every Profile-enabled dataset. It answers "who is this person right now?" in milliseconds, like the hotel receptionist with perfect memory. Once Priya is stitched, her profile holds her orders, her browsing, her Gold tier and her consent, with **three identities**: Email, BloomID and ECID. A lookup by email or by BloomID reaches the same person.

Her BloomID becomes an identity through her order (F4); on her CRM record it is a plain attribute. The sample file `sample-profile-priya.json` lists BloomID in its identityMap only as a teaching shape.

Journeys in Adobe Journey Optimizer (AJO) and the audiences you build read the **profile**, never the raw datasets. Get the profile wrong and every journey inherits the error.

### 2. Profile truth versus dataset truth
"One ingest, two worlds: the lake keeps the history, the profile store keeps the current person." The **data lake** keeps every row as it arrived, so the Dallas row and the Austin row both stay there. The **profile** must show one merged answer: dataset truth versus profile truth. They answer different questions, so do not expect them to agree row for row.

### 3. The union schema: the cheapest proof
The **union schema** merges every Profile-enabled schema of one class into a single view. If your schema's objects appear in it, your schema contributes to Profile; if not, it never reached Profile. This matters because saving identities and the Profile flag in one Save can silently drop the flag while the screen still says "Schema saved successfully". For Bloom Customer Profile, look for `personalEmail`, `person`, `homeAddress` and `mobilePhone`.

### 4. Duplicate rows on one email become one profile
Records that share an identity value belong to one person. Email is the primary identity on Bloom Customer Profile, so two CRM rows with the same email **collapse into one profile**, not two customers. Episode 5's calculated field lower-cased and trimmed every email at the door, so two spellings of one address arrive as the same value. Where the duplicate rows disagree, the **merge policy** decides which value the profile shows. A dataset's row count is not a customer count.

Caution from episode 7: rows that share an email but carry different names may be two people. Collapsing them is an **over-link**, so check the other columns first.

### 5. Merge policies: which value wins
A **merge policy** is the rule that decides which value wins when two sources disagree about the same person.

| Policy | How it decides | Priya's home city | Suits |
|---|---|---|---|
| Timestamp-ordered | The most recent value wins, field by field | Austin (the 2026 app update) | Values where the newest is truest: preferences, self-service updates |
| Dataset precedence | You rank datasets; the highest-ranked source wins, whatever its date | Dallas (CRM ranked first) | Values one system owns with authority: a legal name from billing |

Same data, two answers.

What "most recent" means: Adobe describes the time-based policy as "the most recently ingested value wins". Ingested means loaded into the platform, so re-loading an old file can make its old values the newest.

### 6. Default Timebased and ID stitching
Every sandbox ships **Default Timebased**, marked as the default merge policy: the most recently ingested value wins. Its editor is a four-step wizard. The **Configure** step holds:
- **ID stitching**: *None* assembles the profile from a single identity; *Private graph* assembles it across the whole identity graph. In Bloom's sandbox, Default Timebased uses Private graph; check what your own screen shows. The business question: "Is this one person across laptop, phone and CRM record, or three people?"
- **Default merge policy**: whether this policy is used when nobody names one ("What does a report show if the analyst does not choose?")
- **Active-On-Edge Merge Policy**: whether the same policy is used for edge decisions

A sandbox can hold at most **five** merge policies.

### 7. A business decision with a named owner
There is no technically correct merge policy, only a business one. Newest-wins is right for a delivery address and wrong for a legal name. Decide what should win for each attribute that matters, name the owner, and write it down. If different uses need different answers, you may need more than one policy. Bloom's home address decision goes to Anjali, in writing. Interview line: **"The merge policy is a business decision, not a technical default."**

### 8. Profile hygiene
- **Pseudonymous profiles** (ECID only, not yet stitched to a known identity) can pile up, because many visitors never sign in. Treat them as anonymous for privacy until they are stitched.
- Keep an eye on the profile counts that matter for your licence.
- Adobe offers data expiry settings for profile data. Check the current documentation; this course gives no numbers.

## In the product

Labels as of October 2026.

1. **Union schema.** Go to **Customer**, **Profiles**, then the **Union Schema** tab. Set **Class** to **XDM Individual Profile**. Look for your customer schema's objects: `personalEmail`, `person`, `homeAddress`, `mobilePhone`.
2. **Merge policies.** Go to **Profiles**, then the **Merge Policies** tab. Find **Default Timebased** (Default merge policy: Yes) and open it. The wizard steps are **Configure**, **Select Profile datasets**, **Select ExperienceEvent datasets** and **Review**. On Configure, read **ID stitching** (None or Private graph), the **Default merge policy** toggle and **Active-On-Edge Merge Policy**. Close it without saving.
3. **Creating a policy** (only in your own development sandbox): **Create merge policy**, then choose **Timestamp ordered**, or **Dataset precedence** and rank the datasets. At most five per sandbox.
4. **Profile lookup.** Go to **Profiles**, **Browse**. Choose a **Merge policy**, an **Identity namespace** and an **Identity value**, press **View**, then click the **Profile ID**. The detail tabs are **Details**, **Attributes**, **Events** and **Audience membership**.

In Bloom's build, step 4 with Default Timebased, Email and `priya.sharma@example.com` returned **No profiles found**, even though both batches succeeded, both datasets were Profile-enabled and the schema was in the union. Episode 9 investigates.

## Common mistakes

- Treating the profile as one more dataset, or expecting a dataset and the profile to agree row for row.
- Skipping the union schema check and trusting "Schema saved successfully".
- Announcing a dataset's row count as the number of customers.
- Accepting Default Timebased by habit because it shipped with the sandbox.
- Reading "most recent" as the date on the record. It means most recently ingested, so a re-loaded old file can win.
- Editing the shipped default merge policy in a shared sandbox: every lookup that names no policy uses it.
- Arguing about Dallas and Austin while ignoring ID stitching, which decides whether there is one Priya at all.
- Letting an engineer choose the merge policy alone, with no named business owner and nothing in writing.
- Rebuilding a correct build the moment a lookup returns nothing.

## Glossary

| Term | Meaning |
|---|---|
| Real-Time Customer Profile | The profile store: one merged, current view per person, built from Profile-enabled datasets |
| Profile truth, dataset truth | One current person, versus every row as it landed |
| Union schema | The merged view of every Profile-enabled schema of one class |
| Merge policy | The rule deciding which value wins when two sources disagree about a person |
| Timestamp-ordered | A merge policy where the most recently ingested value wins |
| Dataset precedence | A merge policy where a ranked dataset wins, whatever the timestamp |
| Default Timebased | The time-based merge policy every sandbox ships with, marked as default |
| ID stitching | None (profile from a single identity) or Private graph (across the whole identity graph) |
| Active-On-Edge Merge Policy | Whether the same merge policy is used for edge decisions |
| Profile viewer | Profiles, Browse: look a person up by any identity |
| Pseudonymous profile | An anonymous, ECID-only profile not yet stitched to a known identity |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Real-Time Customer Profile, UI guide: https://experienceleague.adobe.com/en/docs/experience-platform/profile/ui/user-guide
- Merge policies, UI guide: https://experienceleague.adobe.com/en/docs/experience-platform/profile/merge-policies/ui-guide
- Identity Graph viewer: https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/identity-graph-viewer
- Search Experience League for: union schema, profile data expiration, pseudonymous profile data expiration

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
