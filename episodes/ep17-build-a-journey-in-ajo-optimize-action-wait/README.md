# Episode 17: Build a Journey in AJO: Optimize, Action, Wait

**Watch:** Video coming soon on iTV

[Previous](../ep16-adobe-journey-optimizer-tutorial-for-beginners/) · [Next](../ep18-ajo-test-mode-vs-simulation-vs-dry-run-vs-proof/)

## What you will learn

- Build a journey on the 2026 canvas: **entry, Optimize, Action, Wait, End**
- Choose between **audience qualification** and **Read audience**, and know Read audience's rules
- Split people with **Optimize** and a **Data source condition**, and put the paths in the right order
- Explain the **journey data-source field limit** and the **audience-membership** workaround
- Read **Alerts**, guardrails and the journey lifecycle, including what to do after an **accidental publish**

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers. In Act One the team built one real-time customer profile and governed audiences on Adobe Experience Platform (AEP). Episode 16 opened Act Two: Divya set the deadline ("Relaunch Monday: Bloom Welcome v1 is the first live journey") and her first rule (everyone works from a test seat carrying their own inbox). Kavya built the Bloom Gold Thank-You campaign in Adobe Journey Optimizer (AJO) and stopped at Review to activate. But the welcome email is still a Tuesday batch job, so new customers wait up to six days.

## Key ideas

### 1. The 2026 journey canvas
A **journey** is a path one person moves through, with every step evaluated for that person. Bloom Welcome v1: **entry** (joins New This Month), **Optimize** (Gold members or Others), **Action** (a welcome email on each path, placeholder content for now), **Wait** (two days), **End**.

You add each step with the **+** between two activities. The list is grouped as **Events**, **Orchestration** and **Actions**. **Optimize** stays greyed out until the journey has an entry. A brand-new journey shows **Alert (1)** straight away, because a journey with no entry is invalid.

### 2. Audience qualification versus Read audience
Divya's rule: *if the moment matters, use the event; if the state matters, use the audience.* Any order is a moment, but being a first-time customer is a state, and the New This Month audience already defines it.

| | Audience qualification | Read audience |
|---|---|---|
| Who enters | One person, the moment they join (or leave) an audience | Everyone in the audience, like a snapshot |
| When | As it happens | Once, Daily, Weekly or Monthly |
| Rules | Adobe's advice for real-time needs | Only one per journey, and it must be the first step |
| Who gets in | Whoever qualifies | Only profiles with **Realized** status (they have qualified) |
| Bloom example | The welcome | Say, for example, a Monday note to every Gold member |

Bloom enters on audience qualification into New This Month, which was designed as a **streaming** audience. Streaming updates in near real time, but Adobe gives no minutes figure, so "within a minute" is Bloom's target to measure, not Adobe's promise.

### 3. Condition is gone: Optimize
The **Condition** activity was removed from the UI in 2026. The **Optimize** activity replaces it, and its default method, **Data source condition**, does the same job. Journeys built earlier with Condition keep working.

**Only the first path whose rule is true is taken**, so order paths from most to least specific. **Show path for other cases than the one(s) above** adds an **Others** path for everyone who matched nothing.

Optimize can also split by **Time condition** (hour of day or day of week), **Date condition** (a date range), **Percentage split** (a random share, for tests), **Profile cap** (the first N people take the path) or **Audience** (membership of another audience).

### 4. Journeys see only data-source fields
Kavya searched the expression editor for the loyalty tier and points under `_bloom` and found nothing, although Priya's 2,340 points are on her profile. **Journey conditions can only see fields an admin has added to the journey's data source**, shown as the **ExperiencePlatform** branch of the editor's tree. Bloom's held basic person fields (name, home address, personal email, phones) and nothing under `_bloom`.

Two fixes:
1. Ask an admin to add the fields. This is shared configuration, so it needs a request and a review.
2. **Split on audience membership**, which always works. Divya built a small helper audience, **Gold Members** (loyalty tier = Gold, batch), and the Gold path's rule reads "the Gold Members audience membership is true".

Gold Members is batch because Adobe no longer offers streaming for new rules that use only profile attributes. Batch audiences are evaluated once every 24 hours, so someone who turned Gold this morning may take the Others path today.

### 5. One Action activity, and a Duration wait
The separate Email, SMS and Push tiles are deprecated. You add **one Action activity and choose the channel inside it**, so the journey stays readable as channels are added. Marketers select the admin-owned **channel configuration**; they never build it.

A **Wait** counts from each person's own entry, not from one date for everyone. Types: **Duration** (up to 90 days), **Custom** (a date you calculate) and **Send-Time Optimization** (Adobe picks each person's best time). A person can stay in a journey for at most 91 days.

### 6. Alerts and the journey lifecycle
**Errors must be zero to publish; warnings may stay.** Bloom Welcome v1 shows zero errors and one warning: the opt-out link is not present in the email body. With an email on each path, your screen may list it once per email. The Bloom footer fragment clears it in episode 19.

| Status | How you get there | What it means |
|---|---|---|
| Live | Publish | Real people enter; read-only |
| Paused | Pause | Nobody moves until resumed |
| Closed | Close to new entrances | Nobody new enters; those inside finish |
| Stopped | Stop | Everyone inside is timed out; emergencies only |
| Finished | Automatic | The work is done; only now can it be deleted |

**Published by mistake?** Tell your lead at once, then use **Close to new entrances** from the menu at the top right. People already inside finish their path, emails included. **Stop** is for emergencies, such as an email that is wrong for everyone who receives it.

### Numbers worth knowing

| Guardrail | Limit |
|---|---|
| Activities in one journey | 50, cannot be raised |
| Active journeys (live, closed, paused, dry run) | 100 in a development sandbox, 200 in production |
| Longest Wait / longest stay | 90 days / 91 days |
| Read audience | 500 to 20,000 profiles per second (default 5,000), shared per sandbox; at most 5 runs at once per organisation |
| Journey payload | 4.0 MB, shown in Journey properties |

Interview line: *"There is no Condition activity in 2026, so I split with Optimize and order paths from specific to general. When a field is outside the journey's data source, I split on audience membership instead."*

## In the product

Labels as of October 2026. Practise only in a development sandbox, on a journey named with your initials, and never click Publish.

1. In Journey Optimizer, open **Journey Management**, then **Journeys**, and click **Create Journey**.
2. In **Journey properties**, type a **Name** and click **Save**. The status reads **Draft**. Leave **Allow reentrance** on and **Reentrance wait period** at 5 minutes. The panel also shows **Current journey payload size**.
3. Click the **+** and choose **Audience qualification** from **Events**, then pick the audience.
4. Click the **+** after the entry and choose **Optimize** from **Orchestration**. Keep **Data source condition** and rename **Path1**.
5. Click the pencil beside **Expression**. In **Add an expression**, the tree shows **Context**, **Audiences**, **ExperiencePlatform** and **Journey properties**. Drag your audience from **Audiences**, then click **Ok** twice.
6. Tick **Show path for other cases than the one(s) above**. The new path is labelled **Others**. Click **Save**.
7. On each path, click **+** and pick **Action**. In **Select action type**, keep **Marketing**, choose **Email** and click **Add**. Use **Configure action** to pick the channel configuration, then **Edit content**. Do not click **Send proof**: it sends real emails.
8. Click **+** after each email and pick **Wait**. It opens as **Duration**, **1 Day**. Set the delay, label it, and click **Save**.
9. Open **Alerts** (top right). Hover any exclamation mark to see what an activity needs.
10. Check the status next to the journey name: **Draft**. Your build ends here.

## Common mistakes

- Looking for **Condition** because an old tutorial says so. Optimize with Data source condition replaces it.
- Entering a time-critical journey from a batch audience or a scheduled Read audience.
- Putting a broad path above a specific one, so it swallows people meant for the narrower path.
- Re-ingesting files when a field is simply not in the journey's data source.
- Reading a wait as a fixed date for everyone. It counts from each person's arrival.
- Ignoring the opt-out warning until go-live.
- Hitting **Stop** by reflex after an accidental publish, and cutting off customers halfway through.

## Glossary

| Term | Meaning |
|---|---|
| Journey | A path one person moves through, with steps, decisions and waits |
| Audience qualification | A journey entry that admits a person the moment they join or leave an audience |
| Read audience | A journey entry that reads everyone in an audience, once or on a schedule |
| Optimize activity | The 2026 activity that splits a journey's path by data, audience, time or percentage |
| Data source condition | Optimize's default method: a rule on a field or on audience membership |
| Journey data source | The fields an admin has made visible to journey conditions |
| Action activity | The single 2026 activity that sends a message; the channel is chosen inside it |
| Channel configuration | The admin-owned sending set-up a message goes out on |
| Duration wait | A delay that counts from each person's own entry |
| Close to new entrances | Stops new people entering while those inside finish |
| Stop | Times out everyone inside a journey; for emergencies |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Journey Optimizer create a journey, Optimize activity, Read Audience activity, audience qualification events, journey guardrails and limitations, close a journey to new entrances

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
