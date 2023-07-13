# Маргарита Куваева, 6-я когорта - Финальный проект. Инженер по тестированию плюс
import samokat_diplom_request
import data


# метод проверки создания\получения заказа
def test_positive_create_get_order_assert():
    # создаем заказ и получение track заказа
    response = samokat_diplom_request.post_create_order(data.create_new_order_body)
    order_track = response.json()["track"]
    # получаем заказ по track
    response = samokat_diplom_request.get_get_order(order_track)
    # проверки
    assert response.status_code == 200
    assert response.json()["order"]["track"] == order_track
