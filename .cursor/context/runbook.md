# Repository Runbook — isrc-watcher

## Project overview
This repository contains a small FastAPI backend and a frontend client.
The backend exposes an API endpoint for ISRC verification and persistence.

Main directories:
- backend/ : FastAPI application, services, database models
- frontend/ : client application
- tests/ : pytest tests for backend endpoints

---

## Backend execution

Start the backend locally:

uvicorn backend.main:app --reload

The API will be available at:

http://localhost:8000

Example endpoint:

POST /api/isrc/verify

Example request body:

{
  "isrc_code": "ISRC123456"
}

---

## Running tests

Run all tests:

pytest -v

Run a specific test file:

pytest tests/test_isrc.py -v

Tests are designed to avoid connecting to a real PostgreSQL database.
Database calls should be mocked in tests.

---

## Database

The backend uses PostgreSQL via SQLAlchemy async engine and asyncpg.

DATABASE_URL is loaded from the `.env` file.

Example format:

postgresql+asyncpg://user:password@localhost:5432/isrcdb

Tests should not require a live database connection.

---

## Development guidelines

When modifying the codebase:

- Prefer small changes.
- Preserve the existing project structure.
- Do not introduce new frameworks or infrastructure without clear need.
- Ensure tests continue to pass.

---

## Typical development workflow

1. Implement a small change.
2. Run tests with pytest.
3. Verify the endpoint behavior locally.
4. Commit with a clear message.