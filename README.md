# seldom-api-testing

介绍： 这是一个基于 [Seldom](https://github.com/SeldomQA/seldom) 测试框架实现的接口自动化项目。


### 被测试系统

http://quick.testpub.cn

> 该项目用于教学，请不要做压测，服务器很垃圾。记得把自己创建的垃圾数据删除。

### 安装

* 安装 seldom

```shell
pip install seldom==3.2.0
```

* 运行测试

```shell
> seldom -p test_dir/
2023-03-21 22:55:06 cache.py | INFO | Clear all cache data

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v3.2.0
-----------------------------------------
                             @itest.info


XTestRunner Running tests...

----------------------------------------------------------------------
user {'username': 'admin', 'password': 'admin123456'}
2023-03-21 22:55:06 request.py | INFO | -------------- Request -----------------[🚀]
2023-03-21 22:55:06 request.py | INFO | [method]: POST      [url]: http://quick.testpub.cn/api/v1/login/
2023-03-21 22:55:06 request.py | DEBUG | [data]:
 {
  "username": "admin",
  "password": "admin123456"
}
2023-03-21 22:55:06 request.py | INFO | -------------- Response ----------------[🛬️]
2023-03-21 22:55:06 request.py | INFO | successful with status 200
2023-03-21 22:55:06 request.py | DEBUG | [type]: json      [time]: 0.38355
2023-03-21 22:55:06 request.py | DEBUG | [response]:
 {
  "success": true,
  "error": {
    "code": "",
    "message": ""
  },
  "data": {
    "Token": "11aa6ac8a881b9166b83ff9fe463a7cf42c5cca2",
    "User": "{\"id\": 1, \"name\": \"admin\"}"
  }
}
2023-03-21 22:55:06 cache.py | INFO | Set cache data: admin = 11aa6ac8a881b9166b83ff9fe463a7cf42c5cca2
...
````

* 测试报告

![](./report.png)


### 目录结构

接口自动化项目，请参考下面的目录结构进行设计。 

```shell
mypro/
.
├── __init__.py
├── run.py   # 运行用例入口文件
├── quick_public  # 封装公共调用
│   ├── __init__.py
│   ├── module
│   │   ├── __init__.py
│   │   └── module_v1.py  # v1 通过版本号减少后续兼容问题
│   ├── project
│   │   ├── __init__.py
│   │   └── project_v1.py
│   └── user
│       ├── __init__.py
│       └── user_v1.py
├── reports   # 测试报告&日志目录
│   ├── 2022_05_18_12_05_04_result.html
│   └── seldom_log.log
├── test_data  # 测试数据目录
│   ├── __init__.py  # 存放通用的测试数据
│   └── json_data.json  # 具体用例的数据驱动文件
└── test_dir   # 测试用例目录
    ├── __init__.py
    ├── test_case   # 按照功能模块划分
    │   ├── __init__.py
    │   ├── test_case_create.py
    │   └── test_case_query.py
    ├── test_module
    │   ├── __init__.py
    │   └── test_module_query.py
    ├── test_project
    │   ├── __init__.py
    │   └── test_project_query.py
    └── test_user
        ├── __init__.py
        └── test_user_abnormal.py
```
