# Release Process

## Semantic Versioning

This project follows [Semantic Versioning 2.0.0](https://semver.org/).

**Format:** `vMAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (e.g., removing/renaming models, changing field types)
- **MINOR**: New features (e.g., adding new models, adding optional fields)
- **PATCH**: Bug fixes (e.g., fixing validation logic, documentation updates)

## When to Bump Versions

### MAJOR (v1.0.0 → v2.0.0)
- Removing or renaming SQLAlchemy models
- Removing or renaming model fields
- Changing field types in breaking ways
- Changing Pydantic schema validation rules

### MINOR (v1.0.0 → v1.1.0)
- Adding new SQLAlchemy models
- Adding new optional fields to existing models
- Adding new Pydantic schemas
- Adding new utility functions

### PATCH (v1.0.0 → v1.0.1)
- Fixing bugs in validation logic
- Documentation updates
- Code formatting/linting fixes
- Test improvements

## Release Steps

1. **Update version in pyproject.toml**
   bash
  # Edit pyproject.toml
  version = "1.2.3"


2. **Run tests**
   bash
  uv run pytest


3. **Commit changes**
   bash
  git add .
  git commit -m "chore: bump version to v1.2.3"


4. **Create git tag**
   bash
  git tag v1.2.3


5. **Push with tags**
   bash
  git push origin main --tags


6. **Update dependent services**

   After releasing, update the version in dependent services (api, etl, database):
   toml
  # In their pyproject.toml
  dependencies = [
      "shared @ git+https://github.com/SV-Darmstadt-98/shared.git@v1.2.3",
  ]


## Current Version

See pyproject.toml for the current version.