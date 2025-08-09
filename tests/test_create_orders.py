import allure
from methods.user_methods import UserMethods
from methods.orders_methods import OrderMethods
from data import HTTP_STATUS, INGREDIENTS, ERROR_MESSAGES

class TestCreateOrders:

    @allure.title("Создание заказа с авторизацией")
    @allure.description("Проверяем успешное создание заказа с авторизацией")
    def test_order_create_with_auth_true(self, user):
        status_code, login_response = UserMethods.user_login(user)
        token = login_response["accessToken"]
        payload = INGREDIENTS
        status_code, response_data = OrderMethods.order_create(payload, token)
        assert status_code == HTTP_STATUS["OK"] and response_data["success"] is True

    @allure.title("Создание заказа без авторизации")
    @allure.description("Проверяем создание заказа без авторизации")
    def test_order_create_without_auth_false(self):
        payload = {"ingredientIds": ["some_ingredient_id"]}
        status_code, response_data = OrderMethods.order_create(payload)
        assert status_code == HTTP_STATUS["BAD_REQUEST"]

    @allure.title("Создание заказа с ингредиентами")
    @allure.description("Проверяем создание заказа с ингредиентами")
    def test_order_create_with_ingredients_true(self, user):
        payload = INGREDIENTS
        UserMethods.user_login(user)
        status_code, response_data = OrderMethods.order_create(payload)
        assert status_code == HTTP_STATUS["OK"] and response_data["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверяем создание заказа без ингредиентов")
    def test_order_create_without_ingredients_false(self):
        payload = {}
        status_code, response_data = OrderMethods.order_create(payload)
        assert status_code == HTTP_STATUS["BAD_REQUEST"] and response_data["message"] == ERROR_MESSAGES["NO_INGREDIENTS"]

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Проверяем создание заказа с неверным хешем ингредиентов")
    def test_order_create_with_invalid_ingredients_false(self):
        payload = {"ingredientIds": ["invalid_ingredient_id"]}
        status_code, response_data = OrderMethods.order_create(payload)
        assert status_code == HTTP_STATUS["BAD_REQUEST"] and response_data["message"] == ERROR_MESSAGES["NO_INGREDIENTS"]    

