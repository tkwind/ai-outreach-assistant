# AI-Powered Lead Scoring & Outreach System

An agentic AI system that evaluates B2B sales leads and generates personalized outreach messages using a locally hosted LLM.

## Architecture

- Scoring Agent: evaluates lead quality
- Messaging Agent: generates outreach content
- Orchestrator: controls decision flow and thresholds

## Key Features

- Agent separation (decision vs execution)
- Configurable score thresholds
- Explainable decision traces
- Local LLM inference (Ollama + Mistral)
- CSV-driven, testable workflow

## Tech Stack

- Python
- Ollama (Mistral-Instruct)
- Pandas

## How It Works

1. Load leads from CSV
2. Score and prioritize leads
3. Generate outreach for qualified leads
4. Save results with audit trail

## Run

```bash
python outreach_generator.py
```
