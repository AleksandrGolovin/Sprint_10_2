from data import URLS
import requests
from requests_toolbelt import MultipartEncoder
import allure

class AdvertMethods:

    @allure.step('Создание объявления')
    def create_advert(self, auth_token, advert_data):
        me_payload = MultipartEncoder(advert_data)
        response = requests.post(
            url = URLS.ADD_ADVERT_URL, 
            data = me_payload, 
            headers = {'Authorization': auth_token,'Content-Type': me_payload.content_type}
        )
        return response

    @allure.step('Удаление объявления')
    def remove_advert(self, auth_token, advert_id):
        response = requests.delete(
            url = f'{URLS.REMOVE_ADVERT_URL}/{advert_id}', 
            headers = {'Authorization': auth_token}
        )
        return  response
    
    @allure.step('Редактирование объявления')
    def edit_advert(self, auth_token, advert_id, edited_advert_data):
        me_payload = MultipartEncoder(edited_advert_data)
        response = requests.patch(
            url=f'{URLS.EDIT_ADVERT_URL}/{advert_id}',
            data = me_payload, 
            headers = {'Authorization': auth_token,'Content-Type': me_payload.content_type}
        )
        return response
