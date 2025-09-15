import requests
import allure
from data import URLS

class UserMethods:
    timeout = 10
    
    @allure.step('Создание нового пользователя')
    def signup_user(self, email, password):
        payload = {
            "email": email,
            "password": password,
            "submitPassword": password
        }
        response = requests.post(
            url=URLS.SIGNUP_URL,
            data=payload,
            timeout=self.timeout
        )
        return response

    @allure.step('Авторизация пользователя')
    def signin_user(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(
            url=URLS.SIGNIN_URL,
            data=payload,
            timeout=self.timeout
        )
        return response
