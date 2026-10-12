# Episode 23: AJO Frequency Capping, Quiet Hours, Suppression

**Watch:** Video coming soon on iTV

[Previous](../ep22-offer-decisioning-in-ajo-eligibility-ranking/) · [Next](../ep24-ajo-journey-not-sending-triage-with-step-events/)

## What you will learn

- Configure a **frequency cap** that covers every marketing message, and know when it resets and why it can block a proof
- Explain where a **rule set** applies: the **GLOBAL RULE SET**, or an activated rule set selected on every action
- Set **quiet hours** in the customer's time zone, and choose **Queue message** or **Discard message**
- Tell the **suppression list** from an **unsubscribe** (consent), and spot the **Transactional** loophole
- Explain **deliverability** basics: sender reputation, domain blacklisting and **IP warm-up**

## The story so far

Bloom, a wellness brand with 1.2 million customers, is in its loyalty relaunch fortnight. In episode 22 three approved offers (20% Comeback, Early Access Drop, Free Shipping as the fallback) went into one decision policy in the Bloom Win-Back email. Then Anjali Mehta, the Chief Marketing Officer, read about a rival brand that spammed its customers into unsubscribing, and asked: "Can that happen to us?" Bloom Welcome v1 is live, Cart Rescue v1 is built, and nobody has counted how many emails one person gets in a week.

## Key ideas

### 1. Business rules: Channel and Journey rule sets
Adobe Journey Optimizer (AJO) calls its guardrails **business rules**. They live under **Administration, Business rules**, grouped into **rule sets**:

| Rule set | What it limits | Rules inside |
|---|---|---|
| Channel rule set | Messages per person | **Channel Capping**, **Quiet Hours** (category **Marketing**) |
| Journey rule set | Journeys per person | Journey entries, concurrent journeys |

A journey's own settings, such as Cart Rescue v1's re-entry limit, cover only that journey. Business rules look across everything.

### 2. Per-journey capping is not capping
A cap inside one journey cannot see the others, so a customer in five journeys can still receive five messages. Agree the cap as a business rule **first**: **count, period, channel, category**.

Bloom's rule: **at most 2 marketing emails per profile per week.** Two used to be the schedule; now it is the ceiling.

Interview line: *"Frequency capping applied per journey is not frequency capping."*

### 3. Where a rule set applies (the detail that catches teams out)
- A **Draft** rule set applies to nothing. Only **activated** rule sets can be selected.
- A **custom** rule set applies **only where it is selected**: in a campaign's **Business rules** drop-down (Adobe documents it on the **Actions** tab; check what your screen shows), or on a journey action through **Add Business Rule**.
- The **GLOBAL RULE SET** applies to all messages, with no selecting.
- A sandbox allows at most **10 rule sets per domain**. Here "domain" means the rule set's kind, Channel or Journey, not an email sending domain.

So "two a week across everything" means the cap sits in the **global rule set**, or in an **activated custom rule set selected on every campaign and every journey action**. Bloom chose the global rule set: nobody has to remember to select it.

### 4. Resets, delivery and proofs
- Counters reset in **Coordinated Universal Time (UTC)**: end of the hour (hourly), 23:59:59 (daily), Saturday 23:59:59 (weekly), month end (monthly). In India, the weekly reset falls a little before 5:30 AM on Sunday.
- A message counts **once it is delivered**. Schedule sends at least **10 minutes** ahead.
- **Caps apply to proofs.** A test profile that has reached its cap silently gets nothing: no error, no email.
- **Simulation** applies no suppression list, allowed list, consent, frequency caps or quiet hours, so a delivered simulation proves the journey, not the guardrails.

### 5. Quiet hours
A send at 09:00 server time is a 03:00 message for somebody.
- **Quiet Hours** is a rule type in a Channel rule set.
- Weekly or custom dates, **up to 5 periods**.
- The customer's **local** time zone, or a **fixed** one.
- **Queue message** (send when quiet hours end) or **Discard message**. Messages queued for more than **7 days** are discarded.

Illustrative: Cart Rescue v1 waits 4 hours, so a cart abandoned at 8 PM makes the reminder due at midnight. With quiet hours of, say, 9 PM to 8 AM local time and **Queue message**, it waits until 8 AM. Queue what still makes sense tomorrow; discard what expires.

### 6. Suppression list versus unsubscribe
| | Suppression list | Unsubscribe (consent) |
|---|---|---|
| A matter of | Deliverability | Permission |
| Who | Hard bounces and spam complaints (immediately), repeated soft bounces past the retry threshold, manual additions | People who opted out |
| Where | Administration, Channels, Email settings, Suppression list | Consent on the profile |

**Unsubscribed people are not on the suppression list.** Their choice lives on the profile as consent, and Journey Optimizer removes them from future marketing messages. At Bloom, Ananya never gave email consent, so she never enters Lapsed 90, and she is on no suppression list.

**Consent is a state, not a checkbox:** it has a source, a timestamp, a scope and a lifecycle, and it must be enforced, not merely recorded. The **allowed list** (episode 18) is different: a test-only guard in non-production sandboxes. When it is Deactivated, nothing stops a real send.

### 7. The Transactional loophole
A **channel configuration** is the admin-owned sending set-up. Its email type is **Marketing** (opt-outs respected) or **Transactional** (opt-outs overridden, and the screen warns you), which is for receipts and service notices. Sending a promotion through it mails people who said no. **If it sells, it is Marketing.**

The configuration also holds **List unsubscribe** (a Mailto address plus a one-click URL in the mail client). Adobe recommends both, together with an unsubscribe link in the body.

### 8. Deliverability as a design constraint
Mailbox providers decide whether mail reaches the inbox, largely from the **sending domain's reputation**: earned slowly, destroyed quickly. Bounces and spam complaints damage it, which is why the suppression list exists. The channel configuration names the subdomain and the **IP pool** (the internet protocol addresses mail leaves from). A new domain or IP has no reputation, so teams **warm it up**: small volumes first, raised gradually. **One bad month can blacklist a domain**, and then a technically perfect journey reaches nobody.

## In the product

Labels as of October 2026. Everything here is sandbox-wide: read it, do not change it.

1. **Journey Optimizer**, **Administration**, **Business rules**: the rule sets list, including **GLOBAL RULE SET** (Active, applies to all messages).
2. How a capping rule is built (read along; do not repeat in a shared sandbox): create a rule set with domain **Channel**, then **Create Rule**. **Rule type** **Channel Capping** (the other type is **Quiet Hours**); category fixed to **Marketing**; **Capping count** 2, **Reset capping frequency** Weekly, **Every** 1 week, channel **Email**. Ticking several channels makes one combined count.
3. Using a rule set: a campaign's **Business rules** drop-down (Adobe: on the **Actions** tab; your screen may instead list it in the **Properties** card of Review to activate, as "No rule sets selected"), or a journey action's **Add Business Rule**. Only activated rule sets appear.
4. **Administration**, **Channels**, **Email settings**, **Suppression list**: **Download CSV**, **Edit suppression rules** (changes the retry threshold for the whole sandbox), **Recent uploads**, **Add email or domain**. The **Allowed list** is in the same panel.
5. **Administration**, **Channels**, **General settings**, **Channel configurations**: email type Marketing or Transactional, subdomain, IP pool, **List unsubscribe**. It opens in edit mode with an **Update** button: leave without clicking it.

## Common mistakes

- Capping inside one journey and calling it frequency capping.
- Leaving the rule set in **Draft**.
- Selecting a custom rule set on only some campaigns and journey actions.
- Forgetting that counters reset in UTC, not India time.
- Blaming the email when a proof to a capped test profile never arrives; trusting Simulation to prove guardrails.
- One fixed time zone for customers in India and the United States.
- Searching the suppression list for an unsubscribed customer and concluding the opt-out failed.
- A promotion sent as Transactional "so it reaches everyone".
- Treating deliverability and IP warm-up as an admin detail for later.

## Glossary

| Term | Meaning |
|---|---|
| Business rule | A guardrail such as frequency capping or quiet hours, applied across messages |
| Rule set | A container of business rules; Channel or Journey |
| Channel Capping | A rule limiting marketing messages per person per period |
| GLOBAL RULE SET | The rule set that applies to all messages without being selected |
| Quiet hours | Periods when marketing messages are queued or discarded, in local or fixed time |
| Suppression list | Addresses Journey Optimizer never mails, because of bounces, spam complaints or manual addition |
| Unsubscribe | A customer's opt-out, stored on the profile as consent |
| Allowed list | A test-only guard in non-production sandboxes limiting who test mail can reach |
| Channel configuration | The admin-owned sending set-up: Marketing or Transactional, subdomain, IP pool |
| List unsubscribe | An unsubscribe option inside the mail client: Mailto plus one-click URL |
| Sender reputation | How much mailbox providers trust a sending domain and IP |
| IP warm-up | Starting a new sending IP or domain on small volumes and raising them gradually |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Journey Optimizer business rules, frequency capping rules, quiet hours, suppression list, allowed list, channel configuration, deliverability best practices

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
