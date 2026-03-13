# NexTrack STATE

## Checkpoint
Git Tag: v0.1.0-bootstrap
Git Tag: v0.2.0-architecture-baseline


## Runtime & Language
- Primary language: Python 3.9 (venv)
- UI framework: Streamlit (default execution mode)
- CLI mode planned (non-default)
- Currently application launched via: `python app.py`
- Optional launch may be: `streamlit run app.py`

## Architectural Model
- app.py is entry point
- All front-end interaction (Streamlit or CLI) flows through a service layer
- Service layer mediates all datastore communication
- Data engine abstraction layer selects backend at initialization
- All default/'system' settings for NexTrack will default to sqlite
- Supported datastore targets (planned):
  - SQLite (default)
  - JSON (alternative)

## What Exists
- Repository reset
- Python project scaffold
- requirements.txt present
- .gitignore configured for Python environment
- README.md
- This file
- Basic testing scaffolding
- docs/CONTRIBUTING.md

## What Is Intentionally Missing
- No persistence logic implemented
- No CLI interface implemented
- No CI/CD pipeline configured

## Immediate Next Action
Begin domain-level TDD:
1. Project entity
2. Task entity
3. Service layer orchestration

## In Progress
- Basic testing framework
- Following TDD principles
- pytest.ini in project root
  Architecture guardrail test enforcing:
  domain must not import:
- services
- infrastructure
- tests

## Repository Phase
- testing infrastructure (in progress)
- test runner (initialized)
- architecture guardrails (completed)
- Test directories (created)


## Checkpoint Forecasting 
v0.1.0-bootstrap (Established)
v0.2.0-architecture-baseline (Established)
v0.3.0-domain-model
v0.4.0-services-layer
v0.5.0-first-persistence
v0.6.0-api
v0.7.0-ui
v1.0.0-initial-release


## Post Session Corrections Go here.
In the future will install import-linter

