# Shared

[![CI](https://github.com/SV-Darmstadt-98/shared/actions/workflows/ci.yml/badge.svg)](https://github.com/SV-Darmstadt-98/shared/actions/workflows/ci.yml)

Shared Pydantic schemas and SQLAlchemy models for the Soccer Club Analytics Platform.

Consumed by `api`, `database`, and `etl` as a git submodule.

## Structure

```
src/shared/
├── models/      # SQLAlchemy table definitions
└── schemas/     # Pydantic request/response schemas
```
