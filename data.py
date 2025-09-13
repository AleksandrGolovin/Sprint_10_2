from pathlib import Path


class URLS:

    BASE_URL = r'https://qa-desk.stand.praktikum-services.ru/api'
    SIGNUP_URL = f'{BASE_URL}/signup'
    SIGNIN_URL = f'{BASE_URL}/signin'
    ADD_ADVERT_URL = f'{BASE_URL}/create-listing'
    REMOVE_ADVERT_URL = f'{BASE_URL}/listings'
    EDIT_ADVERT_URL = f'{BASE_URL}/update-offer'

class MESSAGES:
    
    SIGNUP_NONUNIQUE_EMAIL = 'Почта уже используется'
    REMOVE_ADVERT_SUCCESS = 'Объявление удалено успешно'
    EDIT_ADVERT_FAILURE = 'Оффер не найден или у вас нет прав на его редактирование'
        
REGISTERED_USER = {
    'email': 'ya@ne.ya',
    'password': '1111'
}

INVALID_ADVERT_ID = 1

ADVERT = {
    'name': 'Сухарик',
    'category': 'Технологии',
    'condition': 'Новый',
    'city': 'Москва',
    'description': 'Хлеб со степенью прожарки УЛЬТРА',
    'price': '1000',
    'images': ('images', open((Path(__file__).parent / "assets" / "bread.png").resolve(), 'rb'), 'image/png')
}
ADVERT_EDITED = {
    'name': 'Сухарик_edit',
    'category': 'Авто',
    'condition': 'Б/У',
    'city': 'Казань',
    'description': 'Хлеб со степенью прожарки УЛЬТРА и немного тухлый',
    'price': '2000',
    'images': ('images', open((Path(__file__).parent / "assets" / "bread2.jpg").resolve(), 'rb'), 'image/jpg')
}

ADVERT_CATEGORY = ["Авто", "Книги", "Садоводство", "Хобби", "Технологии"]
