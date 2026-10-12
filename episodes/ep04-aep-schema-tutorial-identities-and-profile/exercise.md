# Exercise 04: Identities and the Profile switch

You will design Bloom's identities on paper, check the design against three sample records, and write the checkpoint that proves a schema build is finished.

Files: `sample-profile-priya.json`, `sample-web-event.json` and `sample-order-event.json` from the repo's `/data` folder.

## Track A: No Adobe access needed

1. **Fill the identity design table** for Bloom's three schemas. Add one row per identifier, including any identifier that should stay a plain attribute.

   | Schema | Field | Namespace | Namespace type | Primary, second identity, or plain attribute? |
   |---|---|---|---|---|
   | Bloom Customer Profile | | | | |
   | Bloom Web Event | | | | |
   | Bloom Order Event | | | | |

2. **Justify the primary identity.** In two sentences, explain why email, not the ECID, is the primary identity on Bloom Customer Profile.
3. **Explain the order event.** In three or four sentences, explain why the order event carrying both `bloomId` and `orderEmail` lets the platform attach Priya's order history to her profile without anyone writing a join.
4. **Validate on paper.** Open the three sample files. Check each one field by field against your design from task 1. List every mismatch or missing home you would fix before enabling anything. For each, say whether you would change the schema, the sample, or nothing.
5. **Write the end-of-build checkpoint** you expect in **Schemas**, **Browse**: the identity count for each schema, the **Enabled for Profile** value, and the **Behavior** value.
6. **The episode's practice question.** Say, for example, Bloom adds a login ID for its app. Which namespace type would you choose, and why must you choose carefully?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production, and only objects that carry **your own initials**.
- **Enable for Profile cannot be undone.** Do it only on the schema you create in this exercise, never on anyone else's.
- **Never create identity namespaces in a shared sandbox.** This track uses only the standard Email namespace.
- Nothing here needs **Activate**, **Publish** or any send. Do not click them.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Go to **Identities**, **Namespaces**. Find **Email** and **ECID** and note their owner and type. Do not create anything.
2. Go to **Schemas**, **Browse**, **+ Create schema**. Choose **Standard**, then **Manual**, then **Select**. Pick **Individual Profile**, click **Next**, name it **Bloom Customer Profile &lt;your initials&gt;**, and click **Finish**.
3. Next to **Field groups** click **Add**. Tick **Personal Contact Details** and **Demographic Details**, then click **Add field groups**.
4. Type `personalEmail` in **Search schema** and click **address**. In **Field properties**, tick **Identity**, set **Identity namespace** to **Email**, and tick **Primary identity**. Scroll down, click **Apply**, then click **Save**. Confirm the fingerprint icon and the **Identities** entry in the left panel.
5. Now give Profile its own save. Click the schema name row in **Composition**. In **Schema properties** turn on **Profile**, read the dialog, click **Enable**, then **Save**.
6. Go back to **Schemas**, **Browse** and find your schema. Write down **Identities**, **Enabled for Profile** and **Behavior**. If it reads **Not enabled**, repeat step 5 and look again.

## Check yourself

1. What question does an identity namespace answer?
2. Name the four namespace types and what each identifies. Which one is BloomID?
3. What can you never do to a namespace after it is created?
4. What is the difference between **Apply** and **Save** in the schema editor?
5. How can you tell from the screen that a field is an identity?
6. Why does the stock `personID` field not give you an identity?
7. Can you disable Profile on a schema once it is enabled and saved? What does it need first?
8. Why can "Schema saved successfully" be misleading, and where do you check instead?

<details><summary>Check your answers</summary>

**Task 1: a model design table**

| Schema | Field | Namespace | Namespace type | Role |
|---|---|---|---|---|
| Bloom Customer Profile | `personalEmail.address` | Email | Standard; its type is set by Adobe | Primary |
| Bloom Customer Profile | the BloomID value | none | none | Plain attribute, no identity |
| Bloom Web Event | `_bloom.visitorId` | ECID | Standard; its type is set by Adobe (it names a browser or app install) | Primary |
| Bloom Order Event | `_bloom.bloomId` | BloomID | Individual cross-device ID (custom, chosen by Bloom) | Primary |
| Bloom Order Event | `_bloom.orderEmail` | Email | Standard; its type is set by Adobe | Second identity |

Standard namespaces arrive with their type already set, so read it in the **Namespaces** list rather than guessing. The only type Bloom chose is BloomID's.

**Task 2: why email**
An ECID belongs to a browser or app install, not to a person, so one person has several and a shared family tablet puts several people behind one. An email follows the person across devices, and it is the identifier Bloom's customer records, orders and email tool all share.

**Task 3: the order event**
The order row carries both Bloom's customer number and the email address, and both are declared as identities. The customer profile also carries the email as its primary identity. Because the same email value appears on both, the platform can recognise that the order and the profile belong to one person, so the order history attaches to her without anyone writing a join. The same order is where Priya's BloomID becomes an identity, which is why the BloomID can stay a plain attribute on the profile. Stitching itself is episode 7.

**Task 4: what a careful check finds** (the method matters more than matching this list word for word)
- **Profile sample:** standard fields sit at the root and loyalty and consent sit under `_bloom`, with email marked primary. Good. Its identityMap also lists BloomID; that is a teaching shape, because Bloom Customer Profile declares one identity, Email. The phone arrives as `+1-469-555-0142`, not the cleaned `+14695550142`; that is a value to clean in Data Prep (episode 5), not a schema change. Check that your design has a home for every other field, such as the birthday and the favourite category. The consent block holds email, SMS and push, so your consent design needs all three.
- **Web event sample:** `_id`, `timestamp` and a single identity, the ECID, marked primary. Good. The ECID sits in the identityMap, while your schema declares `_bloom.visitorId` as the ECID field, so agree with the web team which shape they will send. The custom web fields under `_bloom` need a home in your design.
- **Order sample:** `_id`, `timestamp`, purchase ID `BLM-88412`, total 54.00, and two line items in `productListItems`. Good. Its identityMap marks **Email as primary**, but Bloom Order Event marks **BloomID** as primary. The schema is the contract, so fix the sample. Its identities sit in the identityMap rather than in `_bloom.bloomId` and `_bloom.orderEmail`, so make sure each value has its home. The custom order fields under `_bloom` need a home, or a deliberate decision to leave them out.

**Task 5: the checkpoint**
Three rows. Identities: customer profile one, web event one, order event two. **Enabled for Profile:** Enabled on all three. **Behavior:** Record for the customer profile, and Time-series for the two event schemas. Anything else means something did not save.

**Task 6: practice question**
Individual cross-device ID, because a login ID identifies a person, not a browser or a device. Choose carefully because the type is permanent and the namespace can never be renamed or deleted.

**Track B: what to expect**
Your schema shows **Identities** 1, **Enabled for Profile** Enabled, and **Behavior** Record. If you set the identity and the Profile toggle in one save, you may see **Not enabled** even though the message said "Schema saved successfully"; that is the trap from the episode.

**Check yourself**
1. What kind of ID a string is.
2. Cookie ID identifies a browser. Individual cross-device ID identifies a person. Hardware device ID identifies a device. Non-people identifiers identify things like a SKU and are kept off the identity graph. BloomID is an Individual cross-device ID.
3. Rename it or delete it. Its type is also permanent.
4. **Apply** commits the Field properties panel; **Save** commits the schema. Without Apply, the identity never exists.
5. The fingerprint icon on the field, and the **Identities** entry in the left panel naming it.
6. It ships with its **Identity** box unticked, so a value mapped there is stored as plain text.
7. No. The dialog says "Once enabled and saved, the schema can't be disabled." It needs a primary identity first.
8. Saving identities and the Profile flag in one save can silently drop the flag while the message still reports success. Check the **Enabled for Profile** column in **Schemas**, **Browse**.

</details>
