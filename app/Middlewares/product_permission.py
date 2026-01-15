from functools import wraps
from flask import jsonify
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt,
    get_jwt_identity
)
from app.Models.Product import Product

def product_owner_or_admin():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()

            claims = get_jwt()
            user_id = get_jwt_identity()

            # Admin => allow everything
            if claims.get("is_admin"):
                return fn(*args, **kwargs)

            # Normal user => check ownership
            product_id = kwargs.get("product_id")
            product = Product.query.get(product_id)

            if not product:
                return jsonify({"message": "Product not found"}), 404

            if product.user_id != user_id:
                return jsonify({"message": "Permission Denied!"}), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper
