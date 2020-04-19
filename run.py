import time
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from db_fixture import test_data


if __name__ == "__main__":
    test_data.init_data()  # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './reports/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='发布会签到系统接口自动化测试',
                            description='运行环境：MySQL(PyMySQL), Requests, unittest ')
    # 指定测试用例为当前文件夹下的 interface 目录
    case = defaultTestLoader.discover('./interface', pattern='*_test.py')
    runner.run(case)
    fp.close()
