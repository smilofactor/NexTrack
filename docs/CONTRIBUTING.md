# NexTrack Contribution Guide

## Project Structure

app.py
Application entry point.
Launches UI interface, currently defaults to streamlit.

data/
data/engines
Persistence adapters and storage engines.
SQLite is the default backend.

domain/
Domain entities and core business objects.
These objects represent projects, tasks, and related
concepts independent of persistence or UI concerns.

services/
Application service layer.
Coordinates domain objects and persistence adapters.
All database access must pass through this layer.

tests/
Automated tests for all aspects of the NexTrack project.

ui/
User interface layer.
Currently primary interface is streamlit, cli and other guis will be added later.


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
