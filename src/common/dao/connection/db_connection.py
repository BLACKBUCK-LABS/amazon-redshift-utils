from common.config.config import *
from sqlalchemy import create_engine



class DBConnection:
    def __init__(self):

        #self.conn = MySQLdb.connect(host=DB_HOST, passwd = DB_PASSWORD, port=DB_PORT, user=DB_USER, database=DB_NAME)
        self.engine = create_engine('mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME, echo=False)

    def get_cursor(self):
        return self.conn.cursor()

    def close_connection(self):
        self.conn.commit()
        self.conn.close()

    def get_engine(self):
        return self.engine