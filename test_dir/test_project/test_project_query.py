"""
author: bugmaster
data: 2022/05/17
"""
import seldom
from seldom import Seldom, data
from seldom.request import ResponseResult
from quick_public.user.user_v1 import UserLogin
from test_data import UserInfo
from seldom.utils import genson


class TestProjectQuery(seldom.TestCase):
    """
    测试项目查询
    """
    @classmethod
    def start_class(cls):
        login = UserLogin(UserInfo.user_1)
        cls.user_token = login.get_user_token()

    def start(self):
        self.url = f"{Seldom.base_url}/api/v1/project/"

        self.headers = {
           "token": self.user_token
        }

    def test_project_check(self):
        """
        项目数据检查
        """
        data_ = {"page": 1, "size": 6}
        self.get(self.url, params=data_, headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("success", True)

        # 获取接口的数据schema
        # schema = genson(self.response["data"]["projectList"])
        # print("schema:\n", schema)

        ResponseResult.response = self.response["data"]["projectList"]
        assert_data = {
            "$schema": "http://json-schema.org/schema#",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "describe": {
                        "type": "string"
                    },
                    "status": {
                        "type": "boolean"
                    },
                    "create_time": {
                        "type": "string"
                    }
                },
                "required": [
                    "create_time",
                    "describe",
                    "id",
                    "name",
                    "status"
                ]
            }
        }
        self.assertSchema(assert_data)
