import allure
import pytest
from methods.user_methods import UserMethods
from data import HTTP_STATUS, ERROR_MESSAGES


class TestUserChange:

    @allure.title("Изменение информации пользователя")
    @allure.description("Проверяем успешное изменение информации пользователя")
    @pytest.mark.parametrize("payload", [
        {"firstName": "UpdatedName"},
        {"lastName": "UpdatedLastName"}])
    def test_user_update_info_true(self, user, payload):
        status_code, login_response = UserMethods.user_login(user)
        token = login_response["accessToken"]
        status_code, response_data = UserMethods.user_update_info(token, payload)
        assert status_code == HTTP_STATUS["OK"] and response_data["success"] is True

    @allure.title("Изменение информации пользователя без авторизации")
    @allure.description("Проверяем изменение информации пользователя без авторизации")
    @pytest.mark.parametrize("payload", [
        {"firstName": "UpdatedName"},
        {"lastName": "UpdatedLastName"},
        {"email": "test@testovich.ez"},])
    def test_user_update_info_unauthorized_false(self, payload):
        status_code, response_data = UserMethods.user_update_info(None, payload)
        assert status_code == HTTP_STATUS["UNAUTHORIZED"] and response_data["message"] == ERROR_MESSAGES["UNAUTHORIZED"]
