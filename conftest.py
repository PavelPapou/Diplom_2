import pytest
from methods.user_methods import UserMethods
from helpers import CreateUserData


@pytest.fixture
def user():
    payload = CreateUserData.create_user_data()
    UserMethods.user_create(payload)
    yield payload
    status_code, response_data = UserMethods.user_login(payload)
    token = response_data["accessToken"]
    UserMethods.user_delete(token)
