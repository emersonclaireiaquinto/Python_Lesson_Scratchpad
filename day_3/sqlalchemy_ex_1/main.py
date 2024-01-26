from sqlalchemy.orm import Session

from database import engine, get_db, create_database, create_user, get_user
from models import User

def main():
    create_database() # create the database
    db = next(get_db()) # create a new session

    user = create_user(db, name='John Doe', email='John.Doe@mysite.com', password='password') # create a new user
    print(user.id) # print the user id
    print(user.name) # print the user name
    print(user.email) # print the user email
    print(user.password) # print the user password

    user = get_user(db, user_id=1) # get the user with the id 1
    print(user.id) # print the user id
    print(user.name) # print the user name
    print(user.email) # print the user email
    print(user.password) # print the user password

if __name__ == '__main__':
    main()