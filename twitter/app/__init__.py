from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)
    login.init_app(app)

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.posts import posts_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)

    with app.app_context():
        db.create_all()

    return app
