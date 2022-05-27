"""
author: bugmaster
data: 2022/05/17
"""
import seldom
from seldom import Seldom, data


class TestLoginAbnormal(seldom.TestCase):
    """
    登录异常
    """

    def start(self):
        self.url = f"{Seldom.base_url}/api/v1/login/"

    @data([
        {"scene": "user_null", "username": "", "password": "1234", "code": "10010", "msg": "用户名密码为空"},
        {"scene": "pawd_null", "username": "user", "password": "", "code": "10010", "msg": "用户名密码为空"},
        {"scene": "error", "username": "error", "password": "error", "code": "10011", "msg": "用户名密码错误"},
    ])
    def test_login(self, _, username, password, code, msg):
        """
        测试用例登录异常
        """
        self.post(self.url, data={"username": username, "password": password})
        self.assertStatusCode(200)
        self.assertPath("error.code", code)
        self.assertPath("error.message", msg)

