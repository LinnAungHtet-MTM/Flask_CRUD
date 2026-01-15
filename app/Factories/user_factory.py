from app.Models.User import User

class UserFactory:

    @staticmethod
    def admin():
        user = User(
            email="admin@gmail.com",
            role=True
        )
        user.set_password("admin123")
        return user

    @staticmethod
    def guest():
        user = User(
            email="guest@gmail.com",
            role=False
        )
        user.set_password("guest123")
        return user
