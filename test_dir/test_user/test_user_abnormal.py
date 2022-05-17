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
        ("case_user_null", "", "1234", "10010", "用户名密码为空"),
        ("case_pawd_null", "user", "", "10010", "用户名密码为空"),
        ("case_error", "error", "error", "10011", "用户名密码错误"),
    ])
    def test_login(self, _, username, password, code, msg):
        """
        测试用例登录异常
        """
        self.post(self.url, data={"username": username, "password": password})
        self.assertStatusCode(200)
        self.assertPath("error.code", code)
        self.assertPath("error.message", msg)

