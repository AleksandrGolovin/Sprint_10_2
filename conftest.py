import pytest
import helpers
from methods.user_methods import UserMethods
from data import REGISTERED_USER


@pytest.fixture
def auth_user():
    user_methods = UserMethods()
    signin_response = user_methods.signin_user(REGISTERED_USER['email'], REGISTERED_USER['password'])
    if signin_response.status_code == 201:
        yield f'Bearer {signin_response.json()['token']['access_token']}'
    else:
        raise Exception('Что-то пошло не так, проверьте параметры запроса')
