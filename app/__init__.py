import  os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app.database_manager import DBManager

db_manager = DBManager()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']

    db_manager.init_app(app)

    login_manager.login_view = 'routes.login'
    login_manager.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app