# NexTrack STATE

## Checkpoint
Git Tag: v1-bootstrap


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

## What Is Intentionally Missing
- No test framework configured
- No persistence logic implemented
- No CLI interface implemented
- No CI/CD pipeline configured

## Immediate Next Action
Introduce pytest and create first failing test targeting service layer.


## Post Session Corrections Go here.
