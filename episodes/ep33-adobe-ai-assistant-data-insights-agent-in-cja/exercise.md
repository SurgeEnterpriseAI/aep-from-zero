# Exercise 33: Interrogate Bloom

You will write ten questions about Bloom's build with their true answers before you ask any AI, score AI answers in an evidence sheet, judge five generated subject lines, correct a caption that miscounted, and sort Adobe's 2026 AI names into what is known and what is not.

**Ground rules for every task:** never paste customer data (names, emails, phone numbers, order rows) into any AI tool. Use only tools your organisation, school or you yourself are allowed to use. The Bloom sample files are fictional, but practise the habit anyway.

## Track A: No Adobe access needed

1. **Truth first.** Write ten questions about Bloom's build, and the true answer for each, **before** you ask any AI. Use the episodes and the sample files:
   - four about **schema usage** (for example: which schemas declare an Email identity?)
   - three about **audience overlap** (for example: can anyone be in both Lapsed 90 and Window Shoppers?)
   - three about **journey status** (for example: what state is Bloom Welcome v1 in, and what does that state allow?)

   For each, also write **where the truth lives** (a schema screen, an audience rule, the journey list, an episode).
2. **Fill the evidence sheet.** Ask an AI tool you are allowed to use five **general** product-knowledge questions (not Bloom data), for example:
   - Can you turn off Enable for Profile on an AEP schema once it is saved?
   - In Customer Journey Analytics, does a flow visualisation count people?
   - What does a merge policy decide in AEP?
   - Is the Condition activity still in the Journey Optimizer palette in 2026?
   - In AEP, does "Records failed" count rows or error instances?

   Write the true answer first, then fill one row per question: **prompt, output, verdict (right, incomplete or wrong), correction**.
3. **Five subject lines, keep two.** Generate (with an allowed tool, or write yourself) five subject lines for Bloom's win-back email to Lapsed 90. Check each against these rules from Bloom's brand sheet (`bloom-brand-sheet.md` in the course data folder), as the episode describes them: Bloom's win-back offer is the **20% Comeback**; the voice is warm, with no shouting and no false urgency; no promise the product cannot keep. Keep the two that fit, and write **one line on why each rejected line fails**. Then write who would approve the kept lines.
4. **Fix the caption.** A caption on a Flow says: *"The most common channel before 'email' accounts for 48 (8%) People."* The email node holds **600 path views** (illustrative numbers). Rewrite the caption so it is true, and write one sentence on how you proved the base.
5. **Untangle the names.** For each statement, mark it **Adobe says**, **a login showed**, or **nobody has said**:
   - a. AI Assistant in CJA includes the Data Insights Agent.
   - b. The CJA header icon is labelled Ask Coworker.
   - c. CX Enterprise Coworker replaces AI Assistant.
   - d. Data Insights Agent access was given through 28 February 2026 and through 31 March 2026.
   - e. The Create project banner calls Coworker "an evolution of AI Assistant".
6. **The episode's practice question.** Say an assistant tells you that 120 people sit in both Lapsed 90 and Window Shoppers. What is your verdict, and how do you prove it?

## Track B: If you have access to Adobe's AI features (optional)

Safety first:
- Use Adobe's AI features **only with your organisation's approval**. Never accept generative AI terms yourself; that is the organisation's decision.
- **Never paste customer data** into a prompt. Ask about objects, not people.
- Work in a **development** sandbox, on objects that carry **your own initials**. Never click **Activate**, **Publish** or **Send proof**, and never click **Try now** on the Coworker card.
- In shared environments: look, screenshot, leave.

Steps:
1. Write down **what your own login shows**: is there an AI Assistant in Experience Platform? In CJA, hover the header icon just left of **Help** and note its tooltip. Screenshot it with the date. Press Esc if a card opens.
2. If AI Assistant is available to you, ask it three of your Track A questions about **your own** schemas or audiences. Score each answer in your evidence sheet.
3. In CJA, on a chart **you** built (Line, Bar or Flow with at least 3 data points), click the **Intelligent captions** icon at the top right. Read every caption with **<** and **>**. Check each number against the table behind the chart, and write a verdict and a correction for at least one.
4. Do not save, share, schedule or publish anything other than your own project.

## Check yourself

1. What is the difference between a product-knowledge question and an operational question?
2. Why must you write the true answer before you ask?
3. What are the four columns of the AI evidence sheet?
4. Which schemas in Bloom's build use the BloomID namespace?
5. Which visualisations can the Data Insights Agent build, and name two it cannot?
6. What is the rule for Adobe's 2026 AI names?
7. Why does nobody at Bloom click Try now on the Ask Coworker card?
8. What did Kavya record about the agent flow, besides its answer?
9. What is the most common mistake with intelligent captions on a Flow?
10. Who is accountable for a generated subject line that goes out?

<details><summary>Check your answers</summary>

**Task 1: truth first (model answers)**

| # | Question | True answer | Where it lives |
|---|---|---|---|
| 1 | Which schemas declare an Email identity? | Bloom Customer Profile (primary) and Bloom Order Event (order email, second identity) | Schemas, Browse; episode 4 |
| 2 | Which schemas use the BloomID namespace? | Bloom Order Event only, as its primary identity | Schemas, Browse; episode 7 |
| 3 | How many identities does each schema declare? | Customer profile one, web event one, order event two | Schemas, Browse |
| 4 | What class and identity does Bloom Web Event use? | XDM ExperienceEvent; ECID | Schemas; episode 4 |
| 5 | Can anyone be in both Lapsed 90 and Window Shoppers? | No: zero orders ever versus a last order more than 90 days ago | The two audience rules |
| 6 | Which audience must Window Shoppers exclude, and why? | New This Month: a first-time buyer stays a window shopper until the next daily batch run | Episode 11 |
| 7 | Can a customer without email consent be in Lapsed 90? | No: the rule requires email consent true | The Lapsed 90 rule |
| 8 | What state is Bloom Welcome v1 in? | Live since relaunch Monday; read-only, so changes need a new version | The journey list |
| 9 | What happens in Cart Rescue v1 when a person buys? | They exit on any purchase; re-entry at most once per 7 days | Journey properties; episode 21 |
| 10 | How do people enter Bloom Welcome v1? | Audience qualification into New This Month | The journey canvas; episode 17 |

The repo's `sample-profile-priya.json` lists BloomID in its identityMap as a teaching shape; in the real build the customer profile schema declares only Email.

**Task 2: true answers for the five general questions**
- No. Enable for Profile is irreversible: "Once enabled and saved, the schema can't be disabled."
- No. A flow counts path views; one person can produce several.
- Which value wins when two sources disagree about a person.
- No. Condition was removed from the UI in 2026; Optimize replaces it.
- Error instances, not rows. One bad row can raise two errors.

Any answer that says otherwise gets the verdict **wrong**; one that is right but leaves out the key caveat gets **incomplete**.

**Task 3: subject lines (model rejection reasons)**
- An invented offer ("30% off today only"): Bloom's win-back offer is the 20% Comeback, so the line promises something that does not exist.
- A health or results promise ("clear skin in 7 days, guaranteed"): no wellness brand can honestly promise it.
- Shouting or false urgency ("LAST CHANCE" in capitals): breaks the brand sheet's tone rules and claims a deadline that is not true.
- Lines worth keeping are warm **and** true. For example, "A little something to welcome you back" is true because every Lapsed 90 customer is eligible for the 20% Comeback.
- Approval: Divya, who owns the brand voice, approves the kept lines. The approver, not the tool, is accountable.

**Task 4: the caption**
"48 of the 600 paths through email (8%) came from that channel." Proof: 48 ÷ 600 = 8%, the percentage the caption printed, so its base was path views, not people. A flow counts path views, and one shopper who walks the same path twice counts twice.

**Task 5: the names**
- a. Adobe says.
- b. A login showed (October 2026).
- c. Nobody has said. Adobe does not say whether Coworker replaces AI Assistant or the Data Insights Agent.
- d. Adobe says (both dates appear on Adobe's pages, and both have passed).
- e. A login showed.

**Task 6: practice question**
Verdict: **wrong**. Prove it from the two rules, not from another AI: Window Shoppers requires zero orders ever, and Lapsed 90 requires a last order more than 90 days ago, so nobody can qualify for both. Correction: "No overlap: the rules exclude each other." Then log the prompt, output, verdict and correction in your evidence sheet.

**Track B: what to expect**
Your login may show different names, icons or nothing at all; that is the point of the rule. Record what you see, with the date. Labels as of October 2026.

**Check yourself**
1. Product knowledge asks how the product works; operational asks what is true about your own objects.
2. Without a known truth you cannot tell a good reply from a confident wrong one.
3. Prompt, output, verdict, correction.
4. Only Bloom Order Event, as its primary identity.
5. Line, Multi-line, Freeform table, Bar, Donut, Summary number. It cannot build Flow, Fallout, Cohort table or attribution.
6. What your own login shows is the fact.
7. It may start a trial or ask the organisation to accept AI terms, which is the organisation's decision.
8. What it read, what it compared, and what it changed.
9. Reading path views as people.
10. The human who approved it.

</details>
