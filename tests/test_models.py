from shared.models import Base, User, UserRole


def test_user_role_values():
    assert UserRole.ADMIN == "admin"
    assert UserRole.ANALYSE == "analyse"
    assert UserRole.COACH == "coach"
    assert UserRole.PERFORMANCE == "performance"
    assert UserRole.MANAGEMENT == "management"


def test_user_model_tablename():
    assert User.__tablename__ == "users"


def test_user_model_inherits_base():
    assert issubclass(User, Base)
