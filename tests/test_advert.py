import allure
import pytest
from methods.advert_methods import AdvertMethods
from data import ADVERT_CATEGORY, ADVERT, ADVERT_EDITED, INVALID_ADVERT_ID, MESSAGES


@allure.title('Тестирование функциональности объявлений')
class TestAdvert:

    @allure.title("Создание объявления")
    @allure.description('Успешное создание объявления в любой категории')
    @pytest.mark.parametrize('advert_category', ADVERT_CATEGORY)
    def test_create_advert_valid_advert_data_success(self, advert_category, auth_user):
        advert_methods = AdvertMethods()
        auth_token = auth_user
        advert_data = ADVERT
        advert_data['category'] = advert_category
        
        response = advert_methods.create_advert(auth_token, advert_data)
        
        assert response.status_code == 201
        
    @allure.title("Удаление объявления")
    @allure.description('Успешное создание объявления в любой категории')
    def test_remove_advert_valid_advert_id_success(self, auth_user):
        advert_methods = AdvertMethods()
        auth_token = auth_user
        advert_data = ADVERT
        create_response = advert_methods.create_advert(auth_token, advert_data)
        advert_id = create_response.json()["id"]
        
        response = advert_methods.remove_advert(auth_token, advert_id)
        
        assert all(
            [
                response.status_code == 200,
                response.json()['message'] == MESSAGES.REMOVE_ADVERT_SUCCESS
            ]
        )
    
    @allure.title("Редактирование своего объявления")
    @allure.description("Успешное редактирование любого поля объявления")
    def test_edit_advert_valid_advert_id_success(self, auth_user):
        advert_methods = AdvertMethods()
        auth_token = auth_user
        advert_data = ADVERT
        create_response = advert_methods.create_advert(auth_token, advert_data)
        advert_id = create_response.json()["id"]
        
        response = advert_methods.edit_advert(auth_token, advert_id, ADVERT_EDITED)
        
        assert response.status_code == 200
        
    @allure.title("Редактирование чужого объявления")
    @allure.description("Редактирование объявления, созданного не тем пользователем, под токеном которого производится редактирование")
    def test_edit_advert_invalid_advert_id_failure(self, auth_user):
        advert_methods = AdvertMethods()
        auth_token = auth_user
        advert_id = INVALID_ADVERT_ID
        
        response = advert_methods.edit_advert(auth_token, advert_id, ADVERT_EDITED)
        
        assert all(
            [
                response.status_code == 401,
                response.json()['message'] == MESSAGES.EDIT_ADVERT_FAILURE
            ]
        )
