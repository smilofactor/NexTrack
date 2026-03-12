# NexTrack Contribution Guide

## Project Structure

app.py
Application entry point.
Bootstraps the application, launches a UI interface.
Currently defaults to Streamlit.
Behavior may be modified by using command line switches.


infrastructure/
Adapters to external systems such as databases,
APIs, and network transports.

Framework-specific code belongs here.

This layer isolates NexTrack's core logic from 
external frameworks and storage implementations.

infrastructure/database/
Provides persistence adapters used by the service layer.
Database adapters implement persistence logic for
domain entities and use engines for low-level
datastore access.

Services interact with this layer to store
and retrieve domain entities.
UI must NEVER import infrastructure directly.
Only services should ever have direct access.

infrastructure/database/engines/
Engines provide low-level storage access for
different backends.

SQLite is the default backend.  JSON may be used
for lightweight storage or testing.

(Future)
infrastructure/api


domain/
Defines NexTrack's core business entities and rules.
Therefore no framework code is to ever be used here.

Business rules belong here.

Contains entity definitions and business rules for
concepts such as projects, tasks, and dependencies.
This layer must not depend on database code, UI code,
or external services.

services/
Application workflow layer orchestration code goes here.
In order for services to be used from any interface no 
framework code is to ever be used here.

Business rules belong in domain NOT here.

Orchestrates domain entities and infrastructure adapters.
All database access is to pass through this layer.


tests/
Automated tests for all aspects of the NexTrack project.

tests/unit/
Contains testing packages for NexTrack infrastructure

tests/unit/domain/
Testing NexTrack domain/ packages

tests/unit/services/
Testing NexTrack services/ packages

tests/architecture
Enforces NexTrack project architecture.
Tests to determine if domain is importing internal NexTrack
packages, throwing an error if detected.


ui/
User interface layer.
Framework code may go here.
Currently primary interface is streamlit
cli and other guis will be added later.


## Commit Message Conventions

Format:

<scope>: <description>

Scopes:

arch     architecture changes
docs     documentation updates
domain   domain entities
infra    infrastructure changes
repo     repository setup or configuration
service  service layer logic
state    STATE.md updates
storage  changes related to datastore
test     automated tests
ui       interface layer



## Architecture Principles

• Domain layer must remain framework-independent
• Services orchestrate workflows also remain framework-independent
• Infrastructure implements external adapters
• UI handles presentation only
• Business rules belong only in domain never anywhere else.
• Framework specific code belongs in ui or infrastructure

## Architecture Examples

GOOD:
services/create_task.py
    call domain.Task(...)


BAD (This belongs in domain):
services/create_task.py
    if deadline < today:
        reject task


## Dependency Rules

ui → services → domain
infrastructure → domain
services → infrastructure
domain must not depend on infrastructure or UI


## Flow (to put it another way)

           UI
            ↓
        Services
        ↓      ↓
    Domain   Infrastructure
                   ↓
                Engines


## TDD Layer Order

domain
↓
services
↓
infrastructure


## TDD Rule

Domain + Services → TDD
Infrastructure → add tests after interface stabilizes
UI → minimal testing


## TDD Path

Project entity
Task entity
Task lifecycle
Project contains tasks
TaskService
ProjectService


## AI Rehydrate Context Path

README.md
STATE.md
docs/CONTRIBUTING.md
recent commits (git log, optionally git log --stat)
tree
.gitignore



