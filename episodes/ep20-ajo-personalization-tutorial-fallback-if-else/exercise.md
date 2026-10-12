# Exercise 20: Write the fallback first

You will fix broken greetings, write an if-else line on a Bloom loyalty field, predict what a conditional-content block really shows, choose between a content variant and a journey branch, and catch copy that disagrees with its audience.

## Track A: No Adobe access needed

1. **Fix three broken greetings.** Rewrite each one so it can never render `Hi ,` or start with a bare comma. Write the fallback version first, then the personalised one.
   - a) `Hi {{profile.person.name.firstName}},`
   - b) `Dear {{profile.person.name.firstName}} {{profile.person.name.lastName}},`
   - c) A subject line: `{{profile.person.name.firstName}}, your Bloom picks are here`
2. **Write the if-else line.** Using Bloom's loyalty field `profile._bloom.loyalty.tier`, write one line that shows Gold members an early-access perk and everyone else a nudge to reach Gold. Then list **two ways** the Gold text could silently never appear for a real Gold member.
3. **Predict the conditional content.** A component has conditional content switched on.
   - **Block 1.** Default variant: "As a Gold member, you get early access to every new launch." Variant - 1: "Reach Gold to unlock early access." Variant - 1's condition was opened in the builder but never saved. Who sees which text? What does the generated code say?
   - **Block 2.** Variant - 1 (condition: tier equals Gold): the Gold perk. Variant - 2 (condition: tier equals Silver): "You are close to Gold." Default variant: "Welcome to Bloom rewards." What do a Gold, a Silver, a Bronze and an empty-tier profile each see?
4. **Variant or branch?** For each scenario, choose a content variant or a journey branch (or a different journey), and give the reason in one line. Scenarios marked "say, for example" are illustrative.
   - a) Gold members see a different perk sentence in the thank-you email.
   - b) Lapsed customers should get a win-back message instead of a thank-you.
   - c) Say, for example, skincare buyers see a skincare tip and supplement buyers a supplement tip, in the same welcome email.
   - d) Say, for example, Gold members should get a push message first while everyone else gets an email.
   - e) Say, for example, Gold members should wait two days before the next step and everyone else five.
5. **Find the copy that disagrees with its audience.** This draft goes to **New This Month** (first-ever order within the last 30 days). Mark every line that is false for part of the audience, and every place that can break on missing data.

   ```
   Subject: {{profile.person.name.firstName}}, thanks for years of loyalty
   Hi {%= profile.person.name.firstName ?: "there" %},
   Your first Bloom order is on its way.
   As a Gold member, you get early access to every new launch.
   We missed you! It has been a while since your last order.
   Here is how to get the most from your Vitamin C Serum.
   ```
6. **The episode's practice question.** Say, for example, a Gold customer with a real first name receives `Hi there` and the reach-Gold nudge. What two things do you check first?

## Track B: If you have a development sandbox (optional)

Safety first:
- Work only in a **development** sandbox, in **your own draft** campaign or email named with **your initials**.
- **Never** click **Activate**, **Publish** or **Send proof**. Simulate content is enough for this exercise.
- Use **your own** test profiles only (IDs starting `TD-`, `@example.com` addresses). Never a real customer.
- Do **not** click **Save condition**: it adds the rule to a library the whole organisation shares. Leave the builder with **Cancel**. (Divya saves conditions in Bloom's own sandbox; in a shared one, use the typed if-else line in step 3 instead.)
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Open your own draft, then the **Content** tab, then **Edit email body**.
2. Change the greeting to a fallback version. Try the personalisation editor's ellipsis and **Insert with fallback text**, and compare what it writes with what you would have typed.
3. Add a **Text** component and type an if-else line on your sandbox's loyalty field. Read the exact path, with its tenant prefix, from a real test profile's attributes first. **Save**.
4. Optional, look only: select a component, click **Enable conditional content**, look at the **Default variant** and **Variant - 1**, open the condition builder, then **Cancel**. If the designer shows you its code, find what an unsaved condition becomes.
5. Click the arrow next to **Simulate content**, choose **Simulate content (AEP profiles)**, add two of your own test profiles under **Manage test profiles** (one that matches your condition, one that does not), and switch with **Test profile name**.
6. Screenshot both versions. Read every static line and the subject: is each one true for both profiles?

## Check yourself

1. What does a plain value token print when the field is empty?
2. What does "write the fallback first" force you to do?
3. How many equals signs does a PQL comparison use?
4. Name two reasons a token renders blank when the customer's data is fine.
5. In conditional content, when does the Default variant show?
6. What does a variant with no saved condition turn into, and who sees it?
7. Why was "You are one of our Gold members" true in the real campaign but wrong in Kavya's draft?
8. When do you choose a journey branch over a content variant?
9. Give one situation where you should not personalise at all.

<details><summary>Check your answers</summary>

**Task 1: three greetings**
- a) `Hi {%= profile.person.name.firstName ?: "there" %},` gives `Hi Priya,` or `Hi there,`.
- b) Two fields that can each be empty make a fragile greeting (`Dear  ,` or `Dear Priya ,`). Use the first name only, with a fallback: `Hi {%= profile.person.name.firstName ?: "there" %},`. "Dear Valued Member" is not a good fallback, because nobody talks like that.
- c) The subject opens with a bare comma when the name is empty. Either `Hi {%= profile.person.name.firstName ?: "there" %}, your Bloom picks are here`, or drop the name: `Your Bloom picks are here`. Subject lines need fallbacks too.

**Task 2: the if-else line (one good answer)**
```
{%#if profile._bloom.loyalty.tier = "Gold"%}As a Gold member, you get early access to every new launch.{%else%}Reach Gold to unlock early access to new launches.{%/if%}
```
Ways the Gold text can silently never appear: a wrong or missing tenant prefix (`profile.bloom...`, or a prefix copied from another company's example); wrong case in the path (`Loyalty`); comparing against a value that is not spelled exactly as stored. Simulate on a real Gold test profile catches all three. Also check the syntax itself: PQL compares with a single `=`, not `==`.

**Task 3: conditional content**
- Block 1: Variant - 1's unsaved condition is generated as `{%#if false %}`, so it can never show. **Everyone**, Gold or not, falls through to the Default variant and is promised the Gold perk: a confidently wrong email. Safer: the perk in a variant with a saved Gold condition, the nudge in the Default.
- Block 2: Gold sees the Gold perk (Variant - 1). Silver sees "You are close to Gold." (Variant - 2). Bronze and the empty-tier profile match no added variant, so they see the Default: "Welcome to Bloom rewards."

**Task 4: variant or branch**
- a) Content variant: same intent, different detail.
- b) Branch or a different journey: the intent differs (thank versus win back).
- c) Content variant: same welcome, different detail.
- d) Journey branch: the channel of the next step differs.
- e) Journey branch: the wait differs, so what happens next differs.

**Task 5: copy that disagrees**
- Subject: "thanks for years of loyalty" is false for first-time buyers, and the name token has no fallback, so an empty name opens with a comma.
- "As a Gold member..." is a static tier claim; most new customers are not Gold. Move it inside a Gold condition or remove it.
- "We missed you! It has been a while..." is false for people who ordered within the last 30 days. It is win-back copy, a different intent.
- "Here is how to get the most from your Vitamin C Serum" assumes everyone bought that serum. Unless it is driven by their real order, keep it generic.
- The greeting and "Your first Bloom order is on its way" agree with the audience.

**Task 6: practice question (one good answer)**
Both symptoms usually point at the email, not the customer. First, check the field paths: the case, and the tenant prefix on the tier path (standard fields such as the first name have none). Second, read the stored values on that customer's profile, the first name and the tier exactly as stored, and compare them with what the email expects. Then preview the fix on a Gold test seat.

**Check yourself**
1. Nothing, so the text around it, such as a comma, is left behind.
2. Make the message work without the data, which is what some customers will receive.
3. One: `=`.
4. Wrong case in the field path, and a wrong or missing tenant prefix.
5. Only when none of the added variants matches.
6. `{%#if false %}`; nobody ever sees it.
7. The real campaign goes to High-Value Loyalists, an all-Gold audience. Kavya's draft added an "everyone else" line, so the static Gold claim became false for non-Gold readers.
8. When the intent differs, or when what happens next differs (a different wait or channel).
9. When the inference is weak, for example guessing a skin concern from a single product view. Generic is safer than confidently wrong.

</details>
