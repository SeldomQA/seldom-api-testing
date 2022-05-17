"""
author: bugmaster
data: 2022/05/17
"""
import seldom
from seldom import Seldom
from seldom.utils import genson
from seldom.request import ResponseResult
from quick_public.user.user_v1 import UserLogin
from quick_public.project.project_v1 import Project
from quick_public.module.module_v1 import Module
from test_data import UserInfo


class TestCaseQuery(seldom.TestCase):
    """
    测试用例查询
    """

    @classmethod
    def start_class(cls):
        # 获取用户token
        login = UserLogin(UserInfo.user_1)
        cls.user_token = login.get_user_token()

    def start(self):
        self.headers = {
           "token": self.user_token
        }

    def test_case_check(self):
        """
        用例数据检查
        """
        # 获得项目ID
        project = Project(self.user_token)
        project_id = project.get_project()

        # 获得模块ID
        module = Module(self.user_token)
        module_id = module.get_module(project_id)

        # 模块查询接口
        data_ = {"page": 1, "size": 5}
        self.url = f"{Seldom.base_url}/api/v1/module/{module_id}/cases/"

        self.get(self.url, params=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("success", True)

