# Episode 34: RAG Explained Simply: AI Chatbot on Your Data

**Watch:** Video coming soon on iTV

Part 4: Multiply the team (AI) · [Previous](../ep33-adobe-ai-assistant-data-insights-agent-in-cja/) · [Next](../ep35-ai-agents-and-mcp-explained-for-marketing-teams/)

## What you will learn

- Explain **tokens**, the **context window**, **embeddings** and **temperature** in plain words
- Describe the **retrieval-augmented generation (RAG)** pipeline, and why it beats **fine-tuning** for company knowledge
- Choose a **chunking** approach, and explain how chunking decides answer quality
- Require a **citation** in every answer and an **honest refusal** when retrieval is weak
- Evaluate with a **golden set** written before you build, and diagnose "fluent but wrong" at retrieval

## The story so far

Bloom, a wellness brand with 1.2 million customers, is in the last week of its Adobe programme. In episode 33 Kavya learned to verify Adobe's built-in AI, scoring ten questions against the truth and keeping an evidence sheet. Then Anjali, the Chief Marketing Officer (CMO), asked: "Why can't I just ask a chatbot about our products and campaigns?" Vikram said she could, if the team built the honest version: one that cites its sources and admits what it does not know.

## Key ideas

### 1. Why a general chatbot is not enough
A general chatbot has never read Bloom's **200-product catalogue** or its **campaign FAQ**, but asked anyway, it still answers smoothly, perhaps with an invented price or offer. A fluent, confident, wrong answer is a **hallucination**. Judge a chatbot by whether it is right, not by how it sounds.

### 2. LLM basics
| Term | Plain meaning |
|---|---|
| **Large language model (LLM)** | A model trained on text that predicts the next words; the engine behind chatbots |
| **Token** | A small piece of text, often a word or part of one; models read tokens, not words |
| **Context window** | How many tokens the model can hold at once: your question, the documents you hand it, and its answer |
| **Temperature** | How adventurous its word choice is. Low: steadier, more repeatable answers for facts. Higher: varied drafts for brainstorming |
| **Cost and latency** | More tokens cost more money and take longer to answer |

A model knows only its training plus its context window. Temperature cannot supply a missing fact: consistently wrong is still wrong.

### 3. Embeddings and the vector store
An **embedding** is text turned into a list of numbers (a **vector**) so similar meanings sit close together. "How much do I pay for the vitamin serum?" lands near the catalogue line "Vitamin C Serum 30 ml, price 34.00" (US storefront), though the question never says "price"; keyword search alone misses that link. A **vector store** holds embeddings and supports similarity search. Embeddings do not store the answer; they help find the passage that holds it.

### 4. RAG in four moves
**Retrieval-augmented generation (RAG)**: fetch the relevant passages first, then let the model answer only from them.
1. **Chunk**: split the documents into passages (chunks) that are stored and retrieved as units.
2. **Embed**: turn each chunk into a vector.
3. **Store**: keep the vectors in a vector store.
4. **Retrieve, then answer**: at question time, fetch the chunks closest to the question and hand them to the model with one instruction: answer only from these passages, and say which one you used.

Everything else is engineering detail around one goal: making retrieval good. RAG does not teach the model your data; it hands over the right pages each time.

### 5. RAG versus fine-tuning for company knowledge
| Question | Fine-tuning | RAG |
|---|---|---|
| What changes? | The model's learned habits | What the model reads at question time |
| A price or offer changes | Train again; the old fact can linger | Update one chunk |
| Can it cite? | No page to point at | Cites the exact chunk |
| Answer not in the data? | May guess from habit | Can refuse honestly |

Fine-tuning can help with style or format. For knowledge that changes, retrieve it fresh: *fine-tuning changes how the model talks; RAG changes what it reads.*

### 6. Chunking decides quality
Chunks that are **too small** lose context (a price separated from its product). Chunks that are **too large** bury the relevant sentence. A **fixed character count** cuts wherever the count runs out, even mid-sentence. Split on the document's own **structure**, its headings and sections, wherever you can.

| Check | Fixed character cut | Headings and sections |
|---|---|---|
| One product | Can land in two chunks | One product, one chunk: name, SKU, price and category together |
| One FAQ answer | Can be cut away from its question | Each question stays with its answer |
| What comes back | Partial matches | Whole, citable passages |

There is no perfect chunk size to memorise; test your choice against the golden set.

### 7. Citations and the honest refusal
- **Ground** every answer: answer only from the retrieved passages.
- **Cite** the chunk. Citation turns a plausible answer into a usable one, and makes human review practical rather than theatrical.
- **Refuse honestly**: when retrieval confidence is low, say so instead of guessing.
- **Break it on purpose**: ask a question whose answer is not in your documents, and confirm the refusal fires.

### 8. The golden set, and "fluent but wrong"
A **golden set** is a fixed list of questions with known answers, written **before** you build. Bloom's has ten: **5 answerable, 3 tricky, 2 unanswerable**. The target is **at least 8 of 10**, every answer cited, and both unanswerable questions refused. A set written afterwards quietly bends to the answers you already produce, and a demo that answers three questions impressively is not evidence. Track how often the right chunk was retrieved, not just how good the prose sounds.

**At Bloom:** the first index cut every few hundred characters, and the first run missed the target: one tricky answer was fluent but wrong. Vikram checked retrieval before the model and found the right passage never reached it, because a fixed cut had split one product's details across two chunks. After re-chunking by headings and sections, the second run (same ten questions, word for word) reached at least 8 of 10 with citations and refused both unanswerable questions.

Debugging order for "fluent but wrong": read the cited chunk, list every chunk retrieved, check the right passage is stored in one piece, fix what you find (at Bloom, chunking), re-run the same golden set. Only then look at the prompt or the model.

### 9. Where the value sits
Every team can rent the same models, so the model is a commodity; a company's own grounded content is not. Bloom's assistant reads product and campaign documents only: customer data never goes into a tool that has not been cleared for it.

**Interview line:** *"Fluent but wrong almost always means the right source never reached the model."* Back it with the Bloom build.

## In the product

No Adobe screens this time. Assistants like Bloom's can sit next to Adobe Experience Cloud (over catalogues, campaign wikis, operations runbooks) and are built outside the Adobe interface, on your own stack. Bloom started from the RAG notebook in its asset pack (a coding notebook: runnable code plus notes). The build, in order:

1. Index the catalogue and campaign FAQ: chunk, embed, store.
2. Wire retrieval into the chat loop.
3. Require a citation to a retrieved chunk in every answer.
4. Add the guardrail: low retrieval confidence means say so.
5. Run the 10-question golden set; record the scorecard.
6. Ask something not in the index; confirm the refusal fires.

## Common mistakes

- Turning the temperature down to fix a wrong answer.
- Fine-tuning on a catalogue whose prices and offers keep changing.
- Cutting documents on a fixed character count without reading them.
- Writing the golden set after the build, or testing only easy questions.
- Removing the refusal because it "looks weak" in a demo.
- Swapping the model or rewording the prompt before checking what was retrieved.
- Putting customer data into an AI tool that has not been cleared for it.

## Glossary

| Term | Meaning |
|---|---|
| Large language model (LLM) | A model trained on text that predicts the next words; the engine behind chatbots |
| Token | A small piece of text the model reads, often a word or part of one |
| Context window | How many tokens a model can hold at once |
| Temperature | A setting for how adventurous the model's word choices are |
| Embedding | Text turned into numbers so similar meanings sit close together |
| Vector store | The index that holds embeddings and supports similarity search |
| Chunk | A passage of source text stored and retrieved as a unit |
| Retrieval-augmented generation (RAG) | Fetch the relevant passages first, then let the model answer only from them |
| Fine-tuning | Training an existing model further on your own examples, changing its learned habits |
| Hallucination | A fluent, confident, wrong answer |
| Citation | The chunk an answer came from, named so a reviewer can check it |
| Golden set | Fixed questions with known answers, written before you build, used to score an AI |

## Exercise

Do the exercise in [exercise.md](exercise.md).

## Further reading

Search Experience League for: AI Assistant in Experience Platform, generative AI in Adobe Experience Cloud.

---
**Slides:** [slides.pdf](slides.pdf) &nbsp;|&nbsp; **Exercise:** [exercise.md](exercise.md) &nbsp;|&nbsp; **All episodes:** [course home](../../README.md)
