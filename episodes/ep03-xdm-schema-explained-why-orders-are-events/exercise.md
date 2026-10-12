# Exercise: Episode 03, XDM Schema Explained: Why Orders Are Events

Time: about 45 minutes. You need paper, a pen and a text editor. No Adobe login is required for Track A.

Use the three sample files in the repo's `/data` folder as patterns: `sample-profile-priya.json`, `sample-web-event.json` and `sample-order-event.json`.

## Track A: No Adobe access needed

1. **Profile or event?** Sort these 12 Bloom fields into **profile** or **event**. For each one, write one line that applies the litmus test "can this be recomputed from events?". If a field should not be stored at all, say so.

   | # | Bloom field | Profile or event? | Your reason |
   |---|---|---|---|
   | 1 | Loyalty tier | | |
   | 2 | Points | | |
   | 3 | Email consent | | |
   | 4 | Home city | | |
   | 5 | Order total | | |
   | 6 | Product viewed | | |
   | 7 | Add-to-cart | | |
   | 8 | Refund | | |
   | 9 | Total spent this year | | |
   | 10 | Join date | | |
   | 11 | Phone | | |
   | 12 | Push consent | | |

2. **Three shapes for Maya Rao.** Use these values for Maya Rao, one of Bloom's customers: BloomID `BLM-CUST-000048`, email `maya.rao48@example.com`, tier **Silver**, **880** points. Following the three sample files, write:
   1. her **profile record**, with her custom fields under `_bloom`
   2. one **web event** (an add-to-cart)
   3. one **order event**

   Put `_id` and `timestamp` on both events. Then label the data type of every value: string, integer, date-time, boolean, object or array. Any value you have to make up (an ECID, a timestamp, an order number) is illustrative; say so.

3. **Pick the field groups.** From this list, choose the right field groups for each of Bloom's three schemas (Bloom Customer Profile, Bloom Web Event, Bloom Order Event). Two groups belong to no Bloom schema. Name them and say why.
   - Personal Contact Details (standard)
   - Demographic Details (standard)
   - Consumer Experience Event (standard)
   - Commerce Details (standard)
   - B2B Person Components (standard)
   - Channel Details (standard)
   - `_bloom` Loyalty (custom: tier, points, join date)
   - `_bloom` Preferences and Consent (custom: consent flags)
   - `_bloom` Order fields (custom)

4. **Where does Priya's cart live?** Answer in two sentences. Then say what the platform would wrongly conclude about her 7:44 PM add-to-cart if the three sample files were loaded today.

5. **The practice question from the episode.** A colleague wants to store "date of last order" on every Bloom profile. Good idea or bad idea? Use the litmus test in your answer.

## Track B: If you have a development sandbox (optional, look only)

Safety first: look, screenshot, leave. Create nothing, save nothing, and never touch the Profile toggle. Never click Activate, Publish or Send proof.

1. Check the sandbox switcher under the top bar. Continue only if it says **Development**.
2. In Experience Platform, open **Data Management**, then **Schemas**. Write down which existing schemas use the Individual Profile class and which use ExperienceEvent, and what the **Behavior** column shows for each one (Record or Time-series).
3. Open one existing schema that uses a standard field group such as **Personal Contact Details**. Find the field group in the **Composition** panel and read its fields on the canvas.
4. Select one field to open its **Field properties** panel, and look for its type. Try to find one example each of a string, a date-time, a boolean, an object and an array. Change nothing in the panel.
5. Close the schema without saving. If anything asks you to save, choose not to.

## Check yourself

1. In one sentence, what is XDM, and what does Bloom gain from it?
2. Bloom wants to store "number of orders in the last 12 months" as a field on the profile. Good idea or bad idea, and why?
3. What two fields must every ExperienceEvent carry, and why does one of them make sense philosophically?
4. Why do custom fields live under `_bloom` instead of at the root of the schema?
5. Why does Priya's web event carry no email address?
6. What does "additive-only schema evolution" forbid, and when does the restriction start applying?
7. Which schema choice is permanent from the moment you save, even before any data lands?
8. Where does a customer's shopping cart live in AEP?
9. If the three sample files were loaded today, how many Priyas would the platform see, and why is that acceptable for now?

<details><summary>Check your answers</summary>

**Track A**

1. Model answers:

   | # | Bloom field | Where it lives | Reason |
   |---|---|---|---|
   | 1 | Loyalty tier | Profile | Bloom's current, updatable claim about the customer; it changes in place. |
   | 2 | Points | Profile | Like the balance in the bank test: Bloom's loyalty system keeps it, and the events Bloom sends to AEP do not record every way points are earned or spent, so it cannot be recomputed there. |
   | 3 | Email consent | Profile | A fact about the person. No event can tell you whether she agreed. |
   | 4 | Home city | Profile | Changes in place when she moves. |
   | 5 | Order total | Event | Part of the order event, written once and never edited. |
   | 6 | Product viewed | Event | Something that happened at a moment. |
   | 7 | Add-to-cart | Event | Something that happened at a moment. |
   | 8 | Refund | Event | A new event. The original order is never edited. |
   | 9 | Total spent this year | Not stored | Recomputable by adding up order events. A stored copy drifts out of date. |
   | 10 | Join date | Profile | A fact about the person, recorded once by the loyalty programme. |
   | 11 | Phone | Profile | Changes in place: a new number replaces the old one. |
   | 12 | Push consent | Profile | A fact about the person, like email consent. |

2. One good answer. The ECID, timestamps, purchase ID, product choice and consent values are illustrative.

   Profile record:

   ```json
   {
     "person": { "name": { "firstName": "Maya", "lastName": "Rao" } },
     "personalEmail": { "address": "maya.rao48@example.com" },
     "_bloom": {
       "loyalty": { "tier": "Silver", "points": 880 },
       "preferences": { "marketingConsent": { "email": true, "sms": false } }
     }
   }
   ```

   Web event (anonymous, like Priya's):

   ```json
   {
     "_id": "evt-web-maya-0001",
     "timestamp": "2026-08-20T10:15:00Z",
     "eventType": "commerce.productListAdds",
     "identityMap": { "ECID": [ { "id": "11112222333344445555", "primary": true } ] },
     "productListItems": [ { "SKU": "BLM-MOIST-HYA-50", "priceTotal": 20.00 } ]
   }
   ```

   Order event:

   ```json
   {
     "_id": "evt-order-maya-0001",
     "timestamp": "2026-08-20T10:30:00Z",
     "eventType": "commerce.purchases",
     "identityMap": { "Email": [ { "id": "maya.rao48@example.com" } ],
                      "BloomID": [ { "id": "BLM-CUST-000048" } ] },
     "commerce": { "order": { "purchaseID": "BLM-90001", "priceTotal": 20.00 } },
     "productListItems": [ { "SKU": "BLM-MOIST-HYA-50", "priceTotal": 20.00 } ]
   }
   ```

   Data types:

   | Value | Type |
   |---|---|
   | "Maya", "Rao", the email address, "Silver", every `_id`, `eventType`, SKU and ID value | string |
   | 880 (points) | integer |
   | both `timestamp` values | date-time |
   | consent `true` and `false` (illustrative values) | boolean |
   | `person`, `name`, `personalEmail`, `_bloom`, `loyalty`, `commerce`, `order`, each line item | object |
   | `productListItems` | array (of objects) |

   `priceTotal` holds a decimal number. It is not one of the six types named in the episode; episode 6 shows what happens when a price arrives as text. `identityMap` is an object whose entries are arrays of objects; episode 4 explains it.

   Check your shapes: are the events' `_id` values unique, does every event have a timestamp, and do only Bloom's own fields sit under `_bloom`?

3. Bloom Customer Profile: Personal Contact Details, Demographic Details, `_bloom` Loyalty, `_bloom` Preferences and Consent. Bloom Web Event: Consumer Experience Event (episode 4 adds a custom web identity field). Bloom Order Event: Commerce Details and `_bloom` Order fields. The two distractors: **B2B Person Components** (for people inside business accounts, not consumers) and **Channel Details** (none of Bloom's three schemas needs it; Adobe's field group list changes over time, so do not worry if your own sandbox names it differently or does not show it).
4. Nowhere: there is no cart object. A cart is derived: add-to-cart events not followed by a purchase. Loaded today, her 7:44 PM add-to-cart carries only an ECID, and no purchase follows on that ECID, so it would look like an abandoned cart, and the platform would see two Priyas. Identity stitching (episode 7) fixes this.
5. Bad idea. "Date of last order" can be recomputed from order events, so a stored copy starts drifting out of date the moment the next order arrives. Compute it from the events.

**Track B**

There is no single right list: different sandboxes hold different schemas. You should find Individual Profile schemas showing Record and ExperienceEvent schemas showing Time-series. If you could not find a boolean or an array, that is fine; not every schema has one. If you saved nothing, you did it right.

**Check yourself**

1. XDM is Adobe's one standard vocabulary for customer data. Bloom translates each source once, at the door, and every downstream service reads the same fields by the same names.
2. Bad idea. It can be recomputed from order events, so a stored copy starts drifting out of date the moment it is written.
3. `_id` and `timestamp`. An event is a fact about a moment; without a "when" it is not an event at all.
4. The tenant namespace keeps Bloom's fields apart from Adobe's standard fields, so Adobe can evolve its fields without ever colliding with Bloom's.
5. The app session was anonymous: Priya had not signed in, so the event only knows the app install's ECID.
6. Removing or retyping fields. It applies once data has landed against the schema, which is why you design and check on paper first.
7. The class (XDM Individual Profile or XDM ExperienceEvent).
8. Nowhere. There is no cart object; a cart is derived from add-to-cart events not followed by a purchase.
9. Two: the anonymous ECID person and the known email person. That is acceptable for now because identity stitching (episode 7) joins them.

</details>
