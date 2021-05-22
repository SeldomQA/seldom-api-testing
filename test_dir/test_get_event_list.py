import seldom
from seldom import data


class GetEventListTest(seldom.TestCase):
    """ 获得发布会列表 """

    def start(self):
        self.get_event_list = "/api/get_event_list/"

    @data([
        ("查询结果为空", 901, 10022, "query result is empty"),
        ("查询结果成功", 1, 10200, "success"),
    ])
    def test_get_by_eid(self, _, eid, status, msg):
        self.get(self.get_event_list, params={"eid": eid})
        self.assertStatusCode(200)
        self.assertPath("status", status)
        self.assertPath("message", msg)
        if status == 10200:
            self.assertPath("data.name", "红米Pro发布会")
            self.assertPath("data.address", "北京会展中心")

    @data([
        ("关键字‘abc’查询", "abc", 10022, "query result is empty"),
        ("关键字‘发布会’模糊查询", "发布会", 10200, "success"),
    ])
    def test_get_by_name(self, _, eid, status, msg):
        self.get(self.get_event_list, params={"name": eid})
        self.assertStatusCode(200)
        self.assertPath("status", status)
        self.assertPath("message", msg)
        if status == 10200:
            self.assertPath("data[0].name", "红米Pro发布会")
            self.assertPath("data[0].address", "北京会展中心")


if __name__ == "__main__":
    seldom.main(base_url="http://127.0.0.1:8000", debug=True)
