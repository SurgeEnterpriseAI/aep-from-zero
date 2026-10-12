# Exercise 19: The Bloom message kit

You will write Bloom's channel priority policy, design the footer fragment that clears the opt-out warning, and explain why a content template and a Transactional configuration both need care.

## Track A: No Adobe access needed

1. **Write Bloom's channel priority policy** for four message types: the welcome, the cart rescue, a delivery delay and the monthly newsletter. For each one, say which channel goes first, what the fallback is, and whether SMS is ever allowed. Justify every use of SMS in one sentence.
2. **Design the Bloom footer fragment.** Bloom's legal block, colours and tone rules are in the brand sheet, `bloom-brand-sheet.md` in the course data folder. Write down:
   - what it contains
   - the type of its Unsubscribe link
   - its Output Level, and why
   - whether inheritance may be broken, and why
   - whether it is a Visual fragment or an Expression fragment
3. **Fragment or content template?** Bloom has 40 emails already built. Legal changes one line of the company address. Explain what happens if that line lives in a content template, and what happens if it lives in a fragment.
4. **Why does a Transactional configuration need extra care?** Answer in two or three sentences, and give one message that belongs on it and one that never does.
5. **Interrupt or wait?** For each message, choose an interrupting channel (push, email or SMS) or a content card:
   - Priya's balance of 2,340 points
   - "Your order is delayed until tomorrow"
   - A tip on how to use the Vitamin C Serum
   - A welcome after a first order
6. **The episode's practice question.** A footer was never locked, and a teammate clicks the unlock icon to fix a typo in one email. What happens to that email when Legal changes the footer next month, and what should she have done instead?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production, and only objects that carry **your own initials**.
- Never click **Publish** on a fragment, never edit or **Modify** a fragment you did not create, and never click the **unlock icon** in someone else's email.
- Under Administration, open screens only to read them. Never click **Update** on a channel configuration.
- Never click **Activate**, **Publish** (journeys) or **Send proof**. In a shared sandbox: look, screenshot, leave.

Steps:
1. Open **Content Management**, then **Fragments**. Read the list: note each fragment's status (Draft or Live) and type (Visual or Expression).
2. Open one existing fragment and use **Explore references** to see which emails use it. Change nothing.
3. Click **Create fragment**. Name it with your initials, for example `AB - Bloom footer practice`, choose **Visual fragment**, and click **Create**.
4. In the designer, drag a structure onto the canvas first, then a **Text** component into it. Type an address line and the word Unsubscribe.
5. Select Unsubscribe and read the link **Type** options and the **Output Level** options in the **LINK** panel. Read the **Fragment inheritance** choices in the right panel. **Save** and leave it in **Draft**.
6. Optional, read-only: open **Administration**, **Channels**, **Channel configurations**, and note whether the email configuration is Marketing or Transactional and what List unsubscribe holds. Leave without clicking **Update**.

## Check yourself

1. What does a channel configuration hold, and who sets it up?
2. What does "Transactional overrides opt-outs" mean for a customer who unsubscribed?
3. What is Bloom's default channel priority, and why is SMS last?
4. When should a message be a content card instead of a push?
5. What is the difference between a fragment and a content template?
6. What are the three statuses of a fragment, and what happens if a Draft fragment sits in an email at publish?
7. What does the unlock icon do, and how do you stop it for a legal footer?
8. What is the difference between Output Level Identity and Output Level Channel?
9. Why does a Landing page link not record an opt-out on its own?
10. Where may proofs and seed sends go?

<details><summary>Check your answers</summary>

**Task 1: a model channel priority policy**

| Message | First | Fallback | SMS? |
|---|---|---|---|
| Welcome after a first order | Push, if the customer has the app and allows notifications | Email | Never: it is not time-critical |
| Cart rescue | Push for app users | Email | No: it is a marketing nudge, not a time-critical service message |
| Delivery delay | Push | Email | Yes, if push cannot reach the customer: it is a time-critical service message. It goes through a Transactional configuration, so check with Legal which consent rules apply to service texts |
| Monthly newsletter | Email | A short content card for app users | Never |

Reasonable policies differ. What matters is that the order is written down before anything is built, that one message goes by one channel, and that SMS is justified every time it is used. (In the story, Bloom Welcome v1 stays one email per path for relaunch Monday, because that is the version the team tested; its push version waits in the message kit.)

**Task 2: the Bloom footer**
- Contents: the legal block from the brand sheet (company address) and one word, Unsubscribe.
- Link type: **One click Opt-out**, with an optional confirmation page.
- Output Level: **Channel**, because a customer who clicks Unsubscribe means stop, not "stop at this one address". Identity is defensible only if you can explain why one address should keep receiving offers.
- Inheritance: **Prevent inheritance from being broken**, because a legal footer that drifts in one email is exactly the one that fails an audit.
- Type: a **Visual fragment**, built in the Email Designer, email only.

**Task 3: template or fragment**
- Content template: an email copies it as a starting point, so the 40 built emails keep the old line. Someone must fix 40 emails by hand.
- Fragment: emails reference it, so one edit to the fragment reaches all 40, live ones included, unless someone broke inheritance in one of them.

**Task 4: Transactional**
Transactional overrides opt-outs, so a Transactional configuration can mail people who unsubscribed from marketing. That is right for an order receipt or a delivery delay, and wrong for a promotion, which would be mailing people who said no. An administrator owns the configuration, and the type must match the message.

**Task 5: interrupt or wait?**
- Points balance: content card. Worth saying, not worth interrupting for.
- Order delayed: interrupt. It is time-critical service information (push first; SMS only if the policy allows it).
- Serum tip: content card.
- Welcome: interrupt, by the written priority (push or email). It is the first message a new customer gets.

**Task 6: practice question**
The unlock icon breaks inheritance, so that email keeps a frozen copy of the footer. Next month's legal change reaches every other email but not this one, which now carries an outdated legal block. She should have fixed the typo once, in the fragment itself, so every email inherits it. Setting the footer to **Prevent inheritance from being broken** stops this from happening.

**Check yourself**
1. The email type (Marketing or Transactional), the sending subdomain, the IP pool, the sender, and List unsubscribe. An administrator sets it up; marketers only select it.
2. Their opt-out is not applied, so they may still receive Transactional messages.
3. Push, then email as the fallback, then SMS only for time-critical service messages. SMS costs money per message and customers tolerate irrelevant texts least.
4. When it is worth saying but not worth interrupting for, such as a balance, a tip or a nudge.
5. A fragment is referenced, so changes flow to every email using it; a template is copied, so changes reach nothing already built.
6. Draft, Publishing, Live. Adobe documents that it raises an error when the campaign or journey is published.
7. It breaks inheritance in one email, freezing its copy. Set the fragment to Prevent inheritance from being broken.
8. Identity stops mail to the one address that clicked; Channel stops marketing email to every address on the profile.
9. The click only opens the page. An opt-out form on that page records the choice: Adobe's two-step opt-out.
10. Only to your own inbox.

</details>
