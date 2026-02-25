from sqlalchemy.orm import declarative_base

Base = declarative_base()

from shared.models.user import User, UserRole  # noqa: E402, F401
