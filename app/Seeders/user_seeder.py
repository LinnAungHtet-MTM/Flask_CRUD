from app.extension import db
from app.Models.User import User
from app.Factories.user_factory import UserFactory

def seed_users() -> bool | None:
    """
    Returns:
        True  -> seeded successfully
        False -> skipped (already exists)
        None  -> error occurred
    """
    if User.query.first():
        return False

    try:
        admin = UserFactory.admin()
        guest = UserFactory.guest()

        db.session.add_all([admin, guest])
        db.session.commit()
        return True

    except Exception as e:
        db.session.rollback()
        raise e
