from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db' # create a database file called sql_app.db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # connect_args is used to prevent an error when using sqlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create a session object

Base = declarative_base() # create a base class for the models

def create_database():
    Base.metadata.create_all(bind=engine) # create the database

from models import User

def get_db():
    db = SessionLocal() # create a new session
    try:
        yield db # yield the session
    finally:
        db.close() # close the session

def create_user(db, name: str, email: str, password: str):
    db_user = User(name=name, email=email, password=password) # create a new user
    db.add(db_user) # add the user to the session
    db.commit() # commit the changes to the database
    db.refresh(db_user) # refresh the user
    return db_user # return the user


def get_user(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first() # get the user with the specified id