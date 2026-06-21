# Growth Marketing AI Toolkit
## AI-Powered SEO Content Production Research

**Built by:** Mahargha Barman
**Purpose:** Portfolio research project for 100 Hires application
**Topic:** AI-Powered SEO Content Production
**Last Updated:** June 2026

---

## What This Repository Is

This repository documents a systematic research project into AI-powered SEO content production — how the best practitioners in the world are actually building systems that produce SEO content using AI, at scale, without sacrificing quality.

This is not a collection of blog posts about AI SEO. It is primary source material — YouTube transcripts and LinkedIn posts — from 10 practitioners who are running real AI content production systems at real companies and agencies.

---

## Why I Chose This Topic

I have been doing SEO and content production professionally for two years at a digital marketing agency, working across multiple B2B and B2C clients. I have used AI for content production daily — building prompt systems, producing 40+ pieces per month, implementing structured data, and tracking performance in Google Search Console.

That hands-on experience is exactly why this topic matters to me personally. I have seen the difference between using AI to scale bad content faster and using AI to build systems that produce genuinely better content. The gap between those two approaches is what this research explores.

The experts in this repository are the people I would want to learn from if I were building an AI content production system from scratch today.

---

## Repository Structure

**Root level**
- README.md — this file
- fetch_transcripts.py — Python script used to collect YouTube transcripts via Supadata API

**research/**
- sources.md — full expert list with annotations and selection methodology

**research/linkedin-posts/**
One file per expert, containing 3 manually collected LinkedIn posts each — ryan-law.md, kevin-indig.md, koray-tugberk-gubur.md, nathan-gotch.md, britney-muller.md, aleyda-solis.md, brendan-hufford.md, wil-reynolds.md, ross-hudgens.md, gael-breton.md

**research/youtube-transcripts/**
One folder per expert containing transcript text files — ryan-law, kevin-indig, koray-tugberk-gubur, nathan-gotch, britney-muller, aleyda-solis, brendan-hufford, wil-reynolds, ross-hudgens

---

## The 10 Experts

| # | Expert | Role | Focus |
|---|--------|------|-------|
| 1 | Ryan Law | Director of Content, Ahrefs | AI content automation systems |
| 2 | Kevin Indig | Growth Advisor, Growth Memo | AI citation research and content visibility |
| 3 | Koray Tugberk Gubur | CEO, Holistic SEO and Digital | Topical authority and semantic content systems |
| 4 | Nathan Gotch | Founder, Gotch SEO and Rankability | AI SEO campaigns and content optimization |
| 5 | Britney Muller | AI Implementation Expert | Data science meets content production |
| 6 | Aleyda Solis | Founder, Orainti | AI search optimization and E-E-A-T |
| 7 | Brendan Hufford | Founder, Growth Sprints | B2B SaaS AI content strategy |
| 8 | Wil Reynolds | Founder, Seer Interactive | Training data strategy and AI content ROI |
| 9 | Ross Hudgens | Founder, Siege Media | Data-driven GEO and content format research |
| 10 | Gael Breton | Co-founder, Authority Hacker | AI content production systems and eval frameworks |

Full annotations, why each expert was selected, and key frameworks extracted from their content are in research/sources.md.

---

## How Content Was Collected

**YouTube Transcripts**
Collected using the Supadata API (free tier) and the youtube-transcript-api Python library. 16 transcripts collected across 9 experts. One expert (Gael Breton) is LinkedIn-only as his YouTube content focuses on affiliate marketing rather than AI SEO production systems — including weaker content to reach 10 would have compromised research quality.

**LinkedIn Posts**
Manually collected from each expert's LinkedIn profile. Only posts specifically relevant to AI-powered SEO content production were included. Posts about personal achievements, tool promotions, or unrelated topics were excluded. Several experts required extensive profile review to find 3 relevant posts — this process itself validated their inclusion.

---

## How I Worked — Commit History

This project was built incrementally with regular commits throughout:

- Set up repository structure and README
- Added fetch_transcripts.py script
- Collected and committed YouTube transcripts per expert batch
- Added LinkedIn posts per expert as collected
- Added sources.md with full expert annotations
- Updated README with final research summary

Each commit reflects a meaningful unit of work rather than one giant push at the end — consistent with how professional async teams operate.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Cursor IDE | Code editor and repository management |
| Claude Code | AI assistant for script writing and workflow automation |
| Python | Transcript fetching script |
| Supadata API | YouTube transcript collection |
| GitHub | Version control and portfolio hosting |

---

## Key Findings From The Research

After collecting and reviewing this material, six themes emerged consistently across all 10 experts:

**Quality over volume** — AI content fails when it scales bad content faster. Editorial standards, not AI capability, are the differentiator.

**Off-property signals drive AI citations** — Brand mentions on retrieval sources matter more than on-page optimization for AI visibility.

**Training data timing is strategic** — Publishing before a training cutoff has fundamentally different ROI than after. Most content calendars ignore this entirely.

**Research is the bottleneck** — Finding genuinely new information is the hard part. AI handles the writing. Sub-agents and community mining solve the research problem.

**Measurement is broken** — AI visibility metrics without business outcome tracking are misleading.

**Human judgment is irreplaceable** — AI can match patterns and scale distribution. It cannot decide which pattern to break or whether content respects the reader's time.

---

## What This Research Could Support

This repository is designed to support a full AI-powered SEO content production playbook. The source material collected here covers every layer needed:

- Strategic frameworks for deciding what to produce and why
- Technical systems for producing content with AI at scale
- Quality control processes for maintaining editorial standards
- Measurement frameworks for tracking real business outcomes
- Distribution strategies for maximizing AI citation visibility

---

## About The Researcher

Mahargha Barman is an AI-powered SEO and Content Specialist based in Pune, India, with two years of agency experience across B2B and B2C clients. Currently working at Magicworks IT Solutions, building AI-assisted content workflows, structured data systems, and SEO production pipelines for clients including ThatsmyEV and VJ Instruments.

**GitHub:** https://github.com/Mahargha07
**LinkedIn:** https://www.linkedin.com/in/mahargha-barman