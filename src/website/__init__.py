from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() 
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cfwhbgvrhbfh-hvvrgv' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Create database
    db.init_app(app) # Initialize database

    login_manager = LoginManager() 
    login_manager.login_view = 'auth.login' # Redirect to login page if user is not logged in
    login_manager.init_app(app) # Initialize login manager

    @login_manager.user_loader # Decorator which loads user from database
    def load_user(id):
        return User.query.get(int(id))

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    with app.app_context():
        db.create_all()
    
    return app

def create_database(app):
    # Create database if it doesn't exist using SQLAlchemy
    if not path.exists('instance/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
