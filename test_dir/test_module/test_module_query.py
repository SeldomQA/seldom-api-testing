"""
author: bugmaster
data: 2022/05/17
"""
import seldom
from seldom import Seldom
from seldom.utils import genson
from quick_public.user.user_v1 import UserLogin
from quick_public.project.project_v1 import Project
from test_data import UserInfo


class TestModuleQuery(seldom.TestCase):
    """
    测试模块查询
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

    def test_module_query(self):
        """
        模块数据检查
        """
        # 获得项目ID
        project = Project(self.user_token)
        project_id = project.get_project()

        self.url = f"{Seldom.base_url}/api/v1/project/{project_id}/moduleTree/"
        self.get(self.url, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("success", True)

        # 获取模块数据schema
        # schema = genson(self.response["data"][0])
        # print("schema:\n", schema)

        assert_data = {
            "$schema": "http://json-schema.org/schema#",
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "parent_id": {
                    "type": "integer"
                },
                "label": {
                    "type": "string"
                },
                "children": {
                    "type": "array"
                }
            }
        }
        self.assertSchema(assert_data, self.response["data"][0])
