# Олег Новиков, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import api_requests


# Функция создания заказа и получения его трека
def get_track():
    # В переменную response сохраняется результат запроса на создание заказа
    response = api_requests.create_order()
    # Если заказ успешно создан, то функция возвращает его трек
    if response.status_code == 201:
        return response.json()["track"]
    # Если заказ не был создан, то функция выдаёт сообщение об ошибке
    else:
        print(f"Ошибка создания заказа: {response.status_code}")


# Функция получения заказа по его треку
def test_get_order_by_track():
    # В переменную track сохраняется трек заказа
    track = get_track()
    # В переменную response сохраняется результат запроса на получение данных о заказе по его треку
    response = api_requests.get_order(track)

    # Проверяется, что код ответа равен 200
    assert response.status_code == 200
