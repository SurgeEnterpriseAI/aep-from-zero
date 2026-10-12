# Episode 30: Fallout, Flow and Cohort Analysis in CJA

**Watch:** Video coming soon on iTV

[Previous](../ep29-marketing-attribution-models-explained-cja/) · [Next](../ep31-publish-cja-audiences-to-aep-close-the-loop/)

## What you will learn

- Build a **fallout** in Customer Journey Analytics (CJA), choose **Eventual path** or **Next event** and the **container**, and avoid **Invalid container within segment**
- Break a fallout step down to find **where a leak concentrates**
- Use **segment comparison** and name a **confounder** before you claim a cause
- Read a **flow** (it counts **path views**, not people) and a **cohort table** (rows, columns and the diagonal)
- Report a **holdout** result honestly, including when it is still soft

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers. It is week five, two weeks into the loyalty relaunch. In episode 29, Rohan Desai, Bloom's analyst, refereed the revenue fight, and Anjali Mehta, the Chief Marketing Officer, got ranges with a named model and window instead of one triumphant number. Now Anjali asks three questions about people: where do customers drop out between the journey and the purchase, did Cart Rescue v1 really recover anyone, and do first-time buyers come back?

## Key ideas

### 1. Fallout counts people
A **fallout** shows how many people continue, and how many drop out, at each step of a sequence you define. The first bar is **All People**; each step after it is a **touchpoint**. Touchpoints can be dimensions, dimension items, metrics or segments. Adobe says fallout suits journeys with a **predefined sequence** and a single entry point.

Bloom's fallout over the relaunch fortnight (people):

| Step | People | Continued from the step before |
|---|---|---|
| Journey entry | 2,000 | |
| Email click | 620 | 31% |
| Site visit | 540 | 87% |
| Add to cart | 300 | 56% |
| Purchase | 132 | 44% |

**Big absolute drop-offs are often normal.** Entry to click loses 1,380 people, which is the normal shape of email. The interesting step is **add to cart to purchase**: 168 of 300 people with products already in a cart did not buy.

### 2. The settings that change the answer
| Setting | Options | Meaning |
|---|---|---|
| Path per touchpoint | **Eventual path** (default) | The step counts if it happens any time later |
| | **Next event** | The step counts only if it is the very next event |
| Container | **Person** (default) | Steps may spread across visits and days |
| | **Session** | Every step must happen inside one visit (Bloom Marketing ends a visit after 30 minutes) |

Person is where identity stitching pays off: Priya added her serum on her phone and paid on her laptop eight minutes later, and because Bloom 360 stitched her phone rows to her email, a fallout sees one buyer, not a false abandon.

**The container rule.** A segment used as a touchpoint must use a container at a **lower level** than the fallout's own. Otherwise CJA shows **Invalid container within segment**. Kavya's "Email click" segment was a Person segment inside a Person fallout. The fix was the **dimension item** with the same name.

### 3. Breaking down a touchpoint
Right-click a touchpoint and choose **Breakdown fallout at this touchpoint** to split the people who dropped by any dimension. Broken down by device and by the loyalty band derived field, Bloom's leak concentrates at **checkout, on mobile, among non-Gold customers**. The overall average hid it. Compare each group's drop **rate**, not its raw count: a group with more shoppers always has more drop-outs.

### 4. Segment comparison, confounders and the honest sentence
- **Segment comparison** means analysing two groups side by side, with everything else held constant, to isolate a difference.
- **A comparison across different time windows is not a comparison.** Rohan compared mobile non-Gold shoppers with everyone else in the same fortnight, with the same steps and settings.
- A **confounder** is a third factor that explains an apparent relationship. Perhaps mobile shoppers are newer customers with smaller carts, and the device is not the cause.
- **Correlation is not causation.** The honest sentence: "X is associated with Y; to test whether it causes it, we would need to do Z."

Bloom's version: "Mobile non-Gold shoppers are associated with a much higher drop at checkout. To test whether the device causes it, we would compare new customers with similar carts on mobile and on desktop."

### 5. A flow counts path views, not people
A **flow** shows the paths people take before and after a point you choose, as columns of **nodes**. Each node counts **path views**. One shopper who walks the same path in two visits can count twice in a flow but once in a fallout. Settings to check: **Include repeat instances** (off by default) and **Flow container** (Person or Session).

| | Fallout | Flow |
|---|---|---|
| Question | Who continues, who drops? | Where do people go next? |
| Path | Steps you define | Paths people actually took |
| Counts | People | Path views |
| Best for | A predefined sequence | Exploring around one point |

For non-linear journeys with many entry points, Adobe points to **Journey canvas**.

### 6. Cohort tables and the diagonal
A **cohort table** groups people by a start week and tracks one behaviour over the weeks that follow.
- **Across a row:** one cohort as it ages.
- **Down a column:** cohorts compared at the same age. The first column is each cohort's day-seven repeat rate.
- **Along a diagonal:** one calendar week across every cohort. A whole diagonal that is high or low points to something that happened that week (a sale, a big send, an outage), not a better or worse cohort.

If a table puts calendar weeks in the columns instead, the roles swap: each cohort's first week runs along the diagonal.

In the episode, illustrative numbers (not Bloom results) show day-seven repeat rising from 6 to 10 percent in relaunch week, but the older cohort, which bought before Bloom Welcome v1 went live, also rose that week, so Welcome v1 cannot take the whole jump.

### 7. Reading a holdout honestly
Cart Rescue v1 has held back a random 10% since day one. Over the relaunch fortnight, recovery was **11.8%** for people who got the journey and **7.9%** for the holdout: about 4 more recoveries per 100 abandoners. Rohan calls it **soft, because it is only two weeks of data**, and reports the delta with its window and caveat. Use ranges and deltas, never a single triumphant number.

Interview line: *"A drop-off is a question, not a conclusion."*

## In the product

Labels as of October 2026.

1. **Fallout:** in an Analysis Workspace panel, click the **+** inside the panel and choose **Fallout**. The first bar is **All People**. Drag components onto **Add touchpoint**. For a dimension item, click the **>** beside the dimension in the left panel to open its items, then drag the item.
2. On each touchpoint, choose **Eventual path** or **Next event**. Set the container to **Person** or **Session**.
3. If you see **Invalid container within segment**, the segment's container is equal to or higher than the fallout's. Use the dimension item, or a segment built on a lower container.
4. **Compare segments:** drag segments from the left panel onto the drop zone at the top of the fallout. Adobe says you can compare an unlimited number.
5. **Touchpoint menu** (right-click): Trend touchpoint, Trend touchpoint (%), Trend all touchpoints (%), Breakdown fallthrough at this touchpoint, **Breakdown fallout at this touchpoint**, Create segment from touchpoint, Create audience from selection. (Adobe's documentation spells it "Break down". Create audience from selection is episode 31: never click it in a shared organisation.)
6. **Flow:** **+**, then **Flow**. Fill **Starts with**, **Contains** or **Ends with**. **Show advanced settings** offers Wrap labels, **Include repeat instances**, Limit to first/last occurrence, **Number of columns** (up to 5), **Items expanded per column** (up to 10) and **Flow container**. Then **Build**. Hover a node to see its path views, **Entries** and **Exits**.
7. **Cohort table** is in the same **+** list of visualisations.
8. Save a new project manually the first time. A new panel opens on "This month", so check the date range.

## Common mistakes

- Calling the biggest absolute drop the problem, when it is the normal shape of email.
- Quoting a fallout number without its path setting and container.
- Using a Person segment as a touchpoint in a Person fallout, and getting **Invalid container within segment**.
- Comparing two groups across different date ranges.
- Announcing a cause without naming a confounder and a test.
- Pasting a flow node's number into a report as "customers".
- Crediting a journey with a cohort column without reading the diagonal.
- Reporting a soft holdout result as a victory.

## Glossary

| Term | Meaning |
|---|---|
| Fallout | A chart showing how many people continue or drop at each step of a sequence |
| Touchpoint | One step in a fallout: a dimension, dimension item, metric or segment |
| Eventual path | Fallout setting: a step counts if it happens any time later (default) |
| Next event | Fallout setting: a step counts only if it is the very next event |
| Container | The level a report counts at: person, session or event |
| Invalid container within segment | The error when a touchpoint segment's container is not lower than the fallout's |
| Segment comparison | Analysing two groups side by side, everything else held constant |
| Confounder | A third factor that explains an apparent relationship between two things |
| Flow | A chart of the paths before and after a point; it counts path views |
| Path view | One pass along a path; one person can produce several |
| Journey canvas | A visualisation for non-linear journeys with many entry points |
| Cohort table | People grouped by a start week, tracked over the following weeks |
| Diagonal | The cells of a cohort table that fall in the same calendar week |
| Holdout | A random group deliberately sent nothing, to measure what happens anyway |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Customer Journey Analytics fallout visualization, flow visualization, cohort table, Journey canvas

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
