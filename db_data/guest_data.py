import sys
from seldom.testdata import get_now_time, get_past_time, get_future_time
from seldom.utils import file_dir

sys.path.append(file_dir())
from base import ConnectDB


# create data
datas = {
    'sign_event': [
        {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
         'start_time': get_future_time(), "create_time": get_now_time()},
        {'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '北京会展中心',
         'start_time': get_future_time(), "create_time": get_now_time()},
        {'id': 3, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0, 'address': '北京会展中心',
         'start_time': get_future_time(), "create_time": get_now_time()},
        {'id': 4, 'name': '发布会已结束', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
         'start_time': get_past_time(), "create_time": get_now_time()},
        {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京国家会议中心',
         'start_time': get_future_time(), "create_time": get_now_time()},
    ],
    'sign_guest': [
        {'id': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1,
         "create_time": get_now_time()},
        {'id': 2, 'realname': 'has sign', 'phone': 13511001101, 'email': 'sign@mail.com', 'sign': 1, 'event_id': 1,
         "create_time": get_now_time()},
        {'id': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com', 'sign': 0, 'event_id': 5,
         "create_time": get_now_time()},
    ],
}


# Insert table data
class GuestData(ConnectDB):

    def insert(self):
        self.db.init_table(datas)

    def select(self):
        result = self.db.select_data(table="sign_event", where={'name': '红米Pro发布会'})
        return result

    def delete(self):
        self.db.delete_data(table="sign_event", where={"id": 1})


if __name__ == '__main__':
    GuestData().insert()

