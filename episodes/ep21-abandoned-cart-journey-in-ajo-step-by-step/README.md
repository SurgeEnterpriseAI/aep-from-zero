# Episode 21: Abandoned Cart Journey in AJO, Step by Step

**Watch:** [Watch episode 21 on YouTube](https://youtu.be/CvcLbZqFkLI)

Part 2: Speak to your customer (Adobe Journey Optimizer) · [Previous](../ep20-ajo-personalization-tutorial-fallback-if-else/) · [Next](../ep22-offer-decisioning-in-ajo-eligibility-ranking/)

## What you will learn

- Explain why a cart-abandonment trigger must be **event based**, fed by **streaming** logic, and never a daily batch audience
- Choose a **wait window** from your own data, and know where a second touch fits
- Render the actual cart items from the triggering **event payload**, with null-safe **fallbacks** and a dynamic subject line
- Let buyers leave with **exit criteria** on any purchase plus a **pre-send check**, and cap **re-entry** at once in seven days
- Prove the exit in **Test mode**, because Simulation does not support exit criteria
- Measure **incremental** revenue with a **holdout** set on day one, instead of trusting attributed revenue

## The story so far

Bloom, a direct-to-consumer wellness brand with 1.2 million customers, is relaunching its loyalty programme on Adobe Experience Platform (AEP) and Adobe Journey Optimizer (AJO).
In episode 20, Kavya wrote every fallback first, added an if-else Gold line, and made the copy agree with its audience.
On relaunch Monday, Bloom Welcome v1 went live as the first live journey.
The next morning Divya named the journey that pays for the programme: Cart Rescue v1.

## Key ideas

### 1. There is no cart object
A cart is **derived**: add-to-cart events that were not followed by a purchase. In Act One that sentence became the audience **Cart Abandoners 24h**, designed for streaming evaluation. Today the same logic drives a journey.

### 2. The trigger has to be fast
A cart rescue is useful only while the intent is still warm. A batch audience is evaluated once every 24 hours, far too late. So Cart Rescue v1 enters on **the abandon event**, through an **event entry** (also called a unitary event entry), which admits one person the moment something happens.

- In the audience, "not followed by a purchase" was a clock inside the rule. In the journey, the clock becomes a **wait** and the missing purchase becomes the **exit**.
- Which events a journey can listen to is set up once by an admin; these notes keep that set-up generic.
- Farhan's Postman abandon sequence qualifies Kavya's test seat (TD-KAVYA-01) into Cart Abandoners 24h. Adobe documents this flow; check what your own screen shows.

### 3. The wait window is a business decision
Too short and you interrupt someone who is still shopping. Too long and the moment has passed. Most retailers land between **one and four hours** for the first touch, with a second touch around **24 hours**. The right number comes from the client's own gap between add to cart and purchase, not from a blog post.

Bloom's first touch waits **four hours**, after its natural return window. A second touch can repeat the pattern once the first proves itself. Watch the clock: 11 PM plus four hours is a 3 AM email, which **quiet hours** (episode 23) handle.

### 4. Render the actual cart from the event payload
The **event payload** is the data the triggering event carried: what was actually in the cart at that moment. Profile attributes say who the customer is and hold no cart. Cart Rescue's email repeats one row per item, with **name, image and price** read from the payload.

**Null-safe fallbacks** (write the fallback first): a missing image shows the name and price with no broken box; a missing item list falls back to "You left something lovely in your cart"; an empty first name reads "Hi there". Test profiles flatter you; real events arrive with gaps.

**Dynamic subject line:** an if-else on the loyalty band under `_bloom`, with a single `=` and "Gold" spelled exactly as stored: an early-access tone for Gold, gentle urgency for everyone else. It is a content variant, not a journey branch. Urgency must be true.

### 5. The exclusion everyone forgets
Between the trigger and the send, some people buy. If you do not exclude them, they are asked to finish an order they already finished. Bloom uses two locks:

- **Exit criteria:** any purchase event removes the person from the journey, wherever they are inside it.
- **Pre-send check:** an **Optimize** activity just before the email, with its default method **Data source condition**, reading the **current** profile rather than the state at entry. Journey conditions only see fields an admin has added to the journey's data source, so agree those fields with the admin early.

**Priya on 18 August:**

| Time | What happened | Cart Rescue v1 |
|---|---|---|
| 7:44 PM | Adds a Vitamin C Serum in the app on her phone; the event carries only the app's Experience Cloud ID (ECID) | She enters; the four-hour clock starts |
| Moments later | Signs in on the app: the linking event | The app's ECID is linked to her email |
| 7:52 PM | Buys on her laptop: order BLM-88412, 54.00 (`BLM-SER-VITC-30`, `BLM-MOIST-HYA-50`) | Exit criteria remove her |
| 11:44 PM | Would have been the send | No email |

Without the sign-in that stitched the app's ECID to her email, the identity her order carried, the journey could never link her order to her cart.

### 6. Re-entry and proving the exit
- **Allow reentrance** is on by default, with a **Reentrance wait period** of 5 minutes. Cart Rescue v1 keeps re-entry on but sets 7 days: at most one entry in any seven days. Switching re-entry off would rescue each customer's first cart and never again.
- **Simulation does not support exit criteria**. The team uses **Test mode**: stored test profiles only, real email to their own inboxes, waits shortened to 10 seconds. Kavya's Gold seat got the early-access subject; Rohan's Silver seat (empty name, image removed) got "Hi there" and no broken image; Farhan's seat fired a purchase and received nothing.
- Test mode takes the top branch of a split, so keep the sending path on top of both splits. It proves the exit, not every path.

### 7. Attributed revenue is not incremental revenue
**Attributed revenue** counts money from people who bought after the message, whether or not it caused the purchase; a shopper like Priya, who was coming back anyway, is counted if she buys just after the email. **Incremental revenue** is what the journey caused over and above what would have happened anyway.

A **holdout**, a random share of qualifying people deliberately sent nothing, is the only way to measure it. Cart Rescue v1 holds back **10 percent** with an Optimize **Percentage split** straight after the entry. Illustrative: if 10 in 100 emailed shoppers buy and 7 in 100 of the holdout buy anyway, the journey caused about 3 in 100. Set it on day one; adding one after a client has seen a big number is a very difficult conversation.

Interview line: *"Attributed revenue is not incremental revenue. Set a holdout on day one."*

## In the product

Labels as of October 2026. Practise only on a Draft in a development sandbox, with your initials in the name.

1. **Journey Management**, **Journeys**, **Create Journey**. In **Journey properties**, add a name and description, then **Save**. It is a **Draft**, with one alert until it has an entry.
2. The **+** between activities lists **Events**, **Orchestration** and **Actions**. The abandon event appears only if an admin has set it up.
3. Holdout: **Optimize**, **Percentage split**: 90 percent on the top path, 10 percent to End.
4. **Wait**: a Duration of four hours (up to 90 days).
5. Pre-send check: **Optimize**, **Data source condition**, on the current profile.
6. One **Action** activity, **Email** chosen inside it; item block from the event's fields, with fallbacks.
7. Exit criteria on any purchase event. Adobe documents this; check what your screen shows.
8. **Journey properties**: **Allow reentrance** on, **Reentrance wait period** 7 days.
9. **Simulate** opens **Test and validate**: **Simulation** or **Test mode**. Both send real email: in a shared sandbox, read the dialog and close it. Only Test mode proves an exit.

## Common mistakes

- Triggering a cart rescue from a daily batch audience.
- Copying a wait window from a blog instead of reading your own data.
- Building the item block from profile attributes, which hold no cart.
- No fallback for a missing image or an empty item list.
- Forgetting the purchase exclusion, or checking a value copied at entry.
- Leaving the Reentrance wait period at 5 minutes, or switching re-entry off.
- Trying to prove the exit with Simulation.
- Reporting attributed revenue as the result, or adding a holdout after the big number.

## Glossary

| Term | Meaning |
|---|---|
| Abandonment | Adding to cart without completing a purchase within a defined window |
| Event entry (unitary) | A journey entry that admits one person the moment something happens |
| Event payload | The data carried by the triggering event, usable in message personalisation |
| Wait activity | A pause in a journey, measured from each person's own entry |
| Exit criteria | A rule that removes a person from a journey, such as "made a purchase" |
| Pre-send check | An Optimize step just before the send that reads the current profile |
| Reentrance wait period | How long a person must wait before entering the same journey again |
| Test mode | Runs a journey on test profiles, sending real email to their inboxes, with waits shortened to 10 seconds |
| Simulation | A run with temporary simulated users; a real send; it does not support exit criteria |
| Attributed revenue | Revenue from people who bought after a message, whether or not the message caused it |
| Incrementality | The additional outcome caused by the campaign, over and above the baseline |
| Holdout | A randomly withheld group used to measure what would have happened anyway |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Streaming segmentation: https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/methods/streaming-segmentation
- Search Experience League for: Journey Optimizer exit criteria, journey re-entrance, unitary event journeys, test mode, journey simulation, contextual event data

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
