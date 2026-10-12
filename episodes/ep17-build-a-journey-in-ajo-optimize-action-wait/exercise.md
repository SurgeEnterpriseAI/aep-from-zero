# Exercise 17: The one-minute welcome

You will draw Bloom Welcome v1, choose the right entry for three situations, explain the missing loyalty points, match Optimize methods to Bloom uses, and decide what to click after an accidental publish.

## Track A: No Adobe access needed

1. **Draw Bloom Welcome v1 on paper.** Show the entry, an Optimize step with two paths in the right order, an Action on each path, a Wait and an End. Label each box with the activity name used in the 2026 canvas.
2. **Choose the entry.** For each of these three options, write one sentence on when it is right for Bloom:
   - audience qualification
   - Read audience
   - an event
3. **The missing loyalty points.** Kavya searched the expression editor for the loyalty tier and points and found nothing, although the points are on Priya's profile. Explain why in two sentences, and give the two ways to fix it.
4. **Optimize methods.** Name one Bloom use for each method: Data source condition, Time condition, Percentage split, Profile cap.
5. **The accidental publish.** A colleague published a journey by mistake. Write what you click, where you find it, and why you do not click Stop.
6. **The episode's practice question.** Say, for example, Divya adds a path for a smaller audience: Gold members who also use the Bloom app. Should that path sit above or below the Gold members path, and why?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- Name everything you create with **your own initials**.
- Never click **Publish**, **Simulate**, **Dry run** or **Send proof**. A draft journey runs nothing; those buttons can.
- Do not open journeys that are not yours. In a shared sandbox: look, screenshot, leave.

Steps:
1. In Journey Optimizer, open **Journey Management**, then **Journeys**, and click **Create Journey**. Name it with your initials plus `- Welcome practice`, and click **Save**. Confirm the status reads **Draft** and the toolbar shows **Alert (1)**.
2. Read **Journey properties**: note the **Allow reentrance** default, the **Reentrance wait period** and the **Current journey payload size**. Do not change them.
3. Add an entry: **Audience qualification** (Events) on an audience you created, or any small audience in your practice sandbox.
4. Add **Optimize** (Orchestration), keep **Data source condition**, and split on audience membership: drag an audience from **Audiences** in the **Add an expression** tree. Tick **Show path for other cases than the one(s) above**.
5. On the first path, add **Action**, choose **Email** under the **Marketing** category, and type placeholder content only.
6. Add a **Wait**: **Duration**, **1 Day**.
7. Open **Alerts** and confirm **zero errors**. A warning (for example, no opt-out link) may remain. Leave the journey as **Draft**. Do not publish.

## Check yourself

1. What does Alert (1) on a brand-new journey mean?
2. Why does Bloom Welcome v1 enter on audience qualification rather than Read audience?
3. Name three rules Read audience plays by.
4. What replaced the Condition activity in 2026, and what is its default method?
5. Why must the Gold members path come before the Others path?
6. Why did the loyalty points not appear in the expression editor?
7. Why is Gold Members a batch audience, and what does that mean for someone who turned Gold this morning?
8. What is the difference between Close to new entrances and Stop?

<details><summary>Check your answers</summary>

**Task 1: Bloom Welcome v1 on paper**

1. **Audience qualification** into New This Month (the entry)
2. **Optimize**, method Data source condition:
   - path 1, **Gold members**: the Gold Members audience membership is true
   - path 2, **Others**: everyone else
3. **Action** (Email) on each path: Gold welcome, Standard welcome
4. **Wait**: Duration, 2 days, after each email
5. **End**

The Gold path comes first because only the first true path is taken.

**Task 2: choosing the entry**
- **Audience qualification:** when a person's state changes and you want to act at once, such as a first-time customer joining New This Month. On a streaming audience it is the fastest audience-based way in.
- **Read audience:** when you want a whole group on a schedule, such as a Monday note to every Gold member. One per journey, first step only, Realized profiles only.
- **An event:** when the moment itself matters, such as a cart being abandoned (Cart Rescue, episode 21). It admits one person the moment something happens.

**Task 3: the missing loyalty points**
Journey conditions can only see fields an admin has added to the journey's data source, and Bloom's held only basic person fields, nothing under `_bloom`. The profile has the data; the journey's view of it is narrower. Fix 1: ask an admin to add the fields (shared configuration, so request and review). Fix 2: split on audience membership, which always works, for example a Gold Members audience.

**Task 4: Optimize methods** (the Bloom uses are illustrative)
- **Data source condition:** Gold members versus everyone else in the welcome.
- **Time condition:** say, for example, a different path for people who enter at the weekend.
- **Percentage split:** say, for example, half get one welcome subject line and half get another, as a fair test.
- **Profile cap:** say, for example, only the first 100 people who enter get an early-access sample; everyone after takes the standard path.

**Task 5: the accidental publish**
Tell your lead at once. From the menu at the top right of the Live journey, choose **Close to new entrances**: nobody new enters, and people already inside finish their path, emails included. **Stop** times out everyone inside at once and is for emergencies, such as an email that is wrong for everyone. A Live journey is read-only, so you cannot edit your way out, and it can be deleted only once Finished.

**Task 6: practice question**
Above it. Only the first path whose rule is true is taken. A Gold member who uses the app is also a Gold member, so if the broad Gold members path came first it would take all of them, and the app path would never be reached. Order paths from most to least specific; the Others path always comes last.

**Track B: what to expect**
The new journey opens as Draft with Alert (1). Journey properties shows Allow reentrance on, a 5-minute reentrance wait period and a payload size out of 4.0 MB. Optimize is greyed out until the entry exists. After the build, Alerts shows zero errors and probably one warning about the missing opt-out link. Labels as of October 2026; check what your screen shows.

**Check yourself**
1. The journey has no entry yet, so it is invalid. Add the entry first.
2. The welcome reacts to one person joining New This Month, a streaming audience. Read audience reads a scheduled snapshot, and Adobe advises audience qualification for real-time needs.
3. Any three of: only one per journey; it must be the first step; only Realized profiles enter; it runs Once, Daily, Weekly or Monthly; its reading rate is shared per sandbox; at most 5 runs at once per organisation.
4. The Optimize activity. Its default method is Data source condition.
5. Only the first path whose rule is true is taken, so the specific path must come before the catch-all.
6. They were not in the journey's data source, and journey conditions see only those fields.
7. Adobe no longer offers streaming for new rules that use only profile attributes. Batch audiences are evaluated once every 24 hours, so that person may take the Others path today.
8. Close to new entrances lets people already inside finish; Stop times everyone out and is for emergencies.

</details>
