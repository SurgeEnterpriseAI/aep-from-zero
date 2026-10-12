# Exercise 18: Test without emailing a stranger

You will sort Journey Optimizer's testing options by who they can reach, design Bloom's four test seats, write the rules for loading them, and work out why one test mode can never prove a split.

## Track A: No Adobe access needed

1. **Fill the testing table.** Copy this table and fill every cell.

   | Option | Can it reach a real inbox? | Which profiles or addresses does it use? | What is it best for? |
   |---|---|---|---|
   | Alerts panel | | | |
   | Dry run | | | |
   | Test mode | | | |
   | Simulation | | | |
   | Send proof | | | |

2. **Design four test profiles for Bloom.** For each one write a `TD-` ID, a first name, an `@example.com` address, a loyalty state, and one sentence on what it proves. One of the four must be deliberately incomplete.
3. **Write the four rules for loading test data**, with the reason for each rule in one line.
4. **Count the emails.** A tester opens Send proof with 5 test profiles selected and types one colleague's address, and nobody else's. How many emails go out, who receives them, and which rule was broken? Then do the same sum for 3 typed addresses and 5 test profiles.
5. **Prove the split.** Bloom Welcome v1 splits on Gold Members membership, with an Others path below it. Explain in two or three sentences why the Test mode run did not prove the Others path, and which option can.
6. **Spot the risk.** Simulation skips five protections that a normal send applies. Name all five, and write the one habit that keeps a Simulation run safe.

## Track B: If you have a development sandbox (optional)

Safety first:
- Use a **development** sandbox only, never production, and only objects that carry **your own initials**.
- Put **only your own email address** on any test profile, simulated user or proof.
- Never click **Activate** or **Publish**, never toggle the **Allowed list**, and never open someone else's journey or email.
- Never enable Profile on a schema that is not yours. If you are unsure which schema or dataset to use, ask your administrator first.
- In a shared sandbox: look, screenshot, leave. Skip steps 1 and 4 there.

Steps:
1. Create one test profile that carries only your own inbox: an ID starting `TD-` plus your initials, `testProfile` set to true, loaded into **your own** dataset with its **Profile** toggle switched on **before** you upload. Never reuse an existing customer's ID.
2. Open **Administration**, **Channels**, **Email settings**, **Allowed list**, and read whether the toggle says Deactivated. Change nothing.
3. Open the email in your own draft journey or campaign. Click **Simulate content**, choose **Simulate content (AEP profiles)**, add your test profile under **Manage test profiles**, and read the preview. Look at every personalised field: what would it print if the field were empty?
4. Optional: click **Send proof** with **only your own address**, and only if your administrator allows it. Check your inbox and spam folder. Do not run Test mode, Simulation or Dry run unless your administrator has said so.

## Check yourself

1. Which three options can reach a real inbox, and which two never do?
2. What does the `testProfile` field do?
3. Why must the Profile toggle be on before you upload a test seat?
4. What happens if a test row reuses a real customer's ID?
5. What does Test mode do to a two-day wait?
6. Why did Rohan's Silver seat get the Gold welcome?
7. What does Dry run cost, even though it contacts nobody?
8. Why might a simulated user fall to the Others path?
9. Why can a capped test profile receive no proof at all?
10. What does a deliberately incomplete test profile catch?

<details><summary>Check your answers</summary>

**Task 1: the testing table**

| Option | Can it reach a real inbox? | Which profiles or addresses does it use? | What is it best for? |
|---|---|---|---|
| Alerts panel | Never | None; it checks the journey | Finding errors before anything runs |
| Dry run | Never | Real profiles, counted only; no email, no profile change | Proving how many real people take each path |
| Test mode | Yes | Stored test profiles (`testProfile` true), up to 100; mail goes to the address stored on each | The email and the top path, end to end, with waits cut to 10 seconds |
| Simulation | Yes | Simulated users you create, with the address you type | Quick trials with no stored profile; a real send with protections off |
| Send proof | Yes | Up to 10 typed addresses, multiplied by test profiles | Checking one email's content |

**Task 2: four test profiles (model answer)**

| ID | First name | Address | State | Proves |
|---|---|---|---|---|
| TD-KAVYA-01 | Kavya | kavya.test@example.com | Gold | Gold content |
| TD-FARHAN-02 | Farhan | farhan.test@example.com | Silver, recent buyer | What everyone else sees |
| TD-DIVYA-03 | Divya | divya.test@example.com | Lapsed: last order more than 90 days ago, email consent true | The win-back path |
| TD-ROHAN-04 | (empty on purpose) | rohan.test@example.com | Silver | That test profiles lie: an empty name prints `Hi ,` |

Every row has `testProfile` set to true. In real practice each address is the seat owner's own inbox.

**Task 3: the four rules**
1. IDs start with `TD-`: test rows are easy to find and remove.
2. Load only into your own dataset: shared datasets belong to everyone.
3. Switch the dataset's Profile toggle on before uploading: data loaded while it is off never reaches the profile store.
4. Never reuse an existing customer's ID: a batch replaces that customer's whole row.

Also accept: carry only your own inbox, and leave the Update profile activity alone while practising.

**Task 4: counting proofs**
One typed address multiplied by 5 test profiles is **5 emails**, all to the colleague. The broken rule: type only your own address. With 3 typed addresses and 5 test profiles, 15 emails go out. Frequency caps apply to proofs, so a capped profile may silently produce fewer.

**Task 5: proving the split**
In Test mode the top branch of a split was always taken, so every test seat, Gold or not, goes down the Gold Members path. Nobody reaches Others, so the Test mode run does not prove it. **Dry run** can: it shows how many real profiles would take each path, and it contacts nobody.

**Task 6: Simulation's missing protections**
The suppression list, the allowed list, consent, frequency caps and quiet hours. The habit: type only your own address on a simulated user, and never use real customer data.

**Track B: what to expect**
The allowed list page shows a toggle at the top; in some development sandboxes it reads Deactivated, which means nothing limits where test mail goes. Simulate content (AEP profiles) shows your email filled with your test profile's values, and nothing is sent. A field with no fallback prints empty, which is exactly what episode 20 fixes.

**Check yourself**
1. Test mode, Simulation and Send proof can. Alerts and Dry run never do.
2. It flags the profile as a test profile; Test mode admits only flagged profiles.
3. Data loaded while the toggle is off never reaches the profile store.
4. The batch replaces that customer's whole row in the dataset.
5. It shortens it, like every wait, to 10 seconds.
6. In Test mode the top branch of a split is taken, and Gold Members is the top path.
7. It counts against the sandbox's active-journey limit (100 in development), runs for up to 14 days and needs publish rights.
8. A simulated user is not a stored profile, so it is not a member of a stored audience such as Gold Members.
9. Frequency caps apply to proofs.
10. Personalisation gaps, such as a greeting with no fallback printing `Hi ,`, before real customers see them.

</details>
