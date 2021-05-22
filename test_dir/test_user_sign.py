import seldom
from seldom import file_data


class UserSignTest(seldom.TestCase):
    """ 用户签到 """

    def setUp(self):
        self.user_sign = "/api/user_sign/"

    @file_data("user_sign.xlsx", sheet="Sheet1", line=2)
    def test_user_sign(self, eid, phone, status, msg):
        self.post(self.user_sign, data={"eid": int(eid), "phone": int(phone)})
        self.assertPath("status", int(status))
        self.assertPath("message", msg)

    def test_user_sign_all_null(self):
        """ 参数为空 """
        self.post(self.user_sign, data={"eid": "", "phone": ""})
        self.assertPath("status", 10021)
        self.assertPath("message", "parameter error")


if __name__ == "__main__":
    seldom.main(base_url="http://127.0.0.1:8000", debug=True)

