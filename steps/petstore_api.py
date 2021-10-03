import requests

user_data = {
    "id": 10,
    "username": "ivan.andyk",
    "firstName": "Ivan",
    "lastName": "Andyk",
    "email": "test@gmail.com",
    "password": "sdf45SDF45",
    "phone": "123",
    "userStatus": 0
}

params = {
            "username": "ivan.andyk",
            "password": "sdf45SDF45"
        }


class TestSteps:

    @staticmethod
    def get_headers():
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        return headers

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2/user'
        self.headers = self.get_headers()

    def create_user(self, user_data):
        url = self.base_url
        response = requests.request(
            "POST", url, json=user_data)
        output = response.status_code
        assert output == 200, f'{output} not equal 200'
        print("User created")

    def login_user(self, params):
        url = self.base_url + "/login"
        response = requests.request(
            "GET", url, headers=self.headers, params=params)
        output = response.status_code
        assert output == 200, f'{output} not equal 200'
        print("User logged in")

    def get_user_data(self, username):
        url = self.base_url + "/" + username
        response = requests.request(
            "GET", url, headers=self.headers)
        output = response.json()
        assert output == user_data,\
            f"{output} invalid user_data"
        print("User data received")

    def logout_user(self):
        url = self.base_url + "/logout"
        response = requests.request(
            "GET", url, headers=self.headers)
        output = response.status_code
        assert output == 200, f'{output} not equal 200'
        print("User logged out")

    def delete_user(self, username):
        url = self.base_url + "/" + username
        response = requests.request(
            "DELETE", url, headers=self.headers)
        output = response.status_code
        assert output == 200, f'{output} not equal 200'
        print("User deleted")
