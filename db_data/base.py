from seldom.db_operation import MySQLDB, SQLiteDB


class ConnectDB(object):

    def __init__(self):
        # mysql
        self.db = MySQLDB(host="127.0.0.1",
                          port="3306",
                          user="root",
                          password="198876",
                          database="guest3")
        # sqlite3
        # self.db = SQLiteDB(r"D:\learnAPI\db.sqlite3")
