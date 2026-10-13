# Episode 10: AEP Segment Builder Tutorial: Build Audiences

**Watch:** [Watch episode 10 on YouTube](https://youtu.be/j4u9gy1QlBY)

[Previous](../ep09-aep-no-profiles-found-debug-an-empty-profile/) · [Next](../ep11-batch-vs-streaming-vs-edge-segmentation-in-aep/)

## What you will learn

- Explain why an audience is not a list, and why audiences only became trustworthy after identity stitching
- Choose **Build rule** or **Compose audience**, and read the Segment Builder's three panels
- Use the four kinds of logic: attribute, event with a time window, sequential and exclusion
- Build Bloom's relaunch five from a written spec, refusing conditions that do not belong
- Turn a vague request into the decisions hiding inside it
- Read the Profile Query Language (PQL) in **Code view**

## The story so far

Bloom, a wellness brand with 1.2 million customers, is rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch.
In episode 9 the profile store stayed empty, and the team escalated with an evidence chain instead of rebuilding.
Two days later profile ingestion was restored, Farhan re-ingested, and Priya appeared as one profile with three identities (Email, BloomID, ECID).
Now Anjali, the Chief Marketing Officer, asks: who do we talk to first?

## Key ideas

### 1. A list rots; an audience is a living rule
A **list** is a snapshot. The moment you export it, it starts rotting: someone on a "lapsed" list buys tonight and still gets a comeback discount tomorrow. An **audience** is a rule, for example "loyalty band is Gold and three or more orders in the last 12 months". The platform keeps re-evaluating it, so people move in and out on their own. AEP calls these **audiences**; many people still say "segment", and the builder is still the **Segment Builder**.

Audience rules read the merged **Real-Time Customer Profile**, so they only become trustworthy after identity stitching. Unstitched, a shopper who browsed on her phone and bought on her laptop looks like two people, and every rule about her is silently wrong.

### 2. Build rule versus Compose audience
**Create audience** offers two methods:

| Method | What it is | Use it when |
|---|---|---|
| **Build rule** | "Use attributes and events to create an audience". Opens the Segment Builder | Describing people by their data |
| **Compose audience** | A multi-step workflow over audiences you already have | Combining finished audiences (episode 11) |

### 3. The Segment Builder's three panels
- **Left, Fields:** tabs **Attributes** (what is true about this person: state, loyalty band, consent), **Events** (what did they do, and when: ordered, browsed, added to cart) and **Audiences** (who is already in another audience; helper audiences come in episode 17), plus a search box and the **XDM Individual Profile** field tree.
- **Centre, the rule canvas:** "Start building", where you drag fields in.
- **Right, Audience properties:** Qualified profiles, Estimated profiles, Refresh estimate, View profiles, Code view, Apply access labels, Name, Description, Tags and **Evaluation method**, which defaults to **Batch**.

### 4. Four kinds of logic

| Logic | What it looks like at Bloom |
|---|---|
| Attribute | Loyalty band is Gold; email consent is true; home city is Dallas |
| Event with a time window | An order in the last 90 days; 5 or more product views in the last 30 days |
| Sequential | Add-to-cart **not followed by** a purchase within 24 hours |
| Exclusion | 5 or more product views **and zero orders ever** |

Sequential logic needs event order and a clock, which no spreadsheet can express. There is no "cart" object: a cart is add-to-cart events not followed by a purchase. Priya added to cart on her phone at 7:44 PM and bought on her laptop at 7:52 PM, so, once stitched, she never qualifies.

### 5. The relaunch five, from a written spec

| Audience | Rule | Feeds |
|---|---|---|
| High-Value Loyalists | Loyalty band = Gold AND 3+ orders in the last 12 months | Early access |
| Cart Abandoners 24h | Add-to-cart NOT followed by purchase within 24 hours | Cart Rescue (episode 21) |
| Lapsed 90 | Last order more than 90 days ago AND email consent true | Win-back (episode 22) |
| New This Month | FIRST-ever order within the last 30 days | Welcome journey (episode 17) |
| Window Shoppers | 5+ product views in 30 days AND zero orders ever | Nurture |

High-Value Loyalists reads the **derived** loyalty band from episode 5's calculated field (Gold is 1,500 points and above), so in episode 14 a broken band quietly thins it. Every audience stays on Batch for now; episode 11 decides which two must update within minutes.

### 6. Trap conditions
Part of building well is refusing conditions that sound sensible. Five examples (the exercise has the full set):
- **Email opens 3 or more** (loyalists): the platform holds no email opens until Journey Optimizer starts sending, so this would empty the audience.
- **Has an ECID** (loyalists): anyone who opens the Bloom app or website gets one, so it says nothing about value.
- **Home city is Dallas** (loyalists): geography says nothing about value.
- **No orders ever** (lapsed): never-buyers are not lapsed; they never started.
- **Has placed any order, ever** (new this month): nearly every customer has ordered in 18 months of history. "Any" is not "first".

### 7. Consent inside the rule
Ananya never gave email consent, so she can never enter Lapsed 90 or land in the win-back file. The platform enforces this inside the rule, not a checklist. It only works because episode 6 re-mapped the three consent columns from the email and phone status fields, where auto-map first put them, to the `_bloom` consent fields. A rule can only enforce consent it can find in the right field.

### 8. The hidden decisions in a vague brief
"Our good customers in Texas" hides four decisions, each needing an owner in writing before anyone builds:

| Vague word | The decision hiding inside it |
|---|---|
| good | Loyalty band? Lifetime spend? Order count? Over what period? |
| customers | Anyone with a profile, or only people who have bought? |
| in Texas | Home address, billing address, or the shipping address of the last order? |
| (unsaid) consent | Do we hold valid marketing consent? If not, nothing else matters |

The Segment Builder is easy. Agreeing what the audience actually means is the job.

### 9. PQL and Code view
**Code view** shows the rule in **Profile Query Language (PQL)**, the language the builder writes behind the canvas. A rule on one attribute reads:

```
homeAddress.stateProvince = "TX"
```

Adding "and has at least one order" adds a second part that counts order events; you write it in the exercise.

## In the product

Labels as of October 2026.

1. Go to **Customer**, **Audiences**, then click **Create audience**.
2. Choose **Build rule** ("Use attributes and events to create an audience") and click **Create**.
3. In the left **Fields** panel, pick a tab: **Attributes**, **Events** or **Audiences**. Use the search box, or expand **XDM Individual Profile**.
4. Drag a field onto the canvas, for example `homeAddress` then `stateProvince`. Set the operator to **equals** and the value to `TX`.
5. For behaviour, switch to **Events** and add an event condition with a time window. Event rules support sequential logic ("then", "not followed by") on the canvas; check what your own screen shows.
6. On the right, under **Audience properties**, read **Qualified profiles** and **Estimated profiles**, open **Code view** to read the PQL, and fill in **Name** (with your own initials when you practise), **Description** and **Tags**. Leave **Evaluation method** on **Batch** for now.
7. **Save as draft**. In a shared or practice sandbox, never Publish or Activate a practice audience.

## Common mistakes

- Exporting an audience and editing it by hand, which turns it back into a list.
- Building from a vague brief before naming its decisions and their owners.
- Adding a condition because the field exists (email opens before the platform has sent any email).
- Using "any order, ever" when the spec says "first-ever order".
- Forgetting the time window, so an event condition counts a customer's whole history.
- Leaving consent to a send-time checklist instead of putting it in the rule.

## Glossary

| Term | Meaning |
|---|---|
| Audience | A group of profiles defined by a rule that the platform keeps re-evaluating |
| Segment Builder | The AEP canvas for writing audience rules from attributes, events and other audiences |
| Build rule | The Create audience method that opens the Segment Builder |
| Compose audience | The Create audience method that combines audiences you already have |
| Attribute condition | A rule clause on a profile fact, such as loyalty band is Gold |
| Event condition | A rule clause on something that happened, usually bounded by a time window |
| Sequential logic | "Followed by" or "not followed by": rules where the order of events matters |
| Exclusion | Subtracting people who match a condition, such as zero orders ever |
| Evaluation method | How often membership is re-checked: batch, streaming or edge (episode 11) |
| Profile Query Language (PQL) | The rule language the Segment Builder writes for you |
| Code view | The Audience properties button that shows a rule's PQL |

## Exercise

See [exercise.md](exercise.md).

## Further reading

- Audience Portal overview: https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/overview
- Segment Builder UI guide: https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder
- Search Experience League for: Profile Query Language, sequential segmentation

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
