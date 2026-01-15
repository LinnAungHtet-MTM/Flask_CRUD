from flask import Blueprint
from app.Controllers.ProductController import ProductController

# API blueprint
api = Blueprint("api", __name__)

api.get("/products")(ProductController.index)
api.post("/products")(ProductController.store)
api.put("/products/<int:product_id>")(ProductController.update)
api.delete("/products/<int:product_id>")(ProductController.destroy)
