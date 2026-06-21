# LinkedIn Posts — Britney Muller

**Profile:** https://www.linkedin.com/in/britney-muller
**Role:** AI Implementation Expert | Former Senior SEO Scientist, Moz
**Why included:** Bridges data science and marketing with rare technical depth. One of the few practitioners who understands both the SEO and machine learning sides of AI content production. Known for correcting industry misconceptions about how LLMs actually work.
**Collected:** 20-06-2026

---

## Post 1

**Date:** ~June 2026
**Topic:** Context Window — AI's Working Memory and what marketers miss

Context Window = AI's Working Memory

Ever had AI seem to "forget" instructions you gave it earlier in a long conversation? This is why:

The context window is the amount of text, in tokens, that an AI model can consider at any one time. Think of it as working memory; it determines how long a conversation it can carry out before forgetting details from earlier.

Everything you put into your prompt, any documents, conversation history, and the AI's responses all need to fit within this limit. What happens when that fills up? The model begins to "forget" from the beginning; like a queue where new information enters and old information exits.

But here's what most people miss: bigger isn't always better! As the context window grows, model performance can actually start to degrade.

There's also a quirk called "Lost in the Middle": Models perform best when relevant information is toward the beginning or end of the context. Information buried in the middle is more likely to be missed or underweighted, even when it's technically 'in' the conversation.

Practical workarounds shared by practitioners:
- Prompt that "the conversation is getting too long" and ask for a summary and a prompt for a new chat
- Use Claude Code's /compact command to manually tell Claude to summarize key information and clear out the noise while keeping what matters
- Use Claude first to create a project spec sheet that breaks your project into smaller, defined chunks, then feed each chunk to the build tool one at a time

One problem, three different solutions — all shared inside Orange Labs this month.

---

## Post 2

**Date:** ~June 2026
**Topic:** 6 things marketers succeeding with AI do differently

Marketers Succeeding With AI Do These 6 Things:

Rule #0: You start with the PROBLEM, not the tech. If you can't clearly name your task in one sentence, you aren't ready yet.

#1 You understand the power of examples.
The #1 research-backed tip is "few-shot learning": show the model 2-3 examples of what 'good' looks like, plus what to avoid. Instead of "write me a newsletter," try "here are 3 past newsletters. Write the next one in this style covering [topic/info]."

#2 You have a brand mentions strategy.
Brand mentions are the new backlinks. Reddit alone accounts for ~24% of all Perplexity citations. AI search engines pull real human convos into their answers. Most brands post to their own feed and wonder why "AI Search" ignores them.

What to do:
- Use SparkToro to find where your audience is already talking
- Show up with genuine value, not self-promotion
- Publish proprietary surveys, benchmarks, and data under your brand name

#3 You gut check before automating.
Could mistakes harm people? Damage your brand? Have unintended consequences? If yes to any: human in the loop. Always.

#4 You write your draft first. Then hand it to AI.
Most people start with AI but you'll get further starting with YOUR draft. Bring your unique perspective, opinions, and data in first. Then let AI make it sharper and tighter. AI generates the average of everything it's seen; your unique writing, voice, and tone is what will stand out from the slop.

#5 You know if your V1 is perfect, you waited too long.
Stop planning. Start prompting/experimenting. Run it. See what breaks. Fix it. Done beats Perfect.

#6 You use AI to help get you unstuck.
"Here are the common tasks I do throughout a typical week: [list them]. Which of these might be good candidates for AI? For each one, explain why or why not."

---

## Post 3

**Date:** ~April 2026
**Topic:** Grounding doesn't mean what you think it means — RAG vs true grounding

"Grounding" Doesn't Mean What You Think It Means

Words matter, especially when they're quietly reshaping how an entire industry thinks.

"Grounding" comes from "ground truth," rooted in statistics and originally cartography, where it literally meant going outside to verify that your map matched reality.

The core problem with LLMs is that there's no ground truth signal during training or generation. The model isn't checking its answer against the facts; it's only predicting the next most likely word.

What Microsoft calls "grounding" is actually RAG (Retrieval-Augmented Generation): retrieving web documents to supplement a response. Useful! But web text is written by humans, about reality, not reality itself. Those documents can be wrong, biased, SEO-manipulated, or outdated.

RAG is better-informed guessing. True "grounding" is fundamentally a different thing.

Microsoft's new "Grounding Queries" metric in Bing Webmaster Tools makes this even more confusing. Those aren't user queries. They're background searches AI quietly generates when a user submits a prompt.

SEOs are now optimizing for a word we don't have a shared definition of. And when AI researchers hear you use "grounding" this way, it'll erode your credibility.

As AI continues to reshape industries, it's more important than ever for us to understand these nuances. By learning the true meaning behind AI terms and tech we can communicate more effectively, make better decisions and drive real results.