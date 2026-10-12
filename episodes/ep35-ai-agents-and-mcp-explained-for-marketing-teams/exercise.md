# Exercise 35: Extend the brief-writer

You will list a campaign-brief agent's tools and their access, write the contract for a 48-hour frequency-guardrail tool and show it trip, write the agent's one-page governance note, and design an approval gate that people will actually read.

**Safety rule for every task:** never put customer data into a public AI service. Use only the sample data below.

## Sample data (fictional, for this exercise)

The same three tables are in `bloom-agent-sample-data.json` in the course data folder, ready for the optional coding task.

**Audiences the agent can count**

| Audience | Rule (short) | Estimate |
|---|---|---|
| Lapsed 90 | Last order more than 90 days ago and email consent true | 3,890 of the 10,000-customer extract |
| Gold Members | Loyalty tier is Gold | Not given; leave it as a placeholder |

**Offer library**

| Offer | Eligible | Ranking |
|---|---|---|
| 20% Comeback | Lapsed 90 only | Ranks above Early Access Drop |
| Early Access Drop | Gold only | Second |
| Free Shipping | Everyone (the fallback) | Used only when nothing else qualifies |

**Send log** (the agent runs today at 09:00; times are illustrative)

| Sent | Message | Audience |
|---|---|---|
| Yesterday, 15:00 | Bloom Win-Back | Lapsed 90 |
| Six days ago, 10:00 | Bloom Gold Thank-You | High-Value Loyalists |

## Track A: No Adobe access needed

1. **List the tools.** Bloom's campaign-brief agent has an audience-count lookup, an offer-library check and a brief writer, and you are adding a frequency-guardrail check. For each tool, write one line on what it does and mark it **read-only** or **write**. Then name one tool the agent must **not** have, and say why.
2. **Write the guardrail's contract.** Fill in four lines: input, check, output, and how it changes the draft. Then run it by hand against the send log for the goal "win back lapsed Gold members": how many hours have passed since Lapsed 90 was last messaged, does the guardrail trip, and what does the brief now recommend?
3. **Write the one-page governance note.** Use these headings:
   - a. Goal and scope
   - b. Tools and their access
   - c. What the agent may do alone
   - d. What needs a human approval, and whose
   - e. Dry-run mode (when it is on)
   - f. Stopping conditions (steps, spend, time, definition of done)
   - g. Failure behaviour
   - h. Audit: what is logged, who reads it, how often
4. **Design one approval gate without approval fatigue.** Say where the gate sits, who approves, what the approver sees on one screen, and what happens if nobody answers.
5. **Optional coding.** In any language, or with any agent framework, build a two-tool agent over the sample data above: an audience-count tool and a send-log tool. Give it a dry-run flag, a step limit and a log that records every call with its inputs and outputs. Make the code, not the model, run the send-log check before any recommendation to send.

## Track B: If you have a development sandbox (optional, look only)

Safety first:
- Practise only in a **development** sandbox, and only on objects that carry your own initials.
- Look only. Never click **Activate**, **Publish**, **Send proof** or **Approve**, and never create, edit or delete anything.
- Never connect an agent, notebook or script to a shared sandbox with write access.
- In a shared environment: look, screenshot, leave.

Steps (labels as of October 2026):
1. In Adobe Experience Platform, expand **Customer**, select **Audiences**, then the **Browse** tab. Find one audience you own and note its count. This is what an audience-count tool would read.
2. In Journey Optimizer, open **Decisioning**, **Catalogs**, and read one decision item's eligibility. This is what an offer-library tool would read.
3. In Journey Optimizer, open **Journey Management**, **Reports**, then **Campaigns**. With the default period, **Last 7 full days**, see which campaigns sent in that period. This is close to what a send-log tool would read. Remember that this reporting is in UTC.
4. For each of the three screens, write whether an agent doing the same check needs read access or write access.

## Check yourself

1. What separates an agent from an assistant?
2. In tool calling, who actually runs the tool?
3. What does MCP standardise, and what does it not decide?
4. Why did the first run of the brief agent miss the recent send?
5. What is the agent's dry-run mode, and how is it different from Journey Optimizer's Dry run?
6. Name the four stopping conditions.
7. What should an agent do when a tool fails?
8. Where should the human approval gate sit, and why not at every step?
9. Why log every agent action?
10. Give the interview line for this episode, and one sentence of evidence from your build.

<details><summary>Check your answers</summary>

**Task 1: tools (model answer)**

| Tool | What it does | Access |
|---|---|---|
| Audience-count lookup | Counts people in Lapsed 90 and Gold Members | Read-only |
| Offer-library check | Lists the offers those people qualify for, in ranked order | Read-only |
| Frequency-guardrail check | Reads the send log; warns if the audience was messaged in the last 48 hours | Read-only |
| Brief writer | Saves the draft brief into one drafts folder | Write, one folder only |

The agent must not have a send tool (or a journey-publish or export tool). A send is irreversible, the brief does not need it, and a tool you do not need is risk you do not need.

**Task 2: the contract and the trip**
- Input: the audience name (Lapsed 90) and a 48-hour window.
- Check: the send log, for any message to that audience inside the window.
- Output: "clear", or a warning naming the last message and its time.
- Effect: on a warning, the brief must recommend waiting before any new send to that audience.
- The trip: Bloom Win-Back went to Lapsed 90 yesterday at 15:00, and the agent runs today at 09:00. That is 18 hours, inside 48, so the guardrail trips. The brief drops the next-morning send and recommends waiting until the window has passed, then checking the weekly cap of 2 marketing emails per profile before scheduling anything.

**Task 3: a model governance note (short form)**
- a. Goal and scope: drafts Bloom's weekly campaign brief from a goal; development data only; never contacts a customer.
- b. Tools: three read-only (audience counts, offer library, send log), one write (brief writer, one drafts folder).
- c. Alone: read counts, offers and the send log; write and overwrite drafts.
- d. Approval: turning any brief into a send needs Divya's decision. Adding any new write tool needs the architect's sign-off first.
- e. Dry-run mode: on by default for every new version and every new tool.
- f. Stopping conditions: say, for example, ten tool calls and a few minutes per run, a spend cap, and done = audience, offer, recommendation, every check logged.
- g. Failure: stop and report what failed, with the log. Never retry forever, never guess an offer.
- h. Audit: every call with inputs, outputs and the stated reason; Kavya reads the logs weekly; the log is kept with the brief.

**Task 4: a gate without fatigue (one good design)**
One gate only, where the brief becomes a send. Divya approves. Her one screen shows the audience and its count, the offer, the guardrail result with the last send time, and the proposed send time. If nobody answers, nothing is sent: the default is no. Reading and drafting need no approval, so the one gate stays meaningful.

**Task 5: optional coding, what good looks like**
The log shows every call with inputs and outputs; the dry-run flag stops any write; the step limit ends the run cleanly; and the send-log check runs in code before any "send" recommendation, so the model cannot skip it.

**Check yourself**
1. An agent plans, acts with tools, observes the result and continues towards a goal until it is met or a limit is hit. An assistant answers and stops.
2. The software around the model (in Bloom's case, the notebook's code). The model only asks for a tool by name with inputs, then reads the result.
3. MCP standardises how tools are described (name, job, inputs) so agents can discover and call them. It does not decide which tools an agent should be allowed to use.
4. It had no tool that could check recent sends. An agent can only check what it has a tool for.
5. The agent plans, calls read-only tools and reports, but changes nothing. Journey Optimizer's Dry run is a journey test that counts how many profiles would take each path.
6. Maximum steps, maximum spend, a timeout, and a definition of done.
7. Stop and report what failed, with the log, instead of retrying forever or guessing.
8. Before irreversible actions: a send, a delete, an export. At every step, people soon approve without reading (approval fatigue).
9. So every decision can be reconstructed, defended to a client or a regulator, and improved.
10. "Put the human approval where the action is irreversible." Evidence: "I extended a campaign-brief agent with a 48-hour frequency guardrail, ran it in dry-run mode and watched it change the brief."

</details>
