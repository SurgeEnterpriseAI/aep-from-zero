# Episode 12: Adobe Web SDK, Datastreams & AEP Destinations

**Watch:** Video coming soon on iTV

[Previous](../ep11-batch-vs-streaming-vs-edge-segmentation-in-aep/) · [Next](../ep13-aep-data-governance-dule-labels-policies/)

## What you will learn

- Explain what the **Web SDK** and a **datastream** do, and trace one click from the website to the Real-Time Customer Profile in five stations
- Choose a **file-based** or **streaming** destination for a given partner, and tell **profile export** from **audience export**
- Build an **activation**: an audience plus a destination plus an attribute mapping
- Explain why emails travel **hashed** and why you **map the minimum**
- Describe how consent is **captured once and enforced in layers**: the audience rule, the destination, the channel at send time

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch. In episodes 10 and 11 Kavya built the relaunch five audiences and chose an evaluation method for each: streaming for Cart Abandoners 24h and New This Month, batch for the rest. The audiences are right, but they still sit inside the platform. Marketing wants two of them at the agency every night, and the website's clicks are trapped in old tracking pixels.

## Key ideas

### 1. One tag, one edge, one router (Web SDK, Edge Network, datastream)
Bloom's website carried one tracking pixel per tool: analytics, every ad platform, personalisation. Each slowed the page and described the same visit differently. This is **pixel spaghetti**.

The **Web SDK** (SDK = software development kit) is Adobe's single tag. It captures behaviour as **XDM events** (the Experience Data Model shapes Bloom designed in episodes 3 and 4) and sends them to the **Edge Network**, Adobe's servers close to the customer (the outpost). There a **datastream** receives each event once and routes it to every service configured for it: AEP today, Adobe Journey Optimizer (AJO) next week. Adding a service is adding a route; the page never changes.

The **Datastream ID** wires the tag on the page to its datastream. A wrong ID can pour production traffic into a development sandbox, so check it for every environment before a release.

### 2. Five stations of one click
| # | Station | What happens |
|---|---|---|
| 1 | The click | A shopper taps Add to cart on Bloom's website |
| 2 | Web SDK tag | Captures it as an XDM event with an event ID, a timestamp and the browser's ECID |
| 3 | Edge datastream | Receives the event and routes it |
| 4 | Bloom Web Events dataset | Lands in the data lake, which keeps the history |
| 5 | Real-Time Customer Profile | Folds into the person, because the dataset is enabled for Profile |

It is the same five stations as a batch load (source, collection, routing, dataset, profile), at click speed instead of file speed. If the dataset is not enabled for Profile, the click stops in the lake. Debug any pipe by asking which station the data last reached.

### 3. File-based versus streaming destinations
A **destination** is a configured exit where audiences are sent.

| | File-based | Streaming |
|---|---|---|
| How it arrives | A scheduled file (CSV or Parquet) in cloud storage | Server to server |
| How fast | On a cadence, for example nightly | Within minutes of qualifying |
| Suits | Agencies and batch partners | Ad platforms, retargeting |
| Cost | Lower | Higher |

Ask one question: how quickly does this partner act on the data? Bloom's agency ingests one file a night, so Bloom chose a **file-based cloud storage destination**. Both audiences it receives are batch audiences, evaluated once every 24 hours, so a nightly file fits them.

Journey Optimizer reads an audience directly. It does not need a destination.

### 4. Profile export versus audience export
The destinations framework distinguishes the two. In plain words, a **profile export** sends people with the fields you map; an **audience export** sends membership (which identities are in the audience) for a partner to match against its own users. The agency file is a profile export, which is why its mapping matters so much. If a partner only needs to know who is in, do not send what they are like.

### 5. Activation = audience + destination + mapping
Bloom sends two audiences, and only two:
- **High-Value Loyalists** (estimated 1,180 of the 10,000 customers): the seed the agency uses to find similar people
- **Lapsed 90** (estimated 3,890): Divya's win-back list

Cart Abandoners 24h feeds a rescue journey, New This Month feeds the welcome, and nobody asked for Window Shoppers. Export the minimum starts with the audiences.

### 6. Hashed emails and map the minimum
Marketing asked for email, phone, first name, city, loyalty band and loyalty points. For each field, ask what the partner needs it for.
- **Email, hashed.** A hash is a one-way scramble: the same address always gives the same code, which hides the address but still matches, so a hashed email is still personal data. The agency hashes its own list and matches codes without holding Bloom's raw addresses. This only works because episode 5 lower-cases and trims every email as it lands; one stray capital letter gives a different code.
- **Loyalty band** (Gold, Silver, Bronze), to shape the creative.
- **First name, city, points:** no job to do, so cut. Every extra field is extra risk, more for the partner contract to cover, and one more thing to explain in an audit. "They might want it later" is not a mapping strategy.
- **Phone:** marketing insisted, so Kavya flagged it for review. Episode 13 settles it.

### 7. Consent: captured once, enforced in layers
Consent is data on each person's profile (Bloom's email, SMS and push consent sit in the `_bloom` consent fields mapped in episode 6), not a spreadsheet someone maintains. It is enforced in layers:
1. **The audience rule.** Lapsed 90 (episode 10) admits only people with email consent true. Ananya never gave email consent, so she never enters it, and the win-back file cannot contain her. (High-Value Loyalists has no consent condition yet, so this layer protects the win-back list only; episode 13 adds one.)
2. **The destination.** Governance policies decide what may flow where (episode 13).
3. **The channel.** Journey Optimizer checks consent again at send time (Act II).

Interview line: *"Consent is a profile attribute enforced by the platform, not a process document enforced by goodwill."*

## In the product

Labels as of October 2026. Adobe documents the Web SDK set-up and the activation this way; check what your screen shows.

1. **Data Collection** in the left navigation lists **Tags**, **App Surfaces**, **Datastreams**, **Extension Management**, **Event Forwarding**, **Monitoring** and **Assurance**.
   - **Tags** is Adobe's tag manager, the usual way the Web SDK is deployed.
   - **Datastreams** lists each datastream with its **Datastream ID**, and a **New Datastream** button at the top right.
   - **Assurance** inspects live events arriving from a device: the first place to look when "the website is not sending anything".
2. **Destinations** (under Connections) has five tabs: **Overview**, **Catalog**, **Browse**, **Accounts**, **System view**.
   - **Catalog**: every destination you could connect to. The left rail filters by **Types** (Connections, Extensions), by **Data types** (Accounts, Datasets, Prospects, Audiences; not the Accounts tab) and by category, for example **Cloud storage**, **Advertising** or **Email marketing**.
   - **Browse**: the destinations you have configured.
   - **Accounts**: the credentials behind connections, managed separately, so one credential can serve several connections. When an integration stops, check whether the account expired.
   - **System view**: a map of what flows where.
3. On a cloud storage card in **Catalog**, **Activate audiences** opens the activation wizard: **Select audiences**, **Scheduling**, **Mapping** (source fields to target fields), **Review**. If your screen shows an extra step, such as choosing which destination connection to use, follow your screen.

Never click Activate, or finish an activation wizard, in a shared sandbox.

## Common mistakes

- Copying the wrong **Datastream ID**, so live traffic lands in a development sandbox.
- Assuming a click lands straight in the profile. If the dataset is not enabled for Profile, it stops in the lake.
- Choosing a streaming destination because it sounds modern, and paying for minutes nobody uses.
- Sending every audience "to be safe". Export the minimum starts with the audiences.
- Mapping every field marketing asks for, instead of the minimum the partner needs.
- Hashing emails that were never cleaned, so the partner's match silently fails.
- Trusting the agency, or a spreadsheet, to remove people without consent.
- Blaming the destination when an integration stops, when the account's credentials expired.

## Glossary

| Term | Meaning |
|---|---|
| Pixel spaghetti | The old pattern of one tracking pixel per tool, each slow and inconsistent |
| Web SDK | Adobe's single tag that captures website behaviour as XDM events |
| Edge Network | Adobe's servers close to the customer, used for fast collection and decisions |
| Datastream | The router on the Edge Network that sends each event to the services configured for it |
| Datastream ID | The value that wires the tag on the page to its datastream |
| Tags | Adobe's tag manager, the usual way the Web SDK is deployed |
| Assurance | Live inspection of events arriving from a device |
| Destination | A configured exit where audiences are sent |
| File-based destination | Delivers a scheduled file to storage; suits agencies and batch partners |
| Streaming destination | Delivers server to server within minutes; suits ad platforms; costs more |
| Profile export | Sends people, with the fields you map |
| Audience export | Sends membership, for a partner to match |
| Activation | An audience plus a destination plus a mapping of which fields go along |
| Hashed email | An email sent as a one-way code so a partner can match without the raw address |
| Map the minimum | Send only the fields the partner needs |
| Consent | Recorded permission to contact a person, stored on the profile and enforced by the platform |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Web SDK overview: https://experienceleague.adobe.com/en/docs/experience-platform/web-sdk/home
- Destinations overview: https://experienceleague.adobe.com/en/docs/experience-platform/destinations/home
- Search Experience League for: datastreams overview, Adobe Experience Platform Assurance, activate audiences to batch profile export destinations

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
