import os
from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///contacts.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
db = SQLAlchemy()    