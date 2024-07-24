import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.database_manager import DBManager
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

db_manager = DBManager()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')

    db_manager.init_app(app)

    # Import models to ensure they are registered before creating tables
    from app import models
    
    # Ensure tables are created
    with app.app_context():
        db_manager.base.metadata.create_all(bind=db_manager.engine)

    login_manager.login_view = 'routes.login'
    login_manager.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
