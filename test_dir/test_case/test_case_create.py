"""
author: bugmaster
data: 2022/05/18
"""
import seldom
from seldom import Seldom, file_data
from quick_public.user.user_v1 import UserLogin
from quick_public.project.project_v1 import Project
from quick_public.module.module_v1 import Module
from test_data import UserInfo


class TestCaseCreate(seldom.TestCase):
    """
    创建用例
    """

    @classmethod
    def start_class(cls):
        # 获取用户token
        login = UserLogin(UserInfo.user_1)
        cls.user_token = login.get_user_token()
        # 获得项目ID
        project = Project(cls.user_token)
        project_id = project.get_project()
        # 获得模块ID
        module = Module(cls.user_token)
        cls.module_id = module.get_module(project_id)

    def start(self):
        self.url = f"{Seldom.base_url}/api/v1/case/create/"
        self.headers = {
           "token": self.user_token
        }

    @file_data("test_data/json_data.json", key="create_case")
    def test_create_case_abnormal(self, _, req, resp):
        """
        用例创建异常检查
        """
        data_ = {
            "name": req["name"],
            "module_id": self.module_id,
            "method": req["method"],
            "url": req["method"],
            "header": req["header"],
            "params_type": req["params_type"],
            "params_body": req["params_body"],
            "result": req["result"],
            "assert_type": req["assert_type"],
            "assert_text": req["assert_text"]
        }
        self.post(self.url, json=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("error.code", resp["code"])
        self.assertInPath("error.message", resp["message"])

