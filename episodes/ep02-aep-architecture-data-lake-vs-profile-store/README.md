# Episode 02: AEP Architecture: Data Lake vs Profile Store

**Watch:** [Watch episode 2 on YouTube](https://youtu.be/33Dob_DQRKE)

Part 1: Know your customer (AEP and Real-Time CDP) · [Previous](../ep01-what-is-adobe-experience-platform-cdp-explained/) · [Next](../ep03-xdm-schema-explained-why-orders-are-events/)

## What you will learn

- Describe the five pieces inside Adobe Experience Platform (AEP): sandboxes, datasets and the data lake, the Real-Time Customer Profile store, the Edge Network and governance.
- Explain the difference between the data lake and the profile store, and which one a journey asks.
- Explain what "Enabled for Profile" means and why it is irreversible for a schema.
- Explain why development and production sandboxes exist, and how to check which one you are in.
- Define "real-time" precisely at each layer: profile lookup, edge, streaming and batch.

## The story so far

At the Monday stand-up, Kavya Menon, Bloom's new marketing technologist, met the team: 1.2 million customers in three systems that do not talk, and a loyalty relaunch two weeks away.
Vikram Joshi, the solution architect, drew the map: AEP is the memory, Adobe Journey Optimizer (AJO) the voice, Customer Journey Analytics (CJA) the eyes, and the AI layer the colleague.
The next morning he sits Kavya in front of Bloom's development sandbox. The left menu looks overwhelming, but almost everything in it belongs to one of five pieces.

## Key ideas

### 1. Five pieces, one mental model

| Piece | Think of it as | What it does |
|---|---|---|
| Sandbox | A practice kitchen | An isolated copy of the platform, so practice never touches real customers |
| Datasets and the data lake | The archive | Keeps the complete history: thorough, not fast |
| Real-Time Customer Profile (profile store) | A hotel receptionist with perfect memory | Knows who each person is right now and answers in milliseconds |
| Edge Network | The outpost | Makes instant decisions close to the customer |
| Governance | The legal department in the pipes | Labels and policies that block misuse automatically |

When a screen confuses you, ask which of the five pieces it belongs to.

### 2. Sandboxes: the practice kitchens

A **sandbox** is a complete, isolated copy of the platform. Companies usually run:

- **one production sandbox**: real customer data, treated with respect;
- **several development sandboxes**: practice spaces you can break and reset back to empty.

Every screen is scoped to one sandbox, and development and production look exactly the same. So the first habit is: **check which sandbox you are in before you touch anything.** If you ever land in production by accident: look, screenshot, leave.

### 3. Datasets and the data lake: the archive

Every piece of data you bring into AEP lands in a **dataset**, a managed table for one kind of data (for example Bloom's orders). Every dataset follows a **schema**, the blueprint for one kind of record (episode 3).

All datasets together form the **data lake**: the complete historical archive. The lake is where you run SQL (Structured Query Language), export data in bulk (for example to train a model) and keep years of history. Query Service runs SQL over the lake (episode 15). The lake is thorough, but it is **not fast**, so a journey that needs to know a person right now never asks it.

### 4. The Real-Time Customer Profile: the receptionist

A hotel receptionist with perfect memory does not remember every sentence every guest ever spoke; that is the archive's job. She remembers **who each guest is right now**, and answers instantly.

The **Real-Time Customer Profile**, or **profile store**, is that receptionist. For each person it keeps **one merged, current view: attributes plus recent events**, and it answers in **milliseconds**.

When a journey must decide "is Priya Gold right now?", it asks the profile store, **never the lake**.

| | Data lake | Profile store |
|---|---|---|
| Keeps | Complete history | The current person |
| Speed | Thorough, not fast | Milliseconds |
| Who asks it | Queries, exports, analysis | Journeys and audiences |
| Think of it as | The archive | The receptionist |

### 5. Enabled for Profile: one ingest, two worlds

One checkbox connects the two worlds. When a dataset is **enabled for Profile**, each row lands in the lake **and** is folded into that person's live profile. Datasets that are not Profile-enabled stay archive-only.

> **One ingest, two worlds: the lake keeps the history, the profile store keeps the current person.**

The switch appears in two places: on the **schema** (episode 4) and on the **dataset** (episode 5). The dataset's switch only appears for a schema that is already enabled for Profile.

**Enabling a schema for Profile is irreversible.** The dialog says: *"Once enabled and saved, the schema can't be disabled."* It also needs a primary identity on the schema first (episode 4). So design the schema on paper, check it against sample data, and only then enable it. Never turn on Profile for a schema that is not yours.

### 6. The Edge Network and governance

- **Edge Network (the outpost):** some decisions cannot afford a round trip to a data centre, such as a personalised banner chosen while a page loads. Adobe runs servers physically close to customers that hold a lightweight copy of what those instant decisions need. Bloom sends its website events through the edge in episode 12.
- **Governance (the legal department in the pipes):** you put **data usage labels** on fields ("this is sensitive", "this may not be shared with advertisers") and write **policies** that enforce them automatically. If someone tries to export a restricted field to an advertising platform, the platform itself blocks the export. Episode 13 sets this up for Bloom.

### 7. What "real-time" means at each layer

"Real-time" is not one speed. Name the layer:

| Layer | How fast it really is |
|---|---|
| Profile lookup | Milliseconds |
| Edge decision | Within the same page load |
| Streaming audience | Near real time as streamed data arrives; Adobe gives no minutes figure |
| Batch audience | Evaluated once every 24 hours |

**The trap:** batch-loaded data waits for the daily run, so even a streaming audience does not react the moment a nightly file lands.

At Bloom: a welcome for a brand-new customer is planned in near real time; a win-back for customers lapsed 90 days is fine on a daily batch. Ask how quickly the business must react, not how fast it could be. Episode 11 turns this into a rule.

## In the product

Labels as of October 2026. Look only: nothing in this episode needs you to create, save or enable anything.

1. Sign in to Adobe Experience Cloud at `experience.adobe.com`, open the **App switcher** (nine dots, top right) and choose **Experience Platform**.
2. Find the **sandbox switcher** just under the top bar. It shows the current sandbox and its type: **Development** or **Production**.
3. Double-check in the browser's address bar: the part after `sname:` is your sandbox's name.
4. Read the left rail. It is grouped, for example:
   - **Data Management**: Schemas, Datasets, Monitoring
   - **Connections**: Sources
   - **Customer**: Profiles, Audiences, Identities

   It only shows what your permissions allow, so two colleagues can see slightly different menus.
5. Know the warning before you ever meet it: when you turn on a schema's **Profile** toggle, a dialog says *"Once enabled and saved, the schema can't be disabled."* Episode 4 does this on Bloom's own schemas.

## Common mistakes

- **Assuming you are in development** because the screens look the same. Read the sandbox switcher.
- **Treating the data lake as the database journeys read.** To know a person right now, journeys ask the profile store, not the lake.
- **Thinking the profile store is a second copy of the lake.** It keeps the current person, not the whole archive.
- **Assuming every dataset feeds profiles.** Only Profile-enabled data reaches the profile store.
- **Flipping Enable for Profile "to see what happens".** For a schema it can never be undone.
- **Promising a client "real-time" without naming the layer,** or promising a number of seconds for streaming.
- **Expecting a streaming audience to react to a nightly file.** Batch-loaded data waits for the daily run.

## Glossary

| Term | Meaning |
|---|---|
| Sandbox | An isolated copy of the platform. Development sandboxes are practice kitchens; production holds real data. |
| Development sandbox | A practice sandbox you can experiment in and reset to empty. |
| Production sandbox | The sandbox with real customer data. Look, screenshot, leave. |
| Dataset | A managed table in AEP where ingested data lands; every dataset follows a schema. |
| Data lake | All datasets together: the complete historical archive. Thorough, not fast. |
| Real-Time Customer Profile | The profile store: one merged, current record per person, answered in milliseconds. |
| Enabled for Profile | A schema or dataset setting that sends data to the profile store as well as the lake. Irreversible for schemas. |
| Edge Network | Adobe's servers close to the customer, used for fast data collection and decisions. |
| Governance | Labels on fields plus policies that automatically block misuse of data. |
| Data usage label | A sticker on a field saying what the data is or how it is restricted (episode 13). |
| Journey | A planned path of messages and waits that one customer moves through (Adobe Journey Optimizer). |
| Query Service | SQL over the data lake inside AEP (episode 15). |
| Streaming audience | An audience whose membership updates in near real time as streamed data arrives. |
| Batch audience | An audience evaluated once every 24 hours. |
| Sandbox switcher | The control under the top bar showing the current sandbox and its type. |

## Exercise

Do the tasks in [exercise.md](exercise.md): paper-only by default, with an optional look-only track if you have a development sandbox.

## Further reading

- [Getting around the Platform UI](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-ui/ui-guide)
- Search Experience League for: sandboxes overview
- Search Experience League for: Real-Time Customer Profile overview
- Search Experience League for: enable a schema for Real-Time Customer Profile
- Search Experience League for: Edge Network overview
- Search Experience League for: data governance overview
- Search Experience League for: audience evaluation methods

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
