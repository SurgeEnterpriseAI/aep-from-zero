# Exercise 08: Dallas or Austin?

You will decide which source should win for Bloom's key attributes, predict what a merge policy shows, and explain the profile to a marketer in plain words.

File: `bloom-customers-500.csv` from the repo's `/data` folder.

## Track A: No Adobe access needed

1. **Decide the winner, attribute by attribute.** Copy this table. For each attribute, choose **timestamp-ordered** (newest value wins) or **dataset precedence** (a ranked source wins), name the system that should own it, and write one line on why.

   | Attribute | Policy | Owning system | Why |
   |---|---|---|---|
   | Home address | | | |
   | Legal name | | | |
   | Email preference | | | |
   | Loyalty tier | | | |
   | Phone | | | |

2. **Dallas or Austin.** Priya's CRM record (2023) says Dallas. An update she made in the Bloom app (2026) says Austin.
   - What does her profile show under a timestamp-ordered policy?
   - What does it show under dataset precedence with the CRM dataset ranked first?
   - Write the one-sentence question you would ask Anjali to sign off, and say what the signed note must contain.
3. **Duplicates in the CRM sample.** Open `bloom-customers-500.csv` in a spreadsheet and sort it by the `email` column. Find one email address that appears on two (or more) rows with different values in the `city` column.
   - How many profiles will those two rows become, and why?
   - Predict what the profile's city shows under each policy. Is there anything a merge policy cannot settle here?
   - Now read the other columns on those two rows. What would you tell the CRM owner?
4. **Explain it to a marketer.** In three sentences, explain why a journey reads the profile and not the data lake.
5. **The episode's practice question.** Bloom ranks the CRM dataset first, and tomorrow Priya changes her city in the app again. Which city does her profile show, and who should have signed off on that choice?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- This track is read-only. Do not create, edit or save any merge policy, and never change which policy is the default.
- Nothing here needs **Activate**, **Publish** or any send. Do not click them.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Go to **Customer**, **Profiles**, then the **Union Schema** tab. Set **Class** to **XDM Individual Profile**.
2. Check that your own customer schema's objects are listed, for example `personalEmail`, `person`, `homeAddress` and `mobilePhone`. Write down what you found.
3. Go to the **Merge Policies** tab. Find **Default Timebased** and note whether it says Default merge policy: Yes.
4. Open it and read each wizard step: **Configure**, **Select Profile datasets**, **Select ExperienceEvent datasets**, **Review**. On Configure, write down the **ID stitching** value, the **Default merge policy** toggle and the **Active-On-Edge Merge Policy** setting.
5. Close the editor **without saving any change**.

## Check yourself

1. What is the Real-Time Customer Profile, in one sentence?
2. Why do journeys and audiences read the profile instead of the raw datasets?
3. Which screen is the cheapest proof that a schema contributes to Profile, and what do you look for?
4. Two CRM rows share one email. How many profiles result, and what decides the values?
5. What does ID stitching set to None decide, and what does Private graph decide?
6. What is the Default merge policy toggle for, and why should you never edit the default in a shared sandbox?
7. Why is a merge policy a business decision and not a technical default?
8. What is a pseudonymous profile, and how should you treat it?

<details><summary>Check your answers</summary>

**Task 1: one reasonable set of answers**

There is no single right table. The reasoning and the named owner matter more than the choice.

| Attribute | Policy | Owning system | Why |
|---|---|---|---|
| Home address | A business call: dataset precedence with the CRM first, or timestamp-ordered if the customer's own update should win | Decided and signed by Anjali | It sits on the border between "newest is truest" and "one system is the authority" |
| Legal name | Dataset precedence, billing or CRM ranked first | Billing or CRM | One system owns it with authority; a newer stray value must not overwrite it |
| Email preference | Timestamp-ordered | Wherever the customer last chose: the app or the email tool | Preferences change, and the newest choice is the truest |
| Loyalty tier | Dataset precedence, CRM ranked first | CRM (it holds the loyalty programme's records) | Tier follows points in the loyalty programme; a stray value from another system must not overwrite it |
| Phone | Usually timestamp-ordered | Whichever system customers update it in | The number the customer most recently gave is usually the right one |

If your answers differ by attribute, that is a sign you may need more than one merge policy for different uses (a sandbox holds at most five). That is a conversation for the owner, not the engineer.

**Task 2: Dallas or Austin**
- Timestamp-ordered: **Austin**, because the 2026 update is the most recent value, provided it was also ingested after the CRM record.
- Dataset precedence with the CRM ranked first: **Dallas**, whatever the date.
- A sample question: "When the CRM and the app disagree about a customer's home address, which one do we trust?" The signed note names the attribute, the competing sources, the chosen policy, the reason, the owner and the date.

**Task 3: duplicates**
- One profile. Both rows carry the same email, Email is the primary identity, and records that share an identity value belong to one person.
- The profile still shows one city, and the merge policy still decides it, but it cannot decide it well. Under timestamp-ordered, the most recently ingested value wins, and both rows arrive in the same file, so the file alone cannot tell you which city that will be. Dataset precedence ranks whole **datasets**, so it has nothing to rank between two rows of the **same** dataset. This conflict has to be fixed at the source.
- In the course sample, the rows that share an email also carry different first names, last names and BloomIDs. They are probably different people sharing one email address, so collapsing them into one profile would be an over-link, the guardrail from episode 7. Send the rows back to the CRM owner with that evidence.

**Task 4: a sample answer**
The data lake keeps every row that ever arrived, so it holds both the Dallas row and the Austin row. The profile merges those rows into one current person, and the merge policy decides which value it shows. A journey has milliseconds to decide what to send, so it reads that one current answer instead of re-joining raw datasets.

**Task 5: practice question**
**Dallas.** With the CRM dataset ranked first, the CRM value wins however recent the app update is. A named business owner, Anjali for Bloom's home address, should have signed off on that choice in writing.

**Track B: what to expect**
Your customer schema's objects should appear in the union schema for XDM Individual Profile; if they do not, your schema never reached Profile. Default Timebased should say Default merge policy: Yes, with ID stitching set to Private graph in Bloom's build. Your screen may differ, and you saved nothing.

**Check yourself**
1. One merged, current view of a person: the union of every attribute and event known about them.
2. It answers "who is this person right now?" instantly, without re-joining raw data, and every journey inherits its correctness.
3. Profiles, Union Schema, with the class set. Look for your schema's objects in the union.
4. One profile. The merge policy decides which values it shows where the rows disagree. If the rows carry different names, check for an over-link first.
5. None assembles the profile from a single identity. Private graph assembles it across the whole identity graph.
6. It decides which policy is used when nobody names one. Editing the default changes what everyone else sees.
7. The same data gives different answers under different policies, and only the business can say which source should win. Someone must own that, in writing.
8. An anonymous, ECID-only profile not yet stitched to a known identity. Treat it as anonymous for privacy, and do not let such profiles pile up.

</details>
