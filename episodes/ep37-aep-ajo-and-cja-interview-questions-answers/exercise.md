# Exercise 37: Your mock interview

You will answer five interview questions out loud in the claim, example, trade-off, verification pattern, write five resume bullets that each point to an artefact, time a 90-second architecture story of Bloom, write one war story of your own, and choose what to study next.

**Ground rules:** answer from what you have actually built or checked in these exercises. If a result is something you only read about, say so. Never paste real customer data into any tool.

## Track A: No Adobe access needed

1. **Five recorded answers.** Pick five questions from the interview bank below: two AEP, one AJO, one CJA and one AI. Record yourself answering each in four parts: **claim, example, trade-off, verification**. Time each answer and aim for about one minute. Play them back and mark any part you skipped.

   | Area | Interview bank |
   |---|---|
   | AEP | 1. What is the difference between AEP and Real-Time CDP? 2. Why are orders events and loyalty tier profile? 3. Walk me through your identity design. 4. Tell me about an ingestion failure. 5. Everything is green but the profile is empty: what do you do? 6. Two sources disagree about a customer's city: which wins? 7. Batch or streaming for an audience? 8. How is consent enforced? |
   | AJO | 9. Journeys versus campaigns versus decisioning? 10. Which test options can reach a real inbox? 11. Tell me about a journey that failed. 12. How do you cap messages across every journey? |
   | CJA | 13. CJA versus Adobe Analytics? 14. Why does the person ID matter? 15. Which channel earned the revenue? 16. What does closing the loop mean? |
   | AI | 17. How do you govern AI-assisted work? 18. Where does RAG fail? 19. Where does an agent's autonomy stop? |

2. **Five resume bullets.** Write five bullets, each tied to an artefact from your own exercises in this series (a schema design table, an error log, an audience estimate sheet, a journey drawing, a Workspace table, an evidence sheet). Use the shape: **strong verb + what you built + a number or named object + the artefact**. Put them under a heading such as "Practice project: Bloom (fictional brand)", never as client work, and use verbs that match what you really did (designed on paper is not launched). Delete any bullet you could not show on request.
3. **Your 90-second architecture story.** Write Bloom's story in this order: the problem in one sentence; four beats through Priya (identity, audience, journey, measurement); one number with its baseline; one thing you would do differently. Read it aloud with a timer, then cut until it fits 90 seconds.
4. **One war story of your own.** Choose something that broke in your own practice during this series. Write it in five lines: **symptom, layer, evidence, fix, prevention**. Add one sentence on how you proved the fix.
5. **What next.** List three topics you will study next, and one reason for each. The course did not cover advanced Data Distiller, the B2B edition, CJA administration at enterprise scale, or Adobe Experience Manager (AEM).
6. **The episode's practice question.** Answer aloud, timed: "Walk me through your identity design."

## Track B: If you have a development sandbox (optional)

Safety first:
- Practise only in a **development** sandbox, on objects that carry **your own initials**.
- Never click **Activate**, **Publish** or **Send proof**. Never enable a governance policy or turn on Profile for a schema that is not yours.
- Never paste customer data into any tool. In shared environments: look, screenshot, leave.

Steps (read-only: build an evidence folder for your resume bullets):
1. In **Schemas, Browse**, screenshot the **Enabled for Profile** column for your own schemas.
2. In **Monitoring, Batch end-to-end**, clear the **ONLY INGEST FAILURES** filter and screenshot one of your own batches, including **Records in Profile**.
3. Open one of your own audiences and screenshot **Audience properties**: the estimate, its **Last updated** time and the **Evaluation method**. Close without saving.
4. Open one of your own draft journeys and screenshot its **Alerts**. Do not publish it, and do not start a Dry run on a shared journey.
5. In Customer Journey Analytics, open your own connection and screenshot the person ID per dataset and **Records skipped**.
6. Date every screenshot and write which resume bullet it supports. Labels as of October 2026; check what your own screen shows.

## Check yourself

1. What are the four parts of the answer pattern?
2. What are technical panels really marking?
3. What is the one-sentence answer to "AEP or Real-Time CDP?"
4. Which test options can reach a real inbox, and which never does?
5. Name the five steps of journey triage, in order.
6. Which three words describe CJA against Adobe Analytics?
7. What makes a number defensible?
8. What are the five lines of a war story, as taught here?
9. What makes a resume bullet evidence-backed?
10. What do you say when you do not know, and what must follow it?

<details><summary>Check your answers</summary>

**Task 1: model answers for five bank questions**

*3. Walk me through your identity design.*
- **Claim:** Identity stitching turns anonymous traffic into known customers at the moment they authenticate.
- **Example:** Bloom uses three namespaces: Email (the customer profile schema's primary identity), ECID for browser and app installs, and a custom BloomID namespace of type Individual cross-device ID. Priya's 7:44 PM add-to-cart carried only an ECID; her app sign-in carried the ECID and her email together; her 7:52 PM laptop order carried her email and BloomID. One profile, three identities.
- **Trade-off:** BloomID became an identity only through orders, because the customer file put it in a plain field, so a customer who never ordered cannot yet be found by it. The risk to name: links chain, so a shared family tablet can merge two relatives. Namespace types can never be changed, so they were chosen on paper first.
- **Verification:** looked up by email, then by BloomID, the same person returned with three identities.

*4. Tell me about an ingestion failure.*
- **Claim:** 14 of 14 mapped is not 14 of 14 correct, and partial ingestion is not "ignore errors": it sets the blast radius.
- **Example:** Bloom's 500-row order trial ingested 0 rows. Three rejected rows and seven logged errors threw away 497 good orders, because partial ingestion is off by default. With it on at a 5% threshold, 497 rows loaded.
- **Trade-off:** the threshold is a business decision: sensible for a marketing file, far too loose for a finance file. Someone must own it.
- **Verification:** the dataset row count (500 minus 497 = 3 rows rejected), because "Records failed" counts error instances, not rows.

*9. Journeys versus campaigns versus decisioning?*
- **Claim:** A campaign answers what do we send. A journey answers what happens to this customer next. Decisioning chooses the offer inside the message.
- **Example:** Bloom Gold Thank-You is a scheduled campaign; Bloom Welcome v1 and Cart Rescue v1 are journeys; Bloom Win-Back's email chooses between the 20% Comeback, the Early Access Drop and the Free Shipping fallback.
- **Trade-off:** one decision policy replaces many hard-coded versions, but only approved items are served, so someone owns approval.
- **Verification:** the welcome split was proven with Dry run path counts, because Test mode only ever took the top branch.

*13. CJA versus Adobe Analytics?*
- **Claim:** CJA is person-based, dataset-based and retroactive.
- **Example:** a phone visit and a laptop order become one person on the email; the Journey Optimizer datasets sit beside orders and profiles in Bloom 360; a Lowercase derived field merged "email" (150) and "Email" (30) into 180, for past data too.
- **Trade-off:** existing segments and calculated metrics must be rebuilt; Activity Map and Contribution analysis are not supported; alerts are daily, weekly or monthly, not hourly.
- **Verification:** the person ID matches on every dataset and is case sensitive, so emails are lower-cased before they land.

*17. How do you govern AI-assisted work?*
- **Claim:** AI may draft. A human approves, and the approver is accountable.
- **Example:** Bloom's AI evidence sheet logs prompt, output, verdict and correction for every answer checked; two of five generated subject lines were kept, with written reasons for rejecting three.
- **Trade-off:** checking is slower, but it catches the confident wrong answers before a customer or the board sees them.
- **Verification:** each answer was scored against a truth written down before asking.

**Short claims for the rest of the bank:** (1) Real-Time CDP is the commercial name for AEP's profile, audience and activation capabilities. (2) Orders never change; tier changes in place. (5) The lake received it, the identity graph received it, the profile store did not; here is the row. (6) The merge policy is a business decision with a named owner. (7) Will a journey need to react within minutes? If yes, streaming. If not, batch. (8) Consent is a profile attribute enforced by the platform, not a process document enforced by goodwill. (10) Test mode, Simulation and Send proof; Dry run never does. (11) Read the step events in order: entry, qualification, wait, action, delivery. (12) Frequency capping applied per journey is not frequency capping. (14) A connection with the wrong person ID produces confident, wrong numbers. (15) Attribution models are assumptions, not truths; name the model and the window. (16) Closing the loop means the next campaign changes. (18) Fluent but wrong almost always means the right source never reached the model. (19) Put the human approval where the action is irreversible.

**Task 2: model resume bullets** (for a portfolio section headed "Practice project: Bloom, a fictional brand")
1. Designed a three-schema XDM customer data model (profile, web event, order event) with Email, ECID and a custom cross-device ID, and stitched one customer's phone, app and laptop activity into one profile. *Artefact: schema design table and identity walk-through.*
2. Diagnosed a batch that ingested 0 of 500 rows (3 rows rejected, 7 errors logged), recovered 497 rows with partial ingestion at a 5% threshold, and named an owner for the threshold. *Artefact: error log and threshold note.*
3. Built five rule-based audiences with consent inside the rule, two designed as streaming, and caught a 9,930-of-10,000 estimate before activation. *Artefact: audience estimate sheet.*
4. Designed a welcome journey and a cart-recovery journey with exit on purchase, a 10% holdout from day one, and a test plan that proves splits with Dry run path counts. *Artefact: journey drawings and test plan.*
5. Answered five business questions in CJA on one person ID, found a mobile checkout leak with fallout, and turned it into an audience for a helpful journey. *Artefact: Workspace tables and loop drawing.*

**Task 3: model 90-second story (about 220 words)**
"Bloom, a wellness brand, had 1.2 million customers in three systems that did not talk, so nobody could say who the customer was, and everyone got the same 20% discount twice a week. We built one customer profile in Adobe Experience Platform. Take Priya. At 7:44 PM she added a serum to her cart on an anonymous phone. Her app sign-in linked that phone's ECID to her email, and her 7:52 PM laptop order linked the email to her BloomID: one person, three identities. Then audiences: five living rules, with consent inside the rule, so a customer who never consented can never reach the win-back file. Then journeys in Journey Optimizer: a welcome that fires when someone joins New This Month instead of on a Tuesday batch, and Cart Rescue, which waits four hours and lets buyers like Priya exit. Then measurement in Customer Journey Analytics, on one person ID: 1,240 orders in the relaunch fortnight, and Cart Rescue recovered 11.8% against 7.9% for a 10% holdout. That is soft, two weeks of data. Fallout then showed a leak at mobile checkout, which we sent back as an audience for a helpful journey. What I would do differently: settle the identity design for every customer number on day one, because BloomID became an identity only through orders."

**Task 4: a model war story (the shape to copy)**
- **Symptom:** my test seat entered a welcome journey and no email arrived.
- **Layer:** the journey, not delivery or the cap.
- **Evidence:** step events showed entry, the Gold Members path and the wait, then no action row.
- **Fix:** restored the missing email action; a second run showed an action row, a send and an open.
- **Prevention:** before go-live, someone other than the builder checks that every path carries its message.

**Task 5: sample topics and reasons**
- Advanced Data Distiller: deeper SQL work on the data lake, beyond the Query Service basics in episode 15.
- The B2B edition: for companies that sell to other businesses, where the customer is often a company rather than one person.
- CJA administration at enterprise scale: many connections, permissions and governance across teams.
- Adobe Experience Manager (AEM): the content and website side of the same family.

**Task 6: practice question**
Use the model answer to question 3 above, in under a minute.

**Track B: what to expect**
Your screens may differ by licence and release. Record what you see, with the date. If any screenshot contradicts a resume bullet, change the bullet.

**Check yourself**
1. Claim, example, trade-off, verification.
2. Judgement: is the business better off, can you defend your decisions, would you be safe in front of a client.
3. Real-Time CDP is not separate software; it is the commercial name for AEP's profile, audience and activation capabilities.
4. Test mode, Simulation and Send proof can; Dry run never does.
5. Entry, qualification, wait, action, delivery.
6. Person-based, dataset-based, retroactive.
7. You can state its model, window and source, and its baseline, and you say so if it is soft.
8. Symptom, layer, evidence, fix, prevention.
9. A strong verb, what you built, a number or named object, and an artefact someone could ask to see.
10. "I don't know, but here is how I would find out", followed by exactly how: the documentation, a sandbox test, and the owner you would ask.

</details>
