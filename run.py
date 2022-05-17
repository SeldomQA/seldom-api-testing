import seldom


if __name__ == "__main__":
    # 执行测试用例目录
    seldom.main(path="./test_dir/",
                base_url="http://quick.testpub.cn",
                title="Quick接口自动化平台",
                tester="虫师",
                # debug=True,
                rerun=2,
                description="windows 11")
