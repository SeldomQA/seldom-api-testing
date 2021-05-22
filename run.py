import seldom
from db_data.guest_data import GuestData

if __name__ == "__main__":
    # 初始化数据库
    GuestData().insert()
    # 执行测试用例目录
    seldom.main(path="./test_dir/",
                base_url="http://127.0.0.1:8000",
                title="发布会签到系统",
                description="windows 10")
