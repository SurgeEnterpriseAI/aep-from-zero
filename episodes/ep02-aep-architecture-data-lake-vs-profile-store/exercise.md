# Exercise 02: AEP architecture, data lake vs profile store

Time: about 30 minutes. You need paper and a pen. No Adobe login is required for Track A.

## Track A: No Adobe access needed

1. **Draw the five pieces.** Draw five boxes and label them: sandbox, datasets and data lake, profile store, Edge Network, governance. Under each, write its analogy and one line on its job.
2. **Follow one row.** On the same page, draw one new Bloom order arriving in a **Profile-enabled** dataset. Show where it lands and what each place keeps. Then draw the same row arriving in a dataset that is **not** Profile-enabled. What changes?
3. **Lake or profile store?** For each question below, built from the ten Bloom facts in episode 1, write who is asking (a journey that needs the answer now, or someone analysing history) and whether the question goes to the **profile store** or the **data lake**. Give a one-line reason.

   | # | Fact | Question | Lake or profile store? |
   |---|---|---|---|
   | 1 | Loyalty tier | A journey must choose an email: is Priya Gold right now? | |
   | 2 | Order total | What was the average order total each month over the last 18 months? | |
   | 3 | Email consent | Before sending anything, does Priya allow email right now? | |
   | 4 | Product view | Which products were viewed most during the last 18 months? | |
   | 5 | Home city | Which city should a journey mention in Priya's delivery message today? | |
   | 6 | Points | How many loyalty points does Priya have at this moment? | |
   | 7 | Add-to-cart | Every add-to-cart event over 18 months, to study seasonal patterns | |
   | 8 | Refund | How many refunds happened in each quarter of the last 18 months? | |
   | 9 | Phone | A journey wants Priya's current phone number for an SMS | |
   | 10 | Join date | Export every customer's join date in bulk to train a model | |

4. **The real-time ladder.** Write the four layers and how fast each really is: what happens in milliseconds, within the same page load, in near real time, and once every 24 hours. Add one sentence on why a streaming audience does not react the moment a nightly file lands.
5. **Pause before you click.** In exactly two sentences, explain why Enable for Profile deserves a pause before you click it.
6. **The practice question from the episode.** A journey must decide whether Priya is Gold right now, and Rohan wants every Bloom order from the last 18 months. Which question goes to the data lake, which goes to the profile store, and why?

## Track B: If you have a development sandbox (optional, look only)

Safety first:
- Use a **development** sandbox only. If the switcher says **Production**: look, screenshot, leave.
- Create, save and enable nothing. Never turn on **Profile** for any schema or dataset, yours or anyone else's, in this exercise.
- Never click **Activate**, **Publish** or **Send proof**.

Steps:
1. Sign in to Adobe Experience Cloud, open the **App switcher** and choose **Experience Platform**.
2. Find the **sandbox switcher** just under the top bar. Write down whether it says **Development** or **Production**.
3. Check the browser's address bar: find the part after `sname:` and confirm it matches the switcher.
4. List the groups you can see in the left rail, and the items under **Data Management**, **Connections** and **Customer**. Note anything the episode named that your login does not show (that is usually a permission).
5. Next to each item you listed, write which of the five pieces it belongs to. Then close the tab.

## Check yourself

1. What are the five pieces inside AEP, and what is the analogy for each?
2. What is the difference between a development sandbox and a production sandbox?
3. Where do you look to see which sandbox you are in?
4. What does the data lake keep, and what is it good for?
5. What does the profile store keep, and how fast does it answer?
6. Which one does a journey read?
7. What happens to a row that lands in a dataset that is not Profile-enabled?
8. What does the dialog say when you enable a schema for Profile?
9. Name the four layers of "real-time" and the speed of each.

<details><summary>Check your answers</summary>

**Track A**

1. Sandbox: the practice kitchen; an isolated copy of the platform. Datasets and data lake: the archive; complete history, thorough but not fast. Profile store: the hotel receptionist with perfect memory; one merged, current view per person, in milliseconds. Edge Network: the outpost; instant decisions close to the customer. Governance: the legal department in the pipes; labels and policies that block misuse automatically.
2. Profile-enabled: the order lands in its dataset (so the lake keeps it as history) **and** is folded into the customer's live profile (so a journey can use it now). Not Profile-enabled: the order lands in the lake only. It stays archive-only, useful for analysis but invisible to the profile store.
3. Model answers:

   | # | Lake or profile store? | Why |
   |---|---|---|
   | 1 | Profile store | A journey needs the current person, in milliseconds |
   | 2 | Data lake | A history question across 18 months |
   | 3 | Profile store | Current consent, checked before a send |
   | 4 | Data lake | Analysis over history |
   | 5 | Profile store | The current attribute, used by a journey now |
   | 6 | Profile store | Points as they are right now |
   | 7 | Data lake | Every event over 18 months is archive work |
   | 8 | Data lake | Counting over history |
   | 9 | Profile store | The current phone number, for a journey. Note: Priya's SMS consent is false, so a journey that respects consent would not text her at all (episode 12 shows how consent is enforced) |
   | 10 | Data lake | Bulk exports, for example to train a model, come from the lake |

   The pattern: "right now, for one person, for a journey" goes to the profile store. "History, many people, analysis or export" goes to the lake.
4. Milliseconds: a profile lookup. Within the same page load: an edge decision. Near real time: a streaming audience, as streamed data arrives (Adobe gives no minutes figure). Once every 24 hours: a batch audience. Batch-loaded data waits for the daily run, so a streaming audience does not react the moment the file lands; it picks the change up at the daily run.
5. Example: "Enabling a schema for Profile is irreversible: once enabled and saved, the schema can't be disabled. So you design it on paper and check it against sample data first, and you never enable a schema that is not yours."
6. Priya's tier goes to the profile store, because a journey needs the current person in milliseconds. Rohan's 18 months of orders go to the data lake, because that is a history question and the lake keeps the complete archive.

**Track B**

Your switcher should read **Development**. If it reads **Production**, you should have stopped at step 2. Rails differ by login: the episode's groups were Data Management (Schemas, Datasets, Monitoring), Connections (Sources) and Customer (Profiles, Audiences, Identities). Schemas and Datasets belong to the datasets-and-lake piece, Profiles to the profile store, Audiences are read from the profile store, Identities help records become people (episode 7), and Sources bring data in (episode 5). Whatever your own screen shows is the fact.

**Check yourself**

1. Sandbox (practice kitchen), datasets and data lake (archive), profile store (receptionist with perfect memory), Edge Network (outpost), governance (legal department in the pipes).
2. Development is a practice space you can break and reset to empty; production holds real customer data and is treated with respect.
3. The sandbox switcher just under the top bar, which shows the name and the type. The address bar shows the name after `sname:` too.
4. The complete history of everything loaded. It is good for SQL queries, bulk exports and years of history, but it is not fast.
5. One merged, current view per person (attributes plus recent events). It answers in milliseconds.
6. The profile store, not the lake, whenever it needs to know the person right now.
7. It stays in the lake only (archive-only) and never reaches the profile store.
8. "Once enabled and saved, the schema can't be disabled."
9. Profile lookup: milliseconds. Edge: within the same page load. Streaming audience: near real time, no published minutes figure. Batch audience: once every 24 hours.

</details>
