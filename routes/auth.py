from flask import Blueprint
from app.Controllers.AuthController import AuthController

# Auth blueprint
auth = Blueprint("auth", __name__)

auth.post("/register")(AuthController.register)
auth.post("/login")(AuthController.login)
auth.post("/refresh")(AuthController.refresh)