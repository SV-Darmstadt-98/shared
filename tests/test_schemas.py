from datetime import datetime

from shared.models.user import UserRole
from shared.schemas import UserCreate, UserRead, UserUpdate


def test_user_create():
    user = UserCreate(
        username="jdoe",
        first_name="John",
        last_name="Doe",
        email="jdoe@example.com",
        password="secret",
        role=UserRole.COACH,
    )
    assert user.username == "jdoe"
    assert user.role == UserRole.COACH


def test_user_read():
    now = datetime.now()
    user = UserRead(
        id=1,
        username="jdoe",
        first_name="John",
        last_name="Doe",
        email="jdoe@example.com",
        role=UserRole.ADMIN,
        is_active=True,
        created_at=now,
        updated_at=now,
    )
    assert user.id == 1
    assert user.is_active is True


def test_user_update_partial():
    update = UserUpdate(first_name="Jane")
    assert update.first_name == "Jane"
    assert update.last_name is None
    assert update.email is None
    assert update.role is None
    assert update.is_active is None
