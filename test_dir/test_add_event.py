import seldom
from seldom import file_data


class AddEventTest(seldom.TestCase):
    """ 添加发布会 """

    def start(self):
        self.add_event = "/api/add_event/"

    def test_add_event_null(self):
        """ 测试参数为空 """
        payload = {'eid': '', '': '', 'limit': '', 'address': "", 'start_time': ''}
        self.post(self.add_event, data=payload)
        self.assertStatusCode(200)
        self.assertPath("status", 10021)
        self.assertPath("message", 'parameter error')

    @file_data("add_event.json", key="add_event")
    def test_add_event(self, d):
        """ 参数化 """
        payload = {'eid': d['eid'], 'name': d['name'], 'limit': d['limit'], 'address': d["address"],
                   'start_time': d['start_time']}
        self.post(self.add_event, data=payload)
        self.assertStatusCode(200)
        self.assertPath("status", d["status"])
        if d["status"] == 10024:
            self.assertIn(d["msg"], self.response['message'])
        else:
            self.assertPath("message", d["msg"])


if __name__ == '__main__':
    seldom.main(base_url="http://127.0.0.1:8000", debug=True)
