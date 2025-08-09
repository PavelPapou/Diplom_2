import pytest
import allure
from methods.user_methods import UserMethods
from helpers import CreateUserData
from data import HTTP_STATUS, ERROR_MESSAGES


class TestUserCreate:

    @allure.title("Cоздания нового пользователя")
    @allure.description("Выполняем создание нового пользователя")
    def test_create_user_true(self):
        payload = CreateUserData.create_user_data()
        status_code, response_data = UserMethods.user_create(payload)
        assert status_code == HTTP_STATUS["OK"] and response_data["success"] is True

    @allure.title("Создание пользователя с уже существующим логином")
    @allure.description("Проверяем создание пользователя с уже существующим логином")
    def test_create_exist_user_false(self):
        payload = CreateUserData.create_user_data()
        UserMethods.user_create(payload)
        status_code, response_data = UserMethods.user_create(payload)
        assert status_code == HTTP_STATUS["FORBIDDEN"] and response_data["message"] == ERROR_MESSAGES["USER_EXISTS"]

    @allure.title("Создание пользователя без обязательных полей")
    @allure.description("Проверяем создание пользователя без обязательных полей (email, password)")
    @pytest.mark.parametrize("payload", [
        {"email": "", "password": "123123", "name": "Testich"},
        {"email": "Test", "password": "", "name": "Testich"}])
    def test_create_user_without_required_fields_false(self, payload):
        status_code, response_data = UserMethods.user_create(payload)
        assert status_code == HTTP_STATUS["FORBIDDEN"] and response_data["message"] == ERROR_MESSAGES["REQUIRED_FIELDS"]