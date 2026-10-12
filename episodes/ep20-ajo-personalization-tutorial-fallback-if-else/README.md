# Episode 20: AJO Personalization Tutorial: Fallback, If-Else

**Watch:** Video coming soon on iTV

[Previous](../ep19-ajo-fragments-email-designer-one-brand-voice/) · [Next](../ep21-abandoned-cart-journey-in-ajo-step-by-step/)

## What you will learn

- Insert profile values into an Adobe Journey Optimizer (AJO) email and add **fallbacks**, so missing data still reads naturally
- Write an **if-else** personalisation condition with the right syntax (a single `=`) and exact, **case-sensitive field paths**
- Use **conditional content** and read the code it generates, so you can debug a variant that never shows
- Decide when to use a **content variant** and when to use a **journey branch**
- Recognise **when not to personalise**, and check that every line of copy agrees with its audience

## The story so far

Bloom is a direct-to-consumer wellness brand with 1.2 million customers, preparing the first live journey of its loyalty relaunch. In episode 19 the emails found one voice: a shared channel configuration, a written channel priority, and header and footer fragments whose One click Opt-out link cleared the opt-out warning on Bloom Welcome v1. But Rohan's test seat, whose first name is empty on purpose, still read `Hi ,`, and relaunch Monday is days away.

## Key ideas

### 1. Personalisation is a spectrum; build only on data you trust
At one end of the spectrum is a first name in a greeting. At the other is a ranked offer chosen for each person at send time (Bloom builds that in episode 22). Most of the commercial value sits in the middle: the right product category, the right tone, the right reason to come back.

The rule for the whole spectrum: **personalise at the level your data can support.** Before you personalise on a field, ask how often it is empty and how often it is wrong. A field that is forty percent empty is a machine for producing awkward emails.

### 2. Value tokens and fallbacks: write the fallback first
A **token** is a placeholder that asks the profile for a value at send time. It points at a field path on the customer's merged profile in Adobe Experience Platform (AEP). AJO's syntax mixes two styles:

| Goal | What you type | Result |
|---|---|---|
| Print a value (Handlebars style) | `{{profile.person.name.firstName}}` | `Priya`, or nothing at all when the field is empty |
| Value with a **fallback** (PQL) | `Hi {%= profile.person.name.firstName ?: "there" %},` | `Hi Priya,` or `Hi there,` |

A plain token prints nothing for an empty field, so the comma stays behind: `Hi ,`. A **fallback** is the default text used when the field is empty. The personalisation editor's ellipsis next to a field offers **Insert with fallback text**.

**Write the fallback first, then the personalised version.** It forces the message to work without the data. Choose words a person would say: "Dear Valued Member" is a different kind of broken.

### 3. If-else: a single equals sign and exact paths
A **conditional** (if-else) line shows different text to different customers inside one email. Kavya's line, in her own draft copy of the Bloom Gold Thank-You email:

```
{%#if profile._bloom.loyalty.tier = "Gold"%}As a Gold member, you get early access to every new launch.{%else%}Reach Gold to unlock early access to new launches.{%/if%}
```

- Profile Query Language (PQL) compares with a **single** `=`, not `==`.
- Field names are **case-sensitive**: `_bloom.Loyalty.tier` is a different (non-existent) field from `_bloom.loyalty.tier`.
- Custom fields live under the **tenant namespace** (`_bloom` at Bloom). Standard Adobe fields such as `person.name.firstName` do not. A wrong or missing tenant prefix is the most common reason a personalised email shows a blank.
- Compare against the value exactly as it is stored. Read it on a real test profile first.

### 4. Conditional content: the no-code way, and the code it writes
**Conditional content** builds the same logic without typing. Select a component in the Email Designer and click **Enable conditional content**. A **Conditional Content** panel appears with a **Default variant** and **Variant - 1**. Each added variant gets its own text and its own condition.

- Added variants are checked **in the order shown**.
- The **Default variant** is listed first, but it shows **only when no added variant matches**. It is the fallback for the whole block.
- **Save condition** adds the condition to a conditions library that the whole organisation shares, so name it clearly.

**Read the generated code.** Kavya's Variant - 1 had no saved condition, so the designer wrote `{%#if false %}`: it could never show. Her Default variant held the Gold perk, so every reader would have been promised it. When a variant never shows, the generated condition usually tells you why. Safer layout: the perk in a variant with a saved condition, the generic line in the Default.

### 5. Copy and audience must agree; subject lines need fallbacks too
With **Simulate content (AEP profiles)**, Kavya's Gold seat saw the perk and Farhan's Silver seat saw the nudge. But Farhan's version still said "You are one of our Gold members", and the subject read "Farhan, thank you for being Bloom Gold". Those static lines were true only because the real campaign goes to High-Value Loyalists, an all-Gold audience. In the "everyone else" version they were false.

- Every line must be true for every person who can receive the email. Move tier claims inside the matching side of the if-else.
- **Subject lines need fallbacks.** A subject starting with a name token and no fallback opens with a bare comma when the name is empty. Kavya's fix: `Hi {%= profile.person.name.firstName ?: "there" %}, a thank-you from Bloom`.

### 6. Variant or journey branch, and when not to personalise
- **Same message, different detail: content variant**, such as a tier-specific perk line. One message instead of five near-identical copies.
- **Different intent: journey branch** (an Optimize activity, episode 17) or a different journey, such as thanking a loyalist versus winning back a lapser, or a different wait or channel next.

**When not to personalise.** If the inference is weak, generic is safer. Customers forgive a generic email; they remember a confidently wrong one. "We do not have the data to do that responsibly yet" is a senior answer.

Interview line: *"Write the fallback first."*

## In the product

Labels as of October 2026.

1. **Open the email.** In your own draft campaign: the **Content** tab, then **Edit email body**, which opens the Email Designer.
2. **Add a fallback.** In the personalisation editor, open the ellipsis next to the field and choose **Insert with fallback text**. Or double-click the greeting line and type the fallback version shown above.
3. **Add an if-else line.** Add a **Text** component and type the `{%#if%} ... {%else%} ... {%/if%}` line with your own two sentences, then **Save**.
4. **Conditional content.** Select a component, click **Enable conditional content** in its toolbar, and work in the **Conditional Content** panel (**Default variant**, **Variant - 1**, **Add variant**). The condition icon next to a variant opens the builder (**Select condition**, then **Create new**), with **Attributes**, **Contextual** and **Audiences** tabs. **Save condition** writes to the organisation-wide library.
5. **Preview on test seats.** Click the arrow next to **Simulate content**, choose **Simulate content (AEP profiles)**, add your own test seats under **Manage test profiles**, and switch with **Test profile name**. Do not click **Send proof**: it sends real emails.

## Common mistakes

- Testing tokens only on complete profiles.
- Fallbacks in the body, none in the subject line.
- Typing `==` instead of a single `=`.
- Wrong case or a missing tenant prefix in a field path, so the token can render blank.
- A variant with no saved condition (`{%#if false %}`), and never reading the generated code.
- Static copy that is true for only part of the audience.
- Five cloned emails for a one-line difference, or two intents forced into one email.
- Personalising on a weak guess.

## Glossary

| Term | Meaning |
|---|---|
| Personalisation spectrum | The range from a first name in a greeting to a ranked offer chosen per person at send time |
| Token | A placeholder in a message that is filled from the profile (or event) at send time |
| Field path | The dotted address of a field on the profile, such as `person.name.firstName`; case-sensitive |
| Tenant namespace | Your company's own prefix for custom fields (`_bloom`); standard Adobe fields do not use it |
| Fallback | The default text used when personalisation data is missing |
| Insert with fallback text | The personalisation editor option that adds a fallback for you |
| Profile Query Language (PQL) | The rule language behind audience rules, also used for fallbacks and conditions in AJO |
| If-else (conditional) | A block that shows one text when a condition is true and another otherwise |
| Conditional content | The Email Designer's no-code way to build variants of a component |
| Default variant | The variant shown only when no added variant matches |
| Save condition | Adds a condition to the organisation-wide conditions library |
| Simulate content (AEP profiles) | Renders a message for stored test profiles, without sending |
| Content variant | An alternative block inside one message, chosen by a condition |
| Journey branch | A separate path in a journey, used when the intent differs |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

- Search Experience League for: Journey Optimizer personalization editor, personalization syntax, fallback values
- Search Experience League for: Journey Optimizer conditional content, simulate content, test profiles

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
