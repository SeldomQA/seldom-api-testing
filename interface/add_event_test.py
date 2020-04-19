from base import TestCase
from base import run


class AddEventTest(TestCase):
    ''' 添加发布会 '''

    def setUp(self):
        self.base_url = self.host_url + "/add_event/"

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'eid': '', '': '', 'limit': '', 'address': "", 'start_time': ''}
        r = self.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        ''' id已经存在 '''
        payload = {'eid': 1, 'name': '一加4发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017'}
        r = self.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        ''' 名称已经存在 '''
        payload = {'eid': 11, 'name': '红米Pro发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017'}
        r = self.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        ''' 日期格式错误 '''
        payload = {'eid': 11, 'name': '一加4手机发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017'}
        r = self.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])

    def test_add_event_success(self):
        ''' 添加成功 '''
        payload = {'eid': 11, 'name': '一加4手机发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017-05-10 12:00:00'}
        r = self.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    run()
