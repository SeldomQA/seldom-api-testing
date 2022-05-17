from seldom import Seldom
from seldom.request import HttpRequest, check_response


class UserLogin(HttpRequest):

    def __init__(self, user):
        print("user", user)
        self.username = user.get("username")
        self.password = user.get("password")

    @check_response("获取用户token", 200, ret="data.Token")
    def get_user_token(self):
        """
        获取用户token
        """
        url = f"{Seldom.base_url}/api/v1/login/"
        r = self.post(url, data={"username": self.username, "password": self.password})
        return r
