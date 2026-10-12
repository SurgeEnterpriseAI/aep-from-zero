# Bloom relaunch campaign FAQ (sample)

An internal FAQ for Bloom's marketing team during the loyalty relaunch. Bloom is a fictional brand, and this file is practice material for the AEP From Zero course (episode 34). Product prices are in the product catalogue (`bloom-product-catalogue.csv`), not in this FAQ.

## What are the loyalty bands?

Bloom groups loyalty members by their points. Bronze is below 500 points, Silver is 500 to 1,499 points, and Gold is 1,500 points and above. A member's band follows their points balance.

## Which offer do lapsed customers get?

The 20% Comeback offer. It is for the Lapsed 90 audience only: customers whose last order was more than 90 days ago and who agreed to receive Bloom emails (email consent true).

## Which offer is for Gold members?

The Early Access Drop. Only Gold members are eligible for it.

## What if a customer qualifies for both offers?

The 20% Comeback ranks above the Early Access Drop. A Gold member who is also in Lapsed 90 is shown the 20% Comeback.

## What happens if no other offer applies?

Free Shipping is the fallback offer. It is shown only when no other offer qualifies.

## Can an offer go out before it is approved?

No. Every offer stays in Draft until Anjali, the Chief Marketing Officer, signs it off and Divya approves it. Only approved offers are shown to customers.

## How many marketing emails can one customer receive?

At most 2 marketing emails per customer per week. The rule covers every campaign and every journey.

## When does a new customer hear from Bloom?

Bloom Welcome v1 sends a welcome email when a customer's first-ever order puts them in the New This Month audience. There is a Gold version and a version for everyone else.

## What happens when a shopper leaves items in the cart?

Cart Rescue v1 waits 4 hours and then sends one email that shows the items left in the cart. A shopper who buys in the meantime leaves the journey and gets no email. Nobody gets more than one rescue email in any 7 days. A random 10% of qualifying shoppers are a holdout and get no email, so Bloom can measure what the email really adds.

## Does email consent matter for the offers?

Yes. Lapsed 90 requires email consent true, so a customer who never gave email consent is never in it and never receives the 20% Comeback. High-Value Loyalists carries the same consent condition.

## How does a customer stop marketing emails?

Every marketing email carries the Bloom footer, with Bloom's legal block and a one-click Unsubscribe link.

## Where may test sends and proofs go?

Only to your own inbox. Test profiles use IDs that start with `TD-` and `@example.com` addresses. Never type a customer's address into a test send.
