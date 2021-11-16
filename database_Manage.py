import pandas as pd
from pandas.io import sql
import mysql.connector
from sqlalchemy import create_engine

config = {
    "host": "localhost",
    "user": "root",
    "password": "82276300",
}
class my_SQL:
    def __init__(self, st):
        self.st = st
        self.db = mysql.connector.connect(**config)
        self.cursor = self.db.cursor()
        self.cursor.execute("create database IF NOT EXISTS Power_Prediction")
        config['database'] = "Power_Prediction"

        self.con = mysql.connector.connect(**config)
        self.cursor = self.con.cursor()

    def check_table(self):
        stmt = "SHOW TABLES LIKE 'Historical_Power_Data'"
        self.cursor.execute(stmt)
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

    def creat_historical_tabel(self, file_path):
        try:
            engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                                   .format(host="localhost", db="Power_Prediction", user="root", pw="82276300"))

            con = engine.connect()

            df = pd.read_csv(file_path)

            df.to_sql(con=con, name='Historical_Power_Data',
                      if_exists='replace', index=False)

            return None

        except (mysql.connector.Error, ValueError) as err:

            return err

