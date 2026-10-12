# Episode 22: Offer Decisioning in AJO: Eligibility & Ranking

**Watch:** Video coming soon on iTV

[Previous](../ep21-abandoned-cart-journey-in-ajo-step-by-step/) · [Next](../ep23-ajo-frequency-capping-quiet-hours-suppression/)

## What you will learn

- Explain **offer, eligibility, ranking and fallback**, and why **a library is not a decision**
- Tell the legacy **Decision Management** from the newer **Decisioning**, and map Bloom's three offers onto decision items, a collection, a selection strategy and a decision policy
- Configure **eligibility** (audience versus decision rule), **priority**, **capping** and **status**, and know that **Approve** is what makes an item servable
- Explain why **Enable decisioning** clears email content, why an **email placement** must exist, and how to protect your work
- Place eligibility deliberately across the **item**, the **strategy** and the **campaign or journey**

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, now in the relaunch fortnight of its loyalty programme. In episode 21 Kavya and Divya built Cart Rescue v1: an event-triggered entry, a four-hour wait, cart items rendered from the event payload, and exit criteria that let Priya leave the moment she bought. Now Anjali, the chief marketing officer, wants margin back: Bloom still gives almost everyone the same 20% discount, even loyal Gold members who would buy anyway.

## Key ideas

### 1. Four words: offer, eligibility, ranking, fallback
Decisioning moves offer logic out of the email and into a governed library. The email asks one question, "what should this customer see?", and the engine answers per person.

| Word | The question it answers | Bloom |
|---|---|---|
| **Offer** (decision item) | What could we say? | 20% Comeback, Early Access Drop, Free Shipping |
| **Eligibility** | Who may see it? | Comeback: Lapsed 90 only. Early Access: Gold only |
| **Ranking** | Of the eligible offers, which wins? | Comeback above Early Access where both qualify |
| **Fallback** | What if nothing qualifies? | Free Shipping |

**Capping** is an optional extra: how many times an offer may be shown. Priority never makes an offer eligible; it only orders the offers a person already qualifies for.

### 2. A library is not a decision
A sandbox can hold twenty approved offers and still show nothing in any email. A list has no rule for choosing and no answer for when nothing fits. A decision needs **eligibility, ranking and a fallback**, delivered into a place in a message. One governed engine replaces dozens of hard-coded campaign variants.

### 3. Two systems in Journey Optimizer

| | Decision Management | Decisioning |
|---|---|---|
| Adobe calls it | Carries a **Legacy** badge | "Our next-generation decision framework" |
| Left menu | Offers, Components | Catalogs, Strategy setup |
| The unit | Personalized offer, plus fallback offers | Decision item, in one catalog called **Offers** |
| Content | A **representation** per placement | Item attributes and fragments |
| Grouping | **Collection qualifiers** (Adobe: "previously known as" tags) | Collections built by **rules** |
| The logic | A **decision** | A **selection strategy** inside a **decision policy** in the message |

The legacy Offers screen also has a **Simulation** tab (it asks for a test profile and a decision scope). Adobe publishes no one-to-one mapping and no end date for Decision Management, so recognise both. Bloom started fresh in Decisioning.

### 4. Decision items
- **Offer name** is the only required field. **Priority** defaults to 1, and the higher number wins among eligible items. Bloom gave Comeback the higher number (illustrative: 20 against 10).
- **Eligibility**: **All visitors**, **Visitors who fall into one or more audiences** (computed earlier, so possibly a little out of date), or **By rule** (a decision rule checked at every decision). Bloom used **Lapsed 90** (episode 10, email consent inside its rule) for Comeback and **Gold Members** (episode 17) for Early Access.
- **Capping** counts decision events (default), clicks, a custom event, or impressions (inbound channels only, so not email); in total or per profile; daily, weekly or monthly, resetting at 12 am UTC (Coordinated Universal Time), week starting Sunday. Up to 10 rules; any one met caps the item.
- **Statuses**: Draft, Approved, Archived. **Approve** makes an item available to the engine; Draft is never served. An approved item in use cannot be deleted until **Undo approve**; an archived item never comes back.
- An item's image and text come from catalog **custom attributes**. Adding them means **Edit schema**, which changes the form for the whole sandbox: a planned, one-time admin change.
- Changes can take **up to 15 minutes** to take effect.

### 5. Collections and selection strategies
A **collection** picks items by rule (up to 500). Adobe says **Contains** works like IN: a list of exact values, not partial text. So read **NUMBER OF ITEMS** before **Create**. Bloom's collection holds Comeback and Early Access (2); Free Shipping joins later as the fallback.

A **selection strategy** is a collection, plus optional eligibility, plus a **ranking method**: **Offer priority** (Bloom's choice), **Formula** (a score you write) or **AI model** (Adobe recommends 1,000 impressions and 100 conversions per item per week, so not for a brand with no offer history).

### 6. Three places eligibility can sit

| Layer | Bloom |
|---|---|
| The item | Lapsed 90 (Comeback), Gold Members (Early Access) |
| The selection strategy | All visitors |
| The campaign or journey's audience | Bloom Win-Back goes to Lapsed 90 |

A rule that belongs to the **offer** goes on the **item**, so it travels wherever the item is reused. If Comeback relied only on the Win-Back audience, reusing the strategy in a newsletter to everyone would hand 20% to every customer.

### 7. Decision policy, placement, fallback, and the switch that wipes an email
A **decision policy** lives inside the message. It names the catalog (only Offers) and the **Number of items**, then runs up to 10 strategies or items in order. **Fallback offers** show when nothing qualifies, regardless of their own dates or eligibility; without one, "nothing will be displayed". An **email decision policy needs a placement**; Bloom had none, so one was created first.

Adobe: enabling decisioning **clears existing email content**, so save a designed email as a **template** first. Kavya nearly flipped it on the finished Bloom Win-Back email, with its fragments, fallback greeting and legal block.

### 8. Bloom's result
Anjali signed off and Divya clicked **Approve**. After the wait, Divya sent a proof to her own address, rendered once for each of the team's test seats:

| Test seat | State | Offer |
|---|---|---|
| TD-DIVYA-03 | Lapsed, email consent true | 20% Comeback |
| TD-KAVYA-01 | Gold | Early Access Drop |
| TD-FARHAN-02 | Silver, recent buyer | Free Shipping (fallback) |
| A lapsed Gold member | Both eligible | 20% Comeback (higher priority) |

In the real Bloom Win-Back send everyone is in Lapsed 90, so Comeback usually wins there; the proofs show all three offers working.

Approving, the decision policy, the email placement, Insert syntax and the send are Adobe's documented steps: **Adobe documents it this way; check what your screen shows.**

Interview line: *"A library is not a decision. Decisioning needs eligibility, ranking and a fallback."* And in three lines: a campaign answers "what do we send?"; a journey answers "what happens to this customer next?"; decisioning answers, inside either, "which offer should this person see?".

## In the product

Labels as of October 2026.

1. Left navigation: **Decision Management** (Offers, Components) and **Decisioning** (Catalogs, Strategy setup).
2. **Decisioning, Catalogs**: catalog **Offers**, buttons **Edit schema** (leave it alone) and **Create item**.
3. **Create offer item**: steps **Attributes**, **Eligibility**, **Review**. Then **Save**; the item opens as **Draft** with **View usage** and **Approve**.
4. **Catalogs, Collections, Create collection**: **Collection rules** (Select attribute, Select operator, value), **Preview collection**, **NUMBER OF ITEMS**, **Create**.
5. **Strategy setup, Selection strategies, Create selection strategy**: **Select collection**, **Eligibility** (All visitors, Audiences, Decision rule), **Ranking method** (Offer priority, Formula, AI model), **Create**.
6. **Strategy setup, Placements, Email**: check a placement exists. An empty list reads **No results found**, with a **Create placement** button.
7. Campaign **Content** tab: **Enable decisioning** sits next to **Content template**. Template first.
8. Adobe's documented policy steps: **Add decision policy**, name, catalog, **Number of items**, strategies or items, fallback, **Next**, **Create**, then **Assign placement** and **Insert syntax**. Adobe documents it this way; check what your screen shows.

## Common mistakes

- Treating a full offer library as a decision.
- Expecting priority to make an offer eligible.
- Leaving items in **Draft** and wondering why nothing shows.
- Leaving a discount on **All visitors** because the campaign audience is already right.
- Clicking **Edit schema** in a shared sandbox.
- A collection that counts 0 because Contains needs exact values.
- Choosing **AI model** ranking with no offer history.
- Switching on **Enable decisioning** in a finished email without a template.
- No email placement, or no fallback.
- Testing straight after Approve, before changes apply.

## Glossary

| Term | Meaning |
|---|---|
| Offer / decision item | One thing a customer could be offered, with eligibility, priority and caps |
| Eligibility | Who may see an offer: all visitors, audiences, or a decision rule |
| Decision rule | A condition checked again every time a decision is made |
| Ranking | The method that chooses among eligible offers |
| Capping | A limit on how often an offer is shown, in total or per profile |
| Fallback offer | What shows when nothing qualifies; without one, nothing is displayed |
| Decision Management | The legacy offer system in Journey Optimizer |
| Decisioning | Adobe's next-generation decision framework |
| Custom attributes | Catalog fields such as an item's image and text; changed through Edit schema |
| Collection | A group of items picked by rules, up to 500 |
| Selection strategy | A collection plus optional eligibility plus a ranking method |
| Decision policy | The container inside a message that asks the engine which offer to show |
| Placement | Where an offer appears in a channel; an email decision policy needs one |
| Approve | The action that makes an item available to the engine |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Journey Optimizer Decisioning, decision items, collections, selection strategies
- Search Experience League for: Journey Optimizer decision policy in email, email placements, enable decisioning
- Search Experience League for: Journey Optimizer Decision Management offers, collection qualifiers

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
