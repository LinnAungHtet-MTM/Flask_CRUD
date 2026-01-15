from app.Middlewares.product_permission import product_owner_or_admin
from app.Middlewares.admin_required import admin_required
from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from pydantic import ValidationError
from app.Models.Product import Product
from app.Requests.ProductRequest import CreateProductRequest, UpdateProductRequest

class ProductController:

    @staticmethod
    # @admin_required()
    @jwt_required()
    # Get All Proudcts
    def index():
        current_app.logger.info("GET ALL PRODUCT LIST")
        products = Product.query.all()
        return jsonify({
            "count": len(products),
            "data": [u.data for u in products]
        })

    @staticmethod
    @jwt_required()
    # Create Prodcut
    def store():
        try:
            payload = CreateProductRequest(**request.get_json())
        except ValidationError as e:
            return jsonify(e.errors()), 422

        # product = Product(
        #     name=payload.name,
        #     category=payload.category,
        #     price=payload.price,
        #     description=payload.description
        # )
        user_id = int(get_jwt_identity())
        product = Product(**payload.dict())
        product.user_id = user_id
        product.save()

        return jsonify({"message": "Product created", "product": product.data}), 201

    @staticmethod
    @product_owner_or_admin()
    @jwt_required()
    # Update Product
    def update(product_id):
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"message": "Product not found"}), 404

        try:
            payload = UpdateProductRequest(**request.get_json())
        except ValidationError as e:
            return jsonify(e.errors()), 422

        if payload.name:
            product.name = payload.name
        if payload.category:
            product.category = payload.category
        if payload.price:
            product.price = payload.price
        if payload.description:
            product.description = payload.description
        if payload.in_stock:
            product.in_stock = payload.in_stock

        product.save()
        return jsonify({"message": "Product updated", "product": product.data})

    @staticmethod
    @product_owner_or_admin()
    @jwt_required()
    # Delete Product
    def destroy(product_id):
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"message": "Product not found"}), 404

        product.delete()
        return jsonify({"message": "Product deleted"})
