from seldom.request import check_response
from seldom.request import HttpRequest


class Common(HttpRequest):

    @check_response(
        describe="获取登录用户名",
        status_code=200,
        ret="headers.Account",
        check={"headers.Host": "httpbin.org"},
        debug=True
    )
    def get_login_user(self):
        """
        调用接口获得用户名
        """
        headers = {"Account": "bugmaster"}
        r = self.get("http://httpbin.org/get", headers=headers)
        return r


if __name__ == '__main__':
    c = Common()
    c.get_login_user()
