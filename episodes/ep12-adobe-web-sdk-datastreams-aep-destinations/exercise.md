# Exercise 12: Open the taps

You will trace one click into the platform, choose the right exit for four partners, cut a field list down to the minimum, and find the layer that keeps a customer without consent out of a file.

## Track A: No Adobe access needed

1. **Order the five stations.** Put these in the order one click travels, from Bloom's website to the Real-Time Customer Profile:
   - It lands in the Bloom Web Events dataset
   - The Web SDK tag captures it as an XDM event
   - A shopper taps Add to cart on Bloom's website
   - Profile-enabled, it folds into the shopper's Real-Time Customer Profile
   - The Edge Network datastream receives and routes it
2. **Choose file-based or streaming** for each partner, and justify each choice in one sentence:
   - the media agency's nightly file
   - a retargeting ad platform
   - a data-science team's weekly extract
   - an SMS vendor
3. **Map the minimum.** Marketing asks for email, phone, first name, city, loyalty band and loyalty points for the agency. Write the minimum mapping you would approve, and one reason for each field you keep or cut.
4. **Find the consent layer.** Ananya never gave email consent. Name the layer that keeps her out of the win-back file, and which episode built it.
5. **The episode's practice question.** Say, for example, an ad platform wants Cart Abandoners within minutes for retargeting. File-based or streaming, and which fields would you map?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production.
- This track is **read-only**. Do not click **New Datastream**, **Activate audiences**, **Activate** or **Publish**, and do not edit anything under **Accounts**.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Open **Data Collection**, then **Datastreams**. Read the list: note how many datastreams exist and that each one shows a **Datastream ID**. Do not copy IDs anywhere public.
2. In the same **Data Collection** menu, find **Tags** and **Assurance**. Write one line on what each is for.
3. Open **Destinations**. Read the five tabs: **Overview**, **Catalog**, **Browse**, **Accounts**, **System view**.
4. On **Catalog**, use the **Data types** filter and tick **Audiences**. Then open the **Cloud storage** category and read one card. Do not click **Activate audiences**.
5. Open **Browse** and **System view**. Which audiences, if any, already flow to a destination in your sandbox? Adobe documents the activation wizard as Select audiences, Scheduling, Mapping and Review; check what your screen shows.

## Check yourself

1. What problem does the Web SDK and datastream combination solve, in one sentence?
2. What does the Datastream ID do, and what goes wrong if it is the wrong one?
3. Trace one click from Bloom's website to the profile in five stations.
4. The agency wants a nightly file. File-based or streaming, and why?
5. What is the difference between a profile export and an audience export?
6. Why do emails travel hashed, and why must they be cleaned before hashing?
7. Why do you map only the minimum?
8. Name the three layers that enforce consent.

<details><summary>Check your answers</summary>

**Task 1: the five stations**
1. A shopper taps Add to cart on Bloom's website.
2. The Web SDK tag captures it as an XDM event.
3. The Edge Network datastream receives and routes it.
4. It lands in the Bloom Web Events dataset.
5. Profile-enabled, it folds into the shopper's Real-Time Customer Profile.

It is the same path as a batch load (source, collection, routing, dataset, profile), at click speed.

**Task 2: file-based or streaming**

| Partner | Choice | Why |
|---|---|---|
| Media agency, nightly file | File-based (cloud storage) | The agency acts once a night; minutes add cost and no value |
| Retargeting ad platform | Streaming | Speed pays for itself: the shopper is reached while still interested |
| Data-science team, weekly extract | File-based | A scheduled weekly file matches how the team works. If they want raw data rather than an audience, look at what the catalogue lists under the Datasets data type, and check what your screen shows |
| SMS vendor | It depends on how fast it acts | A scheduled text campaign suits a file; a time-critical text suits streaming. Either way the audience must require SMS consent true, and the phone number is exactly the kind of field Legal checks in episode 13 |

The deciding question every time: how quickly does this partner act on the data?

**Task 3: the minimum mapping**
- Keep **email, hashed**: the agency needs it to match people, and hashing means it never holds the raw address.
- Keep **loyalty band**: the agency needs it to shape the creative.
- Cut **first name, city and points**: no job to do. Every extra field is extra risk, more for the partner contract to cover, and more audit work.
- Cut or escalate **phone**: email already does the matching. Flag it for Legal rather than deciding alone.

Bloom's final mapping is hashed email and loyalty band only.

**Task 4: the consent layer**
The audience rule itself. Lapsed 90 requires email consent true, so Ananya never qualifies and the win-back file cannot contain her. The rule was built in episode 10, and it works only because episode 6 mapped the consent columns to the `_bloom` consent fields.

**Task 5: practice question**
Streaming, because the platform acts within minutes and speed pays for itself in retargeting. Map the minimum: the hashed email the platform needs to match people, and nothing else unless the partner has a clear use for it.

**Track B: what to expect**
Data Collection lists Tags, App Surfaces, Datastreams, Extension Management, Event Forwarding, Monitoring and Assurance. Each datastream shows a Datastream ID. Destinations shows five tabs, and Catalog filters by Data types (Accounts, Datasets, Prospects, Audiences). Browse may be empty in a fresh sandbox; that is normal.

**Check yourself**
1. One tag replaces a pixel per tool: behaviour is captured once, as XDM, and the datastream routes it to every service that needs it, without changing the page.
2. It wires the tag on the page to its datastream. The wrong ID can pour production traffic into a development sandbox.
3. Click, Web SDK tag, Edge datastream, Bloom Web Events dataset, Real-Time Customer Profile.
4. File-based: the agency ingests a scheduled nightly file. Streaming delivers within minutes and costs more, which a nightly reader does not need.
5. A profile export sends people with the fields you map. An audience export sends membership, for the partner to match against its own users.
6. Hashing lets the partner match against its own hashed list without holding raw addresses. The hash of an address with a stray capital letter is a different code, so emails are lower-cased and trimmed first. A hashed email is still personal data, because anyone holding the same address can match it.
7. Every extra field is extra risk, more for the partner contract to cover, and one more thing to explain in an audit.
8. The audience rule, the policy at the destination, and the channel check at send time.

</details>
