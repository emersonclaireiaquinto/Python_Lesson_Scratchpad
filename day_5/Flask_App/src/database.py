



from .models import User
from .dbinit import Base, engine, SessionLocal


def create_database():
    Base.metadata.create_all(bind=engine) # create the database

def drop_database():
    Base.metadata.drop_all(bind=engine) # drop the database

def get_db():
    db_session = SessionLocal() # create a new session
    try:
        yield db_session # yield the session
    finally:
        db_session.close() # close the session
        

def create_user(name: str, email: str, password: str, admin: bool = False):
    db_session = next(get_db())
    db_user = User(name=name, email=email, password=password, admin = admin) # create a new user
    db_session.add(db_user) # add the user to the session
    db_session.commit() # commit the changes to the database
    db_session.refresh(db_user) # refresh the user
    return db_user # return the user


def create_admin(name: str, email: str, password: str):
    db_session = next(get_db())
    db_user = User(name=name, email=email, password=password, admin = True) # create a new user
    db_session.add(db_user) # add the user to the session
    db_session.commit() # commit the changes to the database
    db_session.refresh(db_user) # refresh the user
    return db_user # return the user


def get_admin():
    db_session = next(get_db())
    return db_session.query(User).filter_by( admin = True ).first()


def get_user_by_id(user_id: int):
    db_session= next(get_db())
    return db_session.query(User).filter(User.id == user_id).first() # get the user with the specified id

def get_user_by_email(email: str):
    db_session= next(get_db())
    return db_session.query(User).filter(User.email == email).first() # get the user with the specified email

def get_user_by_name(name: str):
    db_session= next(get_db())
    return db_session.query(User).filter(User.name == name).first() # get the user with the specified name

def get_users(db):
    db_session= next(get_db())
    return db_session.query(User).all() # get all the users