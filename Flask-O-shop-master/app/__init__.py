import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv
from .config import Config

# Initialize extensions
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

def create_app():
    # Load environment variables
    load_dotenv()
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize Flask extensions
    Bootstrap(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    
    # Register Blueprints
    from app.admin.routes import admin
    app.register_blueprint(admin)
    
    with app.app_context():
        db.create_all()
    
    # User loader callback for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .db_models import User
        return User.query.get(user_id)
    
    # Inject current datetime to templates
    @app.context_processor
    def inject_now():
        from datetime import datetime
        return {'now': datetime.utcnow()}
    
    # Import and register routes
    from . import routes
    
    return app
