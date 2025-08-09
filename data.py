BASE_URL = "https://stellarburgers.nomoreparties.site/api/"

GET_INGREDIENTS = f"{BASE_URL}ingredients"
ORDER = f"{BASE_URL}orders"
REGISTER = f"{BASE_URL}auth/register"
LOGIN = f"{BASE_URL}auth/login"
TOKEN = f"{BASE_URL}auth/token"
USER = f"{BASE_URL}auth/user"


HTTP_STATUS = {
    "OK": 200,
    "CREATED": 201,
    "BAD_REQUEST": 400,
    "UNAUTHORIZED": 401,
    "FORBIDDEN": 403,
    "NOT_FOUND": 404,
    "CONFLICT": 409,
    "Internal Server Error": 500
}

ERROR_MESSAGES = {
    "USER_EXISTS": "User already exists",
    "REQUIRED_FIELDS": "Email, password and name are required fields",
    "LOGIN_FAILED": "email or password are incorrect",
    "NO_INGREDIENTS": "Ingredient ids must be provided",
    "UNAUTHORIZED": "You should be authorised"
}

INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa70",
    "61c0c5a71d1f82001bdaaa72"
]