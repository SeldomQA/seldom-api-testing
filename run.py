import seldom

if __name__ == '__main__':
    seldom.main(
        path="./test_dir",  # 运行用例目录
        base_url="https://httpbin.org",  # 基础URL地址
        rerun=3,   # 重跑次数
        language="zh-CN"  # 中文报告
    )
