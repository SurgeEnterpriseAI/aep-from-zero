# Sample data for AEP From Zero

**All data in this folder is synthetic.** Bloom is a fictional brand. Every customer is made up, every email address ends in `@example.com`, every phone number uses the 555-01XX range kept for fiction, and no row describes a real person. There are no credentials anywhere in this folder: the Postman collection holds empty placeholders only.

Prices are US dollars, because the sample files come from Bloom's US storefront. Figures for the relaunch fortnight are fictional, and the ones marked illustrative are practice numbers, not Bloom results.

## Files

| File | What it is for | Episodes |
|---|---|---|
| `bloom-customers-500.csv` | The 500-row trial CRM file: 14 columns, including the three consent columns. Dirty on purpose: mixed-case emails, five phone shapes, and some emails shared by two or more rows | 5, 6, 8, 15 |
| `bloom-orders-500.csv` | The 500-row trial order file, one product line per row (`price` is the line total). Holds the five deliberately broken rows that episode 6 diagnoses | 6, 15 |
| `bloom-identities-200.csv` | Identity links (ECID, email, BloomID) seen together for 200 test customers, including Priya. The two rows at the end share one ECID: a planted shared-tablet over-link | 7 |
| `bloom-customers-xdm.json` | The same 500 customers shaped as XDM JSON (email, name, home address, phone), to compare with the CSV and the mapping in episode 5 | Optional; no exercise needs it |
| `sample-profile-priya.json` | Priya Sharma's profile record. Its identityMap lists BloomID as a teaching shape; Bloom Customer Profile itself declares one identity, Email | 3, 4, 8, 25, 33 |
| `sample-web-event.json` | Priya's anonymous 7:44 PM add-to-cart: ECID only | 3, 4, 21 |
| `sample-order-event.json` | Priya's 7:52 PM order `BLM-88412`: two line items, 54.00 in all. Its Email-primary identityMap is a mismatch episode 4 asks you to find | 3, 4 |
| `bloom-product-catalogue.csv` | Product catalogue sample: the 10 SKUs that appear in the sample files, with name, category, list price, image path and a short description. Image files are not included | 21, 25, 34 |
| `bloom-campaign-faq.md` | Internal relaunch FAQ with one question per heading: loyalty bands, the 20% Comeback, Early Access Drop, Free Shipping, the weekly email cap. No sale dates and no future prices | 34 |
| `bloom-brand-sheet.md` | Bloom's logo notes, colours, tone rules and the legal block for the footer | 19, 33 |
| `bloom-aep-postman-collection.json` | Two read-only Profile Access API requests, with `{{ACCESS_TOKEN}}`, `{{API_KEY}}`, `{{IMS_ORG}}` and `{{SANDBOX_NAME}}` left empty for your own development values. Its pre-request check refuses to send without a sandbox name | 14 |
| `bloom-ajo-welcome-practice-logs.csv` | Simplified step events, message feedback and email tracking rows from the broken practice copy of Bloom Welcome v1 | 24 |
| `bloom-ajo-send-log.csv` | Relaunch-fortnight send log for the ops readout (illustrative): sends, delivered, opens, spam complaints and unsubscribes per message | 24 |
| `bloom-agent-sample-data.json` | Audiences, offer library and send log for the campaign-brief agent and its 48-hour guardrail | 35 |
| `bloom-cja-channels.csv` | Orders by raw channel tag in the relaunch fortnight, including No value and the `email` / `Email` duplicate. Rows sum to 1,240 orders | 27, 36 |
| `bloom-cja-bands.csv` | Orders and revenue by loyalty band in the relaunch fortnight (1,240 orders, $66,260) | 27, 28, 36 |
| `bloom-cja-fallout.csv` | Fallout in people, journey entry to purchase, for the relaunch fortnight | 30, 31 |
| `bloom-cja-cohort-repeat.csv` | Illustrative cohort table: repeat purchase by week of first order, in percent. Bloom Welcome v1 went live at the start of week 3 | 30 |
| `generate_datasets.py` | Rebuilds the first four files in this table, byte for byte. Add `--full` for the 10,000-customer and 25,000-order extract the trial files come from | Any |

## Good to know

- **Do not clean the trial files before the exercises.** The casing, phone shapes, duplicate emails, broken order rows and the tablet over-link are the lessons.
- **Named customers match the episodes:** Priya Sharma `BLM-CUST-004217` (Gold, 2,340 points, Dallas), Liam Iyer `BLM-CUST-000002` (Bronze, 259), Maya Rao `BLM-CUST-000048` (Silver, 880), Noah Kim `BLM-CUST-000101` (Gold, 4,120) and Zara Bose `BLM-CUST-000210` (Bronze, 35). Other rows are background only.
- **Priya's order in the CSV.** The trial order file holds one product line per row, so `BLM-88412` appears with its first line (Vitamin C Serum 30 ml, 34.00). The whole two-line order is in `sample-order-event.json`.
- **Join dates** run up to 29 September 2026; none is in the future.
- **Run it yourself:** `python generate_datasets.py` rewrites the trial files in this folder; `python generate_datasets.py --full --out somewhere` also writes the full-size files. It uses only the Python standard library.
- **Safe practice:** load these files only into a development sandbox, into datasets that carry your own initials, and never send to real customers.
