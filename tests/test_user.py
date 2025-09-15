import allure
from methods.user_methods import UserMethods
from helpers import generate_unique_email
from data import MESSAGES, REGISTERED_USER


@allure.title('Тестирование функциональности пользователя')
class TestUser:

    @allure.title("Регистрация нового пользователя с уникальным email")
    @allure.description('Успешная регистрация нового пользователя с уникальным email (генерировать новый email для каждого теста регистрации обязательно)')
    def test_signup_user_unique_email_success(self):
        user_methods = UserMethods()
        email = generate_unique_email()
        password = '1111'
        
        response = user_methods.signup_user(email, password)
        
        assert response.status_code == 201

    @allure.title("Регистрация нового пользователя с неуникальным email")
    @allure.description('Повторная регистрация пользователя (используется email который уже есть в БД)')
    def test_signup_user_nonunique_email_failure(self):
        user_methods = UserMethods()
        email = REGISTERED_USER['email']
        password = '1111'
        
        response = user_methods.signup_user(email, password)
        
        assert all(
            [
                response.status_code == 400,
                response.json()['message'] == MESSAGES.SIGNUP_NONUNIQUE_EMAIL
            ]
        )
    
    @allure.title("Авторизация зарегистрированного пользователя")
    @allure.description('Успешная авторизация ранее зарегистрированного пользователя')
    def test_signin_registered_user_success(self):
        user_methods = UserMethods()
        email = REGISTERED_USER['email']
        password = REGISTERED_USER['password']
        
        response = user_methods.signin_user(email, password)
        
        assert response.status_code == 201
