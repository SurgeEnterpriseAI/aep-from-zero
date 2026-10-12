# Exercise 34: Ask Bloom anything (honestly)

You will draw the retrieval-augmented generation (RAG) pipeline and its failure modes, compare two ways of chunking, write a golden set before you build, and (optionally) build a tiny retrieval step that cites its source and refuses when it should.

**Data rule:** use only the sample catalogue (`bloom-product-catalogue.csv`) and the sample campaign FAQ (`bloom-campaign-faq.md`) from the repo's data folder. Never put customer data into a public AI service.

## Track A: No Adobe access needed

1. **Draw the RAG pipeline.** On paper, draw the four moves as five boxes, splitting the last move in two: chunk, embed, store, retrieve, answer. Under each box, write one way that stage can fail and what the user would see.
2. **Chunk the FAQ two ways.** Take the sample campaign FAQ.
   - a. Cut it every **200 characters**, ignoring the text. Number the pieces.
   - b. Cut it **by heading**, so each question stays with its answer. Number the pieces.
   - c. Write three questions a colleague might ask. For each, note which piece would need to be retrieved under (a) and under (b), and predict which version retrieves better. Give one reason each.
3. **Write a ten-question golden set** for Bloom's catalogue and FAQ, before building anything:
   - 5 **answerable**: the answer sits clearly in one document
   - 3 **tricky**: worded differently from the documents, or easy to mix up between products or offers
   - 2 **unanswerable**: the answer is in neither document

   For each question write the known answer (or "should refuse") and the chunk that holds it. Set the target: at least 8 of 10, every answer cited, both unanswerable questions refused.
4. **Diagnose "fluent but wrong" on paper.** The assistant says the Hyaluronic Moisturiser 50 ml costs 34.00 and cites a chunk. The catalogue says 20.00. List, in order, the first three things you check, and what you would change if the cited chunk turns out to hold the end of one product and the start of the next.
5. **Optional coding.** In any notebook-friendly language, build a tiny retrieval step over the sample catalogue using keyword search or embedding search.
   - Return the top chunks with their IDs.
   - Every answer must cite a chunk ID.
   - If the best match is below a threshold you choose, print a refusal message such as "I can't find that in Bloom's documents."
   - Score it against your golden set and record the scorecard.

## Track B: If you have a development sandbox (optional, read only)

Safety first:
- Use Adobe's AI features only if your organisation has approved them. Accepting generative AI terms is the organisation's decision, never yours.
- Never paste customer data into any prompt.
- Look, screenshot, leave. Do not save, create or change anything. Never Activate, Publish or send anything.

Steps:
1. If AI Assistant is available in your Experience Platform interface (availability varies), ask it two questions about Experience Platform itself (not about Bloom's catalogue, which it has never read), in the style of your golden set: one whose answer you have already checked in Adobe's documentation, and one you believe it cannot answer.
2. For each, record in your evidence sheet: prompt, output, verdict, correction.
3. Note whether each answer points you to a source you can check, and whether it admits when it does not know. Compare that with the two rules from this episode: cite, or refuse.

## Check yourself

1. What is a token, and what is a context window?
2. Why can't temperature fix a wrong answer?
3. What does an embedding do, and what does it not do?
4. Name the four moves of RAG.
5. Give two reasons RAG beats fine-tuning for a catalogue whose prices change.
6. Why should chunks follow headings and sections rather than a fixed character count?
7. What are the three parts of Bloom's golden set, and what is the target?
8. Why must the golden set be written before the build?
9. An answer is fluent but wrong. Where do you look first?
10. Where does the commercial value of a grounded assistant sit?

<details><summary>Check your answers</summary>

**Task 1: failure modes (model answer)**

| Stage | One failure | What the user sees |
|---|---|---|
| Chunk | A fixed cut splits one product's details across two chunks | A fluent answer built on half the facts |
| Embed | Documents and questions embedded with different settings or models | Irrelevant passages come back |
| Store | Old chunks never removed after a price change | A confident, out-of-date answer |
| Retrieve | The right chunk is not among the closest | Fluent but wrong, or a needless refusal |
| Answer | No "answer only from these passages" instruction, no citation, no refusal rule | A hallucination nobody can check |

**Task 2: chunking prediction**

Cutting by heading usually retrieves better: each answer stays with its own question and heading, so the chunk matches the question as a whole and can be cited by name. A 200-character cut can separate a question from its answer, or glue the end of one answer to the start of the next, so retrieval returns partial matches. Your three predictions should name the piece numbers and say this in your own words.

**Task 3: a sample golden set (yours may differ)**

These match `bloom-campaign-faq.md`, which covers the relaunch offers and gives no sale dates, and `bloom-product-catalogue.csv`, which gives current list prices only. If you use other samples, adjust to what they actually contain.

| # | Type | Question | Known answer |
|---|---|---|---|
| 1 | Answerable | What does the Vitamin C Serum 30 ml cost on the US storefront? | 34.00 US dollars, SKU BLM-SER-VITC-30 (catalogue chunk) |
| 2 | Answerable | What does the Hyaluronic Moisturiser 50 ml cost? | 20.00 US dollars, SKU BLM-MOIST-HYA-50 (catalogue chunk) |
| 3 | Answerable | Which offer do lapsed customers get? | 20% Comeback, for Lapsed 90 only (FAQ chunk) |
| 4 | Answerable | Which offer is for Gold members? | Early Access Drop, Gold only (FAQ chunk) |
| 5 | Answerable | What happens if no other offer applies? | Free Shipping is the fallback (FAQ chunk) |
| 6 | Tricky | How much do I pay for the vitamin serum? | 34.00: same as question 1, worded differently |
| 7 | Tricky | I'm a Gold member who hasn't ordered in four months. Which offer do I get? | 20% Comeback if they are in Lapsed 90 (which also needs email consent): it ranks above Early Access where both qualify |
| 8 | Tricky | A question about one product whose details sit next to a similar product | The right product's details, not its neighbour's |
| 9 | Unanswerable | When does the next sale start? | Should refuse: in neither document |
| 10 | Unanswerable | What will the serum cost next year? | Should refuse: in neither document |

Target: at least 8 of 10, every answer cited, questions 9 and 10 refused.

**Task 4: debugging order**
1. Read the wrong answer and the chunk it cited: does that chunk actually say 34.00 for the moisturiser?
2. List every chunk retrieved for the question: was the moisturiser's own chunk among them?
3. Check the moisturiser's details exist in the index in one piece.

If the cited chunk holds the end of one product and the start of the next, the fixed cut is the fault. Re-chunk by headings, so each product is one chunk, then re-run the same golden set. Do not start by swapping the model or lowering the temperature.

**Task 5 (optional):** a passing build answers at least 8 of 10 correctly, cites a chunk ID in every answer, and prints the refusal for both unanswerable questions. If it misses, look at what was retrieved before changing anything else.

**Check yourself**
1. A token is a small piece of text the model reads, often a word or part of one. The context window is how many tokens it can hold at once: question, documents and answer.
2. Temperature changes how adventurous the word choice is, not what the model knows. Consistently wrong is still wrong.
3. It turns text into numbers so similar meanings sit close together, which lets a question find the right passage. It does not store or produce the answer.
4. Chunk, embed, store, then retrieve and answer only from what was retrieved.
5. A changed price means updating one chunk instead of training again, and RAG can cite the exact chunk (and refuse when nothing matches).
6. A fixed count cuts wherever it runs out, even mid-sentence, so one product or one FAQ answer can land in two chunks. Headings keep each unit whole and citable.
7. Five answerable, three tricky, two unanswerable; at least 8 of 10, every answer cited, both unanswerable questions refused.
8. Written afterwards, it quietly bends to the answers you already produce.
9. Retrieval: which chunks came back. Fluent but wrong almost always means the right source never reached the model.
10. In the company's own grounded content. The model is a commodity; the content is not.

</details>
