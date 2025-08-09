import random
import string

class CreateUserData:

    @staticmethod
    def create_user_data():
        name = ''.join(random.choices(string.ascii_letters + string.digits, k = random.choice(range(1, 5))))
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = random.choice(range(7, 25))))

        payload = {
            "email": f'{name}@example.com',
            "password": password,
            "name": name
        }
        return payload