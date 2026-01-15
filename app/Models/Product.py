from app.extension import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    in_stock = db.Column(db.Boolean, nullable=False, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="products")

    # Save product to database
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Delete product from database
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Serialize product object
    @property
    def data(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "description": self.description,
            "in_stock": self.in_stock,
            "user_id": self.user_id
        }
