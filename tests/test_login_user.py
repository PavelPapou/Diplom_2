import allure
from methods.user_methods import UserMethods
from data import HTTP_STATUS, ERROR_MESSAGES


class TestUserLogin:

    @allure.title("Логин пользователя")
    @allure.description("Проверяем успешный логин пользователя")
    def test_user_login_true(self, user):
        status_code, response_data = UserMethods.user_login(user)
        assert status_code == HTTP_STATUS["OK"]
        assert "accessToken" in response_data

    @allure.title("Логин пользователя с неверными данными")
    @allure.description("Проверяем логин пользователя с неверным логином или паролем")
    def test_user_login_false(self):
        with allure.step("Отправляем неверные данные для логина"):
            payload = {"login": "wrong_login", "password": "wrong_password"}
        status_code, response_data = UserMethods.user_login(payload)
        assert status_code == HTTP_STATUS["UNAUTHORIZED"] and response_data["message"] == ERROR_MESSAGES["LOGIN_FAILED"]
    