# Exercise 21: Recover the cart, let the buyer go

You will design Bloom's Cart Rescue v1 on paper, render two carts from event payloads with fallbacks, walk Priya through the journey to the exact minute she leaves, and answer a revenue claim with a holdout.

## Track A: No Adobe access needed

1. **Draw Cart Rescue v1.** On one sheet, draw the journey from left to right: entry, holdout, wait, pre-send check, email, End. Then add two notes beside it: the exit criteria and the re-entry rule. Label each box with Bloom's setting and one sentence on why.

2. **Render two carts.** Open `data/sample-web-event.json` in the repo. It is Priya's 7:44 PM add to cart. Its item under `productListItems` carries a product code (SKU), a name, a price and a quantity, but no image. A cart email also needs an image for each item, so the two payloads below are built from Priya's two SKUs and add one. Names, prices and image paths come from `data/bloom-product-catalogue.csv` (the images themselves are not in the repo). The field name `imageUrl` is illustrative; your organisation's abandon event will have its own.

   **Cart A** (Kavya's test seat, TD-KAVYA-01, Gold):
   ```json
   {
     "productListItems": [
       { "SKU": "BLM-SER-VITC-30",  "name": "Vitamin C Serum 30 ml",        "priceTotal": 34.00, "imageUrl": "images/BLM-SER-VITC-30.jpg" },
       { "SKU": "BLM-MOIST-HYA-50", "name": "Hyaluronic Moisturiser 50 ml", "priceTotal": 20.00, "imageUrl": "images/BLM-MOIST-HYA-50.jpg" }
     ]
   }
   ```
   **Cart B** (Rohan's test seat, TD-ROHAN-04, Silver, first name empty):
   ```json
   {
     "productListItems": [
       { "SKU": "BLM-SER-VITC-30", "name": "Vitamin C Serum 30 ml", "priceTotal": 34.00 }
     ]
   }
   ```
   In plain words or pseudo-code (not exact product syntax), write:
   - the item block that prints one row per item: image, name, price
   - what Cart B's row shows, since it has no image
   - the fallback line if the item list is missing completely
   - the greeting and the subject line each seat receives

3. **Walk Priya through the journey.** On 18 August she adds a Vitamin C Serum on her phone at 7:44 PM (the event carries only her ECID), signs in on the app moments later, and buys on her laptop at 7:52 PM (order BLM-88412, 54.00). Say exactly where she leaves Cart Rescue v1, what would have happened at 11:44 PM without an exit, and why identity stitching matters for the exit to work.

4. **"It drove 400,000 in revenue."** A client says their cart journey "drove 400,000 in revenue". Write the two questions you would ask, and explain in three or four sentences how a holdout answers them.

5. **The episode's practice question.** A shopper adds to cart at 9 PM and buys at 10:30 PM. With a four-hour wait, where does she leave, and does any email go?

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, and put **your own initials** on everything you create.
- Build a **Draft only**. Never click **Publish**.
- Do not switch on **Test mode** or **Simulation**, and do not use **Send proof**: all three send real email.
- Never configure events or data sources yourself; those belong to the admin.
- In anything shared: look, screenshot, leave.

Steps:
1. In Journey Optimizer, open **Journeys** and click **Create Journey**. In **Journey properties**, name it `<your initials> - Cart Rescue practice`, add a one-line description, and click **Save**. Confirm the status reads **Draft** and read the alert.
2. Click the **+** after Start and read the **Events** group. If an admin has already set up an event for practice, add it as the entry. If not, write down what the list shows and continue without an entry.
3. Add a **Wait** from **Orchestration**: a Duration of four hours.
4. Add one **Action** activity and choose **Email** inside it. Leave the content empty or as a placeholder.
5. Open **Journey properties** again. Read **Allow reentrance** and the **Reentrance wait period**, then set the wait period to 7 days on your own draft.
6. Look for where exit criteria live on your screen. If an event is available, add one for a purchase. If not, note what your screen shows.
7. Read **Alerts**, take a screenshot, and leave the journey as a Draft.

## Check yourself

1. Why must a cart-abandonment trigger be streaming or event based?
2. Where does a customer's cart live in Adobe Experience Platform?
3. How do you choose the wait window, and what is the usual first-touch range?
4. Why do the cart items come from the event payload, not from profile attributes?
5. What should the email show if an image is missing, and if the whole item list is missing?
6. Name the two locks that stop a buyer from receiving a rescue email.
7. Why can Simulation not prove the exit, and what can?
8. What does the Reentrance wait period default to, and what does Cart Rescue v1 use?
9. What is the difference between attributed and incremental revenue?
10. Why set the holdout on day one?

<details><summary>Check your answers</summary>

**Task 1: Cart Rescue v1**

| Part | Bloom's setting | Why |
|---|---|---|
| Entry | The abandon event (an event entry) | The moment matters; a daily batch audience arrives after the intent has cooled |
| Holdout | Optimize, Percentage split: 90 percent on the top path, 10 percent straight to End | The only way to measure what the journey truly causes; the sending path stays on top because Test mode takes the top branch |
| Wait | Duration, four hours | Chosen from Bloom's own gap between add to cart and purchase, after the natural return window |
| Pre-send check | Optimize, Data source condition on the current profile | Catches a purchase that reached the profile some other way |
| Email | One Action activity, Email: cart rows from the payload, fallbacks, dynamic subject | Shows what she actually left behind |
| Exit criteria | Any purchase event | Buyers leave wherever they are in the journey |
| Re-entry | Allow reentrance on, Reentrance wait period 7 days | At most one rescue in any seven days |

**Task 2: two carts** (pseudo-code, not product syntax)
```
for each item in the event's productListItems:
    if the item has an image: show the image
    show the item name
    show the item price
if the item list is missing or empty:
    show "You left something lovely in your cart."
```
- Cart A: two rows, each with image, name and price (34.00 and 20.00).
- Cart B: one row with the name and 34.00, and no empty image frame.
- Kavya's seat: "Hi Kavya", and the early-access subject, because her loyalty band is Gold.
- Rohan's seat: "Hi there" (the first-name fallback), and the gentle-urgency subject, because his band is Silver.

**Task 3: Priya**
She enters at 7:44 PM on the abandon event and her four-hour wait starts. The exit criteria remove her at 7:52 PM, when the purchase event arrives, eight minutes in, so no email is ever sent. Without the exit, at 11:44 PM Bloom would have asked her to finish an order she had already finished. The add to cart carried only her ECID and the order carried her email and BloomID; the sign-in (the linking event) stitched them into one person. Without stitching, the laptop order would belong to "someone else" and the phone's cart would look abandoned.

**Task 4: the 400,000 claim**
- Question 1: How much of that would have come in anyway? What happened to a comparable group that got no message?
- Question 2: What does "drove" mean here: which rule and which time window gave the journey credit for a purchase?

A holdout answers both. A random share of qualifying people is deliberately sent nothing. Compare the purchase rate of the emailed group with the holdout's: the difference, applied to the emailed group, is the incremental revenue. Attributed revenue also counts shoppers like Priya, who were coming back anyway, whenever they happen to buy just after the email.

**Task 5: practice question**
She enters at 9 PM and her wait would end at 1 AM. She buys at 10:30 PM, inside the wait, so the exit criteria remove her then and no email goes. Even without an exit, a 1 AM send is exactly the kind of message quiet hours (episode 23) hold back. If she happened to fall in the 10 percent holdout, she went straight to End and no email goes either.

**Check yourself**
1. A rescue only works while the intent is warm. A batch audience is evaluated once every 24 hours, so it notices the cart hours late.
2. Nowhere. There is no cart object; a cart is add-to-cart events not followed by a purchase.
3. From the client's own data: the actual gap between add to cart and purchase. Most retailers land between one and four hours for the first touch, with a second touch around 24 hours.
4. The payload holds what was in the cart at that moment. Profile attributes describe who the customer is and hold no cart.
5. Missing image: the name and price, with no broken box. Missing item list: a line that works alone, such as "You left something lovely in your cart".
6. Exit criteria on any purchase event, and a pre-send check that reads the current profile just before the email.
7. Simulation does not support exit criteria. Test mode runs the journey on stored test profiles (real email to their own inboxes, waits shortened to 10 seconds), so it can show the purchaser leaving.
8. It defaults to 5 minutes. Cart Rescue v1 uses 7 days.
9. Attributed revenue counts everyone who bought after the message, whether or not it caused the purchase. Incremental revenue is only what the message caused, measured against a holdout.
10. Because adding one after a client has seen a big attributed number is a very difficult conversation, and you cannot measure the past without one.

</details>
