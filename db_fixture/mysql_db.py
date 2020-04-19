# coding=utf8
import pymysql.cursors
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import MySQLConfig


# ======== MySql base operating ===================
class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=MySQLConfig.host,
                                              port=int(MySQLConfig.port),
                                              user=MySQLConfig.user,
                                              password=MySQLConfig.password,
                                              db=MySQLConfig.db_name,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':

    db = DB()
    table_name = "sign_event"
    data = {'id':1,'name':'红米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2016-08-20 00:25:42'}
    table_name2 = "sign_guest"
    data2 = {'realname':'alen','phone':12312341234,'email':'alen@mail.com','sign':0,'event_id':1}

    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
