# pyrequest2

介绍： 这是一个基于 [Seldom](https://github.com/SeldomQA/seldom) 测试框架实现的接口自动化项目。


被测试系统：为 [发布会签到系统](https://github.com/defnngj/guest3) 。

|接口| URL | 请求方式|
|:---|:---|:---|
|添加发布会接口 | http://127.0.0.1:8000/api/add_event/ | POST |
|查询发布会接口 | http://127.0.0.1:8000/api/get_event_list/ | GET |
|添加嘉宾接口 | http://127.0.0.1:8000/api/add_guest/ | POST |
|查询嘉宾接口 | http://127.0.0.1:8000/api/get_guest_list/ | GET |
|嘉宾签到接口 | http://127.0.0.1:8000/api/user_sign/ | GET |

