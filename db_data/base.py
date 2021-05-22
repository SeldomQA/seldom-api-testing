from seldom.db_operation import MySQLDB


class ConnectDB(object):

    def __init__(self):
        self.db = MySQLDB(host="127.0.0.1",
                          port="3306",
                          user="root",
                          password="198876",
                          database="guest3")
