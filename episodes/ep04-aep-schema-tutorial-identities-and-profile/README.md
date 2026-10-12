# Episode 04: AEP Schema Tutorial: Identities and Profile

**Watch:** Video coming soon on iTV

Part 1: Know your customer (AEP and Real-Time CDP) · [Previous](../ep03-xdm-schema-explained-why-orders-are-events/) · [Next](../ep05-aep-data-ingestion-tutorial-batch-vs-streaming/)

## What you will learn

- Choose an identity namespace and its type for each Bloom identifier, and justify email as the primary identity
- Mark an identity field in the right order: **Identity**, namespace, **Primary identity**, **Apply**, then **Save**
- Explain why the order event carries two identities, and why that is the hook for identity stitching
- Enable a schema for Profile safely, knowing it is irreversible and needs its own save
- Verify the end state in **Schemas**, **Browse** instead of trusting a success message

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, rebuilding its customer data on Adobe Experience Platform (AEP) before its loyalty relaunch.
In episode 3, Kavya designed the model on paper: Bloom Customer Profile on the Individual Profile class, Bloom Web Event and Bloom Order Event on the ExperienceEvent class, and custom fields under `_bloom`.
She also found that the platform sees two Priyas, because nothing links Priya's anonymous phone to her email.
In this episode Farhan, the data engineer, opens the real schema editor in Bloom's development sandbox.

## Key ideas

### 1. An email field is not an identity
A field that holds an email is just text until the schema declares it an **identity**: "this value names a person". The mapping step (episode 5) decides which field receives a value; the **schema** decides whether that value can identify anyone. Without a declared identity, rows can still land in the data lake, but the platform can never build a profile from them. In one line: **a schema without a primary identity is a spreadsheet.**

### 2. Identity namespaces
An **identity namespace** answers one question: *what kind of ID is this string?* `BLM-CUST-004217` means nothing alone; tagged with **BloomID** it becomes Bloom's customer number. **Email** and **ECID** ship with the platform (owner **Standard**); **BloomID** is Bloom's own (owner **Custom**). In a shared sandbox the team shares one custom namespace.

### 3. Namespace types are permanent
When a namespace is created, its **type** is permanent, and the namespace **cannot be renamed or deleted**, even though its display name looks editable. The type tells the platform what the value identifies, which changes how the identity graph (episode 7) treats it.

| Namespace type | Identifies |
|---|---|
| Cookie ID | A browser |
| Individual cross-device ID | A person, such as a CRM or login ID |
| Hardware device ID | A device |
| Non-people identifiers | Things like a product SKU; kept off the identity graph |

Bloom's customer number belongs to a person, so **BloomID** is an **Individual cross-device ID**.

### 4. Primary identity: why email beats the ECID
The **primary identity** is the main key for the person; a schema can have only one. The **Experience Cloud ID (ECID)** is an anonymous wristband each browser or app install receives automatically, so a family tablet shared by three people wears one wristband. An email follows the person across devices, and Bloom's customer records, orders and email tool all share it. So **Email** is primary on Bloom Customer Profile, on `personalEmail.address`.

### 5. Marking an identity: Apply is not Save
In **Field properties**: tick **Identity**, choose the **Identity namespace**, tick **Primary identity**, click **Apply**, then **Save**. **Apply** commits the field-properties panel; **Save** commits the schema. Apply sits at the very bottom of the panel, below the fold. Miss it and the identity silently never exists, even though the save message appears. The proof is the **fingerprint icon** on the field and the **Identities** entry in the left panel naming the field.

### 6. Two identities on the order event
Bloom Order Event declares `bloomId` as the primary identity (BloomID) and `orderEmail` as a second, non-primary identity (Email). The customer profile carries the email too, so the platform can attach order history to the right person without anyone writing a join. This is the hook identity stitching grabs in episode 7, and it is where Priya's BloomID becomes an identity (her order carries her email and BloomID together).

| Schema | Field | Namespace | Identity |
|---|---|---|---|
| Bloom Customer Profile | `personalEmail.address` | Email | Primary |
| Bloom Customer Profile | BloomID value | none | Plain attribute, no identity |
| Bloom Web Event | `_bloom.visitorId` | ECID | Primary |
| Bloom Order Event | `_bloom.bloomId` | BloomID | Primary |
| Bloom Order Event | `_bloom.orderEmail` | Email | Second identity |

The stock field `personID` ships with **Identity** unticked, so a customer number mapped there identifies nobody. Naming `bloomId` and `orderEmail` after the file's columns (`bloom_id`, `email`) pays off in episode 6. Note: the sample file `sample-profile-priya.json` lists BloomID in its identityMap as a teaching shape; Bloom Customer Profile itself declares one identity, Email.

### 7. Validate on paper before the irreversible step
Read each sample file field by field against your design: does every value have a home? The **identityMap** is the part of a record that lists its identity values. The clearest mismatch: the order sample marks Email as primary, while the order schema marks BloomID. The schema is the contract. The exercise finds the rest.

### 8. Enable for Profile: a one-way door with its own save
**Enable for Profile** lets a schema's data reach the Real-Time Customer Profile as well as the data lake. It needs a primary identity first, and the dialog warns: *"Once enabled and saved, the schema can't be disabled."* Practise only on your own schema in a development sandbox. Saving identities and the Profile flag in **one** Save can **silently drop the Profile flag** while the message still says "Schema saved successfully" (at Bloom, on the web event schema). So give Profile its own save, then look.

### 9. Verify in Schemas, Browse
The finish line, filtered on "Bloom":

| Schema | Identities | Enabled for Profile | Behavior |
|---|---|---|---|
| Bloom Customer Profile | 1 | Enabled | Record |
| Bloom Web Event | 1 | Enabled | Time-series |
| Bloom Order Event | 2 | Enabled | Time-series |

Anything else means something did not save. Fix it before any data arrives.

## In the product

Labels as of October 2026.

1. **Namespaces (look only):** **Identities** in the left rail, then the **Namespaces** tab. Read each namespace's owner (**Standard** or **Custom**) and type. New ones are made in the **Create identity namespace** dialog; on a shared sandbox, do not create one.
2. **Create a schema:** **Schemas**, **Browse**, **+ Create schema** (top right). Choose **Standard**, then **Manual**, then **Select**. Pick the class card (**Individual Profile** or **Experience Event**), click **Next**, enter the name with your initials, click **Finish**. The class is permanent once saved. In the editor, **Composition** is the left panel, the canvas is in the middle and **Field properties** or **Schema properties** opens on the right.
3. **Add field groups:** next to **Field groups** click **Add**, tick the groups (for example **Personal Contact Details** and **Demographic Details**), click **Add field groups**. For your own fields, switch to **Create new field group** in the same dialog.
4. **Add a custom field:** click the **+** beside the schema root, enter the **Field name**, clear the auto-filled **Display name** before typing it, choose the type (for example **String**), and assign it to your existing field group, not the "(New)" entry.
5. **Mark an identity:** use **Search schema**, click the field, and in **Field properties** tick **Identity**, choose the **Identity namespace** (custom ones are listed first; type to filter), tick **Primary identity** if it is the main key, scroll down to **Apply**, then **Save** (top right). Look for the fingerprint icon.
6. **Enable for Profile:** in the **Composition** panel click the schema name row (not the root node on the canvas). In **Schema properties** turn on **Profile**, read the dialog, click **Enable**, then **Save**. Do this as a save of its own.
7. **Verify:** **Schemas**, **Browse**, filter on your schema names, and read **Identities**, **Enabled for Profile** and **Behavior**. If a row says **Not enabled**, repeat step 6.

## Common mistakes

- Saving without clicking **Apply**, so the identity never exists.
- Making the ECID the primary identity on a customer profile.
- Creating a namespace per project, or guessing its type. Both are permanent.
- Mapping a customer number into `personID` and expecting an identity.
- Setting identities and the Profile toggle in one save, then trusting "Schema saved successfully".
- Turning on Profile for a schema that is not yours.
- Checking only the schema you edited last instead of reading every row in **Browse**.

## Glossary

| Term | Meaning |
|---|---|
| Identity | A field the schema declares as an identifier, such as an email, an ECID or a BloomID |
| Identity namespace | A kind of identifier, such as Email, ECID or the custom BloomID |
| Namespace type | What a namespace identifies (browser, person, device or thing); permanent |
| Individual cross-device ID | The namespace type for a person, such as a CRM or login ID |
| Primary identity | The identity a schema treats as the main key for the person; one per schema |
| Experience Cloud ID (ECID) | The anonymous wristband a browser or app install receives automatically |
| identityMap | The part of a record that lists the identity values it carries |
| Enabled for Profile | A schema setting that lets its data reach the profile store; irreversible |
| Behavior | Record (changes in place) or Time-series (events on a timeline) |
| personID | A stock field with Identity unticked; it creates no identity |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Create a schema in the UI: https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui
- Identity namespaces: https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/namespaces
- Getting around the Platform UI: https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-ui/ui-guide
- Search Experience League for: enable schema for Real-Time Customer Profile, define identity fields in the schema editor

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
