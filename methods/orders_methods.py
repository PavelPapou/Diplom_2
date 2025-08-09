import requests
import allure
from data import ORDER

class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа")
    def order_create(ingredients, token=None):
        payload = {"ingredients": ingredients}
        headers = {"Authorization": token}
        response = requests.post(ORDER, json=payload, headers=headers)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    
    @staticmethod
    @allure.step("Получение заказа пользователя")
    def order_get_user(token=None):
        order = f"{ORDER}"
        headers = {"Authorization": token} if token else {}
        response = requests.get(order, headers=headers)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response