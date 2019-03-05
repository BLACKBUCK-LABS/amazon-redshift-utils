
import pandas as pd

from common.dao.connection.db_connection import DBConnection


class TableInfoRepo:
    def __init__(self):
        self.conn = DBConnection()
        self.engine = self.conn.get_engine()
        self.table = "table_info"

    #def __del__(self):
        #self.conn.close_connection()

    def get_by_activity(self, activity):

        df = pd.read_sql("select * from " + self.table + " where activity = '"+activity+"'", self.engine)
        return df

    def add(self, df):
        return df.to_sql(name=self.table, con=self.engine, if_exists='append', index=False)