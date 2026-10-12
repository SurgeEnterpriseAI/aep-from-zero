# Episode 32: Adobe Analytics vs Customer Journey Analytics

**Watch:** Video coming soon on iTV

Part 3: Prove what worked (Customer Journey Analytics) · [Previous](../ep31-publish-cja-audiences-to-aep-close-the-loop/) · [Next](../ep33-adobe-ai-assistant-data-insights-agent-in-cja/)

## What you will learn

- Map **Adobe Analytics** concepts to **Customer Journey Analytics (CJA)**: containers, report suites, eVars and props, classifications, customer attributes
- Explain how **processing rules** and **VISTA rules** become **Data Prep** and **derived fields**
- List what a migration must **rebuild** (segments, calculated metrics) and what **does not come across** (Activity Map, Contribution analysis, hourly alerts)
- Name the features **only CJA has**, and the Bloom question each would answer
- Answer "Adobe Analytics versus CJA" in an interview in under a minute

## The story so far

Bloom, a direct-to-consumer wellness brand with 1.2 million customers, is five weeks into its Adobe programme. In episode 31 Rohan, the analyst, published the CJA audience **Checkout Leakers - Mobile** to Adobe Experience Platform (AEP), Divya's **Checkout Rescue** journey picked it up through Read audience, and Anjali's exec dashboard now lands on her phone every Monday at 8:00 AM. At the board update, a board member asks Anjali, the CMO, why Bloom did not simply buy Adobe Analytics, the tool she used for years at her last company. The agency asks the same. Rohan writes a one-page memo.

## Key ideas

### 1. Two different products
**Adobe Analytics** is a different, older Adobe product. Its reports are built mainly around website data collected into a **report suite**. **Customer Journey Analytics** is a separate application that reads datasets from AEP's data lake through a **connection**. Never call CJA "Adobe Analytics". Many companies run Adobe Analytics today and are moving to CJA, so "what changes?" is a common interview question.

### 2. Containers are renamed
| Adobe Analytics | CJA | Bloom example |
|---|---|---|
| Hit | Event | Priya's order row at 7:52 PM, purchase ID BLM-88412 |
| Visit | Session | One stretch of activity; ends after 30 minutes of quiet in the data view Bloom Marketing |
| Visitor | Person | Everything Priya did on phone and laptop, stitched to her email in Bloom 360 |
| Entries and Exits | Session Starts and Session Ends | Session length is set in each data view's Session settings |

In CJA a person is whoever the connection's **person ID** says (at Bloom, the email). So an old visitor count and a new person count need not match.

### 3. Report suites become data views; eVars and props no longer exist
Adobe says **data views** are the CJA equivalent of report suites, and they expand the idea of virtual report suites with more controls. Adobe Analytics allows up to 250 **eVars** and 75 **props**. In CJA, eVars, props and events "in the Adobe Analytics sense" no longer exist: **any schema field** can become a dimension or metric, with no fixed number of dimensions and no unique-value limit.

### 4. Attribution moves to report time
Settings such as **attribution and expiration**, once applied when data was collected, are now applied **at report time** in the data view. Changes are **retroactive**, and several data views can hold several versions. The flip side: change the default attribution on a metric in the data view, and everyone's past numbers change. Write down the model and window behind every number.

### 5. Classifications and customer attributes become datasets
| Adobe Analytics | CJA | In Bloom 360 |
|---|---|---|
| Classifications | **Lookup dataset**: reference data joined by a **Key** and a **Matching key**; no person ID needed | The 200-product catalogue, joined on the SKU |
| Customer attributes | **Profile dataset**: attributes of a person, applied to that person's events; needs a person ID | The customer profile, so Gold can be compared with Silver |

The connection Journey Optimizer creates for its own reports holds no customer profile data, so it cannot split Gold from Silver.

### 6. Processing and VISTA rules become Data Prep and derived fields
Processing rules, **VISTA rules** (server-side rules Adobe runs for a client) and marketing channel processing rules are supported in two ways: **Experience Platform Data Prep** and **CJA derived fields**.

| Layer | When it works | Use it when |
|---|---|---|
| Data Prep | At the door, as rows land; older rows change only if you load them again | Journeys and profiles need the clean value too (Bloom's phone and email clean-up) |
| Derived field | At report time; retroactive, past data included | Only reports need it, or the past must change too (Bloom's marketing channel) |

### 7. What must be rebuilt, and what does not come across
- **Segments and calculated metrics**: Adobe says none of the existing ones are compatible with CJA. Rebuild every one on schema fields. (CJA renamed filters to segments in April 2025 to match Adobe Analytics; search filters are still called filters.)
- **Activity Map** and **Contribution analysis**: Adobe marks both "No support, not yet planned".
- **Hourly alerts**: not available. Alerts run daily, weekly or monthly, because of the timing of data collection (data reaches CJA within about 90 minutes of landing in AEP, up to 4 hours with stitching).
- **Project sharing**: only between CJA users, not with Analysis Workspace in Adobe Analytics.

### 8. What only CJA has
Adobe lists many CJA-only features, including derived fields, stitching and cross-device analytics. Four more, with the Bloom question each would answer:

| Feature | Bloom question |
|---|---|
| Journey canvas (in the Workspace visualization list; suits non-linear journeys, while Fallout suits a fixed sequence) | How do new customers really move between email, app and site before a second order? |
| Experimentation analysis (lift and confidence of any experiment from any data source in a connection) | Did Cart Rescue beat its holdout (11.8% against 7.9%, still soft after two weeks)? |
| Forecasting | What might next fortnight's revenue look like if nothing changes? |
| SQL access and the BI (business intelligence) Extension | Can the finance team report the same revenue definition in its own BI tool? |

Bloom has not used these four yet. Adobe documents them this way; check what your screen shows.

### 9. The checklist for teams coming from Adobe Analytics
1. Inventory report suites, segments, calculated metrics and alerts, and who uses each.
2. Translate every term with the table above.
3. Choose the person ID first (case sensitive, must match across datasets), then decide on stitching.
4. Rebuild segments and calculated metrics, each written in plain words first.
5. Reconcile old and new numbers over the same window; explain each gap.
6. Move hourly alerts to daily; list anyone who depends on Activity Map or Contribution analysis.
7. Never click **Use in CJA** to experiment: every row is billed, and it is the organisation owner's decision.

**Interview line:** *"CJA is person-based, dataset-based and retroactive."* Then one example each: a customer's phone visit and laptop order become one person; the Journey Optimizer datasets sit in the same connection as orders and profile; a Lowercase derived field merged "email" (150 orders) and "Email" (30) into 180, for past data too. Finish with what must be rebuilt.

## In the product

Labels as of October 2026. Look only: do not save, create or edit anything.

1. **CJA**, **Data Management**, **Data views**: open a data view. The **Components** tab is where schema fields become metrics and dimensions (no eVars or props). Click a component to read its **Component settings**: **Attribution** on a metric, and **Persistence** on a dimension (how long a value stays attached to later events). That is where an eVar's old attribution and expiration ideas now live. The **Settings** tab holds **Session settings**.
2. **Data Management**, **Connections**: open a connection and read each dataset's type (event, profile, lookup, summary). A lookup shows a **Key** and a **Matching key**.
3. **Workspace**: the **+** inside a panel lists visualizations, including **Fallout**, **Flow**, **Journey canvas** and **Experimentation**.
4. **Components**: segments live here (renamed from filters in April 2025).

## Common mistakes

- Calling CJA "Adobe Analytics", or treating it as a new version that copies everything across.
- Mapping an eVar to a derived field. An eVar maps to an ordinary schema field.
- Expecting the old visitor count to match the new person count, and calling every gap a bug.
- Promising that segments and calculated metrics will carry across as they are. They must be rebuilt.
- Copying every processing rule one for one without deciding: Data Prep at the door, or a derived field at report time?
- Leaving Activity Map, Contribution analysis and hourly alerts out of the memo.
- Listing CJA-only features without the business question each answers.

## Glossary

| Term | Meaning |
|---|---|
| Adobe Analytics | Adobe's older analytics product, built around web data in report suites |
| Report suite | Where Adobe Analytics collects and reports data; data views are the CJA equivalent |
| eVar and prop | Numbered custom variables in Adobe Analytics (up to 250 and 75); they do not exist in CJA |
| Hit, visit, visitor | Adobe Analytics containers; in CJA they are event, session, person |
| Session Starts, Session Ends | The CJA names for Entries and Exits |
| Classification | Adobe Analytics names and categories for a code; in CJA, a lookup dataset |
| Customer attributes | Adobe Analytics facts about known customers; in CJA, a profile dataset |
| Processing rules, VISTA rules | Adobe Analytics rules that reshape data; in CJA, Data Prep and derived fields |
| Lookup dataset | Reference data joined to events by a Key and a Matching key |
| Profile dataset | Attributes of a person, applied to that person's events |
| Retroactive | A change that applies to past data as well as new data |
| Journey canvas | A CJA visualization for non-linear journeys |
| Experimentation analysis | CJA's read of lift and confidence for an experiment from any data source in a connection |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

Search Experience League for: Customer Journey Analytics for Adobe Analytics users, Customer Journey Analytics feature support, Customer Journey Analytics FAQ, data views, lookup datasets, derived fields, alerts.

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
