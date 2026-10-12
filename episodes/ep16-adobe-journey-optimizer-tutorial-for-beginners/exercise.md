# Exercise 16: Campaign or journey?

You will sort eight Bloom messages into campaigns and journeys, explain identity type in plain words, reason about the Flash Sale's test audience, and write the checklist you run before Review to activate.

## Track A: No Adobe access needed

1. **Campaign or journey?** For each Bloom use case, choose **journey** or **campaign**. For a campaign, name the campaign type. For a journey, name the entry (Read audience, an event, or audience qualification). Give one reason each.
   - a welcome for each new customer
   - cart rescue after an abandoned cart
   - the monthly newsletter
   - an account reset email after a customer forgets how to sign in
   - a store-closure notice
   - a win-back message to Lapsed 90
   - an order receipt
   - a flash sale
2. **Identity type in two sentences.** Explain what identity type does in a campaign. Then say what happens to a High-Value Loyalist whose profile has no Email identity when the campaign's identity type is Email.
3. **Where does the email go?** The identity type is Email. Name the setting that decides which address the message is actually sent to, and the object that can override it.
4. **The Flash Sale.** Which campaign type is Flash Sale, and why? Why does its test audience hold only your own test seat?
5. **Your pre-flight checklist.** Write the checklist you would run on a campaign draft before you open Review to activate. Aim for 8 to 10 lines.
6. **The episode's practice question.** Bloom wants to send a thank-you the moment a customer becomes Gold. Is that a journey or a campaign, and which door lets her in?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- Never click **Activate**, **Publish** or **Send proof**. This track ends at the Review to activate screen.
- Type only **your own** email address, anywhere.
- Campaign fields save as you type, and there is no Cancel. Only type inside your own campaign, and never open anyone else's.
- Do not create or edit anything under **Administration** (channel configurations, Execution Fields, subdomains, suppression list, allowed list).

Steps:
1. Open **Journey Optimizer** from the app switcher. Read the sandbox name in the top bar.
2. **Journey Management** → **Campaigns** → **Create campaign** → **Scheduled - Marketing** → **Confirm**. Name it `Gold Thank-You` plus your initials.
3. **Audience** tab → **Select audience** → pick one audience → **Add audience**. Read its count. Set **Identity type** by typing `Email` and picking **Email**.
4. **Actions** tab → **Add action** → **Email**, and select the Marketing email channel configuration the admin set up. Do not create one.
5. **Edit content**. Write a subject line with the first name, using the **Open personalization dialog** icon. Look for the green tick.
6. **Edit email body** → **Design from scratch**. Add a **1:1 column** structure first, then a **Text** block inside it. **Save**.
7. Preview: if you have your own test profile, use **Simulate content (AEP profiles)** with your own address. If not, use plain **Simulate content**, which uses sample data. Do not click **Send proof**.
8. Back arrow, leave **Schedule** on its default, click **Review to activate**, read the summary and any warnings, then leave through **Campaigns** in the left rail without activating. Confirm your campaign still says **Draft**.

## Check yourself

1. What question does a campaign answer, and what question does a journey answer?
2. Name the four campaign types.
3. Why must a promotion never use a Transactional type?
4. Name the three ways into a journey, and give the rule for choosing between an event and an audience.
5. What does identity type do, and how many can a campaign have?
6. Where does the address an email is sent to come from?
7. Who sets up a channel configuration, and what must match the campaign?
8. Why did Kavya's Text block need a structure first?
9. What is the difference between Simulate content and Simulate content (AEP profiles)?
10. What happens if you click Activate on the default schedule?

<details><summary>Check your answers</summary>

**Task 1: campaign or journey**

| Use case | Pick | Type or entry | Why |
|---|---|---|---|
| Welcome each new customer | Journey | Audience qualification into New This Month | Being new is a state; each person enters the moment they join, and Gold members can be treated differently (episode 17) |
| Cart rescue | Journey | An event (the abandon event) | The abandoned cart is the moment; it needs a wait and an exit on purchase (episode 21) |
| Monthly newsletter | Campaign | Scheduled - Marketing | One message, one audience, one time |
| Account reset email | Campaign | API triggered - Transactional | A service message for the one profile named in the call, needed even by people who opted out of marketing |
| Store-closure notice | Campaign | Scheduled - Transactional | A service message to an audience that must ignore marketing opt-outs |
| Win-back to Lapsed 90 | Campaign at Bloom | Scheduled - Marketing | Bloom sends Bloom Win-Back as one campaign to Lapsed 90 (episode 22). A multi-step series with waits and branches would be a journey |
| Order receipt | Campaign | API triggered - Transactional | Bloom's e-commerce platform fires it for the buyer named in the call |
| Flash sale | Campaign | API triggered - Marketing | Another system fires it when the sale starts; it sells, so it is Marketing. If the time is known in advance, Scheduled - Marketing also works |

**Task 2: identity type**
Identity type is the key AJO uses to identify each person in the campaign's audience, and a campaign can have only one. A High-Value Loyalist with no Email identity is not targeted at all: nothing errors, and that person simply receives nothing.

**Task 3: where the email goes**
The sandbox default under Administration, Channels, **Execution Fields** decides which profile field holds the address. A **channel configuration** can override it. The identity finds the person; Execution Fields decide where the message lands.

**Task 4: the Flash Sale**
API triggered - Marketing: another system (here, Postman standing in for one of Bloom's own systems) calls the AJO API to fire it, it targets an AEP audience, and it sells. Its test audience holds only your own seat, so if anything is wrong, the only inbox that receives it is yours. Adobe documents the API triggered flow this way; check what your screen shows.

**Task 5: a model checklist**
1. The name carries my initials, and the status is Draft.
2. The campaign type is right: Marketing for anything that sells.
3. The audience is the right one, and its count is plausible.
4. Identity type is Email, and I know that members without an Email identity are skipped.
5. The channel configuration is the admin's Marketing one, matching the campaign.
6. The subject line personalisation shows a green tick.
7. The body has a structure and text, and it is saved.
8. I previewed it with Simulate content (AEP profiles) on my own test seat.
9. I have read the opt-out warning; a footer with an unsubscribe link fixes it (episode 19).
10. I know the default schedule means Activate sends at once, so I will not click it.

**Task 6: practice question**
A journey that enters on **audience qualification**. The word "moment" tempts you towards an event, but becoming Gold is a change of state: the loyalty tier is a profile value that changes in place, not an event Bloom collects. An audience describes that state, and audience qualification admits each customer the moment she joins it. A campaign cannot do this, because it sends to a whole audience at a set time, or when a system calls it.

**Track B: what to expect**
The campaign saves itself as Draft. Identity type is a type-ahead box: typing `Email` first is more reliable than clicking in the long list. The Email Designer will not take text until a structure is on the canvas. Review to activate shows a summary of content, properties, action and audience, with one warning: "The opt-out link is not present in the email body." That is expected until a footer fragment with an opt-out link is added.

**Check yourself**
1. A campaign answers "what do we send?". A journey answers "what happens to this customer next?".
2. Scheduled - Marketing, Scheduled - Transactional, API triggered - Marketing, API triggered - Transactional.
3. Transactional ignores marketing opt-outs, so a promotion sent that way reaches people who said no.
4. Read audience, an event, audience qualification. If the moment matters, use the event; if the state matters, use the audience.
5. It is the key AJO uses to identify each person in the audience. One per campaign.
6. The sandbox default under Administration, Channels, Execution Fields, which a channel configuration can override.
7. An admin sets it up once and marketers only select it. Its type, Marketing or Transactional, must match the campaign.
8. The Email Designer needs a structure before you can add text.
9. Plain Simulate content fills the preview from sample data; Simulate content (AEP profiles) fills it from a real test profile.
10. It sends at once, to everyone in the audience with the campaign's identity type.

</details>
