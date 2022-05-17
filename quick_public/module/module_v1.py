from seldom import Seldom
from seldom.request import HttpRequest, check_response


class Module(HttpRequest):

    def __init__(self, user_token):
        self.user_token = user_token

    @check_response("查询模块ID", 200, ret="data[0].id", debug=True)
    def get_module(self, project_id: int = None):
        """
        获取一条模块数据
        :param project_id: 项目id
        """
        if project_id is None:
            raise ValueError("项目id 不能为空")

        url = f"{Seldom.base_url}/api/v1/project/{project_id}/moduleTree/"

        headers = {
            "token": self.user_token
        }

        r = self.get(url, headers=headers)
        return r
