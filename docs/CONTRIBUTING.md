# NexTrack Contribution Guide

## Project Structure

app.py
Application entry point.
Launches UI interface, currently defaults to streamlit.

infrastructure/
Contains adapters for external systems such as
databases, APIs, and network transports.

infrastructure/database/
Database adapters are the entry point for storage access
services go through here.

infrastructure/database/engines
Database adapters will access the engines using tasks.
Engines will provide access to JSON and SQLite.
SQLite is the default backend.

domain/
Core business model of NexTrack.
Contains entity definitions and business rules for
concepts such as projects, tasks, and dependencies.
This layer must not depend on database code, UI code,
or external services.

services/
Coordinates domain objects and persistence adapters.
All database access must pass through this layer.

tests/
Automated tests for all aspects of the NexTrack project.

ui/
User interface layer.
Currently primary interface is streamlit
cli and other guis will be added later.


## Commit Message Conventions

Format:

<scope>: <description>

Scopes:

arch     architecture changes
data     persistence adapters
docs     documentation updates
domain   domain entities
repo     repository setup or configuration
service  service layer logic
state    STATE.md updates
test     automated tests
ui       interface layer


## AI rehydrate context path

README.md
STATE.md
docs/CONTRIBUTING.md
recent commits (git log, optionally git log --stat)
