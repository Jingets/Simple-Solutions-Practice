# Task-001 — Project Skeleton

## Objective

Create the initial backend skeleton for the Simple Solutions Practice MVP.

This task creates only the project structure.

No business logic.

No database.

No authentication.

No SDK implementation.

No module implementation.

No repositories.

No services.

Only infrastructure.

---

## Technology

Python 3.14

FastAPI

Uvicorn

Pydantic

Project layout must be suitable for modular architecture.

---

## Directory structure

Create:

backend/

    app/
        __init__.py
        main.py

    core/
        __init__.py

    kernel/
        __init__.py

    modules/
        __init__.py

    sdk/
        __init__.py

    tests/
       __init__.py    

frontend/

docker/

scripts/

---

## requirements.txt

Create requirements.txt containing only:

fastapi

uvicorn

pydantic

---

## pyproject.toml

Create minimal valid pyproject.toml.

---

## FastAPI application

Create

backend/app/main.py

Application name:

Simple Solutions Practice

Create endpoint

GET /

Response:

{
    "status": "ok",
    "application": "Simple Solutions Practice"
}

---

## Restrictions

Do NOT create

database

ORM

SQLAlchemy

JWT

Users

Projects

Repositories

Services

Business logic

Configuration system

Logging

Dependency Injection

Docker configuration

CI

SDK implementation

---

## Output format

THIS FORMAT IS MANDATORY.

Return plain text only.

Do not use Markdown.

Do not use triple backticks.

Do not use file trees.

Do not use explanations.

Output every file exactly in the following format:

=== FILE: backend/app/main.py ===
from fastapi import FastAPI

app = FastAPI(title="Simple Solutions Practice")

=== FILE: requirements.txt ===
fastapi
uvicorn
pydantic

If you use Markdown or code fences, your answer is incorrect.