from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy() 
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cfwhbgvrhbfh-hvvrgv' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Create database
    db.init_app(app) # Initialize database

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    return app

def create_database(app):
    # Create database if it doesn't exist using SQLAlchemy
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
