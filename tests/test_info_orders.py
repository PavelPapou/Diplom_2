import allure
from methods.user_methods import UserMethods
from methods.orders_methods import OrderMethods
from data import HTTP_STATUS, INGREDIENTS, ERROR_MESSAGES

class TestInfoOrders:

    @allure.title("Получение заказа авторизованного пользователя")
    @allure.description("Проверяем получение заказа у пользователя с авторизацией")
    def test_order_get_with_auth_true(self, user):
        status_code, login_response = UserMethods.user_login(user)
        token = login_response["accessToken"]
        payload = INGREDIENTS
        OrderMethods.order_create(payload, token)
        status_code, response_data = OrderMethods.order_get_user(token)
        assert status_code == HTTP_STATUS["OK"] and response_data["success"] is True

    @allure.title("Получение заказа не авторизованного пользователя")
    @allure.description("Проверяем получение заказа у пользователя без авторизации")
    def test_order_get_without_auth_false(self):
        status_code, response_data = OrderMethods.order_get_user()
        assert status_code == HTTP_STATUS["UNAUTHORIZED"]
        assert response_data["message"] == ERROR_MESSAGES["UNAUTHORIZED"]