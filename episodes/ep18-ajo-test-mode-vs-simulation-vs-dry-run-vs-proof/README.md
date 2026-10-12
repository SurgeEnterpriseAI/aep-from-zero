# Episode 18: AJO Test Mode vs Simulation vs Dry Run vs Proof

**Watch:** Video coming soon on iTV

[Previous](../ep17-build-a-journey-in-ajo-optimize-action-wait/) · [Next](../ep19-ajo-fragments-email-designer-one-brand-voice/)

## What you will learn

- Say which Adobe Journey Optimizer (AJO) testing options can reach a **real inbox** and which never do
- Create and load **test profiles** safely: your own inbox, your own dataset, Profile switched on first, never a real customer's ID
- Choose **Test mode**, **Simulation**, **Dry run**, **Send proof** or **Simulate content** for a given testing goal
- Know each option's limits, including **Test mode taking the top branch** of a split
- Use a **deliberately incomplete test profile** to catch personalisation gaps before go-live

## The story so far

Bloom, a direct-to-consumer wellness brand with 1.2 million customers, is days away from relaunch Monday. In episode 17 Kavya and Divya built **Bloom Welcome v1**: an audience-qualification entry into New This Month, an Optimize split on membership of the Gold Members audience (loyalty fields were not in the journey's data source), then a welcome email on each path and a two-day wait. Alerts showed zero errors and one opt-out warning, and the status read Draft. Nobody has run a person through it yet.

## Key ideas

### 1. Some test buttons send real email
Several testing options send real email through the real delivery pipeline. In a non-production sandbox an **allowed list** normally limits who test mail can reach; when its toggle reads **Deactivated**, nothing does.

| Option | Can it reach a real inbox? | Who goes through | Best for |
|---|---|---|---|
| Alerts panel | Never | Nobody: it only checks | Finding errors before anything runs |
| Dry run | Never | Real profiles, counted only | Proving how many people take each path |
| Test mode | Yes | Stored test profiles (their inboxes) | The email and the top path, end to end, fast |
| Simulation | Yes | Simulated users you create | Quick trials with no stored profile |
| Send proof | Yes | Up to 10 addresses you type | Checking one email's content |

Bloom's testing rule: **looking is safe; saving, activating, sending and deleting are not.** Before any test button, ask: whose inbox can this reach?

### 2. Test profiles and Bloom's four seats
A **test profile** is a profile flagged for testing: a true-or-false field called `testProfile` set to `true`. Test mode admits only flagged test profiles. A test seat is still a real profile in the sandbox, so if anyone publishes a journey for Gold members, a Gold seat gets that email. That is why a seat carries only its owner's own inbox.

| Seat | State | Built to prove |
|---|---|---|
| TD-KAVYA-01 | Gold | Gold content |
| TD-FARHAN-02 | Silver, recent buyer | What everyone else sees |
| TD-DIVYA-03 | Lapsed (last order more than 90 days ago), email consent true | The win-back path, later in the act |
| TD-ROHAN-04 | Silver, first name left empty on purpose | That test profiles lie |

Seats use `@example.com` addresses here; in practice, each carries its owner's own inbox.

**Four rules for loading test data**

| Rule | Reason |
|---|---|
| Start every ID with `TD-` | Test rows are easy to find and remove later |
| Load only into your own dataset | Shared datasets belong to everyone |
| Switch the dataset's Profile toggle on **before** uploading | Data loaded while it is off never reaches the profile store |
| Never reuse an existing customer's ID | A batch replaces that customer's whole row in the dataset |

The **Update profile** activity in the journey palette writes to the profile store. It exists, but it is not for practice.

### 3. Test mode: real inboxes, top branch only
Test mode sends real emails through the production pipeline to the addresses stored on test profiles. Only test profiles enter, up to 100 per session. The journey is locked for editing while it runs, and every wait is shortened to 10 seconds.

The limit: **in our testing, the top branch of a split was always taken.** Kavya's Gold seat took the Gold path, and so did Rohan's Silver seat. Test mode proves the email and the top path; it does not prove the other paths.

### 4. Dry run: prove every path, contact nobody
**Dry run** sends no email and changes no profile. It shows how many real profiles would take each path, which is how Divya proved the Others path. It counts against the sandbox's active-journey limit (100 in a development sandbox), runs for up to 14 days and needs publish rights. Run it once, read the counts, then return the journey to Draft.

### 5. Simulation: a real send with the protections off
**Simulation** sends simulated users (made up on the spot, not stored profiles) through the journey. It is a real send through the normal delivery pipeline, and the **suppression list, allowed list, consent, frequency caps and quiet hours are not applied**. Type only your own address, and never put real customer data on a simulated user.
- Up to 20 simulated users per batch, 100 per run.
- No exit criteria, inbound channels or dataset lookups.
- Disconnected nodes block it, even when Alerts shows zero errors.
- On an audience-membership split such as Gold Members, a simulated user may fall to the **Others** path. Check your screen.

### 6. Send proof and Simulate content
- **Simulate content** previews an email with sample data. **Simulate content (AEP profiles)** previews it on real test profiles, so you can switch between Bloom's seats. Previewing sends nothing.
- **Send proof** sends real email to up to 10 typed addresses, **multiplied by the number of test profiles**: 5 addresses and 10 profiles make 50 emails. Frequency caps apply to proofs, so a capped test profile can silently receive nothing. A proof checks content; it does not run the journey.

### 7. Test profiles lie
Test profiles usually have every field filled in; real customer records often do not. Rohan's seat, with its first name empty on purpose, received a welcome that opened `Hi ,`. The fix is a fallback for every personalised field (episode 20). Always walk one deliberately incomplete profile through a journey before go-live.

Interview line: *"Which test options can reach a real inbox? Test mode, Simulation and Send proof. Dry run never does."*

## In the product

Labels as of October 2026. Do this only in a development sandbox, on a journey that carries your own initials.

1. **The journey toolbar** shows **Alert**, **Simulate**, **Dry run** and **Publish**. Open **Alerts** first: errors must be zero, and warnings may stay.
2. **Simulate** opens a dialog called **Test and validate** with two choices: **Simulation** (marked New) and **Test mode**. Choose one, then **Confirm**.
3. **Simulation:** Adobe documents adding a simulated user with **Create from form** (a display name, an identity namespace, then attributes from the union schema), setting the run's email to your own inbox, overriding a Wait to 10 seconds, and reading **Results**. Adobe documents it this way; check what your screen shows. With a loose node the screen says "Disconnected nodes are blocking the simulation mode activation".
4. **Test mode:** only test profiles enter, and the journey's status shows **Draft (Test)** while it is locked.
5. **Dry run:** when you have read the counts, close it and use **Back to Draft**.
6. **Email content:** **Simulate content**, then **Simulate content (AEP profiles)**, then **Manage test profiles**. Add a seat by namespace (Email) and value, click **Add profile**, and switch seats with **Test profile name**. **Send proof** sits on the same screen; do not click it unless the address is your own and your administrator allows it.
7. **Loading a seat:** **Datasets**, **Create dataset**, **Create dataset from schema**, named with your initials. Switch the **Profile** toggle on, then drag the file into **Add data** (up to 5 Parquet or JSON files). Look the seat up in **Profiles**, **Browse**. Adobe publishes no time for batch data to reach Profile.
8. **Allowed list:** **Administration**, **Channels**, **Email settings**, **Allowed list**. Read whether the toggle says Deactivated. Never change it: it is sandbox-wide.

## Common mistakes

- Treating a development sandbox as harmless. Its test emails reach real inboxes, especially when the allowed list is deactivated.
- Putting a colleague's or a customer's address on a test profile or a proof.
- Borrowing a real customer's profile and changing its email, or reusing a real customer's ID, which overwrites their row.
- Loading a seat before switching the dataset's Profile toggle on.
- Reporting that Test mode "checked every branch". It took the top branch; prove splits with Dry run.
- Leaving a dry run running, holding one of the sandbox's active-journey slots.
- Filling every field on every test profile, so every test passes and proves nothing.

## Glossary

| Term | Meaning |
|---|---|
| Test profile | A profile flagged `testProfile = true` so journeys and messages can be tried on it |
| Test seat | Bloom's name for one team member's test profile, carrying their own inbox |
| Allowed list | In a non-production sandbox, the list that limits who test mail can reach |
| Test mode | Runs stored test profiles through a journey with real email; waits cut to 10 seconds; top branch taken |
| Simulation | Runs simulated users through a journey as a real send, with suppression, consent, caps and quiet hours not applied |
| Simulated user | A stand-in created for a Simulation run; not a stored profile |
| Dry run | Shows how many real profiles would take each path; contacts nobody |
| Send proof | Real email to up to 10 typed addresses, multiplied by test profiles |
| Simulate content | A preview of an email, with sample data or with real test profiles |
| Update profile | A journey activity that writes to the profile store; not for practice |
| Fallback | The default text used when a personalised field is missing |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

Search Experience League for: Journey Optimizer test your journey (Test mode), simulate a journey, dry run journey, send proofs, create test profiles, allow list, journey guardrails.

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
