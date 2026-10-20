# DroneDesk

AI-agent powered workshop management for FPV drone repair (course project: Agentic Engineering, SaaS PoC).

## Stack
Backend: Python + FastAPI. Agents: Claude API (tool use). DB: PostgreSQL + SQLAlchemy/Alembic. Frontend: Next.js. Deploy: Railway.

## Layout
- backend/app/agents: triage, estimation, parts-sourcing agents
- backend/app/tools: tools callable by agents
- backend/app/suppliers: mock supplier services
- backend/evals: eval sets for agent quality
- data: synthetic repair history

## MVP
1. Intake + triage (fault type, urgency, likely parts)
2. Time/cost estimate from historical repairs
3. Parts sourcing from mock suppliers (compatibility-aware)
4. Client status page: queue position, ETA, explanation

## Nice-to-have
- Technician assignment by workload
- Agent-led client conversation
- Owner dashboard with natural-language queries

## Conventions
- Queue position and ETA are deterministic code; the agent only explains changes.
- Agent outputs are structured JSON validated by Pydantic.
