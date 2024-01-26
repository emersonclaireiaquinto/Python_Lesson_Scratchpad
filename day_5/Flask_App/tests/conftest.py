import pytest
from src.main import make_app
from src.database import create_database, drop_database, create_user
@pytest.fixture
def app():
    app = make_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.config['WTF_CSRF_ENABLED'] = False
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def database_blank_init():
    create_database()
    yield 
    drop_database()
    
@pytest.fixture
def database_seed_user_init():
    create_database()
    test_user = create_user('test1_username', 'test1_email', 'test1_password')
    yield test_user
    drop_database()
