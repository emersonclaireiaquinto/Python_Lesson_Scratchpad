from src.database import create_user
import pytest


@pytest.mark.usefixtures('database_blank_init')
def test_login_form(client):
    username = 'test_user'
    password = 'test_password'
    email = 'test_email@test.com'
    create_user(name=username, email=email, password=password)
    response = client.post('/login', data=dict(email=email, password=password), follow_redirects=True) # send a post request to the login route
    assert response.status_code == 200 # check that the status code is 200
    print(response.data)
    assert f"Logged in as {username}".encode() in response.data 