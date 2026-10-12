# Exercise 36: Present Bloom in seven minutes

You will write a seven-minute walkthrough told through Priya, fill the 12-point capstone checklist for what you have built, prepare a failure path, answer the three questions you fear, fix three weak numbers, and score yourself and two friends against the Demo Day rubric.

**Ground rules:** the Bloom data is fictional, but practise the real habits. Use only `@example.com` addresses in anything you write. Never paste customer data into any tool that has not been cleared for it.

## Track A: No Adobe access needed

1. **Your seven-minute script.** Write a walkthrough through Priya in six beats: anonymous visit, stitched identity, audiences, journey, measurement, and the change Bloom made. For each beat write:
   - two or three spoken sentences
   - **one artefact** the panel would see (a profile, an audience rule, a journey's step events, a report)
   - a time budget, so the whole talk fits the arc: problem about 1 minute, architecture about 1, walkthrough about 3, numbers about 1, AI layer about 1

   Then write a **five-minute spine** version: the problem in one sentence, four beats (identity, audience, journey, measurement), one number, one thing you would do differently.
2. **Fill the 12-point checklist.** Copy this table for the parts of Bloom you have built in these exercises (paper, JSON, CSV or SQL all count). Mark each point **green** (evidence attached), **amber** (a written caveat) or **red** (fix it), and name the evidence.

   | # | Point | My evidence | Colour | Caveat or fix |
   |---|---|---|---|---|
   | 1 | Schemas | | | |
   | 2 | Ingestion | | | |
   | 3 | Identity | | | |
   | 4 | Audiences | | | |
   | 5 | Activation | | | |
   | 6 | Welcome journey | | | |
   | 7 | Cart rescue | | | |
   | 8 | Decisioning | | | |
   | 9 | Guardrails | | | |
   | 10 | Data view | | | |
   | 11 | Closed loop | | | |
   | 12 | AI evidence | | | |

3. **The failure path.** List, in order, every screenshot you would need if the live system froze during your seven minutes. Number them so they match your script.
4. **The three questions you fear.** Write the three questions you least want to be asked about your build. For each, write the honest answer, the **trade-off** you made and why, and what you would do differently. Then write one question you could not answer, and an answer that starts "I don't know, but here is how I would find out" and names the method.
5. **Fix three weak numbers.** Rewrite each claim so it has a **window**, a **model** (where credit is involved) and a **baseline**, or an honest caveat:
   - a. "Cart Rescue made money."
   - b. "Email is our best channel."
   - c. "Gold customers spend more because they are Gold."

   Use only Bloom's figures: relaunch fortnight 1,240 orders and $66,260; 520 orders No value; email 180 orders once "email" (150) and "Email" (30) were merged; average order Gold $78, Silver $55, Bronze $38; Cart Rescue recovery 11.8% against a 10% holdout at 7.9%.
6. **Record and score.** Record yourself giving the seven-minute walkthrough on your phone, and swap recordings with two friends. Score all three against the 100-point rubric (architecture story 20, live walkthrough 30, business value 20, panel questions 20, clarity and time 10). Write **one strength and one improvement** for each.
7. **The episode's practice question.** Present Cart Rescue's 11.8 percent recovery in two sentences, with its baseline, its window and its honest caveat.

## Track B: If you have a development sandbox (optional, read-only)

Safety first:
- Practise only in a **development** sandbox, on objects that carry **your own initials**.
- Never click **Activate**, **Publish** or **Send proof**. Type only your own email address anywhere.
- Do not start a **Dry run** in a shared sandbox: it holds one of the sandbox's active-journey slots and needs publish rights. Read existing counts, or ask the owner.
- In shared environments: look, screenshot, leave.

Steps:
1. In **Schemas**, **Browse**, screenshot the **Enabled for Profile** column for your own schemas.
2. In **Monitoring**, **Batch end-to-end**, clear the "ONLY INGEST FAILURES: Yes" filter and screenshot **Records in Profile** for your own dataset.
3. Look up **your own test profile** (never a real customer) and screenshot its identities.
4. Open your own draft journey and screenshot the canvas and the **Alerts** panel. Do not publish it.
5. Put the screenshots in one folder, numbered in the order of your script from Task 1. Time how long it takes you to reach any one of them: the target is two clicks.

## Check yourself

1. What do green, amber and red mean on the capstone checklist?
2. Why can Test mode not prove a split, and what does?
3. Name the five parts of the seven-minute arc.
4. What one rule sits above the arc?
5. Name Priya's six beats.
6. List four parts of demo hygiene.
7. What three things must every number carry?
8. Why did Kavya call the 11.8% recovery soft, and when did she say so?
9. What are the five rubric criteria and their points?
10. Why do peers score each other, and what must each score include?

<details><summary>Check your answers</summary>

**Task 1: a model script outline (seven minutes)**

| Time | Part | What you say | Artefact |
|---|---|---|---|
| 0:00 | Problem | Bloom could not tell whether yesterday's buyer was last week's complainer | One sentence, no slide needed |
| 1:00 | Architecture | AEP the memory, AJO the voice, CJA the eyes, AI the colleague | One simple picture |
| 2:00 | Beat 1 | 7:44 PM, a phone adds a Vitamin C Serum to a cart, ECID only | The web event |
| 2:30 | Beat 2 | Sign-in links ECID and email; 7:52 PM laptop order | One profile, three identities |
| 3:00 | Beat 3 | Gold tier puts her in Gold Members; Cart Abandoners leaves her out | The two rules |
| 3:40 | Beat 4 | The abandon event takes her into Cart Rescue v1 at 7:44; her 7:52 purchase lets her exit | Her journey step events |
| 4:15 | Beat 5 | CJA with stitching: one person, no false abandon | Bloom 360 / Bloom Marketing |
| 4:40 | Beat 6 | Non-Gold mobile shoppers leaked; Checkout Rescue now helps them | The published audience and journey |
| 5:00 | Numbers | 1,240 orders (a count); 11.8% vs 7.9% holdout, soft | The scorecard tiles |
| 6:00 | AI layer | Evidence sheet, golden set at least 8 of 10, agent that stops for approval | The evidence sheet |

Five-minute spine: "Bloom could not answer who its customer was. We built identity, audiences, journeys and measurement around one customer, Priya. Cart Rescue recovered 11.8% against a 7.9% holdout, which is soft after two weeks. Next time, I would settle the identity design for every customer number on day one."

**Task 2: a model checklist for the full Bloom build**
Points 1 to 4 and 6 to 12 can be green once each has evidence (a schema screenshot, the Records in Profile column, Priya's profile, the Lapsed 90 rule, Dry run path counts, the journey properties, approved offers, the rule set, the data view, the published audience, the evidence sheet). Point 5, activation, is honestly **amber** unless you can show a delivered file: the mapping (hashed email and loyalty band only) is evidence of design, not of delivery. Point 6 is **red** if your only evidence is Test mode.

**Task 3: a model failure path**
1. The architecture picture. 2. Priya's anonymous web event. 3. The linking event. 4. Her profile with three identities. 5. The Gold Members and Cart Abandoners rules. 6. Cart Rescue v1 and her journey step events. 7. Her stitched person in CJA. 8. The fallout from journey entries to purchases. 9. Checkout Leakers - Mobile and the Checkout Rescue canvas. 10. The scorecard tiles with baselines. 11. The AI evidence sheet and golden-set result. 12. The agent's run log with the guardrail trip.

**Task 4: model feared questions**
- "Can you look up any customer by BloomID?" Not yet, only customers who have ordered; the customer file's BloomID landed in a plain field, and BloomID becomes an identity through the order event. Trade-off: in week one we kept the customer schema to one identity, Email, and did not reopen it before the relaunch. Differently: settle identity design for every customer number on day one, before any data lands.
- "Why are 520 orders No value?" They carry no channel: a tracking gap, not a channel, so channel rankings wait until tracking is fixed. Differently: check channel tracking before launch.
- "Did you prove the welcome journey's Others path?" Not with Test mode, which took the top branch; with Dry run path counts before relaunch.
- "I don't know" model: "How fast does a new customer reach the profile store?" "I don't know, but here is how I would find out: Adobe publishes no time for batch data to reach Profile, so I would time our own batches in Monitoring."

**Task 5: model rewrites**
- a. "Over the relaunch fortnight, shoppers who got Cart Rescue v1 recovered at 11.8%, against 7.9% for a random 10% holdout who got nothing. That is two weeks of data, so it is soft."
- b. "Over the relaunch fortnight, under Last Touch with a 30-day lookback, email had 180 orders once 'email' and 'Email' were merged. But 520 of 1,240 orders have no channel, so no ranking yet."
- c. "Over the relaunch fortnight, Gold orders averaged $78, against $55 for Silver and $38 for Bronze. That is an association: a third factor, such as how long people have been customers, could explain it, and only a test would prove cause."

**Task 7: practice question (model answer)**
"Over the relaunch fortnight, shoppers who received Cart Rescue v1 recovered at 11.8 percent, against 7.9 percent for a random ten percent holdout who received nothing. The gap is promising but soft, because it rests on two weeks of data, so we are keeping the holdout running."

**Check yourself**
1. Green: evidence attached. Amber: a written caveat. Red: fix it today.
2. In our testing, Test mode always took the top branch of a split. Dry run proves the paths by counting real profiles on each, contacting nobody.
3. Problem, architecture, walkthrough, numbers, AI layer.
4. Tell it through a person, not a box diagram.
5. Anonymous visit, stitched identity, audiences, journey, measurement, the change Bloom made.
6. Stable test profiles staged, a ready event payload aimed at your own seat, screens loaded, screenshots of every screen two clicks away (also: rehearse at presenting time, never click Activate, Publish or Send proof).
7. A window, a model (where credit is involved) and a baseline.
8. It rests on two weeks of data. She wrote "soft" on her slide herself, before the panel could say it.
9. Architecture story 20, live walkthrough 30, business value 20, panel questions 20, clarity and time 10.
10. Judging a build is also a job skill. Each score includes one written strength and one improvement.

</details>
