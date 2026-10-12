# Exercise 07: Stitch Priya together

You will follow shared identities to turn Priya's fragments into one person, break the graph on purpose, check the sample data for an over-link, and (optionally) model stitching in Graph Simulation.

Files: `bloom-identities-200.csv` from the repo's `/data` folder. Paper and a pen are enough for everything else.

These are the seven records in Bloom's sandbox for this exercise. F1 to F4 come from Priya's evening of 18 August; F5 is her CRM record from 2023.

| # | Record | Identities it carries |
|---|---|---|
| F1 | Web event: product view in the app | ECID `38472919862011456743` |
| F2 | Web event: add to cart, 7:44 PM | ECID `38472919862011456743` |
| F3 | App sign-in | ECID `38472919862011456743` and Email `priya.sharma@example.com` |
| F4 | Order `BLM-88412`, 7:52 PM | Email `priya.sharma@example.com` and BloomID `BLM-CUST-004217` |
| F5 | CRM loyalty record | Email `priya.sharma@example.com` |
| D1 | Web event: product view | ECID beginning `9021` |
| D2 | Order from another customer, Arjun Patel | Email `arjun.patel@example.com` and his own BloomID |

## Track A: No Adobe access needed

1. **Stitch Priya.** List which of the seven records belong to Priya. Then draw her graph: one dot for each identity value, and one line for each record that carries two values together. Label each line with the record that drew it.
2. **Find the linking event.** Which single record links her anonymous device to her known identity, and what makes it special?
3. **Break it on purpose.** Remove F3 and redraw. What happens to F1 and F2? What does Bloom now believe about Priya's evening?
4. **Look for an over-link.** Open `bloom-identities-200.csv`. Each row links an ECID, an email and a BloomID that were seen together.
   - Pick five customers and trace their links on paper, as dots and lines.
   - Then check the whole file for the pattern a shared family tablet creates. Hint: sort or filter by the `ecid` column and look for one ECID value that appears with two different email addresses. Write down whether your copy of the file has one.
   - Whether or not you find one, write down what the platform would do with such rows, and describe one guard you would apply.
5. **Primary identity.** In one sentence, explain why email beats ECID as the primary identity.
6. **The episode's practice question.** Say, for example, Priya's sign-in had carried only her email and no ECID. Which of her five records would still be one person?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- Graph Simulation ingests nothing, so this track is read-only. Do not create namespaces, upload files or change any setting.
- Nothing here needs **Activate**, **Publish** or any send. Do not click them.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Open **Identities**, then the **Graph Simulation** tab.
2. Click **Add activity**. Row 1: namespace **Email**, value `priya.sharma@example.com`. Click **+**, then Row 2: namespace **ECID**, value `38472919862011456743`. Check both rows, then **Save**.
3. Add a second activity: **Email** `priya.sharma@example.com` and **ECID** `99887766554433221100`. Check both rows, then **Save**.
4. Scroll down and click **Simulate**. Confirm **three nodes and two edges**.
5. Open the namespace dropdown once more and read the list without choosing anything (a click can overwrite a row). Look for BloomID and write down what you find.
6. Predict, then test, the family tablet: start from an empty simulation (if your earlier activities are still listed, try reloading the page) and enter two new activities that share one ECID, each with a different `@example.com` email (for example `relative.one@example.com` and `relative.two@example.com`). For the ECID, type any made-up value of your own, the same in both activities. Draw your prediction before you click **Simulate**, then compare it with the screen.

## Check yourself

1. In one sentence, when does the platform treat two records as the same person?
2. F1 carries only an ECID. How can it possibly be Priya?
3. A web event with ECID `9021…` appears the same evening. Is it Priya? How do you know?
4. What is a linking event, and what are the most common real-world examples?
5. Why can Graph Simulation not model Bloom's order, which links an email to a BloomID?
6. Give one way identity stitching can go wrong, and how you would guard against it.
7. Why does Priya's CRM record (F5) carry only one identity, and how does her BloomID still join her graph?

<details><summary>Check your answers</summary>

**Task 1: Priya's records**
F1, F2, F3, F4 and F5 are Priya. D1 and D2 are not. Her graph has three dots and two lines:

```
ECID 3847...  --(F3, the sign-in)--  Email priya.sharma@example.com  --(F4, the order)--  BloomID BLM-CUST-004217
```

F1 and F2 sit on the ECID dot, and F5 sits on the email dot. One connected graph is one person.

**Task 2: the linking event**
F3, the app sign-in. It is the only record that carries the anonymous ECID and a known identity (her email) at the same time, so it binds the device to the person. Without it, nothing connects the phone events to the order or the CRM record.

**Task 3: remove F3**
The graph splits in two. F1 and F2 float away as an anonymous device with no owner, a pseudonymous ECID-only profile. F4 and F5 still join through the email. Bloom now sees an anonymous stranger who abandoned a cart, and a known customer whose purchase has no browsing behind it.

**Task 4: the over-link**
The over-link pattern is one ECID that appears on two rows with two different email addresses, as when two relatives each sign in on the same family tablet. The sample file has one, planted at the end: ECID `61833074552910846205` appears with `ella.davis121@example.com` (BloomID `BLM-CUST-000121`) and with `olivia.davis144@example.com` (BloomID `BLM-CUST-000144`), two relatives in Dallas. Because the tablet's ECID is shared by both rows, the two emails chain together (with each relative's own device row as well), and the platform would treat two people as one. Rows where one email appears with several ECIDs are expected: that is one person on several devices or browsers. If those rows also carry different BloomIDs, look closer: different customer numbers on one email can be duplicate records, or different people sharing one address. The shared email joins them into one graph either way; episode 8 checks the customer file and treats the second case as an over-link.
Good guards: watch login patterns and review any device seen with more than one person's sign-in before trusting it; limit how aggressively one device can link people; keep test and support logins out of customer data.

**Task 5: primary identity**
Devices are shared and recycled, and an ECID belongs to a browser or app install, while an email address belongs to one person, so email gives a stable, trustworthy key.

**Task 6: practice question**
F3, F4 and F5 would still be one person, because they share her email. F1 and F2 would stay anonymous, because no record would carry their ECID together with a known identity.

**Track B: what to expect**
Step 4: one Email node in the middle joined to two ECID nodes, with the edges numbered 1 and 2 for the activities that created them. If you see disconnected nodes, your two email values were not identical.
Step 5: BloomID is not in the list. Graph Simulation offers only the 16 standard namespaces, so custom namespaces cannot be simulated.
Step 6: by the stitching rule you would predict one ECID node joined to two Email nodes, so two people merged into one graph. This step was not part of Bloom's build, so treat your drawing as a prediction and check what your screen shows. The graph's legend also has a **Removed link** marker, used when a rule in the simulator breaks an edge; this episode does not cover those rules, so if you see one, note it and compare with your prediction.

**Check yourself**
1. When they share an identity value, directly or through a chain of shared identities.
2. F3, the sign-in, carries that same ECID together with her email, so F1 joins her graph through F3.
3. No. ECID `9021…` shares no identity with Priya's records (her app's ECID begins `3847`), and no record links `9021…` to her.
4. One record carrying an anonymous ID and a known ID together. Usually a sign-in, a login or a form submission.
5. Its namespace list offers only the 16 standard namespaces, and BloomID is a custom namespace.
6. A shared family tablet can over-link two people into one; review devices seen with more than one person's sign-in. Or a test or support login used by everyone can balloon one graph; find it and keep it out.
7. Bloom Customer Profile declares one identity, Email, so `bloom_id` landed as a plain attribute. Her BloomID becomes an identity through F4, the order, which carries both her email and her BloomID, so the chain still closes.

</details>
