from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import User
from .database import *
import os

# this is the database object that we will use to interact with the database
DB_NAME = "PreProd_DB.db"
SECRET_KEY = 'abcd1234'

def make_app():
    # Initialize the app
    app = Flask(__name__)
    app.app_context().push() # this is needed to avoid an error with SQLAlchemy
    # Configure the app
    app.config['SECRET_KEY'] = SECRET_KEY
    
    create_database() # create the database

    # import the views and models
    from .views import views
    
    # register the blueprints
    app.register_blueprint(views, url_prefix='/')
    


    # add the admin user to the database
    admin = get_admin()
    if admin is None:
        create_user(name = 'Admin', email = 'admin@mysite.com', password = 'admin', admin = True)


    # Initialize the login manager
    login_manager = LoginManager() # this is used to manage the user sessions
    login_manager.init_app(app) # what this does is that it creates a session for the user when they login.
    login_manager.login_view = 'views.login' # this is the name of the function that handles the login page

    @login_manager.user_loader # this is a decorator that is used to load the user
    def load_user(id): 
        return get_user_by_id(id) # This query gets the user from the database
    

    return app

