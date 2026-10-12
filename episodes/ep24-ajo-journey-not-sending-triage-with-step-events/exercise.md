# Exercise 24: Break it, then explain it

You will triage a broken journey from its step events, match delivery questions to the datasets that answer them, write Bloom's ops readout from a send log, and set the team's naming, versioning and archiving rules.

All figures below are illustrative practice data, not Bloom results. Field names in the logs are simplified for reading; they are not Adobe's column names. The same logs and send log are in the repo's data folder as `bloom-ajo-welcome-practice-logs.csv` and `bloom-ajo-send-log.csv`.

## Track A: No Adobe access needed

### 1. Triage a broken journey

The real Bloom Welcome v1 works like this: people enter when they qualify into New This Month, an Optimize split sends Gold Members down one path and everyone else down Others, and each path sends its welcome email, then waits two days, then ends.

Divya has built a broken practice copy of it, named with your initials at the front, and run it once on four test seats, with each seat following its real path at the split. For this practice, assume Kavya's, Farhan's and Rohan's seats each placed a first order this month, so they qualify into New This Month. Only Kavya's seat is Gold, so only she is in Gold Members. Divya's seat is lapsed: her last order was more than 90 days ago.

The reported symptom: "Farhan, Rohan and Divya got no welcome email." You check the logs on Tuesday at 10:00 UTC.

**Step events (simplified)**

| # | Time (UTC) | Profile | Node | What happened |
|---|---|---|---|---|
| 1 | Mon 09:00 | TD-KAVYA-01 | Entry: audience qualification, New This Month | Entered |
| 2 | Mon 09:00 | TD-KAVYA-01 | Optimize | Took the Gold Members path |
| 3 | Mon 09:00 | TD-KAVYA-01 | Action: welcome email (Gold) | Executed |
| 4 | Mon 09:00 | TD-KAVYA-01 | Wait: 2 days | Started |
| 5 | Mon 09:02 | TD-FARHAN-02 | Entry: audience qualification, New This Month | Entered |
| 6 | Mon 09:02 | TD-FARHAN-02 | Optimize | Took the Others path |
| 7 | Mon 09:02 | TD-FARHAN-02 | Wait: 2 days | Started |
| 8 | Mon 09:04 | TD-ROHAN-04 | Entry: audience qualification, New This Month | Entered |
| 9 | Mon 09:04 | TD-ROHAN-04 | Optimize | Took the Others path |
| 10 | Mon 09:04 | TD-ROHAN-04 | Wait: 2 days | Started |

There are no rows for TD-DIVYA-03.

**Message feedback (simplified):** Mon 09:01, TD-KAVYA-01, welcome email (Gold), Sent.

**Email tracking (simplified):** Mon 09:30, TD-KAVYA-01, welcome email (Gold), Open.

Tasks:
1. For each of the four seats, walk the five steps (entry, qualification, wait, action, delivery) and write the step where its trail stops.
2. Decide, for each seat, whether you are looking at a fault or at the design working. Give one sentence of evidence for each.
3. The logs alone cannot prove the root cause for Farhan and Rohan. Say what you would open next, and what you expect to find.
4. Write the five-part incident note for the real fault: symptom, evidence trail, root cause, fix, prevention.

### 2. Match the question to the dataset

Write the AJO dataset that answers each question:

1. Who passed the wait node in Cart Rescue v1?
2. Did the Bloom Win-Back email to one address bounce?
3. Who clicked the Early Access link?
4. Who unsubscribed from the welcome email?
5. Did the push notification arrive, and did the customer open the app from it?
6. Which offer was decided for a customer in the Bloom Win-Back email?

### 3. Write the ops readout

This is an illustrative send log for the relaunch fortnight, read after the feedback had landed.

| Message | Sends | Delivered | Opens | Spam complaints | Unsubscribes |
|---|---|---|---|---|---|
| Bloom Welcome v1, Gold email | 40 | 40 | 28 | 0 | 0 |
| Bloom Welcome v1, everyone-else email | 360 | 354 | 210 | 1 | 2 |
| Cart Rescue v1 email | 200 | 196 | 112 | 0 | 1 |
| Bloom Win-Back | 1,400 | 1,340 | 380 | 6 | 22 |

Each row is no bigger than the audience that feeds it: the two welcome emails together stay within New This Month (about 480), Cart Rescue v1 within Cart Abandoners 24h (214), and Bloom Win-Back within Lapsed 90 (3,890).

The Journeys report also shows **Journey Failures: 3** for Cart Rescue v1, and **0** for Bloom Welcome v1.

Write Bloom's ops readout for Anjali in four lines: sends, delivery rate, opens, and the two numbers you would flag, one sentence each. State the period and the time zone.

### 4. Set the house rules

Write Bloom's convention for journeys and campaigns in five short lines:
1. A naming pattern, with two examples.
2. What happens when someone needs to change a live journey.
3. When to use Close to new entrances, and when to use Stop.
4. How a journey or practice copy is retired, and what gets recorded.
5. Who may change sandbox-wide settings such as business rules and the allowed list.

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- This track is **read-only**. Never click Activate, Publish, Send proof, Test mode, Stop or Close on any journey or campaign.
- Do not click **Schedule export** in the Share menu, and do not change any business rule or the allowed list.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Open **Journey Management**, then **Reports**. Note which data view the drop-down names.
2. Read the period. Confirm it says **Last 7 full days**, and write down the dates it covers. Remember that reporting runs in UTC.
3. In the **TABLE OF CONTENTS**, open **Highlights** and write down which of these you can see: Journey Engagement, Journey Enters, Journey Failures, CTR, CTOR, People, Clicks, Spam Complaints, Unsubscribes.
4. Open **Journeys** and find the **Journey Exclusions** section. Then open **Campaigns**. Change nothing.
5. If every journey in your sandbox is still a Draft, expect zeros. That is not a fault: no mail has gone out, so there is nothing to report.

## Check yourself

1. What are the five triage steps, in order?
2. Which dataset is the ground truth for whether a person reached a node?
3. Why can an empty Message Feedback result ten minutes after a send be misleading?
4. A trail ends at a wait that started yesterday. Is the journey broken?
5. A trail has no action row at all. Could the frequency cap have blocked the message?
6. What are the five parts of an incident note?
7. What is the default period on the Reports page, and which time zone does AJO reporting use?
8. What four lines go into an ops readout?
9. Why can you not edit a live journey in place?
10. What does the AJO ExD Decision Event Dataset hold, and why do we hedge when we say so?

<details><summary>Check your answers</summary>

**Task 1: triage**

| Seat | Where the trail stops | Fault or design? | Evidence |
|---|---|---|---|
| TD-KAVYA-01 | Delivery: sent and opened, now in the 2-day wait after the email | Design working | An action row, a Sent row in Message Feedback and an Open in Email Tracking |
| TD-FARHAN-02 | Wait: entered, took Others, wait started, no action row | **Fault** | On the Others path the wait comes before any action, so no welcome has been attempted |
| TD-ROHAN-04 | Wait: same as Farhan | **Fault** (same root cause) | Same trail as Farhan |
| TD-DIVYA-03 | Entry: no rows at all | Design working | Her seat is lapsed, so it never joins New This Month, the welcome's entry audience |

Next step for Farhan and Rohan: open the copy's canvas and look at the Others path. Expect to find the wait in front of the welcome email, or no email on that path at all. The logs told you exactly where to look.

Model incident note:
- **Symptom:** Farhan's and Rohan's seats entered the copy on Monday and had no welcome email by Tuesday, 10:00 UTC.
- **Evidence trail:** Both have an entry row, the Others path, and a 2-day wait started at 09:02 and 09:04, with no action row. Kavya's Gold seat, on the other path, has an action row, a send and an open.
- **Root cause (confirmed on the canvas):** On the Others path, the wait sits in front of the welcome email, so the email would go out two days late.
- **Fix:** Put the email action before the wait on the Others path. On a live journey this means a new version, because a live journey is read-only.
- **Prevention:** Before any journey goes live, someone other than the builder checks the order of steps on every path, and the team triages with step events before changing anything.

Divya's seat is not part of the incident: not entering a welcome journey for new customers is correct for a lapsed customer.

**Task 2: datasets**
1. Journey Step Events.
2. AJO Message Feedback Event Dataset (delivery events such as sends and bounces).
3. AJO Email Tracking Experience Event Dataset.
4. AJO Email Tracking Experience Event Dataset.
5. Two answers: whether it was sent or failed is a delivery event, so AJO Message Feedback; what the customer did with it, such as launching the app, is in AJO Push Tracking Experience Event Dataset. Accept either with that reason.
6. AJO ExD Decision Event Dataset, judging by its name.

**Task 3: model readout**
Period: the relaunch fortnight, all figures in UTC, illustrative.
- Sends: 2,000 across the welcome, Cart Rescue and Win-Back emails.
- Delivery rate: 1,930 delivered out of 2,000, 96.5 percent.
- Opens: 730, about 38 percent of delivered emails.
- Flag 1: Bloom Win-Back drew 6 of the fortnight's 7 spam complaints and delivered only about 95.7 percent; Divya reviews the audience and content before the next send, because one bad month can hurt the sending domain.
- Flag 2: Cart Rescue v1 shows 3 journey failures where we expect zero; Kavya will pull the step events for those profiles and write an incident note.

**Task 4: model house rules**
1. Naming: purpose plus version, for example "Bloom Welcome v1" and "Cart Rescue v1"; practice copies carry the owner's initials at the front, for example "KM - Bloom Welcome v1 practice".
2. A live journey is read-only, so a change means a new version with a written change note and a second person's check.
3. Close to new entrances when people already inside should finish; Stop only in an emergency, because it times everyone out.
4. Retire on purpose: close it, record why and what replaced it in the change log, and delete only once it is Finished.
5. Only the setting's owner, with a sign-off, because these settings affect every journey in the sandbox.

**Track B: what to expect**
The Reports page names an AJO Enabled Data View, the period reads Last 7 full days with dates, and the table of contents lists Highlights, Journeys (with Journey Exclusions) and Campaigns. In a sandbox where everything is still a Draft, the numbers read zero, which is correct.

**Check yourself**
1. Entry, qualification, wait, action, delivery.
2. Journey Step Events.
3. Message Feedback arrives in batches, up to 2 hours late.
4. Not necessarily. The person may simply be waiting; check whether an action came before the wait and whether the design meant it.
5. No. With no action row, no message was attempted, so there was nothing for a cap to stop.
6. Symptom, evidence trail, root cause, fix, prevention.
7. Last 7 full days; UTC.
8. Sends, delivery rate, opens, and two numbers to flag.
9. A live journey is read-only; you change it by creating a new version.
10. Decisioning events. The meaning is read from the dataset's name, so we say "judging by its name".

</details>
