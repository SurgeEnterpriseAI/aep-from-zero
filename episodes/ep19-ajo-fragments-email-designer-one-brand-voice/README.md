# Episode 19: AJO Fragments & Email Designer: One Brand Voice

**Watch:** [Watch episode 19 on YouTube](https://youtu.be/dG-Dk6OH8OY)

[Previous](../ep18-ajo-test-mode-vs-simulation-vs-dry-run-vs-proof/) · [Next](../ep20-ajo-personalization-tutorial-fallback-if-else/)

## What you will learn

- Explain what a **channel configuration** holds, and the difference between **Marketing** and **Transactional**
- Decide and document a **channel priority** for a message
- Build **header and footer fragments**, publish them, and understand **inheritance**
- Add a compliant unsubscribe with the right **link type** and **Output Level**
- Choose between a **fragment**, a **content template**, an in-app **content card** and a channel that interrupts

## The story so far

Bloom, the wellness brand, is days away from relaunch Monday. In episode 18 the team tested **Bloom Welcome v1** safely on their own test seats: Test mode sent even Rohan's Silver seat down the Gold path, Dry run proved the other path, and Rohan's empty-name seat exposed a greeting of "Hi ,". The journey still showed one warning: no opt-out link. Now the brand team fears that email, push and SMS will make Bloom "look like a different company" on every channel.

## Key ideas

### 1. One message, several channels, one owner
The content of a message and the channel it goes out on are two separate decisions. Write the message once, in the brand's tone, then shape it per channel: email needs a subject line and a body, push a short title and body, and SMS (short message service) has a hard character budget. Run each channel as its own project and you get three tones of voice and three sets of mistakes. One voice needs **one owner** who reviews across channels.

### 2. The channel configuration: Marketing or Transactional
Every email in Adobe Journey Optimizer (AJO) goes through a **channel configuration**, the admin-owned sending set-up for a channel. An administrator builds it once; marketers only select it. Its **email type** is:
- **Marketing**: opt-out preferences apply, so people who unsubscribed are left out. Offers, welcomes, thank-yous, win-backs.
- **Transactional**: for service messages such as an order receipt. **Transactional overrides opt-outs**, so unsubscribed people may be mailed.

It also holds the sending subdomain, the IP (internet protocol) pool, and **List unsubscribe**: an unsubscribe option inside the mail app (Mailto plus a one-click link). Adobe recommends both, plus a link in the email body.

### 3. Channel priority is a written business decision
If a customer has push enabled, the same promotional message usually should not also go by email. Bloom's default priority, written down before anything was built:
1. **Push**, for customers who use the app and allow notifications
2. **Email**, as the fallback
3. **SMS** only for time-critical service messages, because every SMS costs money and customers tolerate an irrelevant text far less than an irrelevant email

Every extra channel multiplies the consent you must respect: Priya Sharma's email consent is true but her SMS consent is false, so a marketing text must never reach her.

A welcome is never time-critical, so it never goes by SMS. In the story, Bloom Welcome v1 stays one email per path for relaunch Monday, as tested; its push version waits in the message kit.

### 4. Content cards: worth saying, not worth interrupting for
Email, push and SMS interrupt. **Content cards** are in-app messages that wait until the customer is already in the app: high relevance, zero interruption cost, and they persist beyond the short life of a push notification (the inbox pattern). Use them for a loyalty balance, a recommendation or a nudge. Priya's 2,340 points belong on a card, not in a text.

### 5. Fragments: build once, change once, every email follows
A **fragment** is a reusable content block, such as a header, a footer or a legal block, that many emails **reference**. Change it once and every email using it changes, live ones included.

There are two kinds: a **Visual fragment** is built by drag and drop in the Email Designer and works in email only; an **Expression fragment** is written as code and works in most channels, but not in-app.

**Fragment or content template?**

| | Fragment | Content template |
|---|---|---|
| What it is | A block emails reference | A starting point emails copy |
| Change it later | Every email using it updates | Emails already built do not change |
| Use it for | Footer, legal text, brand header | A standard layout to start from |

Somebody must own the library of approved blocks (the **module library**), or it rots. At Bloom, Divya does.

### 6. The fragment lifecycle: Draft, Publishing, Live
A new fragment is **Draft**. **Publish** moves it to **Publishing** and then **Live**. Publishing a fragment sends nothing to anyone; it makes this version the one emails use. Adobe documents that a **Draft fragment inside an email raises an error when the campaign or journey is published**, so fragments that emails rely on must be Live first.

### 7. Inheritance and the lock that protects legal footers
Every email using a fragment **inherits** each edit made to it. Inside an email, the broken-chain icon (Adobe calls it the **unlock icon**) breaks that link: the email keeps a frozen copy and stops receiving updates. A fragment's **Fragment inheritance** setting offers **Allow inheritance to be broken** or **Prevent inheritance from being broken**. Bloom locks its legal footer, and leaves the header open to local changes such as a seasonal banner.

### 8. One click Opt-out and Output Level
A marketing email without an unsubscribe link raises the warning "The opt-out link is not present in the email body". The fix is a footer fragment whose Unsubscribe link has the type **One click Opt-out**, with an optional confirmation page.

**Output Level** decides how far that click reaches:
- **Identity** stops mail to this one address
- **Channel** stops marketing email to every address on the profile

Bloom chose **Channel**: stop means stop.

Other link types, and who records the choice:

| Link type | Who records the choice? |
|---|---|
| One click Opt-out | The click itself |
| External Opt-out/Unsubscription, External Opt-in/Subscription | Your own page, which must record it |
| Landing page | Only an opt-out form on that page (Adobe's two-step opt-out) |
| Mirror page, Deeplink, External link | Nobody: ordinary links, not consent actions |

## In the product

Labels as of October 2026.

1. **Read a channel configuration:** Administration, Channels, Channel configurations (some screens show a General settings level before it), then open the email configuration. Read the email type, the warning that Transactional overrides opt-outs, and List unsubscribe. The screen opens in edit mode with an **Update** button: leave without clicking it.
2. **Create a fragment:** Content Management, Fragments, **Create fragment**. Name, description, **Visual fragment** (channel Email), **Create**. In **Components**, drag a structure (for example a 1:1 column) onto the canvas first, then **Text** into it. **Save**.
3. **Add the unsubscribe:** select the word Unsubscribe. In the **LINK** panel set **Type** to **One click Opt-out**, add a confirmation page if you want one, choose the **Output Level**, then **Save**.
4. **Lock it:** in the right panel's **Fragment inheritance**, choose **Prevent inheritance from being broken** for a legal footer.
5. **Publish:** on the fragment page click **Publish**. The status goes Draft, Publishing, **Live**.
6. **Use it:** open the email body. In the left rail click the **Fragments** icon (second from the top) and drag the fragment into place. Click it once: the right panel shows its ID, **Open fragment** and **Explore references** (every email that uses it). Do not click the unlock icon.
7. **Check:** each email needs the footer itself. Confirm with **Explore references**, then read the journey's **Alerts**. Proofs and seed sends go only to your own inbox.

## Common mistakes

- Sending a promotion through a **Transactional** configuration to dodge opt-outs.
- Letting whoever builds the journey choose the channel, instead of a written priority.
- Pasting the footer into each email by hand instead of using a fragment.
- Leaving a fragment in **Draft** while an email that uses it is about to be published.
- Clicking the **unlock icon** to fix one email, so that email's legal footer stops receiving updates.
- Making Unsubscribe an ordinary link, or leaving **Output Level** as you found it without deciding what the click means.
- Sending proofs to a colleague's address, or never opening them on a phone.

## Glossary

| Term | Meaning |
|---|---|
| Channel configuration | The admin-owned sending set-up for a channel: Marketing or Transactional, subdomain, sender, List unsubscribe |
| List unsubscribe | An unsubscribe option inside the mail app itself (Mailto and one-click link) |
| Channel priority | The agreed order in which channels are tried for a message |
| Content card | A non-interrupting in-app message that waits until the customer is in the app |
| Fragment | A reusable content block; change it once and every email using it changes |
| Content template | A starting point an email copies; later changes do not reach built emails |
| Inheritance | Emails receiving every edit made to a fragment they use |
| Unlock icon | The broken-chain icon that breaks inheritance in one email |
| One click Opt-out | A link type that unsubscribes the customer in one click |
| Output Level | How far an opt-out reaches: Identity (one address) or Channel (every address on the profile) |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

Search Experience League for: Journey Optimizer fragments, content templates, one click opt-out, list-unsubscribe, channel configuration, content cards, email proofs.

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
