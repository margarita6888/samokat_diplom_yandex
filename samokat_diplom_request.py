import configuration
import requests
import data

# метод создания заказа
def post_create_order(body):
    return requests.post(configuration.SERVICE_URL + configuration.CREATE_ORDER_PATH, json=body, headers=data.headers)

# метод получения заказа
def get_get_order(track):
    param={'t': track}
    return requests.get(configuration.SERVICE_URL + configuration.GET_ORDER_BY_TRACK_PATH, params=param, headers=data.headers)
