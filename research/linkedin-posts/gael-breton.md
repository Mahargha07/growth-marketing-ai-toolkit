# LinkedIn Posts — Gael Breton

**Profile:** https://www.linkedin.com/in/gaelbreton
**Role:** Co-founder, Authority Hacker
**Why included:** One of the most specific practitioners on AI-powered content production systems. Has documented actual AI workflows using Claude Code, sub-agents, and eval frameworks for content creation at scale. Focuses on information gain and research quality rather than just AI writing.
**Collected:** 20-06-2026

---

## Post 1

**Date:** ~April 2026
**Topic:** Why AI articles say nothing new — and how to fix it with better research

Your AI articles read fine but say nothing new.

That's because every AI article generator does the same thing: scrape the top 10 Google results and rewrite them. The output is grammatically perfect, well-structured, and completely useless. Zero information gain. Just the same recycled advice in a slightly different order.

The trick isn't better writing. It's better research.

A sub-agent roleplays as someone who just googled your keyword. It reads what's out there and asks: "what am I STILL frustrated about? What didn't these articles answer?"

Think of it as hiring a really picky reader who tells you exactly where the existing content falls short.

Then a research agent goes hunting. YouTube tutorials, Reddit threads, Twitter discussions. The places where people share what they actually learned, not what ranks on Google.

The result? We wrote a Meta ads article where the core advice was a "2-campaign loop" strategy — run a test campaign, find winners, scale them separately. The kind of thing I usually only hear at conferences from people who actually scale ad budgets.

That insight came from a Reddit thread. Not from the top 10 Google results.

Claude handles the writing section by section. Honestly the easy bit now. The hard part was always finding something WORTH writing. And that's what this solves.

---

## Post 2

**Date:** ~May 2026
**Topic:** Static sites vs WordPress — SEO, schema markup and Claude Code

My "$0 website vs $5K WordPress" post hit a nerve this week. 108 comments. Mostly devs. Let's actually answer them.

"What about SEO and structured data?"
Astro ships cleaner semantic HTML than 90% of WordPress themes. Schema markup is a 2-line prompt. Lighthouse on these static sites typically clears 95+ across the board on mobile.

"What about the client who wants to edit content?"
Three options: Markdown in a Git repo if they're technical. Decap or TinaCMS if they need a UI. Or teach them to use Claude Code directly. Non-technical people describe the change in plain English and it ships.

"What about bookings, CRM, analytics?"
Every modern SaaS ships a script tag. Calendly, HubSpot, PostHog, Plausible. Paste in, go.

WordPress still wins one category: high-frequency, multi-author, non-technical editing at scale. News sites. Blogs with 10 staff writers. Keep it there. For everyone else? The math stopped making sense months ago.

The one comment that made me laugh: "why buy a house when wood is free and land is cheap." The analogy is just wrong. The wood IS the house now. Claude Code isn't raw material you assemble. You describe the house, it ships the house.
---

## Post 3

**Date:** ~April 2026
**Topic:** How to build an eval process for AI content skills — stop shipping improvements that make things worse

For months I shipped "improvements" to my AI skills. And half of them probably made the skills worse. I had no way to tell. Then I built an eval process.

Here's the workflow I use now for building and refining any AI skill:

👉 Manually collect what good looks like. No AI. Just screenshots of real top performers in whatever format you're building for.

👉 Turn those examples into 20 yes/no questions. "Can I understand the offer without reading body copy?" "Is there one dominant idea, not three?" "Would the target audience feel 'this is for me'?"

👉 Vibe-build the first output in a chat. Give Claude the examples and the 20 questions as context. Don't write a skill yet.

👉 When the output is acceptable, use the skill-creator skill to extract a formal skill from that chat.

👉 Run the eval against every generation. Score out of 20. First generation usually lands at 11 or 12.

👉 Make changes. Rerun the eval. Score up = commit. Score down = revert.

Now every change has a numerical judge. I've stopped shipping versions that felt better but were actually worse.

Most people skip step 2. They think "I'll know when it's better." They won't.