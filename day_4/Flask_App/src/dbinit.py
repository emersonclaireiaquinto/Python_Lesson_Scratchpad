from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db' # create a database file called sql_app.db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # connect_args is used to prevent an error when using sqlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create a session object

Base = declarative_base() # create a base class for the models