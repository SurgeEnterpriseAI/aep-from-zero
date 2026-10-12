# Episode 26: CJA Data Views and Derived Fields Explained

**Watch:** Video coming soon on iTV

[Previous](../ep25-customer-journey-analytics-tutorial-person-id/) · [Next](../ep27-analysis-workspace-tutorial-for-beginners-cja/)

## What you will learn

- Explain what a Customer Journey Analytics (CJA) **data view** does, and walk its four tabs: **Configure**, **Containers**, **Components**, **Settings**
- Turn schema fields into **metrics** and **dimensions**, and set **attribution**, **count values versus count instances** and **persistence**
- Explain the **person, session and event** containers and the **30-minute session timeout**
- Build five **derived fields**: marketing channel, average order value band, cleaned journey name, abandoned flag, loyalty band
- **Reconcile** data-view totals with the source dataset and explain every gap

## The story so far

Bloom, a direct-to-consumer wellness brand with 1.2 million customers, is two weeks into its relaunch, and Act III is about proving what worked. In episode 25 Rohan, the analyst, designed the connection **Bloom 360**: web, order and journey step events, the customer profile, and the 200-product catalogue as a lookup, with the email as the person ID on every dataset. But a connection only brings data in. Nobody has yet decided what any of it means.

## Key ideas

### 1. A data view is where a raw column becomes a trusted number
A connection decides which datasets come in and who counts as a person. A **data view** sits on top of it and decides what the data means: which fields become metrics and dimensions, what a session is, and which time zone a day uses. **If a metric is not defined in the data view, no analyst can use it.** One connection can carry several data views.

**Naming decides trust.** If one team says "orders" and another says "purchases" for different things, they argue for months. One name, one meaning, one description per metric.

### 2. Containers and the session timeout
**Containers** are the levels you count at: **person** (shown as People), **session** and **event**. "How many customers bought?" is a person question; "how many visits ended in an order?" a session question; "how many orders?" an event question. The **session timeout** (30 minutes in Bloom Marketing) starts a new session after that long with no activity: a last tap at 8:00 PM and a return at 8:45 PM make two sessions. A data view applies its rules at report time, so if you change the timeout later, past sessions are recounted under the new rule. Record every change and its date.

### 3. Metrics, dimensions, one field for many metrics
A **metric** is a number you count or add up (orders, revenue). A **dimension** is a label you split by (marketing channel, loyalty band). A schema field is usable in Workspace only once it is dragged into Metrics or Dimensions. **One field can back several metrics**: Adobe's Journey Optimizer metrics Email Opens, Outbound Clicks, Spam Complaint and Unsubscribes all read `interactionType`, each keeping its own rows through **Include/Exclude values**. Bloom Marketing's core metrics: orders, revenue, cart adds, journey entries, product views.

### 4. Component settings

| Setting | What it controls |
|---|---|
| Format | Decimal, Time, Percent or Currency |
| Attribution | Which touch gets the credit; Last Touch is the usual default (episode 29) |
| Behavior | **Count values** adds the number in the field; **Count instances** adds one per row |
| Include/Exclude values | Keep only matching rows |
| Persistence | Dimensions only: how long a value stays attached to later events |
| Metric deduplication | Count only the first occurrence per person or session |

Priya's order total of 54.00: Revenue with **count values** adds 54; Orders on the same field with **count instances** adds 1. A default set in the data view applies to every analyst.

### 5. Derived fields: report-time and retroactive
A **derived field** is built at report time from fields you already have. It can combine, correct or create values, and the change applies to all reporting, **past included**. A cleaning rule at ingestion (episode 5) shapes only rows that arrive after it; a derived field reads every row when the report runs, with no reload.

| Bloom derived field | Rule in plain words | Built with |
|---|---|---|
| Marketing channel | Read the UTM tag, lower-case it, name the channel; Otherwise set to No value (Adobe's guidance) | URL Parse, Lowercase, Case When |
| Average order value band | Band each order by its total (illustrative: under 40, 40 to under 80, 80 and above, US dollars) | A banding rule (check your screen's number comparisons) |
| Journey name, cleaned | Strip the version tag, so "Bloom Welcome v1" reads "Bloom Welcome"; keep the raw name as its own dimension | Find and Replace (or Regex Replace) |
| Abandoned flag | Cart activity never followed by an order; Priya is not flagged | Plain-words rule, tested on Priya |
| Loyalty band | Gold from 1,500 points, Silver from 500, Bronze below; Gold first (Priya's 2,340 points are also above 500); explicit Otherwise for missing points | Case When, strongest signal first |

Lowercase is what merges `email` and `Email` into one channel value. For channels, Adobe's guidance is to set the Otherwise to **No value**, so a later page view with no tag never overwrites the channel the customer arrived with (see persistence above).

### 6. A derived field belongs to the connection
Derived fields are managed at the connection level: a change made in any data view on Bloom 360 applies to every data view on it. Treat one like shared code: an owner, a description, a warning before any change.

### 7. Reconcile before you chart
Bloom Marketing shows 1,240 orders and $66,260 for the relaunch fortnight (the series' fictional figures). Before anyone builds a chart, compare with the source dataset and explain every gap: the window and time zone (AJO reports in UTC), late data (about 90 minutes, up to 4 hours with stitching), **Records skipped** on the connection (no timestamp, or a missing or invalid person ID), data-view segments or exclude rules, and finally the metric definition itself (count instances on the right field). At Bloom, the first check explained the gap: the source query had cut the fortnight at midnight in a different time zone.

Interview line: *"A data view is where a raw column becomes a number someone can trust, and a derived field fixes last year's data without reloading a row."*

## In the product

Labels as of October 2026. In a shared organisation, look only: do not save, create or edit anything.

1. **CJA**, **Data Management**, **Data views**. A connection's details page also has **Create data view**.
2. **Configure**: **Connection**, **Name**, **External ID**, and the **Calendar** (time zone, calendar type, first month, first day of the week).
3. **Containers**: **person** (shown as People), **session**, **event**.
4. **Components**: **Schema fields** on the left; **Included components**, split into **Metrics** and **Dimensions**, in the middle. Use **Search components**, click a component, and read **Component Settings** on the right.
5. **Settings**: data-view-wide **Segments**, and **Session settings** with **Session timeout** (for example 30 Minutes). Leave through the **Data views** breadcrumb; **Back** only returns to the previous tab.
6. **Components**, then **Create derived field** in the left rail. Drag functions, templates or fields into the rule builder (rules run in order); name it in the field settings; check **Final output**, a preview based on the last 30 days. A saved one appears under **Schema fields**, in **Derived fields**.
7. 18 functions, including **Case When**, **Lowercase**, **URL Parse**, **Find and Replace**, **Regex Replace**, **Trim**, **Lookup**. 19 templates, including **Marketing channels** and **UTM Parameters Parse**.
8. Case When: **If**, **Else If**, **Then set value to**, **Otherwise set value to**; operators such as **Equals any term**, **Contains the phrase**, **Is set**. URL Parse: **Get query string value** with **Query parameter**. Check what your screen offers for number comparisons.

Adobe's guidance: prefer URL Parse over Regex Replace for standard link parts; in Case When, strongest signal first and an explicit Otherwise, set to No value for channels so it does not overwrite earlier channels; Lowercase and Trim before a Lookup. Limits: up to 10 schema fields per derived field, at most 3 from lookup or profile datasets; 100 to 500 derived fields per connection, by package.

## Common mistakes

- Dragging every schema field in, so analysts pick the wrong component.
- Leaving **count instances** on a money field, so Revenue counts rows.
- Comparing reports with different time zones or session definitions and calling the gap a data error.
- Changing a data-view default to fix one report, which changes everyone's numbers.
- Ending a Case When without an explicit Otherwise, or giving a channel field an Otherwise label that overwrites the channel a customer arrived with (Adobe's guidance: No value).
- Putting Silver before Gold in a points band, so a 2,340-point Gold customer lands in Silver.
- Editing a derived field "just for my data view": it belongs to the connection.
- Presenting a total you have not reconciled against the source.

## Glossary

| Term | Meaning |
|---|---|
| Data view | The CJA layer that turns raw fields into named metrics and dimensions |
| Container | A counting level: person, session or event |
| Session timeout | Minutes of inactivity after which a new session starts |
| Metric | A number you count or add up |
| Dimension | A label you split a metric by |
| Count values | Adds the number stored in the field |
| Count instances | Adds one per row |
| Persistence | How long a dimension value stays attached to later events |
| Derived field | A field built at report time; applies to past data too |
| Final output | The derived-field preview, on the last 30 days |
| Reconciliation | Comparing a report total with its source and explaining every gap |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

Search Experience League for: Customer Journey Analytics data views, component settings, count values count instances, persistence, session settings, derived fields, Case When, URL Parse, Marketing channels function template.

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
