<div align="center">

<img src="assets/agensi-logo.png" width="128" alt="AI Outreach Assistant logo">

# AI Outreach Assistant

**Score your leads. Skip the duds. Send messages that sound like a human wrote them.**

An agent skill that ranks B2B sales leads 1–10 and drafts short, personalized cold email or LinkedIn outreach for the ones worth contacting, with a one-line reason behind every decision.

[![Get it on Agensi](https://img.shields.io/badge/Get_the_skill-Agensi-4f46e5?style=for-the-badge)](https://agensi.io/skills/ai-outreach-assistant-lead-scoring-cold-outreach)
[![Works with](https://img.shields.io/badge/Claude_Code_·_Codex_·_Cursor_·_Gemini_CLI-14b8a6?style=for-the-badge)](#works-with)

[Get the skill](#get-the-skill) · [See it work](#see-it-work) · [How it decides](#how-it-decides) · [Run it locally](#run-the-open-source-pipeline) · [FAQ](#faq)

</div>

---

## Get the skill

The skill is on **[Agensi](https://agensi.io/skills/ai-outreach-assistant-lead-scoring-cold-outreach)**. Connect your agent to Agensi once, then ask:

```text
Score these leads and draft LinkedIn outreach for the good ones.
```

No API keys, no local model, no setup. Your agent does the scoring and writing itself.

## See it work

**You type:**

```text
Score these leads and draft LinkedIn outreach for the good ones.
We sell an AI developer-vetting platform for engineering teams.

name,company,role,industry,linkedin_about,pain_point
Rahul Mehta,Acme Tech,CTO,SaaS,Building cloud-native SaaS products,Scaling engineering teams efficiently
Ananya Singh,FinEdge,Head of Engineering,FinTech,Leading fintech platform development,Hiring vetted developers quickly
Priya Nair,BrightMart,Store Operations Manager,Retail,Runs day-to-day operations for 3 stores,Reducing staff turnover
```

**Your agent returns:**

| Name | Company | Score | Priority | Outreach |
| --- | --- | :---: | :---: | --- |
| Ananya Singh | FinEdge | 8 | 🟢 High | Drafted |
| Rahul Mehta | Acme Tech | 8 | 🟢 High | Drafted |
| Priya Nair | BrightMart | 3 | 🔴 Low | Skipped |

> **Ananya Singh** · *Score 8/10 (High) because engineering leader at a FinTech with an urgent hiring pain that developer vetting directly addresses.*
>
> Hi Ananya, leading platform development at FinEdge must mean hiring is rarely off your plate, and in FinTech every new engineer has to clear a high bar for security and reliability. Many engineering heads we speak with lose weeks screening candidates who look strong on paper but stall in technical rounds. We help teams like yours shortlist pre-vetted developers in days, so your senior engineers spend time building rather than interviewing. Would a short call next week to compare notes on your current hiring process be useful?

Everything is saved to `output_messages.csv`: your columns plus score, priority, reason, decision trace and message.

## How it decides

| Step | What happens |
| --- | --- |
| **1. Score** | Each lead gets 1–10 for seniority and buying authority, how well the pain point fits what you sell, industry and company fit, and likely benefit. |
| **2. Gate** | Leads below the threshold (7 by default, change it any time) are skipped. No message is wasted on a bad fit. |
| **3. Write** | One paragraph, under 120 words, at least two real details about the prospect, and a soft question as the call to action. No hype, no emojis, no invented facts. |
| **4. Explain** | Every lead gets a trace, such as `Score 8/10 (High) because… Outreach generated.`, so you can audit or defend the list. |

Missing details on a lead? The agent asks you. If you approve the per-call price, it can fill them in with Agensi's lead-data tools.

## Works with

Any agent that supports the open **SKILL.md** standard: Claude Code, Claude apps, Codex CLI, Cursor, Gemini CLI, VS Code Copilot and more.

## Run the open-source pipeline

This repo also has the original standalone Python version, which runs fully offline on a local model through [Ollama](https://ollama.com).

```bash
git clone https://github.com/tkwind/ai-outreach-assistant.git
cd ai-outreach-assistant
pip install -r requirements.txt
ollama pull mistral
python outreach_generator.py
```

It reads `data/leads.csv` and writes `data/output_messages.csv`. Change the threshold in `config.py` and the prompts in `prompts.py`.

```text
├── outreach_generator.py   # orchestrator: score → gate → write → save
├── agents/
│   ├── scorer.py           # decision agent: score, priority, reason
│   └── messenger.py        # execution agent: drafts the outreach
├── prompts.py              # scoring rubric + message rules
├── config.py               # threshold and fallback values
├── utils.py                # Ollama client
└── data/leads.csv          # sample input
```

## FAQ

<details>
<summary><b>Does it send the messages?</b></summary>

No. It drafts them and saves them to a CSV so you review everything before anything goes out.
</details>

<details>
<summary><b>Can I aim it at my own product?</b></summary>

Yes. Tell the agent what you sell and who is sending. It scores fit and writes messages around your offer.
</details>

<details>
<summary><b>Will it make things up about a prospect?</b></summary>

No. It uses only the data you give it, or data from enrichment you approved. If it's unsure, it generalizes ("many teams in your industry…") instead of inventing details.
</details>

<details>
<summary><b>Skill vs. this repo: what's the difference?</b></summary>

The skill runs inside your AI agent with no setup. This repo is the standalone Python pipeline for people who want to run everything offline on their own machine.
</details>

---

<div align="center">
<sub>Built by <a href="https://github.com/tkwind">@tkwind</a> · Skill available on <a href="https://agensi.io/skills/ai-outreach-assistant-lead-scoring-cold-outreach">Agensi</a></sub>
</div>
