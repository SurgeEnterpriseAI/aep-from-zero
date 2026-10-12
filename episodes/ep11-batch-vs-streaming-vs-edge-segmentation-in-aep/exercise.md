# Exercise 11: Choose the rhythm, smell-test the numbers

You will choose an evaluation method for each of Bloom's relaunch five, audit the old consultants' estimates, and practise the two habits from this episode: the "react within minutes?" question and the estimate as a quality gate.

The relaunch five, for reference (estimates are out of Bloom's 10,000-customer extract):

| Audience | Rule | Feeds |
|---|---|---|
| High-Value Loyalists | Loyalty band Gold AND 3+ orders in last 12 months | Early access, Gold Thank-You |
| Cart Abandoners 24h | Add-to-cart NOT followed by purchase within 24 hours | Cart Rescue |
| Lapsed 90 | Last order more than 90 days ago AND email consent true | Win-Back |
| New This Month | First-ever order within the last 30 days | Welcome journey |
| Window Shoppers | 5+ product views in 30 days AND zero orders ever | Nurture |

## Track A: No Adobe access needed

1. **Assign the rhythm.** For each of the relaunch five, choose batch, streaming or edge. Justify each one in a single sentence that answers: will a journey need to react to this within minutes?
2. **Smell-test the old estimates.** The previous consultants' drafts estimated, out of 10,000 customers:
   - High-Value Loyalists 1,180
   - Cart Abandoners 24h 214
   - Lapsed 90 3,890
   - New This Month 9,930
   - Window Shoppers 640

   Name the implausible one. Then pick the right diagnosis from these four and explain why the other three are wrong:
   - a. The 30-day window is too long for a monthly audience.
   - b. The rule matched any order, ever, instead of the first-ever order in the last 30 days.
   - c. Streaming evaluation double-counts profiles as they re-qualify.
   - d. The estimate includes anonymous profiles that carry only an ECID (Experience Cloud ID).
3. **Reply to "streaming, to be safe".** A colleague wants every audience on streaming "to be safe". Write your reply in two sentences.
4. **Stop the overlap.** Window Shoppers and New This Month are meant to be separate. Describe one way a person could end up in both, and two things you would do about it.
5. **Read a zero.** A new audience shows an estimate of about 0, and the line under it reads "Last updated: Not available". List, in order, what you check before you change the rule.
6. **Qualified or estimated?** Your manager asks how many people are in Lapsed 90 right now. Which number do you quote, which do you not quote as membership, and why?
7. **The episode's practice question.** A colleague wants Lapsed 90 on streaming, to be safe. What do you tell them, in two sentences?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production, and only objects that carry **your own initials**.
- Do **not** touch the **Schedule all audiences** toggle. It is sandbox-wide and affects every audience, including other people's.
- Never **Save** someone else's audience, even if you changed nothing. Press **Cancel** to leave it.
- Nothing here needs **Activate**, **Publish** or any send. Do not click them.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Go to **Customer**, **Audiences**, **Browse**. Find your own draft audience from episode 10 (for example "Texas customers" plus your initials). If you do not have one, skip to step 6.
2. Open it in the Segment Builder. In **Audience properties**, write down the **Qualified** and **Estimated** numbers and the **Last updated** line.
3. Press **Refresh estimate**. Write down what changed, if anything.
4. Look at the **Evaluation method** field and its options. Your rule uses only a profile attribute (home state). Is **Streaming** offered? Write down what you see, then press **Cancel** without saving any change.
5. Open **Code view** and copy the PQL into your notes.
6. In **Browse**, find one audience whose evaluation method is batch and one that is streaming, if any exist. Read their rules (look only) and say whether the "react within minutes?" question supports each choice.

## Check yourself

1. What is an evaluation method, and what is the default?
2. Which two of the relaunch five are streaming, and what business moment justifies each?
3. Name two reasons why streaming everything is a mistake.
4. What changed in 2026 for rules that use only profile attributes?
5. What does "if the builder won't offer Streaming for your rule, the platform is telling you something" mean in practice?
6. What is the difference between Qualified and Estimated?
7. Why is a zero estimate on an empty profile store not proof of a wrong rule?

<details><summary>Check your answers</summary>

**Task 1: the rhythm**

| Audience | Method | Reason |
|---|---|---|
| High-Value Loyalists | Batch | Value changes slowly; a daily refresh is plenty |
| Cart Abandoners 24h | Streaming | The rescue journey has hours, not days, before the cart goes cold |
| Lapsed 90 | Batch | A person becomes lapsed at most once a day |
| New This Month | Streaming | Bloom's target is to welcome a new customer within a minute of the first order, not tomorrow |
| Window Shoppers | Batch | A nurture email that arrives tomorrow loses nothing |

None needs edge: edge is for decisions on the page being loaded, and none of the five powers an on-site decision yet. Streaming here is the design. If the builder will not offer Streaming for a rule, rewrite the rule or agree a slower rhythm with the journey owner.

**Task 2: the implausible estimate**

New This Month at 9,930 of 10,000 is implausible: a "new customers" audience holding 99 percent of the base cannot be right, because nearly every customer has ordered at some point in 18 months. The right diagnosis is **b**: the rule matched any order, ever, instead of the first-ever order in the last 30 days. The fixed rule estimates about 480.
- a is wrong: a 30-day window is exactly what a monthly audience needs, and it would not inflate the count to 99 percent.
- c is wrong: the evaluation method changes how often membership is re-checked, not what the rule counts. Read the rule first.
- d is wrong: the estimate is out of the 10,000-customer extract. Anonymous visitors cannot explain a rule about orders reaching almost every customer.

**Task 3: a sample reply**

"Streaming costs more of our entitlement and limits what a rule may contain, and for slow-moving groups it buys nothing. We stream only where a journey must react within minutes, which is Cart Abandoners and New This Month, and keep the rest on batch."

**Task 4: the overlap**

A shopper browses all month and places her first order today. New This Month, designed as streaming, takes her in near real time once her order streams in; Window Shoppers is batch, evaluated once every 24 hours, so she stays there until its next run. A later edit that drops "zero orders ever" from Window Shoppers would put every new customer who browsed in both. Fixes: write the exclusion of New This Month into the Window Shoppers rule (the Audiences tab lets a rule build on an existing audience), and write down which journey wins when someone is in both (the welcome).

**Task 5: reading a zero**

1. Read the **Last updated** line. "Not available" means there is no estimate to judge yet.
2. Press **Refresh estimate**.
3. Check that profile data exists in the sandbox at all (episode 9's checks).
4. Only if the store is full and the estimate is still zero, read the rule in **Code view** and look for a condition that matches nobody, such as email opens before any engagement data exists.

**Task 6: qualified or estimated**

Quote **Qualified**: the profiles that matched at the last evaluation job. For a batch audience it can be most of a day old, so say when the last run was. Do not quote **Estimated** as membership: it is an approximate figure from a sample job, used to check that the rule is sane.

**Task 7: practice question**

"Lapsed 90 changes at most once a day, so streaming would cost more and buy nothing, because the win-back does not need to react within minutes. Batch, evaluated once every 24 hours, is the right rhythm."

**Track B: what to expect**

On a new rule that uses only a profile attribute, expect Streaming not to be offered, because Adobe no longer offers it for new attribute-only rules. If your sandbox has no profile data, expect an estimate of about 0 with "Last updated: Not available"; that is expected and does not mean your rule is wrong. Your exact numbers will differ from Bloom's.

**Check yourself**
1. How often the platform re-checks who belongs to an audience: batch, streaming or edge. The default is Batch.
2. Cart Abandoners 24h (the rescue journey has hours, not days) and New This Month (Bloom's target is a welcome within a minute of the first order).
3. It consumes more of the licence entitlement, it constrains what a rule may contain, and it buys nothing for slow-moving groups. It is also only fast for data that streams in; batch-loaded data still waits for the daily run.
4. Adobe no longer offers Streaming for new rules that use only profile attributes.
5. Treat it as a signal, not an obstacle: rewrite the rule, or agree a slower rhythm with the journey owner. Never assume a rule is streaming-eligible.
6. Qualified is the actual number that matched at the last evaluation job. Estimated is an approximate figure from a sample job, with its own Refresh estimate and Last updated.
7. The estimate can only count profiles that exist. An empty store gives about zero whatever the rule says.

</details>
