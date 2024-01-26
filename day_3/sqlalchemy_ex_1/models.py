from sqlalchemy import Column, Integer, String

from database import Base

class User(Base):
    __tablename__ = 'users' # set the table name
    
    id = Column(Integer, primary_key=True, index=True) # set the id column, primary_key=True means that the id column is the primary key, index=True means that the id column is indexed
    name = Column(String, unique=True, index=True) # set the name column, unique=True means that the name column is unique so there can't be two users with the same name.
    email = Column(String, unique=True, index=True) # set the email column
    password = Column(String) # set the password column