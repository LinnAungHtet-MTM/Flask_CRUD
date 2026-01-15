from flask import request, jsonify
from pydantic import ValidationError
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from app.Requests.AuthRequest import RegisterRequest, LoginRequest
from app.Models.User import User

class AuthController:

    @staticmethod
    # User registration
    def register():
        try:
            payload = RegisterRequest(**request.get_json())
        except ValidationError as e:
            return jsonify(e.errors()), 422

        if User.query.filter_by(email=payload.email).first():
            return jsonify({"message": "Email already exists"}), 409

        user = User(email=payload.email, role=payload.role)
        user.set_password(payload.password)

        user.save()

        return jsonify({"message": "User registered successfully"}), 201

    @staticmethod
    # User Login
    def login():
        try:
            payload = LoginRequest(**request.get_json())
        except ValidationError as e:
            return jsonify(e.errors()), 422

        user = User.query.filter_by(email=payload.email).first()

        if not user or not user.check_password(payload.password):
            return jsonify({"message": "Invalid credentials"}), 401

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "is_admin": user.role
            }
        )
        refresh_token = create_refresh_token(identity=str(user.id))

        return jsonify({
            "message": 'Login Successfully!',
            "access_token": access_token,
            "refresh_token": refresh_token
        }), 200

    @staticmethod
    @jwt_required(refresh=True)
    # Refresh Token
    def refresh():
        user_id = get_jwt_identity()
        new_access = create_access_token(identity=str(user_id))

        return jsonify({"access_token": new_access})
