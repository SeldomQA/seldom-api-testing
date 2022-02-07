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

    @file_data("json_data.json", key="add_event")
    def test_add_event(self, eid, name, limit, address, start_time, status, msg):
        """ 添加发布会-参数化 """
        payload = {'eid': eid, 'name': name, 'limit': limit, 'address': address,
                   'start_time': start_time}
        self.post(self.add_event, data=payload)
        self.assertStatusCode(200)
        self.assertPath("status", status)
        if status == 10024:
            self.assertIn(msg, self.response['message'])
        else:
            self.assertPath("message", msg)


if __name__ == '__main__':
    seldom.main(base_url="http://127.0.0.1:8000", debug=True)
