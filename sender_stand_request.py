import configuration
import requests
import data


# Функция создания нового заказа.
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body)  # тело запроса


# Сохраняем номер трекера заказа
def get_new_order():
    order = post_new_order(data.create_order_body).json()["track"]
    return order


# Получение заказа по его номеру
def get_new_order_list():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK_PATH + "?t=" + str(get_new_order()))
