# Exercise: Episode 01, What Is Adobe Experience Platform? CDP Explained

Time: about 30 minutes. You need paper and a pen. No Adobe login is required for Track A.

## Track A: No Adobe access needed

1. **The sentence.** Without looking at the notes, write the one-sentence definition of a Customer Data Platform (CDP). Then compare it with the notes and correct it.
2. **The map.** Draw four boxes and label them memory, voice, eyes and colleague. Under each box, write the product or layer it stands for. Draw an arrow between each pair that hands something to the other, and label every arrow with what is handed over.
3. **Where does it live today?** For each of these ten Bloom facts, write which of Bloom's three systems holds it today: the e-commerce platform, the CRM export or the email tool. If you think none of them holds it reliably, say so and say why.

   | # | Bloom fact | Which system holds it today? |
   |---|---|---|
   | 1 | Loyalty tier | |
   | 2 | Order total | |
   | 3 | Email consent | |
   | 4 | Product view | |
   | 5 | Home city | |
   | 6 | Loyalty points | |
   | 7 | Add-to-cart | |
   | 8 | Refund | |
   | 9 | Phone number | |
   | 10 | Join date | |

4. **The naming question.** In exactly two sentences, explain to a friend why "we bought RT-CDP" and "we bought AEP" describe the same software.
5. **The CMO's version.** Write Bloom's problem as three business pains a Chief Marketing Officer would sign. Each pain must be stated in money, time or customers. Do not name any product.
6. **The practice question from the episode.** Bloom wants to win back customers who have not bought anything in 90 days. Which part of the stack finds them, which part speaks to them, and which part proves whether it worked?

## Track B: If you have Adobe access (optional, look only)

Safety first: look, screenshot, leave. Do not create, edit or save anything. Never click Activate, Publish or Send proof. If you are in a company's real environment, there are live customers behind every screen.

1. Sign in to Adobe Experience Cloud.
2. Open the **App switcher**, the nine-dot icon at the top right.
3. Write down every application your login can see. Mark which of the four parts from the episode (memory, voice, eyes, colleague) you can find in that list.
4. Choose **Experience Platform** and stop on the first screen. Take one screenshot for your notes, then close the tab. Episode 2 explains what you are looking at.

## Check yourself

1. What are the three verbs in the CDP sentence?
2. Which product is "the voice", and what does it read before it speaks?
3. A job post asks for "RT-CDP experience". Which skills does it mean?
4. Why is it a mistake to call Customer Journey Analytics "Adobe Analytics"?
5. What does AEP hand to AJO, and what does CJA hand back to AEP?
6. Why is matching customers by name risky?
7. Name the four acts of the programme and the lead voice of each.
8. What is Anjali's deadline, and what does she want to see on Demo Day?

<details><summary>Check your answers</summary>

**Track A**

1. "A Customer Data Platform collects the fragments, joins them into one person, and makes that person usable in real time."
2. Memory = Adobe Experience Platform (AEP). Voice = Adobe Journey Optimizer (AJO). Eyes = Customer Journey Analytics (CJA). Colleague = the AI layer. Arrows: AEP to AJO (profiles and audiences); AJO's sends and journey steps leave records that CJA reads (what was sent and what happened); CJA back to AEP (new audiences built from what worked); the AI layer connects to all three (answers questions, drafts content, does routine work through agents).
3. Model answers:

   | # | Bloom fact | Where it lives today |
   |---|---|---|
   | 1 | Loyalty tier | CRM export |
   | 2 | Order total | E-commerce platform |
   | 3 | Email consent | CRM export (the file carries the consent columns) |
   | 4 | Product view | None reliably. The episode does not say any of the three systems records views; at best the website and app see them, and only as an anonymous visitor until the shopper signs in. |
   | 5 | Home city | CRM export |
   | 6 | Loyalty points | CRM export |
   | 7 | Add-to-cart | Same as product view: none reliably, and usually anonymous. |
   | 8 | Refund | E-commerce platform |
   | 9 | Phone number | CRM export (in several different formats, which episode 5 cleans up) |
   | 10 | Join date | CRM export |

   The point of the task: six facts live in the CRM export, two in the e-commerce platform, none in the email tool, and the behaviour that matters most for a journey (views and add-to-carts) is not tied to a known person anywhere. No single system can answer "who is this customer?"
4. Example: "Real-Time CDP is not a separate product; it is the commercial name for AEP's profile, audience and activation capabilities. So whichever name is on the contract, the team logs in and builds inside AEP."
5. Example: (1) We give a 20% discount to customers who would have paid full price, twice a week. (2) A simple "not bought in 90 days" list takes two days, and new customers can wait up to six days for a welcome email. (3) Thousands of rupees of product are abandoned in carts every night, and nobody can say which campaigns make money.
6. AEP finds them (an audience defined by a rule), AJO speaks to them (a win-back message), and CJA proves whether it worked (did those people buy again).

**Track B**

There is no single right list: different logins see different applications. If you could open Experience Platform, you found the memory. Do not expect "the colleague" as its own entry: Adobe's AI Assistant appears inside the products, and its availability varies. Whatever your own screen shows is the fact.

**Check yourself**

1. Collect, join, make usable (in real time).
2. Adobe Journey Optimizer (AJO). It reads the memory, AEP, before it speaks.
3. Working with profiles, audiences and activation (destinations) inside AEP.
4. Adobe Analytics is a different, older product. CJA is compared with it in episode 32.
5. AEP hands AJO profiles and audiences. CJA hands back new audiences built from what it learned.
6. Two different customers can share a name. A CDP joins records on identifiers, such as an email address.
7. I. Know your customer (Farhan). II. Speak to your customer (Divya). III. Prove what worked (Rohan). IV. Multiply the team (Vikram).
8. The loyalty relaunch goes live in two weeks. On Demo Day the board wants to see one customer Bloom truly knows.

</details>
