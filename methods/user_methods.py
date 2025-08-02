import requests
import allure
from data import REGISTER, USER, LOGIN

class UserMethods:

    @staticmethod
    @allure.step("Создание пользователя")
    def user_create(payload):
        response = requests.post(f"{REGISTER}", json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response

    @staticmethod
    @allure.step("Удаление пользователя")
    def user_delete(token):
        headers = {
            "Authorization": token
            }
        endpoint = f'{USER}'
        response = requests.delete(endpoint, headers=headers)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response    

    @staticmethod
    @allure.step("Логин пользователя")
    def user_login(payload):
        response = requests.post(f"{LOGIN}", json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    

    @staticmethod
    @allure.step('Изменение информации пользователя')
    def user_update_info(token, payload):
        headers = {
            "Authorization": token
            }
        endpoint = f'{USER}'
        response = requests.patch(endpoint, json=payload, headers=headers)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
