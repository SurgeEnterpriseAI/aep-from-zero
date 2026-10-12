# Exercise 05: Land Bloom's data, cleanly

You will plan the mapping for Bloom's customer file, write the three clean-ups that run at the door, and sort Bloom's feeds onto the two roads in.

Files: `bloom-customers-500.csv` from the repo's `/data` folder.

## Track A: No Adobe access needed

1. **Map the 14 columns.** Open `bloom-customers-500.csv`. For each of its 14 columns, write the XDM field it should land in on Bloom Customer Profile.
   - Include `email_consent`, `sms_consent` and `push_consent`, and send each to a `_bloom` consent field.
   - Mark the identity column, and say whether it is primary.
   - Say where `bloom_id` goes on this schema, and why it is not an identity here.
2. **Write the phone clean-up.** Write the steps that turn each of these into `+14695550142`:
   - `(469) 555-0142`
   - `469.555.0142`
   - `4695550142`
   - `1-469-555-0142`
   - `+1-469-555-0142`

   Then run every shape through your steps by hand. Does any of them come out as `+114695550142`?
3. **Write the email clean-up.** Describe the two operations that turn ` Priya.Sharma@Example.com ` (note the spaces) into `priya.sharma@example.com`, and write one sentence on why an identity value must always be spelled exactly the same.
4. **Write the loyalty band.** Write the expression for `loyalty_band` (Bronze below 500, Silver 500 to 1,499, Gold 1,500 and above). Test it on Liam (259), Maya (880) and Noah (4,120), then on the edges 499, 500, 1,499 and 1,500.
5. **Sort eight feeds.** Classify each as batch or streaming, with a one-line reason:
   - 18 months of orders
   - live add-to-cart events
   - the nightly CRM export
   - app sign-in
   - the product catalogue
   - page views
   - a one-time loyalty migration
   - a purchase confirmation
6. **Trace one row.** Write the four stations Priya's customer row passes through, and the fifth possible ending. Then invent one row that you predict would be rejected, and say why.
7. **The episode's practice question.** Bloom wants a thank-you email within minutes of a first purchase, and finance wants last year's refunds loaded once. Which road does each feed take, and which columns must you map before any other?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production, and only objects that carry **your own initials**.
- Use only **your own** schema and dataset. Never turn on Profile for a schema or dataset that is not yours; enabling a schema for Profile is irreversible.
- Nothing here needs **Activate**, **Publish** or any send. Do not click them.
- You will **stop before Finish**, so nothing is loaded.
- In a shared sandbox: look, screenshot, leave.

Steps:
1. Go to **Sources**, **Catalog**, choose the category **Local system**, and on the **Local file upload** card click **Add data**. Write down the name of the workflow and its three steps.
2. On **Dataflow detail**, choose **New dataset** and name it "Bloom Customers" plus your initials. Pick your own Profile-enabled customer schema. Note the moment the **Profile dataset** toggle appears. Turn **Error diagnostics** on. Find **Enable partial ingestion** and write down its default. Click **Next**.
3. On **Select data**, upload `bloom-customers-500.csv`. Read the preview and write down row one.
4. On **Mapping**, stop. Write down every counter you can see, and the target auto-map chose for each of the 14 columns. Compare every one with your Track A plan and circle each difference.
5. Open the **New field type** menu and write down its options. Do not save anything.
6. Leave the workflow **without clicking Finish**. Keep your list of differences: episode 6 uses it.

## Check yourself

1. What single question decides whether a feed goes by batch or by streaming?
2. Name the four stations a row passes through, and the fifth ending.
3. What are Data Prep's two jobs?
4. Why do the identity columns matter more than every other column?
5. Why must the three consent columns land in `_bloom` consent fields rather than anywhere that will take them?
6. What goes wrong if you strip non-digits from `1-469-555-0142` and simply add `+1`?
7. Why must the "1,500 or more" test come before the "500 or more" test?
8. Which three switches sit on **Dataflow detail**, and what should each be set to for Bloom's trial?
9. What does the HTTP API streaming source give the web team, and what is Postman used for?

<details><summary>Check your answers</summary>

**Task 1: the mapping plan**

| CSV column | XDM home | Note |
|---|---|---|
| `email` | `personalEmail.address` | Identity, **primary**, Email namespace; lower-cased and trimmed first |
| `bloom_id` | a plain attribute on the profile | Bloom Customer Profile declares one identity, Email. BloomID becomes an identity through the order file |
| `first_name` | `person.name.firstName` | |
| `last_name` | `person.name.lastName` | |
| `phone` | `mobilePhone.number` | After the phone clean-up |
| `loyalty_tier` | `_bloom.loyalty.tier` | |
| `loyalty_points` | `_bloom.loyalty.points` | Also feeds the calculated `loyalty_band` |
| `join_date` | `_bloom.loyalty.joinDate` | |
| `city` | `homeAddress.city` | |
| `state` | `homeAddress.stateProvince` | |
| `country` | `homeAddress.countryCode` | |
| `email_consent` | the `_bloom` email consent field | Lapsed 90 needs email consent true |
| `sms_consent` | the `_bloom` SMS consent field | |
| `push_consent` | the `_bloom` push consent field | |

The calculated `loyalty_band` goes to a `_bloom` loyalty band field.

**Task 2: phone**
1. Strip every character that is not a digit.
2. If eleven digits remain and the first is `1`, drop that `1`.
3. Put `+1` in front.

All five shapes become `+14695550142`. Without step 2, `1-469-555-0142` and `+1-469-555-0142` both become `+114695550142`: a doubled country code that matches no other row.

**Task 3: email**
Lower-case every letter, and trim the spaces at both ends. Software compares text exactly, character by character, so a capital letter or a stray space makes a different value; an identity value that changes spelling between files can split one person in two.

**Task 4: loyalty band**

```
loyalty_band = iif(points >= 1500, "Gold", iif(points >= 500, "Silver", "Bronze"))
```

| Points | Band |
|---|---|
| 259 (Liam) | Bronze |
| 880 (Maya) | Silver |
| 4,120 (Noah) | Gold |
| 499 | Bronze |
| 500 | Silver |
| 1,499 | Silver |
| 1,500 | Gold |

**Task 5: the eight feeds**

| Feed | Road | Why |
|---|---|---|
| 18 months of orders | Batch | History and bulk |
| Live add-to-cart | Streaming | A journey reacts to it: the abandoned-cart reminder must know the moment it happens |
| Nightly CRM export | Batch | Bulk, on a schedule |
| App sign-in | Streaming | It links anonymous browsing to a known person the moment it happens |
| Product catalogue | Batch | Reference data that changes rarely |
| Page views | Streaming | Live behaviour, sent as it happens (through the Web SDK from episode 12) |
| One-time loyalty migration | Batch | Bulk, once |
| Purchase confirmation | Streaming | Journeys react to it: a first order qualifies a customer as new, and any purchase lets a shopper exit Cart Rescue |

**Task 6: one row**
Priya's row leaves the CSV (source), is mapped and cleaned (Data Prep), lands in the Bloom Customers dataset (data lake), and, because the dataset is enabled for Profile, folds into her live profile. The fifth ending is rejection: the row never reaches the dataset, and the dataflow records why. An order row with an empty timestamp is a good prediction, because every event needs one. A customer row with an empty `email` would have no identity, so it could never attach to a person.

**Task 7: practice question**
The thank-you email reacts within minutes, so the purchase feed goes by streaming. Last year's refunds are history, loaded once, so they go by batch. Map the identity columns first: on an order feed, `bloom_id` (primary, BloomID) and `email` (second identity, Email).

**Track B: what to expect**
The workflow is **Map CSV to XDM schema** (Dataflow detail, Select data, Mapping). The Profile dataset toggle appears only after you pick a Profile-enabled schema. Enable partial ingestion is off by default. The preview's row one is Priya Sharma, Gold, 2,340 points. In Bloom's run the Mapping screen showed a full green bar, **Mapped fields 14 of 14**, and the **New field type** menu offered **Add new field** and **Add calculated field**. Your screen may differ; what it shows is the fact.

**Check yourself**
1. Will something need to react to this within minutes? Yes means streaming; no means batch.
2. Source, Data Prep, dataset, profile; the fifth ending is rejected.
3. Mapping columns to XDM fields, and calculated fields that clean or derive values.
4. They decide which person a row belongs to. A row with no identity is an orphan that no profile, audience or journey will find.
5. Audiences can only use values that land in a field a rule can read. Lapsed 90 needs email consent true, so Ananya is excluded only if her consent lands correctly.
6. You get `+114695550142`, a doubled country code, so the value matches nothing else.
7. Every Gold customer also has 500 or more points, so asking the smaller question first makes every Gold customer Silver.
8. Profile dataset on (before loading), Error diagnostics on, Enable partial ingestion left at its default (off) for the trial.
9. A streaming endpoint, an address that accepts JSON events one at a time. Postman sends test events to it by hand before the app is ready.

</details>
