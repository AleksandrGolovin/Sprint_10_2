# Sprint_10_2: доска объявлений DOSKA API testing

## Описание проекта
Проект автоматизации тестирования API для сервиса доски объявлений "DOSKA". Написан на Python с использованием pytest и Allure для отчетности

Отчет о тестировании: https://aleksandrgolovin.github.io/Sprint_10_2/

## Структура проекта
```
project/
├── assets/
│ ├── bread.png
│ └── bread2.jpg
├── tests/
│ ├── test_advert.py
│ └── test_user.py
├── methods/
│ ├── advert_methods.py
│ └── user_methods.py
├── conftest.py
├── helpers.py
├── data.py
└── requirements.txt
```

## Тестовые классы

### TestUser (test_user.py)
- **test_signup_user_unique_email_success** - Регистрация нового пользователя с уникальным email
- **test_signup_user_nonunique_email_failure** - Регистрация с уже существующим email
- **test_signin_registered_user_success** - Авторизация зарегистрированного пользователя

### TestAdvert (test_advert.py)
- **test_create_advert_valid_advert_data_success** - Создание объявления в разных категориях
- **test_remove_advert_valid_advert_id_success** - Удаление объявления
- **test_edit_advert_valid_advert_id_success** - Редактирование своего объявления
- **test_edit_advert_invalid_advert_id_failure** - Попытка редактирования чужого объявления

## Фикстуры
- **auth_user** (conftest.py) - Фикстура для авторизации пользователя и получения токена

## Data и Helpers
- **data.py** - Содержит URL endpoints, тестовые сообщения, данные пользователей и объявлений
- **helpers.py** - Вспомогательные функции (генерация уникальных email)

## Установка зависимостей
```bash
pip install -r requirements.txt
```

Содержание requirements.txt:
```
pytest
requests
allure-pytest
requests-toolbelt
```

## Запуск тестов и генерация отчета Allure
1. Запустите тесты с сохранением результатов для Allure:
```bash
pytest --alluredir=allure-results
```

2. Откройте отчет Allure:
```bash
allure serve allure-results
```
Ссылка на очет: https://aleksandrgolovin.github.io/Sprint_10_2/

## Дополнительная информация
- Для работы с изображениями в тестах используется директория `assets/`
- Все тесты помечены декораторами Allure для детализированной отчетности
- Проект использует параметризованные тесты для проверки разных категорий объявлений
