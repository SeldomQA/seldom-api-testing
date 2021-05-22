import seldom


class GetGuestListTest(seldom.TestCase):
    """ 获得嘉宾列表 """

    def start(self):
        self.get_guest_list = "/api/get_guest_list/"

    def test_get_guest_list_eid_null(self):
        """ eid 参数为空 """
        self.get(self.get_guest_list, params={"eid": ""})
        self.assertPath("status", 10021)
        self.assertPath("message", "eid cannot be empty")

    def test_get_event_list_eid_error(self):
        """ 根据 eid 查询结果为空 """
        self.get(self.get_guest_list, params={"eid": 901})
        self.assertPath("status", 10022)
        self.assertPath("message", "query result is empty")

    def test_get_event_list_eid_success(self):
        """ 根据 eid 查询结果成功 """
        self.get(self.get_guest_list, params={"eid": 1})
        self.assertPath("status", 10200)
        self.assertPath("message", "success")
        self.assertPath("data[0].realname", "tom")
        self.assertPath("data[0].phone", "13511001199")

    def test_get_event_list_eid_phone_null(self):
        """ 根据 eid 和phone 查询结果为空 """
        self.get(self.get_guest_list, params={"eid": 1, "phone": "10000000000"})
        self.assertPath("status", 10022)
        self.assertPath("message", "query result is empty")

    def test_get_event_list_eid_phone_success(self):
        """ 根据 eid 和phone 查询结果成功 """
        self.get(self.get_guest_list, params={"eid": 1, "phone": "13511001100"})
        self.assertPath("status", 10200)
        self.assertPath("message", "success")
        self.assertPath("data.realname", "alen")
        self.assertPath("data.phone", "13511001100")


if __name__ == "__main__":
    seldom.main(base_url="http://127.0.0.1:8000", debug=True)
