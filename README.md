# DroneDesk

AI-agent powered workshop management for FPV drone repair: triage, parts sourcing, queue ETA.

Course project for Agentic Engineering (SaaS PoC).

## What it does
- **Triage:** an agent classifies the client's request (fault type, urgency, likely parts)
- **Estimate:** time and cost based on historical repairs
- **Parts sourcing:** the agent negotiates with emulated suppliers and picks the best compatible offer
- **Client page:** queue position, ETA, and an explanation whenever the estimate changes

## Stack
Python + FastAPI, Claude API (tool use), PostgreSQL, Next.js, Railway.

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
cp .env.example .env   # fill in ANTHROPIC_API_KEY
cd backend && uvicorn app.main:app --reload
```
Health check: http://localhost:8000/health

## Roadmap
**MVP:** triage, estimation, supplier sourcing, client status page.
**Nice-to-have:** technician assignment, client chat, owner dashboard.
