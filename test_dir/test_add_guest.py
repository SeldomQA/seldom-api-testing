import seldom
from seldom import file_data


class AddGuessTest(seldom.TestCase):
    """ 添加嘉宾 """

    @file_data("add_guest.json", key="add_guest")
    def test_add_guest(self, _, eid, real_name, phone, status, msg):
        payload = {"eid": eid, "realname": real_name, "phone": phone}
        self.post("/api/add_guest/", data=payload)
        self.assertStatusCode(200)
        self.assertPath("status", status)
        self.assertPath("message", msg)


if __name__ == "__main__":
    seldom.main(base_url="http://127.0.0.1:8000", debug=True)
