from petstore_api import TestSteps


params = {
            "username": "ivan.andyk",
            "password": "sdf45SDF45"
        }


def test_3():
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
    user = TestSteps()
    user.get_headers()
    user.create_user(user_data)
    user.login_user(params)
    user.get_user_data(user_data["username"])
    user.logout_user()
    user.delete_user(user_data["username"])
