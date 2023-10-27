# Абзаева Александра, 9-ая когорта, 11 спринт

import configuration
import requests

# Шаг 1: Выполнить запрос на создание заказа
create_order_url = configuration.URL_SERVICE + configuration.CREATE_ORDER  # Создание заказа
create_order_payload = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]  # Заполнение данными для создания заказа
}
response = requests.post(create_order_url, json=create_order_payload)

# Проверка успешности создания заказа
if response.status_code != 201:
    print("Ошибка при создании заказа.")
else:
    # Шаг 2: Сохранить номер трека заказа
    order_data = response.json()
    order_track: object = order_data.get("track")

    if not order_track:
        print("Не удалось получить трек заказа после создания.")
    else:
        # Шаг 3: Выполнить запрос на получение заказа по треку
        get_order_url = configuration.URL_SERVICE + configuration.TAKE_ORDER  # URL получения заказа
        response = requests.get(get_order_url)

        # Проверка кода ответа
        if response.status_code != 200:
            print("Ошибка при получении заказа по треку.")
        else:
            print("Тест успешно завершен. Получен заказ по треку.")
            print(order_track)
