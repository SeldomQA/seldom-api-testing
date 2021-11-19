# seldom-api-testing

介绍： 这是一个基于 [Seldom](https://github.com/SeldomQA/seldom) 测试框架实现的接口自动化项目。

### 安装

```shell
pip install -r requirements.txt
```

### 目录结构

```shell
mypro/
├── db_data/
├── test_dir/
│   ├── test_sample.py
├── test_data/
│   ├── data.json
├── reports/
└── run.py
```

* `db_data/` 数据库配置，以及连接数据库初始化数据。
* `reports/` 测试日志&报告目录。
* `test_data/` 测试参数化数据目录。
* `test_dir/` 测试用例目录。
* `run.py` 运行测试用例主文件。

### 运行

```shell
❯ python .\run.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v2.3.3
-----------------------------------------
                             @itest.info

2021-11-19 21:46:59 [PRINT] generated html file: file:///D:\github\seldom-api-testing\reports\2021_11_19_21_46_58_result.html
2021-11-19 21:46:59 [PRINT] generated log file: file:///D:\github\seldom-api-testing\reports\2021_11_19_21_46_58_log.log
.1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29
```

### 依赖项目

* 被测试系统为

[发布会签到系统](https://github.com/defnngj/guest3) 。

* 测试接口

|接口| URL | 请求方式|
|:---|:---|:---|
|添加发布会接口 | http://127.0.0.1:8000/api/add_event/ | POST |
|查询发布会接口 | http://127.0.0.1:8000/api/get_event_list/ | GET |
|添加嘉宾接口 | http://127.0.0.1:8000/api/add_guest/ | POST |
|查询嘉宾接口 | http://127.0.0.1:8000/api/get_guest_list/ | GET |
|嘉宾签到接口 | http://127.0.0.1:8000/api/user_sign/ | GET |

