# pyrequest2

介绍：
  发布会签到系统：http://github.com/defnngj/guest3

  它包含功能:
  * 测试数据初始化，并对数据的插入做了封装。
  * unittest单元测试框架运行测试
  * HTMLTestRunner生成接口测试报告


Python版本与依赖库：
  * python3.5+ :https://www.python.org/
  * seldom: https://github.com/SeldomQA/seldom
  * PyMySQL: https://github.com/PyMySQL/PyMySQL


```MySQL
// MySQL初始化
ALTER TABLE  `sign_event` CHANGE  `create_time`  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
ALTER TABLE  `sign_guest` CHANGE  `create_time`  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
```
