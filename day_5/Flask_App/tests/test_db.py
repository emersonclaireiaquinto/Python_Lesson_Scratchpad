import src.database as db
import pytest

@pytest.mark.usefixtures('database_blank_init')
def test_db_create_user():
    user = db.create_user('test', 'test', 'test')
    assert user.name == 'test'
    assert user.email == 'test'
    assert user.password == 'test'
    

def test_db_get_user_by_id(database_seed_user_init):
    assert db.get_user_by_id(database_seed_user_init.id) == database_seed_user_init
    


def test_db_get_user_by_email(database_seed_user_init):
    assert db.get_user_by_email(database_seed_user_init.email) == database_seed_user_init
