from seldom.request import check_response
from seldom.request import HttpRequest


class UserApiObject(HttpRequest):

    @check_response(
        describe="获取登录用户名",
        status_code=200,
        ret="form",
        check={"headers.Host": "httpbin.org"},
        debug=True
    )
    def user_account_login(self, username, password):
        """
        调用接口获得用户名
        :param username:
        :param password:
        """
        json_data = {"username": username, "password": password}
        r = self.post("http://httpbin.org/post", data=json_data)
        return r


if __name__ == '__main__':
    c = UserApiObject()
    c.user_account_login()
