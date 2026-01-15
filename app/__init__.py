from flask import Flask
from config.database import DBConfig
from config.jwt import JWTConfig
from app.extension import db, jwt
from flask_migrate import Migrate
from routes.api import api
from routes.auth import auth
from config.logging import file_handler

def create_app():
    app = Flask(__name__)

    # Register file-based logger
    app.logger.addHandler(file_handler)

    # Database & JWT config
    app.config.from_object(DBConfig)
    app.config.from_object(JWTConfig)

    db.init_app(app)
    jwt.init_app(app)
    # Initialize database migration
    Migrate(app, db)

    # Register blueprints
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(api, url_prefix="/api")

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
