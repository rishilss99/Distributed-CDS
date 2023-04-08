# Create database models for users
from . import db # Import database
from flask_login import UserMixin # Import UserMixin class which provides default implementations for the methods that Flask-Login expects user objects to have
from sqlalchemy.sql import func # Import func class which provides access to SQL functions

# Create Note class which inherits from db.Model 
# One User can have many Notes, but a single Note can only belong to one User
class Note(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    # user_id column in the Note table is a foreign key that references the id column of the User table.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

# Create User class which inherits from db.Model and UserMixin
# Define schema for database id, email, password, and first name
class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(150), unique=True) 
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')