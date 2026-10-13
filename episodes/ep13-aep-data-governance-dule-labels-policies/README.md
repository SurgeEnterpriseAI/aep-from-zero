# Episode 13: AEP Data Governance: DULE Labels and Policies

**Watch:** [Watch episode 13 on YouTube](https://youtu.be/SiBHW6aFvU8)

[Previous](../ep12-adobe-web-sdk-datastreams-aep-destinations/) · [Next](../ep14-aep-api-tutorial-with-postman-debug-and-rca/)

## What you will learn

- Explain **labels**, **marketing actions** and **policies** as one sentence, and say which one actually blocks
- Name the **five label categories** and the **three systems that consume labels**
- Explain why Adobe's shipped policies are **Disabled** by default, and who should own enabling them
- Read a **policy violation at activation** and fix the activation correctly
- Explain what **access** and **delete** privacy requests do, and why deleting a CRM row is not deletion

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch. In episode 12 the team wired one Web SDK tag to a datastream and set up a file-based cloud storage destination to send High-Value Loyalists and Lapsed 90 to the agency with hashed emails. Marketing still wanted the phone number in the file. Then Tara Joseph, Bloom's legal and privacy counsel, set her condition: nothing moves without consent, and nothing restricted leaves the building.

## Key ideas

### 1. One sentence: label, marketing action, policy
AEP's governance framework is called **data usage labelling and enforcement (DULE)**. Learn it as one sentence:
- A **label** says what a field **is**: a sticker on the field. Bloom's phone number is C2 data.
- A **marketing action** says what you **want** to do, for example Export to Third Party.
- A **policy** says which combination is **banned**: C2 data with Export to Third Party.

Labels describe, marketing actions intend, policies enforce. A label on its own blocks nothing, and so does a marketing action. Enforcement happens only when a policy ties the two together **and** somebody has switched that policy on.

Why a business cares: a process document depends on someone remembering it. A policy is checked at activation, every time, for everyone.

### 2. Labels: three consumers, five categories
Labels live on the schema's **Labels** tab, which opens with a **Label usage** dialog naming three downstream consumers:

| Consumer | What it decides |
|---|---|
| Governance policies | Whether data can be activated to destinations |
| Consent policies | Whether a profile may be included in an audience |
| Access policy | Attribute-based access control: which user roles can see the field at all |

So labels are not documentation: a wrong label can hide a field from a colleague or drop profiles out of an audience.

| Category | What it describes |
|---|---|
| Identity | Whether the field identifies a person, directly (I1) or indirectly (I2) |
| Sensitive | Sensitive categories such as location or health |
| Contract | Contractual restrictions on use: labels C1 to C12, the family policies act on most often |
| Partner ecosystem | Restrictions from data-partner agreements, such as data collaboration and clean rooms |
| Custom | Labels your organisation defines itself |

Labels are part of the schema, so they **need a schema save**. Custom labels need an owner and a naming convention from day one.

### 3. Marketing actions: the verb
Adobe's shipped marketing actions (for example Data Export, Email Targeting, Export to Third Party) are locked; **Create marketing action** adds your own.

**Destinations declare the marketing actions they perform**, so rules are written about actions, not vendors, and cover partners adopted next year. Bloom's agency destination is set up as performing **Export to Third Party**.

### 4. Shipped policies are Disabled
Every policy Adobe ships pairs associated labels with associated marketing actions, and every one shows **Disabled** out of the box. Governance in AEP is opt-in: a perfectly labelled schema protects nothing until the right policy is enabled. Enabling a policy is a **tenant-wide switch** shared by everyone working in that environment, so it needs a named owner and a written decision. Bloom enabled one, **3rd party export restriction**, after Tara signed it.

The main shipped pairings:

| Shipped policy | Labels | Marketing action it blocks |
|---|---|---|
| 3rd party export restriction | C2 | Export to Third Party |
| Restrict Data Collaboration | C11 | Data Collaboration |
| Restrict data sharing | C11 | Segment Match |
| Restrict data export | C12 | Data Export |
| Restrict email targeting | C4, C5 | Email Targeting |
| Restrict cross site targeting | C4, C5 | Cross Site Targeting |
| Restrict data science | C9 | Data Science |
| Restrict combining directly identifiable data | C3 | Combine with directly identifiable data |

C11 appears twice. One label can be governed by several policies, and enabling one does not enable the other.

### 5. The violation at activation, and the fix
At activation, AEP checks the labels on every mapped field against the enabled policies for the marketing actions the destination performs. Bloom's mapping held hashed email, loyalty band and `mobilePhone.number` (labelled C2). The agency destination performs Export to Third Party and the matching policy was enabled, so the activation was blocked. The violation names **the field, the label and the policy**. Adobe documents the violation screen this way; check what your screen shows.

| Option | Verdict |
|---|---|
| Remove the restricted field from the mapping | Right. Bloom's final mapping: hashed email and loyalty band only |
| Choose a destination that does not perform the banned action | Right, if the use is genuinely allowed |
| Delete the label | Wrong: it hides the truth about the data |
| Disable the policy "for a day" | Wrong: it switches the wall off for every activation |

Getting blocked is not failure; the failure would have been the export succeeding. If a partner truly needs a restricted field, that is a contract conversation, not a mapping change.

Before re-activating, Tara also settled Kavya's episode 12 question: any audience leaving Bloom for advertising must respect marketing consent, so High-Value Loyalists gained Lapsed 90's email consent condition and became a little smaller than 1,180.

### 6. Privacy requests: access and delete
The General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA) give customers the right to see or delete their data. In AEP this is a platform workflow, **Privacy Service**:
- An **access request** returns everything held on a person, as an auditable answer.
- A **delete request** removes the person across the datasets and the profile store.
- Both are **tracked**, so you can prove compliance.

"We deleted her CRM row" is not deletion. The data lake keeps the history, the profile was merged from several sources, and any file already sent to a partner still holds what you mapped: one more reason to map the minimum.

### 7. Consent is a state, and five questions for a client
Consent has a source, a timestamp, a scope and a lifecycle, and it must be enforced at activation, not merely recorded. "They ticked a box in 2021" is not a defensible answer.

Governance's real deliverable is a short document: these five questions, each with a named owner:
1. Which fields carry contractual restrictions, and from which contract?
2. Which marketing actions do we actually perform today?
3. Which policies do we therefore need enabled?
4. Who is allowed to enable or disable a policy?
5. What happens operationally when an activation is blocked, and who triages it?

Interview line: *"I have configured data usage policies and watched them block a bad export."* Say it once you have done it in your own development sandbox.

## In the product

Labels as of October 2026. Adobe documents the violation screen this way; check what your screen shows.

1. **Schemas**, open your schema, then the **Labels** tab (next to **Structure**). Read the one-time **Label usage** dialog.
2. On the Labels tab, tick a field's checkbox and click a label cell on that row. A panel titled **Apply access and data governance labels** opens with the five categories. Expand **Contract**, tick the label, then **Save** the schema.
3. **Privacy**, **Policies**:
   - **Browse**, with the **Governance policies** radio selected (the other radio is consent policies). Read **Associated labels**, **Associated marketing actions** and **Policy status**.
   - **Labels**: the label glossary, with **Create label**.
   - **Marketing actions**: Adobe's locked actions, with **Create marketing action**.
4. **Destinations**, activation wizard (episode 12): a breach raises a data usage policy violation.
5. **Privacy**, **Requests** (Privacy Service): create and track access and delete requests.

Never enable a policy, save labels on someone else's schema, or click Activate in a shared sandbox.

## Common mistakes

- Labelling fields and assuming the data is protected, when no policy is enabled.
- Labelling casually, as if labels were comments, when consent and access policies read them too.
- Applying labels and forgetting to save the schema.
- Enabling a policy on a whim: it is a tenant-wide switch and needs an owner.
- Assuming one enabled policy covers a label everywhere (C11 has two policies).
- "Fixing" a violation by deleting the label or disabling the policy.
- Answering a deletion request by deleting one CRM row.

## Glossary

| Term | Meaning |
|---|---|
| Data usage labelling and enforcement (DULE) | AEP's governance framework: labels, marketing actions and policies |
| Data usage label | A sticker on a field saying what the data is or how it is restricted, for example C2 |
| Marketing action | The thing you intend to do with data, such as Export to Third Party |
| Governance policy | A rule that blocks a label and marketing action combination, enforced at activation |
| Consent policy | A policy deciding whether a profile may be included in an audience |
| Access policy | Attribute-based access control: which roles can see a field |
| Tenant-wide | Applies to everyone working in that environment, not just to you |
| Policy violation | The block at activation that names the field, the label and the policy |
| Privacy Service | AEP's tracked workflow for access and delete requests |
| Access request | Returns everything held on a person, as an auditable answer |
| Delete request | Removes a person across the datasets and the profile store |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Data governance (labels and policies): https://experienceleague.adobe.com/en/docs/experience-platform/data-governance/home
- Privacy Service: https://experienceleague.adobe.com/en/docs/experience-platform/privacy/home
- Search Experience League for: data usage labels glossary, data usage policies overview, enforce data usage policies at activation

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
