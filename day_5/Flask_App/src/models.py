from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
# The main thing I had to change to get this to work. I had to create the db object in this module and then import it into the views module.
# I had to do this because if the db object is created in __init__.py, then the db object is created before the app object is created.
# This caused the app object to be None when the db object was created so creating the db object in __init__.py caused an error.
from .dbinit import Base


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name =  Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    admin = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"{self.name}"
    
    def check_password(self, password):
        return self.password == password
    
    def get_id(self):
        return self.id
    
    def is_admin(self):
        return self.admin




