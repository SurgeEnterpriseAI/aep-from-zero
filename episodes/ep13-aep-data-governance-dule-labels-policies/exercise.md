# Exercise 13: Get blocked on purpose

You will write the governance sentence from memory, find the policy that blocks Bloom's phone number, draft the five questions every client needs answered, and explain why one deleted CRM row is not deletion.

## Track A: No Adobe access needed

1. **The governance sentence.** Without looking at the notes, write one line each for a **label**, a **marketing action** and a **policy**. Then say which of the three actually blocks an export, and what else must be true before it blocks anything.
2. **Find the policy.** Bloom's phone field, `mobilePhone.number`, carries contract label **C2**. Bloom's agency destination is set up as performing **Export to Third Party**. Use the table of the main shipped pairings below.
   - a. Which policy blocks this activation?
   - b. In two sentences, explain why labelling the phone field alone blocks nothing.
   - c. Which label appears in two policies, and what happens if you enable only one of them?

   | Shipped policy | Labels | Marketing action it blocks | Status out of the box |
   |---|---|---|---|
   | 3rd party export restriction | C2 | Export to Third Party | Disabled |
   | Restrict Data Collaboration | C11 | Data Collaboration | Disabled |
   | Restrict data sharing | C11 | Segment Match | Disabled |
   | Restrict data export | C12 | Data Export | Disabled |
   | Restrict email targeting | C4, C5 | Email Targeting | Disabled |
   | Restrict cross site targeting | C4, C5 | Cross Site Targeting | Disabled |
   | Restrict data science | C9 | Data Science | Disabled |
   | Restrict combining directly identifiable data | C3 | Combine with directly identifiable data | Disabled |

3. **Five questions, five owners.** Write the five governance questions you would ask a client. Beside each, name the role that should own the answer at Bloom (for example Legal, the platform owner, the CRM and journeys lead, the data engineer).
4. **Not deletion.** In three sentences, explain why "we deleted her CRM row" is not GDPR deletion, and what is.
5. **Fix it right.** A colleague's activation is blocked by a data usage policy violation two hours before a deadline. They suggest four fixes. Mark each right or wrong, with one reason:
   - a. Delete the label from the field.
   - b. Disable the policy until tomorrow.
   - c. Remove the field from the mapping.
   - d. Choose a destination that does not perform the banned marketing action.
6. **The episode's practice question.** A client has labelled every sensitive field perfectly, yet a restricted field reached an ad partner last night. What two things do you check first?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- This track is **read-only**. Do not save a schema, do not enable or disable any policy, do not click **Activate** or **Publish**, and do not create a privacy request.
- Never enable a policy in a shared sandbox: it changes everyone's activations.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Open one of **your own** schemas (the one with your initials) and click the **Labels** tab. Read the **Label usage** dialog and write down the three consumers it names.
2. Read the label grid. Which of the five categories have any labels on your schema? Leave without saving.
3. Open **Privacy**, then **Policies**, then **Browse**, with **Governance policies** selected. For each policy, note its **Associated labels**, **Associated marketing actions** and **Policy status**. How many are enabled?
4. Open **Marketing actions** and list them. Which are Adobe's locked actions, and has your organisation created any of its own?
5. Open **Privacy**, then **Requests**, and read the list only.

## Check yourself

1. Labels versus policies: what does each do, and which one blocks?
2. Name the five label categories.
3. Name the three consumers of labels from the Label usage dialog.
4. Why can a perfectly labelled schema still let restricted data out?
5. Who should decide to enable a policy, and why?
6. What does a policy violation at activation name?
7. Why is a policy engine better than a process document that says the same thing?
8. What do access and delete requests reach, and why does tracking matter?

<details><summary>Check your answers</summary>

**Task 1: the governance sentence**
- A label says what a field **is** (a sticker on the field, for example C2 on the phone number).
- A marketing action says what you **want** to do (for example Export to Third Party).
- A policy says which label and marketing action combination is **banned**.

Only the **policy** blocks, and only when it is **enabled** and the destination **declares** the marketing action the policy names.

**Task 2: find the policy**
- a. **3rd party export restriction**, which pairs C2 with Export to Third Party.
- b. A label only describes the data. Nothing is enforced until a policy pairs that label with a marketing action and somebody enables the policy, and every shipped policy starts Disabled.
- c. **C11**, in Restrict Data Collaboration and Restrict data sharing. Enabling one does not enable the other, so C11 data is still free to go wherever the other policy's marketing action applies.

**Task 3: five questions, five owners (model answer)**

| Question | Owner at Bloom |
|---|---|
| Which fields carry contractual restrictions, and from which contract? | Legal (Tara), with the data engineer |
| Which marketing actions do we actually perform today? | The platform owner, with the CRM and journeys lead |
| Which policies do we therefore need enabled? | Legal signs; the platform owner enables |
| Who is allowed to enable or disable a policy? | Named in writing; Legal signs every change |
| What happens operationally when an activation is blocked? | A named triage owner, so campaigns do not silently stall |

Any sensible roles are fine. The point is a **name** beside every question, because a tenant-wide switch has no natural owner.

**Task 4: not deletion**
The CRM is one source among several. The data lake keeps the complete history of what was loaded, the profile store holds a merged profile built from several sources, and any file already sent to a partner still holds what you mapped. GDPR deletion is a tracked **delete request** through Privacy Service, which removes the person across the datasets and the profile store and leaves an audit trail.

**Task 5: fix it right**
- a. **Wrong.** It hides the truth about the data and weakens every future check.
- b. **Wrong.** A policy is tenant-wide, so disabling it removes the wall for every activation, not just this one.
- c. **Right.** Send the minimum the partner needs. Bloom's final mapping is hashed email and loyalty band only.
- d. **Right, if the use is genuinely allowed.** If the partner truly needs the field, that is a contract conversation with Legal, not a mapping change.

**Task 6: practice question**
First, is the policy that pairs that label with the partner's marketing action actually **enabled**? Shipped policies start Disabled. Second, does the destination **declare** that marketing action? A policy only acts on destinations that perform the action it names.

**Track B: what to expect**
The Label usage dialog names governance policies, consent policies and access policy. On a fresh schema the label grid is empty. In Policies, Browse, every Adobe-shipped governance policy reads Disabled unless someone in your organisation has enabled it. Adobe's shipped marketing actions are locked; any others in the list were created by people in your organisation with **Create marketing action**. Labels as of October 2026; check what your screen shows.

**Check yourself**
1. Labels describe what data is; policies ban a label and marketing action combination. The policy blocks, labels alone block nothing.
2. Identity, Sensitive, Contract, Partner ecosystem, Custom.
3. Governance policies, consent policies, access policy (attribute-based access control).
4. Because Adobe ships its policies Disabled. Until the right policy is enabled, nothing acts on the labels.
5. A named owner, usually Legal signing and the platform owner switching, because enabling a policy changes what everyone in the tenant can activate.
6. The field, the label and the policy.
7. A document depends on someone remembering it. The policy is checked automatically at activation, every time, for everyone, including future activations.
8. The datasets in the data lake and the profile store. Tracking lets you prove what was done if a regulator asks.

</details>
