from app.extension import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Boolean, nullable=False, default=False)

    # Set user hash password
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Check user password
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Check admin role
    def is_admin(self):
        return self.role

    # Save user to database
    def save(self):
        db.session.add(self)
        db.session.commit()
