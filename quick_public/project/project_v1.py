from seldom import Seldom
from seldom.request import HttpRequest, check_response


class Project(HttpRequest):

    def __init__(self, user_token):
        self.user_token = user_token

    @check_response("查询项目id", 200, ret="data.projectList[0].id", debug=True)
    def get_project(self):
        """
        获取一条项目数据
        """
        url = f"{Seldom.base_url}/api/v1/project/"

        headers = {
            "token": self.user_token
        }

        data_ = {"page": 1, "size": 6}
        r = self.get(url, params=data_, headers=headers)
        return r
