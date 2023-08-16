import requests
import config
import data


# Функция запроса на создание заказа
def create_order():
    # Составление URL запроса
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH, headers=data.headers, json=data.body)


# Функция запроса на получение данных о заказе по его треку
def get_order(track):
    # Составление URL запроса
    return requests.get(config.URL_SERVICE + config.GET_ORDER_PATH + str(track))
