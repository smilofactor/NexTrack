# NexTrack

NexTrack is a local-first project and task management system with optional peer-to-peer synchronization.

## Status

Version: Pre-1. (Active Rebuild)
Stage: Active Development
Goal: MVP
Language: Python


## Architecture

NexTrack follows a layered architecture:

interface
  → services
      → domain
      → infrastructure

Key rule:
The domain layer contains pure business objects and must not depend on services or infrastructure.



## Design Principles

- Local-first data store (SQLite by default)
- Service-layer architecture (all DB access via service boundary)
- Streamlit GUI as default interface
- Optional CLI mode
- Future support for WebRTC synchronization
- AI integration via structured export

## MVP Scope

The MVP is complete when:

- A project can be created.
- Tasks can be created, edited, and marked complete.
- Data persists locally in SQLite.
- All DB interactions go through a defined service layer.
- The app launches via `python app.py` and runs via Streamlit.

## Out of Scope (for MVP)

- Authentication
- Network sync
- AI feedback loop
- Advanced reporting
- Deployment automation

## Running the App

```bash
python app.py
