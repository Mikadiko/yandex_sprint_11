# Ольга Гоголева, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_create_order_200():
    # Записываем в переменную response информацию о заказе по его номеру
    response = sender_stand_request.get_new_order_list()

    #  Проверяется, что код ответа равен 200
    assert response.status_code == 200
