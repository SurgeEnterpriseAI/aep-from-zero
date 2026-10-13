# Episode 24: AJO Journey Not Sending? Triage With Step Events

**Watch:** [Watch episode 24 on YouTube](https://youtu.be/WF6rkwBKP9g)

[Previous](../ep23-ajo-frequency-capping-quiet-hours-suppression/) · [Next](../ep25-customer-journey-analytics-tutorial-person-id/)

## What you will learn

- Triage "the journey did not send" in a fixed order: **entry, qualification, wait, action, delivery**
- Use **Journey Step Events** as the ground truth, and name the Adobe Journey Optimizer (AJO) dataset that answers each delivery question
- Read **Journey Management, Reports**: Highlights, Journeys, Campaigns, the default period and UTC
- Write an **ops readout** (sends, delivery rate, opens, two numbers to flag) and a **five-part incident note**
- Keep a shared organisation tidy with **naming, versioning, archiving and change discipline**

## The story so far

Bloom, a direct-to-consumer wellness brand, is two weeks into its loyalty relaunch, with Bloom Welcome v1, Cart Rescue v1 and Bloom Win-Back live. In episode 23 Divya's guardrails held: two marketing emails per profile per week wherever a marketing message goes, quiet hours in each customer's time zone, and a clean line between suppression and unsubscribes. But a quiet guardrail looks exactly like a broken journey, and today someone asks: why didn't it send?

## Key ideas

### 1. A silent journey is a question about evidence
When a message does not arrive, the room fills with theories, and the first guess is usually the last thing anyone changed. Divya gives Kavya a **deliberately broken copy** of Bloom Welcome v1 in the development sandbox, with Kavya's initials at the front of its name, and asks for evidence, not a theory.

### 2. The datasets Journey Optimizer writes for you
As journeys and campaigns run, AJO writes **system datasets** into the Adobe Experience Platform (AEP) data lake. They are the record of what really happened.

| Dataset | What it holds |
|---|---|
| Journey Step Events | Which profile passed which journey node |
| AJO Message Feedback Event Dataset | Delivery events such as sends and bounces; arrives in batches, **up to 2 hours late** |
| AJO Email Tracking Experience Event Dataset | Opens, clicks, unsubscribes |
| AJO Push Tracking Experience Event Dataset | Push events such as app launches |
| AJO ExD Decision Event Dataset | Decisioning events (judging by its name) |
| AJO Entity Dataset | A lookup of names: journey, campaign, email subject, channel |

A hard bounce goes onto the suppression list immediately (episode 23), so later sends to that address stop.

### 3. Journey step events: the ground truth
A node is one step on the journey canvas. Each step-event record has a timestamp, so you can read one person's path in order, like a courier's tracking page. The **last row** tells you where they stopped:
- No entry row: the journey never received them.
- The trail ends at a wait: they are not lost, just waiting.
- The trail ends before any action: no message was attempted, so no cap or quiet hours touched it.

### 4. The five-step triage

| Step | The question | Where to look | Often innocent because |
|---|---|---|---|
| 1. Entry | Did they enter at all? | Step events: an entry row | They never joined the audience, or re-entrance settings kept them out (Cart Rescue v1 allows re-entry at most once per 7 days) |
| 2. Qualification | Did they take the path that sends? | Step events: the split and path | The split sent them down a path with no message, as designed |
| 3. Wait | Are they simply waiting? | Step events: a wait not yet passed | A two-day wait looks like a failure on day one |
| 4. Action | Did the message node run? | Step events: an action row | They exited on purpose, for example on a purchase |
| 5. Delivery | Sent? Bounced? Opened? | Message Feedback, then Email Tracking | Feedback lags up to 2 hours; a cap or quiet hours held it back |

**Priya's evening of 18 August**, run through Cart Rescue v1: she adds a Vitamin C Serum at 7:44 PM, the journey waits four hours, and she buys on her laptop at 7:52 PM. Her trail is entry, wait, exit on purchase, with no action row. Nothing broke.

Also remember: a journey condition can only see fields an admin has added to the journey's data source, which is why Bloom Welcome v1 splits on **Gold Members** audience membership. And a capped or quiet-hours message looks like a broken journey until the evidence says otherwise; quiet hours can queue a message (later) or discard it (never).

### 5. Kavya's broken copy and the incident note
Kavya's Gold test seat (TD-KAVYA-01) entered the copy and no welcome arrived. Her instinct said the cap, because a capped test seat silently gets nothing (episode 23). Farhan pulled the seat's step events with a short Query Service query (episode 15): entry, the Gold Members path, the two-day wait passed, then nothing. No action row, so it was never the cap. Only then did she open the canvas: the email action was missing from the Gold Members path.

The **incident note** has five parts, a cousin of the episode 14 root cause analysis:

| Part | Kavya's note |
|---|---|
| Symptom | Gold test seat entered the copy; no welcome email arrived |
| Evidence trail | Entry row, Gold Members path, wait passed, no action row |
| Root cause | The email action was missing from the Gold Members path |
| Fix | Action restored in front of the wait; a second run showed an action row, a send and an open |
| Prevention | Before go-live, someone other than the builder checks that every path carries its message |

### 6. Journey Management, Reports
Step events explain one person; **Reports** shows every journey and campaign at once. The default period is **Last 7 full days**, and AJO reporting runs in **UTC**. India is five and a half hours ahead of UTC, so a send at 2 AM in Bengaluru on a Monday counts on Sunday. **CTR** is the click-through rate; **CTOR**, the click-to-open rate, compares clicks with opens. Adobe says these reports are powered by Customer Journey Analytics (CJA), which Act Three opens.

### 7. The ops readout
Four lines, one stated period, written after late feedback has landed: **sends**; **delivery rate** (delivered divided by sent; say, for example, 980 of 1,000 is 98 percent); **opens**; and **two numbers to flag**, one sentence each, saying who checks what next. No Bloom ops figures are fixed in this series; any number here is illustrative. Anjali's reply to Kavya's first readout opens Act Three: "Did any of it work?"

### 8. Ops hygiene in a shared organisation
The next person to open a journey should know what it is without asking.

| Habit | Bloom's rule |
|---|---|
| Naming | Purpose and version (Bloom Welcome v1, Cart Rescue v1); practice copies carry the owner's initials at the front |
| Versioning | A live journey is read-only, so a change means a new version. **Close to new entrances** lets people inside finish; **Stop** times everyone out and is for emergencies |
| Archiving | Retire on purpose and record why and what replaced it. A journey can be deleted only once Finished |
| Change discipline | One owner per journey, a written note before any change, a second person who checks it. Sandbox-wide settings (business rules, the allowed list) change only with their owner's sign-off |

Interview line: *"When a journey does not send, I read the step events in order: entry, qualification, wait, action, delivery."* Use it for "tell me about a journey that failed", then tell the story as your incident note.

## In the product

Labels as of October 2026. Look only; change nothing in a shared sandbox.

1. In Journey Optimizer's left navigation, open **Journey Management**, then **Reports**.
2. At the top: the heading **Reports**, the buttons **Share** and **Analyze in CJA**, and a data view drop-down naming **AJO Enabled Data View** plus your sandbox. Analyze in CJA stays greyed out unless your organisation has CJA and the connection is flagged Use in CJA (episode 25).
3. The period reads **Last 7 full days** with its dates. Adobe documents the date range filter at the top right of the report.
4. The **TABLE OF CONTENTS** lists **Highlights** (Journey Engagement, Journey Enters, Journey Failures, CTR, CTOR, People, Clicks, Spam Complaints, Unsubscribes), **Journeys** (Journeys, Journey Exclusions) and **Campaigns**.
5. Adobe documents a **Share** menu with Download CSV, Download PDF, Schedule export and Manage schedules; check what your screen shows, and never schedule an export without the report owner's agreement.

## Common mistakes

- Starting at the end and blaming the email or the cap before checking entry.
- Fixing the email when the person took another path and never reached it.
- Calling a person in a wait, or a correct exit on purchase, a failure.
- Declaring a bounce ten minutes after sending; Message Feedback arrives up to 2 hours late.
- Reading Last 7 full days for a fortnight readout, or forgetting that reports run in UTC.
- Writing only the fix in an incident note, with no evidence trail and no prevention.
- Quietly fixing "something small" in a colleague's journey instead of a new version with a written note.

## Glossary

| Term | Meaning |
|---|---|
| Journey Step Events | The dataset showing which profile passed which journey node; the ground truth for "why didn't it send?" |
| AJO Message Feedback Event Dataset | Delivery events such as sends and bounces; up to 2 hours late |
| AJO Email Tracking Experience Event Dataset | Opens, clicks and unsubscribes |
| AJO Push Tracking Experience Event Dataset | Push events such as app launches |
| AJO ExD Decision Event Dataset | Decisioning events, judging by its name |
| Incident note | Symptom, evidence trail, root cause, fix, prevention |
| Ops readout | Sends, delivery rate, opens and two numbers to flag, on one stated period |
| CTR / CTOR | Click-through rate / click-to-open rate |
| UTC | Coordinated Universal Time, the time zone AJO reporting uses |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

Search Experience League for: Journey Optimizer journey step events, Journey Optimizer datasets, message feedback event dataset, email tracking dataset, Journey Optimizer reports, journey troubleshooting.

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
