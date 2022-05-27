from seldom import Seldom
from seldom.utils import cache
from seldom.request import HttpRequest


class UserLogin(HttpRequest):

    def __init__(self, user):
        print("user", user)
        self.username = user.get("username")
        self.password = user.get("password")

    def get_user_token(self):
        """
        获取用户token
        """
        # 如果用户已登录过，直接返回token
        user_token = cache.get(self.username)
        if user_token is not None:
            return user_token

        url = f"{Seldom.base_url}/api/v1/login/"
        r = self.post(url, data={"username": self.username, "password": self.password})
        user_token = r.json()["data"]["Token"]
        # 将用户token 写到 cache
        cache.set({self.username: user_token})
        return user_token
