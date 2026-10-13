# Episode 16: Adobe Journey Optimizer Tutorial for Beginners

**Watch:** [Watch episode 16 on YouTube](https://youtu.be/ZLuEwSspNbQ)

[Previous](../ep15-aep-query-service-tutorial-sql-on-the-data-lake/) · [Next](../ep17-build-a-journey-in-ajo-optimize-action-wait/)

## What you will learn

- Explain how **Adobe Journey Optimizer (AJO)** reuses the profiles, audiences and events built in Adobe Experience Platform (AEP)
- Tell a **journey** from a **campaign**, and pick the right one for a Bloom use case
- Name the **four campaign types**, including API triggered, and the **three ways into a journey**
- Explain **identity type**, the **channel configuration**, and where the sending address comes from (**Execution Fields**)
- Build a campaign draft safely on your own **test seat**, and read **Review to activate** without activating

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers. In Act One the team turned three disconnected systems into one governed, real-time customer foundation on AEP. But the welcome email is still a Tuesday batch job, so a customer who pays on Wednesday waits six days to hear from Bloom. Act Two opens with Divya Nair, Bloom's lead for customer relationship management and journeys, and a deadline on the whiteboard: "Relaunch Monday: Bloom Welcome v1 is the first live journey."

## Key ideas

### 1. Divya's first rule: your own seat, your own inbox
Before anyone touches AJO, every team member loads one **test seat**: a **test profile** (flagged `testProfile = true`) that carries their **own inbox**. IDs start with `TD-` (test data) so the rows are easy to find. Nobody ever types anyone else's address, in any test. Some test buttons send real email; episode 18 covers each of them.

| Seat | Profile state | Address in these notes |
|---|---|---|
| TD-KAVYA-01 | Gold | kavya@example.com |
| TD-FARHAN-02 | Silver, recent buyer | farhan@example.com |
| TD-DIVYA-03 | Lapsed: last order more than 90 days ago | divya@example.com |
| TD-ROHAN-04 | Silver | rohan@example.com |

When you practise, put **your own** address on **your own** seat.

### 2. AJO sits on AEP (the voice reads the memory)
AEP is **the memory**, AJO is **the voice**. AJO does not keep its own customer list. It reuses what Act One built:
- the **Real-Time Customer Profile**, with its identities and fields such as first name
- the **audiences**, so the relaunch five (High-Value Loyalists, Cart Abandoners 24h, Lapsed 90, New This Month, Window Shoppers) are already there
- the **events** Bloom collects, which can start a journey once an admin has configured them

AJO reads an audience directly. It does not need a destination.

### 3. Journey versus campaign
- A **campaign** answers *"what do we send?"*: one send, usually to an audience at a time you choose.
- A **journey** answers *"what happens to this customer next?"*: a path one person enters, moves through and leaves, with steps, decisions and waits over days or weeks, evaluated for that one person.

| | Campaign | Journey |
|---|---|---|
| Shape | One send to an audience | Steps, decisions and waits |
| Starts from | A scheduled time, or an API call | Read audience, an event, or audience qualification |
| Built in | Campaigns | Journeys, on the journey canvas |
| Bloom example | Bloom Gold Thank-You | Bloom Welcome v1 (episode 17) |

Clients buy AJO for the second question.

### 4. The four campaign types
Two choices make four types: **when** it sends (Scheduled, or API triggered when another system calls the AJO application programming interface) and **what kind** of message it is (Marketing or Transactional).

| Type | Use it for |
|---|---|
| Scheduled - Marketing | Offers, newsletters, thank-you emails to an audience |
| Scheduled - Transactional | Service messages to an audience that must ignore marketing opt-outs, for example a store-closure notice |
| API triggered - Marketing | A send fired by another system, aimed at an AEP audience |
| API triggered - Transactional | A send to the profiles named in the call (up to 20), such as an order receipt |

**Transactional ignores marketing opt-outs.** Never use it for anything that sells.

### 5. Three ways into a journey
| Entry | Who enters | Bloom example |
|---|---|---|
| **Read audience** | Everyone in an audience, once or on a schedule (a batch snapshot) | Every Gold member, every Monday |
| **Event** | One person, the moment something happens | Priya's add to cart at 7:44 PM |
| **Audience qualification** | A person as they join or leave an audience | A new customer joins New This Month |

The rule: **if the moment matters, use the event; if the state matters, use the audience.** Being Gold, or being a new customer, is a state.

### 6. Identity type, Execution Fields and the channel configuration
- **Identity type** is the key AJO uses to identify each person in the campaign's audience. **One per campaign.** An audience member with no identity of that type (for an email campaign, no Email identity) is **not targeted at all**.
- The address the email actually goes to comes from the sandbox default under **Administration, Channels, Execution Fields**. A **channel configuration** can override it.
- A **channel configuration** is the admin-owned sending set-up: Marketing or Transactional (which must match the campaign), the sending subdomain, the sender name and from address, and optionally the profile field that supplies the recipient address. An admin sets it up once; marketers only select it. Older material calls it a "surface".

### 7. A safe campaign draft
Bloom's warm-up is **Bloom Gold Thank-You**: a Scheduled Marketing campaign to High-Value Loyalists (a little under 1,180 of the 10,000-customer extract), identity type Email. Kavya's draft stops at **Review to activate**: one warning (no opt-out link; episode 19's footer fragment fixes it) and an **Activate** button that, on the default schedule, sends at once.

### 8. The Flash Sale: an API triggered campaign
Divya activates **Flash Sale**, an API triggered Marketing campaign, and fires it from the Postman collection in Bloom's asset pack. In real life, another Bloom system would make the call. Its audience holds exactly **one profile: her own test seat**, so the only inbox that can receive it is hers. Adobe documents the API triggered flow this way; check what your screen shows.

Interview line: *"A campaign answers what do we send. A journey answers what happens to this customer next."*

## In the product

Labels as of October 2026. Practise only in a development sandbox, on objects named with your own initials.

1. **App switcher** (the grid icon, top right) → **Journey Optimizer**. Read the sandbox name in the top bar before every save.
2. Left navigation: **Journey Management** holds **Campaigns**, **Journeys** and **Reports**.
3. **Administration** → **Channels** → **Channel configurations**: read only. **Execution Fields** is under **Administration** → **Channels** too. Do not create or edit either.
4. **Journey Management** → **Campaigns** → **Create campaign** → **Scheduled - Marketing** → **Confirm**.
5. Properties: **Name** (yours: `Bloom Gold Thank-You` plus your initials) and a one-line description. The campaign saves as a **Draft** on its own. Fields save as you type; there is no Cancel.
6. **Audience** tab → **Select audience** → tick the audience → **Add audience**. **Identity type**: clear the box, type `Email`, then pick **Email** from the shortened list.
7. **Actions** tab → **Add action** → **Email**. Select the Marketing email channel configuration. Leave Rule set and Action tracking as they are.
8. **Edit content**. **Subject line**: use the **Open personalization dialog** icon beside the field, or type `{{profile.person.name.firstName}}, thank you for being Bloom Gold`. A green tick means the expression is valid.
9. **Edit email body** → **Design from scratch** → **Components** tab. From **Structures** drag **1:1 column** onto the canvas, then from **Contents** drag **Text** into it. Write the thank-you, then **Save** (top right).
10. Open the arrow next to **Simulate content** → **Simulate content (AEP profiles)** → **Manage test profiles**. Identity namespace **Email**, identity value: **your own** seat's address → **Add profile**. Plain **Simulate content** uses sample data instead. Do **not** click **Send proof**.
11. Back arrow to the campaign. Leave **Schedule** on its default. Click **Review to activate** and read the summary (content, properties, action, audience). Expect one warning: "The opt-out link is not present in the email body."
12. Do **not** click **Activate**. Leave through **Campaigns** in the left rail.

## Common mistakes

- Running a weekly campaign for something that should react to each customer's own moment.
- Choosing a journey entry by habit instead of asking "moment or state?".
- Picking Transactional for a promotion to reach people who opted out.
- Assuming the identity value is the address the email goes to (that is Execution Fields).
- Dragging Text onto an empty canvas: the Email Designer needs a structure first.
- Calling content "tested" after a plain Simulate content preview on sample data.
- Typing in someone else's campaign: fields save as you type.
- Pressing Activate on the default schedule: it sends at once.

## Glossary

| Term | Meaning |
|---|---|
| Adobe Journey Optimizer (AJO) | Builds and runs customer journeys and campaigns across channels; "the voice" |
| Campaign | A one-off or scheduled send to an audience, or one triggered by an API call |
| Journey | A path one person moves through, with steps, decisions and waits |
| Transactional | Service messages that ignore marketing opt-outs; never for promotions |
| API triggered campaign | A campaign fired when another system calls the AJO API |
| Read audience | A journey entry that reads everyone in an audience, once or on a schedule |
| Event entry | A journey entry that admits one person the moment something happens |
| Audience qualification | A journey entry that admits a person the moment they join or leave an audience |
| Identity type | The key AJO uses to identify each person in a campaign's audience; one per campaign |
| Execution fields | The sandbox default for which profile field a message is sent to; a channel configuration can override it |
| Channel configuration | The admin-owned sending set-up for a channel: Marketing or Transactional, domain, sender |
| Simulate content (AEP profiles) | A preview of the message filled in from a real test profile |
| Review to activate | A summary screen before activation; reading it sends nothing |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Journey Optimizer get started with campaigns
- Search Experience League for: Journey Optimizer API-triggered campaigns
- Search Experience League for: Journey Optimizer channel configuration, execution fields
- Search Experience League for: Journey Optimizer create test profiles, simulate content

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
