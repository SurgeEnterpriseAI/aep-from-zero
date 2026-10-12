# Exercise 23: Do not burn the list

You will write Bloom's frequency rule as a real business rule and decide where it must live, design quiet hours for customers in two countries, sort addresses into the suppression list or unsubscribed consent, and answer the colleague who wants to send a promotion as Transactional.

## Track A: No Adobe access needed

1. **Write the cap.** Write Bloom's frequency rule as a business rule, naming the **count**, the **period**, the **channel** and the **category**. Then answer:
   - a. Where must it be placed so it covers every marketing message? Give both valid options.
   - b. Why does a correct rule set in **Draft** protect nobody?
   - c. When does the weekly counter reset, in UTC and in India time?
   - d. What happens to a proof sent to a test profile that has already reached the cap?
2. **Design quiet hours.** Bloom has customers in India and in the United States (the sample storefront has customers in Dallas and Austin, Texas). Design one quiet-hours rule:
   - a. The periods (weekly or custom dates; up to 5 periods).
   - b. The time zone: the customer's local time zone, or a fixed one? Why?
   - c. Queue or discard, for each of these: the Bloom Win-Back email, a Cart Rescue v1 reminder, and a one-night sale that ends at midnight.
   - d. What happens to a queued message that is still waiting after 7 days?
3. **Sort ten addresses.** For each address, write **Suppression list**, **Consent (unsubscribe)** or **Neither**, with a reason.

   | # | Address | What happened |
   |---|---|---|
   | 1 | customer01@example.com | The address does not exist; the first email hard-bounced |
   | 2 | customer02@example.com | Clicked the One click Opt-out link in the Bloom footer |
   | 3 | customer03@example.com | Marked a Bloom email as spam |
   | 4 | customer04@example.com | Mailbox full; kept bouncing temporarily, past the retry threshold |
   | 5 | customer05@example.com | Mailbox full once; the next email was delivered |
   | 6 | customer06@example.com | Never gave email consent (like Ananya) |
   | 7 | customer07@example.com | Asked customer care to stop marketing email; the opt-out was recorded on the profile |
   | 8 | customer08@example.com | Added by hand by the operations team after a complaint |
   | 9 | customer09@example.com | Used the unsubscribe button inside their mail app (List unsubscribe) |
   | 10 | customer10@example.com | Email consent true, SMS consent false (like Priya) |

4. **The Transactional loophole.** A colleague wants to send the Win-Back promotion through the Transactional email configuration "so it reaches everyone". Write your two-sentence reply.
5. **The episode's practice question.** The two-a-week cap sits only in a custom rule set. It is activated and selected only on the Bloom Win-Back campaign. The global rule set holds no cap. Can Cart Rescue v1 still send a customer a third marketing email this week? Why?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- This track is **read-only**. Business rules, the suppression list, the allowed list and channel configurations are **sandbox-wide**: a change affects every campaign and journey, including other people's.
- Do not create, activate or edit any rule set, and never edit the **GLOBAL RULE SET**.
- Do not use **Add email or domain** or **Edit suppression rules**, and do not toggle the allowed list.
- Do not click **Update** on a channel configuration, and never click **Activate**, **Publish** or **Send proof**.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. In Journey Optimizer, open **Administration**, then **Business rules**. List the rule sets, their domains (Channel or Journey) and their status. Is there a **GLOBAL RULE SET**, and is it active?
2. Open one rule set **without editing it**. Note each rule's type (**Channel Capping** or **Quiet Hours**), its category and its count or periods. Leave without saving.
3. Open **Administration**, **Channels**, **Email settings**, **Suppression list**. Note the buttons across the top and whether the list holds anything. Change nothing.
4. In the same panel, open the **Allowed list**. Is it Activated or Deactivated? Write one sentence on what that means for test sends in this sandbox.
5. Open **Channel configurations** under **General settings** and read one email configuration: Marketing or Transactional, and is **List unsubscribe** set? Leave without clicking **Update**.

## Check yourself

1. Why is per-journey capping not frequency capping?
2. Name the two kinds of rule set and what each limits.
3. Where does a custom rule set apply, and where does the GLOBAL RULE SET apply?
4. Why does a Draft rule set protect nobody?
5. When does a message count towards the cap?
6. Do caps apply to proofs? To Simulation?
7. What are the two choices for a message that lands in quiet hours?
8. Are unsubscribed people on the suppression list? Where does their choice live?
9. Why must a promotion never go out through a Transactional configuration?
10. Why can one bad month hurt every journey a brand runs?

<details><summary>Check your answers</summary>

**Task 1: the cap**

Rule: count **2**, period **per week** (Reset capping frequency Weekly, Every 1 week), channel **Email**, category **Marketing**, per profile. Built as a **Channel Capping** rule in a Channel rule set.
- a. Either in the **GLOBAL RULE SET**, which applies to all messages, or in an **activated custom rule set selected on every campaign** (Business rules drop-down) **and every journey action** (Add Business Rule). Bloom chose the global rule set, because nobody has to remember to select it.
- b. A Draft rule set applies to nothing, and only activated rule sets can be selected.
- c. Saturday 23:59:59 UTC, which is a little before 5:30 AM on Sunday in India.
- d. Nothing arrives. Caps apply to proofs, so a capped test profile silently gets nothing, with no error.

**Task 2: quiet hours (model answer; any well-reasoned design is fine)**
- a. For example, one weekly period every evening into the morning, such as 9 PM to 8 AM. Up to 5 periods are allowed if weekends need different hours.
- b. The customer's **local** time zone, so one rule covers India and Texas. A fixed India time zone would put US customers' quiet hours in their daytime and let messages through at their night.
- c. Win-Back: **queue** (still useful in the morning). Cart Rescue reminder: **queue** (a morning nudge still helps). One-night sale ending at midnight: **discard** (by morning the offer has expired).
- d. Messages queued for more than 7 days are discarded.

**Task 3: sort ten addresses**

| # | Answer | Why |
|---|---|---|
| 1 | Suppression list | Hard bounce: added immediately |
| 2 | Consent (unsubscribe) | An opt-out lives on the profile, not on the suppression list |
| 3 | Suppression list | Spam complaint: added immediately |
| 4 | Suppression list | Soft bounces past the retry threshold |
| 5 | Neither | One temporary bounce, below the threshold, and consent is unchanged |
| 6 | Consent | No email consent on the profile, so, like Ananya, this person never enters Lapsed 90 |
| 7 | Consent (unsubscribe) | A recorded opt-out on the profile |
| 8 | Suppression list | Manual addition |
| 9 | Consent (unsubscribe) | An unsubscribe, however it is made, is a permission matter |
| 10 | Neither for email | Email consent is true; the SMS "no" is consent on the profile, not suppression |

**Task 4: model reply**
"A Transactional configuration overrides opt-outs, so this would send an offer to people who told us not to, which is a legal problem and a quick way to collect spam complaints that damage our sender reputation. If it sells, it is Marketing, so it goes through the Marketing configuration and reaches only people who can be contacted."

**Task 5: practice question**
Yes. A custom rule set applies only where it is selected. It is selected on the Win-Back campaign only, so Cart Rescue v1's actions are not capped by it, and the global rule set holds no cap. Fix: put the cap in the global rule set, or select the activated set on every campaign and every journey action.

**Track B: what to expect**
You should see a GLOBAL RULE SET (Active, applies to all messages), possibly next to other people's rule sets. The suppression list shows Download CSV, Edit suppression rules, Recent uploads and Add email or domain, and may be empty in a practice sandbox. If the allowed list reads Deactivated, nothing stops a test send from reaching a real inbox. Labels as of October 2026; check what your screen shows.

**Check yourself**
1. A cap inside one journey cannot see other journeys or campaigns, so a customer in five journeys can still get five messages.
2. Channel rule sets limit messages per person (Channel Capping, Quiet Hours); Journey rule sets limit journey entries and concurrent journeys.
3. A custom rule set applies only where it is selected (campaign Business rules drop-down, journey action Add Business Rule), once activated. The GLOBAL RULE SET applies to all messages.
4. A Draft rule set applies to nothing and cannot even be selected.
5. Once it is delivered.
6. Caps apply to proofs. Simulation applies no caps, quiet hours, suppression list, allowed list or consent.
7. Queue message or Discard message.
8. No. Their choice lives on the profile as consent.
9. Transactional overrides opt-outs, so a promotion would reach people who said no.
10. Bounces and complaints damage the sending domain's reputation; a blacklisted domain stops every journey's mail from reaching the inbox.

</details>
