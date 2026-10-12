# Exercise 22: Three offers, one decision

You will model Bloom's three offers as decision items, predict which offer each test seat receives, find what is missing when a library shows nothing, and place eligibility on the right layer.

## Track A: No Adobe access needed

1. **Model the three offers.** For each of Bloom's offers, **20% Comeback**, **Early Access Drop** and **Free Shipping**, write five lines: offer name, eligibility (All visitors, an audience, or a decision rule, and which one), priority, a cap (or "none", with a reason) and status before and after Anjali's sign-off. Comeback must rank above Early Access where both qualify.
2. **Predict the offers.** Bloom's decision policy runs one selection strategy (Comeback and Early Access, ranked by Offer priority) with Free Shipping as the fallback. Predict the offer each test seat sees, and explain why:

   | Seat | State | Address in these notes |
   |---|---|---|
   | TD-DIVYA-03 | Lapsed: last order more than 90 days ago, email consent true | divya@example.com |
   | TD-KAVYA-01 | Gold | kavya@example.com |
   | TD-FARHAN-02 | Silver, recent buyer (neither lapsed nor Gold) | farhan@example.com |

   Then answer: what does a customer who is **lapsed and Gold** at the same time receive?
3. **The silent library.** A sandbox has twenty approved offers, and no email can show one. List everything that might be missing. Aim for at least four items.
4. **Where does eligibility belong?** For each of Bloom's three offers, decide whether its eligibility belongs on the item, the selection strategy or the campaign, and say why in one sentence. Then say what the Bloom Win-Back campaign's own audience is for.
5. **The three-line rule.** Write the journeys versus campaigns versus decisioning rule in three lines, one question each.
6. **The template trap.** A colleague wants to switch on Enable decisioning in the finished Bloom Win-Back email "just to see what it looks like". Write your two-sentence reply.

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, and put **your initials** (XX below) on everything you create.
- Never click **Approve**, **Edit schema**, **Activate**, **Publish** or **Send proof** in a shared sandbox.
- Never switch on **Enable decisioning** in an email you have already designed.
- Leave everything as **Draft**. Never edit, archive or delete anyone else's objects.
- In shared environments: look, screenshot, leave.

Steps (labels as of October 2026):
1. In Journey Optimizer's left navigation, find **Decision Management** and **Decisioning**. Write down the two items under each.
2. Open **Decisioning, Catalogs**. Do not click **Edit schema**. Click **Create item**.
3. On **Attributes**, type the Offer name `XX - Comeback practice` and set **Priority** to `10`. Scroll down and read **Custom attributes** without changing anything. Click **Next**.
4. On **Eligibility**, choose **Visitors who fall into one or more audiences** and add an audience you created yourself (or leave **All visitors** if you have none). Read the **Capping** section and the **Create capping** button, but do not create a cap. Click **Next**.
5. On **Review**, check the two cards, then click **Save**. Confirm the status reads **Draft**. Do not click **Approve**.
6. Open **Collections**, then **Create collection**. Name it `XX - Win-Back practice`. Add a rule: **Select attribute** **Offer name**, **Select operator** **Contains**, and your full item name typed exactly. Read **NUMBER OF ITEMS**: it must say **1** before you click **Create**. If it says 0, check the spelling, because Adobe says Contains matches exact values only.
7. Open **Strategy setup, Selection strategies, Create selection strategy**. Name it `XX - Win-Back picker`, select your collection, leave **Eligibility** on **All visitors**, choose **Ranking method** **Offer priority**, and click **Create**.
8. Open **Strategy setup, Placements, Email** and write down whether any email placement exists. Do not create one.

## Check yourself

1. Which of the four words decides who **may** see an offer, and which decides which offer **wins**?
2. What does a decision rule do differently from an audience?
3. Which status makes an item available to the engine, and what happens to Draft items?
4. Why is **Edit schema** a decision for the whole sandbox?
5. What does Adobe say the Contains operator works like in a collection rule?
6. Name the three ranking methods. Which one needs real traffic first?
7. Name the three places eligibility can sit.
8. What happens if a decision policy has no fallback and nobody qualifies?
9. What must exist before an email decision policy can render?
10. What does **Enable decisioning** do to an email that is already designed, and how do you protect it?

<details><summary>Check your answers</summary>

**Task 1: the three offers as decision items** (priorities and caps are illustrative)

| | 20% Comeback | Early Access Drop | Free Shipping |
|---|---|---|---|
| Eligibility | Audience **Lapsed 90** (last order more than 90 days ago and email consent true) | Audience **Gold Members** | All visitors. As the fallback it shows when nothing qualifies, regardless of its own eligibility |
| Priority | Higher, for example 20 | Lower, for example 10 | Not ranked: it is the fallback in the decision policy |
| Cap | For example once a week per profile, so the discount is not shown again and again | Optional; none needed for a loyalty reward | None: the fallback must always be able to show |
| Status | Draft until Anjali signs off; then Divya clicks Approve | Same | Same: approve it too, since Draft items are never served |

An audience is computed earlier, so it may lag slightly; that is acceptable for a win-back. A decision rule would be checked at every decision, which matters only when the answer changes fast.

**Task 2: predictions**
- TD-DIVYA-03 (lapsed): **20% Comeback**. She is eligible for Comeback only.
- TD-KAVYA-01 (Gold): **Early Access Drop**. She is eligible for Early Access only.
- TD-FARHAN-02 (neither): **Free Shipping**. Nothing in the strategy qualifies, so the fallback shows.
- A lapsed Gold member is eligible for both. Ranking decides, and **Comeback** wins because its priority number is higher.

**Task 3: the silent library** (any four)
- No **decision**, or in Decisioning no **decision policy** in the email, so nothing asks the engine.
- No **selection strategy** or **collection** tying the offers together (or a collection rule that counts 0 items).
- No **email placement**, so an email decision policy cannot render.
- No **fallback**, and nobody eligible: "nothing will be displayed".
- Items still in **Draft** (in Decisioning), so the engine cannot serve them.
- Eligibility that nobody meets, for example an audience with no members.
- A change made less than 15 minutes ago that has not taken effect yet.

**Task 4: where eligibility belongs**
- **Comeback:** on the **item** (Lapsed 90). It is the offer's own rule, so it travels with the item and the 20% never leaks if the strategy is reused in a message to everyone.
- **Early Access:** on the **item** (Gold Members), for the same reason: it is a Gold reward wherever it appears.
- **Free Shipping:** no restriction; it is the fallback, and fallbacks show when nothing qualifies, whatever their eligibility.
- **Strategy:** All visitors, because this use adds no extra rule.
- **Campaign:** Bloom Win-Back's audience, Lapsed 90, decides who receives the email at all. It is not a substitute for item eligibility.

**Task 5: the three-line rule**
- A campaign answers: what do we send?
- A journey answers: what happens to this customer next?
- Decisioning answers, inside either one: which offer should this person see?

**Task 6: the template trap**
"Adobe says enabling decisioning clears existing email content, so that switch would wipe the fragments, the fallback greeting and the legal block. If we need decisioning in this email, we save it as a template first, and we never flip the switch on someone else's email."

**Check yourself**
1. Eligibility decides who may see an offer; ranking decides which eligible offer wins.
2. A decision rule is checked again every time a decision is made. An audience is computed earlier, so it may not be up to date when the offer is shown.
3. **Approved**. Draft items are never served.
4. It changes the catalog's form for every item in the sandbox, so a new field appears in everyone's item form.
5. Like an IN operator: exact values, not partial or wildcard matches.
6. Offer priority, Formula and AI model. AI model needs traffic: Adobe recommends 1,000 impressions and 100 conversions per item per week.
7. The item, the selection strategy, and the campaign or journey's own audience.
8. Nothing is displayed in the offer slot.
9. An email placement.
10. It clears the existing content. Save the email as a template first.

</details>
