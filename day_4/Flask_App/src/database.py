



from .models import User
from .dbinit import Base, engine, SessionLocal


def create_database():
    Base.metadata.create_all(bind=engine) # create the database


def get_db():
    db = SessionLocal() # create a new session
    try:
        yield db # yield the session
    finally:
        db.close() # close the session
        

def create_user(name: str, email: str, password: str, admin: bool = False):
    db = next(get_db())
    db_user = User(name=name, email=email, password=password, admin = admin) # create a new user
    db.add(db_user) # add the user to the session
    db.commit() # commit the changes to the database
    db.refresh(db_user) # refresh the user
    return db_user # return the user


def create_admin(name: str, email: str, password: str):
    db = next(get_db())
    db_user = User(name=name, email=email, password=password, admin = True) # create a new user
    db.add(db_user) # add the user to the session
    db.commit() # commit the changes to the database
    db.refresh(db_user) # refresh the user
    return db_user # return the user


def get_admin():
    db = next(get_db())
    return db.query(User).filter_by( admin = True ).first()


def get_user_by_id(user_id: int):
    db = next(get_db())
    return db.query(User).filter(User.id == user_id).first() # get the user with the specified id

def get_user_by_email(email: str):
    db = next(get_db())
    return db.query(User).filter(User.email == email).first() # get the user with the specified email

def get_user_by_name(name: str):
    db = next(get_db())
    return db.query(User).filter(User.name == name).first() # get the user with the specified name

def get_users(db):
    db = next(get_db())
    return db.query(User).all() # get all the users