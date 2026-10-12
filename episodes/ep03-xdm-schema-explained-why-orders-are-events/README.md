# Episode 03: XDM Schema Explained: Why Orders Are Events

**Watch:** [Watch episode 3 on YouTube](https://youtu.be/IrMvTAQzOP4)

Part 1: Know your customer (AEP and Real-Time CDP) · [Previous](../ep02-aep-architecture-data-lake-vs-profile-store/) · [Next](../ep04-aep-schema-tutorial-identities-and-profile/)

## What you will learn

- Define **schema**, **class** and **field group**, and pick the right class for any Bloom record.
- Decide whether a fact belongs on the profile or in an event, using the bank test and the litmus test "can this be recomputed from events?".
- Explain why every ExperienceEvent needs `_id` and `timestamp`, and name six core XDM data types.
- Explain why custom fields live under the tenant namespace (`_bloom`) and why schema changes are additive-only.
- Read a profile record, a web event and an order event in JSON, and say what each one knows about the person.

## The story so far

Kavya Menon has joined Bloom, a wellness brand with 1.2 million customers in three systems that do not talk to each other.
In episode 2, Vikram Joshi showed her the inside of Adobe Experience Platform (AEP): sandboxes are practice kitchens, the data lake is the archive, the profile store is the receptionist, and one checkbox sends each row into both worlds.
He ended with a warning: before any data comes in, Bloom must agree what a customer is.
Today, Farhan Qureshi (data engineer) and Vikram help her design Bloom's data model on paper.

## Key ideas

### 1. XDM, the shipping container

Bloom's CRM export says `email_address`, the shop says `EmailAddr`, the email tool says `contact.email`: one fact, three names, and a translation to maintain between every pair of systems.

**Experience Data Model (XDM)** is Adobe's one standard vocabulary for customers and what they do. Data entering AEP must arrive shaped as XDM; in exchange, profiles, audiences, journeys and analytics all understand it natively. Each source is translated once, at the door, into standard fields such as `personalEmail.address`. Analogy: **the shipping container**: standardise the box once, and every ship, crane and truck can handle it.

### 2. Schema = class + field groups

- A **schema** is the blueprint for one kind of record ("what a customer looks like", "what an order looks like").
- The **class** says what the record fundamentally is. Bloom uses two: **XDM Individual Profile** (a person) and **XDM ExperienceEvent** (something that happened at a moment). The class is **permanent once the schema is saved**.
- **Field groups** are reusable bundles of fields you snap on like **LEGO bricks**. Adobe ships hundreds of standard ones; your own fields go in custom field groups.

Bloom's design:

| Schema | Class | Field groups | Behavior |
|---|---|---|---|
| Bloom Customer Profile | XDM Individual Profile | Personal Contact Details, Demographic Details, custom `_bloom` loyalty and consent | Record |
| Bloom Web Event | XDM ExperienceEvent | Consumer Experience Event | Time-series |
| Bloom Order Event | XDM ExperienceEvent | Commerce Details, custom `_bloom` order fields | Time-series |

### 3. Profile versus event: the bank test

| Your account details = **profile** | Your transactions = **events** |
|---|---|
| Name, phone number, account type | "Paid 54 dollars at 7:52 PM on 18 August" |
| Change in place: a new phone number replaces the old one | Written once and never change |
| Answer "who is this person now?" | Answer "what has this person done?" |

At Bloom: loyalty tier, consent and home city are profile; orders, product views and add-to-carts are events. A refund is a **new** event; history is never rewritten.

### 4. The litmus test: can this be recomputed from events?

- **Yes** (for example "total spent this year"): compute it from the events. A stored copy drifts out of date the moment it is written.
- **No** (for example email consent): it is a fact about the person, so it belongs on the profile.

### 5. Every event needs `_id` and `timestamp`

- `_id` is a unique identifier; `timestamp` is the moment it happened.
- An event is a fact about a moment: without a "when" it is not an event at all. Episode 6 shows real errors on order rows with a missing or broken timestamp.

### 6. Six data types

| Type | Plain meaning | Example from Priya's records |
|---|---|---|
| string | Text | `"firstName": "Priya"` |
| integer | Whole number | `"points": 2340` |
| date-time | An exact moment | `"timestamp": "2026-08-18T19:44:12Z"` |
| boolean | True or false | `"email": true` (email consent) |
| object | A bundle of named fields | `"order": { "purchaseID": ..., "priceTotal": ... }` |
| array | A list | `productListItems`, an **array of objects**, one per line item |

The platform's errors name types, for example "Unable to convert ... to schema type DATE_TIME", and "The source field with the leaf schema type STRING cannot be mapped to the destination field of type OBJECT", which Bloom meets in episode 6.

### 7. The tenant namespace `_bloom`

Custom fields live under your company's own space, the **tenant namespace**, shown in the editor as `_{tenantId}` (at Bloom, `_bloom`). Standard fields (`person`, `personalEmail`) sit at the root because Adobe defines them; Bloom's inventions (loyalty, preferences) sit under `_bloom`, so Adobe's changes to its standard fields can never collide with them.

### 8. Additive-only schemas

Once data has landed against a schema, you can **add** fields, but you cannot **remove** or **retype** one. Analogy: **adding rooms to a house people live in**: extensions are fine, demolitions are not. So design on paper first, check the design against sample records, and only then build.

### 9. Priya's evening in three records

**Profile record** (who she is now):

```json
"person":        { "name": { "firstName": "Priya", "lastName": "Sharma" } },
"personalEmail": { "address": "priya.sharma@example.com" },
"_bloom":        { "loyalty": { "tier": "Gold", "points": 2340, "joinDate": "2023-11-02" },
                   "preferences": { "marketingConsent": { "email": true, "sms": false } } }
```

Its `identityMap` section lists the values that identify her (episode 4). The sample lists her BloomID there as a teaching shape; in Bloom's build, BloomID becomes an identity through the order event, not the CRM record.

**Web event, 7:44 PM** (an add-to-cart on the Bloom app on her phone):

```json
"_id":        "evt-web-20260818-000341",
"timestamp":  "2026-08-18T19:44:12Z",
"eventType":  "commerce.productListAdds",
"identityMap": { "ECID": [ { "id": "38472919862011456743", "primary": true } ] },
"productListItems": [ { "SKU": "BLM-SER-VITC-30", "priceTotal": 34.00 } ]
```

No name, no email: only an **Experience Cloud ID (ECID)**, the anonymous ID the app install received. This event is an orphan.

**Order event, 7:52 PM** (on her laptop, as a known customer):

```json
"_id":        "evt-order-20260818-088412",
"timestamp":  "2026-08-18T19:52:47Z",
"eventType":  "commerce.purchases",
"identityMap": { "Email":   [ { "id": "priya.sharma@example.com" } ],
                 "BloomID": [ { "id": "BLM-CUST-004217" } ] },
"commerce":   { "order": { "purchaseID": "BLM-88412", "priceTotal": 54.00 } },
"productListItems": [ { "SKU": "BLM-SER-VITC-30",  "priceTotal": 34.00 },
                      { "SKU": "BLM-MOIST-HYA-50", "priceTotal": 20.00 } ]
```

The order knows the person, the products (Vitamin C Serum 30 ml, Hyaluronic Moisturiser 50 ml), the money and the moment. Which identity is primary is decided in episode 4. Prices are in US dollars (Bloom's US storefront).

### 10. A cart is derived, and today there are two Priyas

- There is **no cart object**. A cart is add-to-cart events not followed by a purchase. It becomes the Cart Abandoners audience in episode 10 and the Cart Rescue journey in episode 21.
- Loaded today, these files would give the platform **two Priyas**: the anonymous app person (ECID) and the known email person, and her add-to-cart would look abandoned. Identity stitching joins them in episode 7.

## In the product

Labels as of October 2026. In this episode, **look only**; episode 4 builds the schemas.

1. In Experience Platform, open the left rail group **Data Management**, then **Schemas**.
2. **Create schema**, then **Standard**, leads to a wizard whose first step is **Select a class**, with cards labelled **Individual Profile**, **Experience Event** and **Other**. The class is permanent once saved. Do not create anything yet.
3. Inside a schema, the **Composition** panel lists its **Field groups**, with **Add**. For a custom group, switch the Add field groups dialog to **Create new field group**.
4. Select a field to open its **Field properties** panel, and look for its type.
5. In the schema list, the **Behavior** column reads **Record** for a profile schema and **Time-series** for an event schema.

## Common mistakes

- **Loading data first and arguing about the shape later.** Every audience, journey and report inherits a bad schema.
- **Picking the class in a hurry.** It is permanent once the schema is saved.
- **Storing orders, totals or counts on the profile.** The next order overwrites or outdates them. If it can be recomputed from events, compute it.
- **Making every field a string.** Text accepts anything, then every number and date rule breaks.
- **Inventing a custom field the standard ones already cover**, such as a second email field on the customer profile.
- **Building live and fixing later.** Once data lands, you cannot remove or retype a field.

## Glossary

| Term | Meaning |
|---|---|
| Experience Data Model (XDM) | Adobe's standard vocabulary for customer data; all data in AEP is shaped as XDM. |
| Schema | The blueprint for one kind of record, built from a class plus field groups. |
| Class | What a record fundamentally is: XDM Individual Profile (a person) or XDM ExperienceEvent (something that happened). |
| Field group | A reusable bundle of fields you snap onto a schema, either standard or your own. |
| ExperienceEvent | A timestamped record of something that happened; it never changes and needs `_id` and `timestamp`. |
| Tenant namespace | Your company's own prefix (`_bloom`) where custom fields live, so Adobe's changes never collide with yours. |
| Data type | The kind of value a field holds; the series names six: string, integer, date-time, boolean, object, array. |
| Additive-only | Once data has landed, fields can be added but never removed or retyped. |
| Behavior (Record, Time-series) | Schema-list column: Record for profile schemas, Time-series for event schemas. |
| identityMap | The part of a record that lists the identity values it carries (episode 4). |
| Experience Cloud ID (ECID) | The anonymous ID a browser or app install receives automatically. |

## Exercise

Do the tasks in [exercise.md](exercise.md): paper and JSON only by default, with an optional look-only sandbox track.

## Further reading

- [Create a schema in the UI](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui)
- [Getting around the Platform UI](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-ui/ui-guide)
- Search Experience League for: XDM system overview
- Search Experience League for: XDM field groups
- Search Experience League for: XDM data types
- Search Experience League for: schema evolution rules

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
