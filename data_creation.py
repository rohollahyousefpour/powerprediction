import pandas as pd
from pandas.io import sql
import mysql.connector
from sqlalchemy import create_engine

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="82276300",
)
cursor = mydb.cursor()
cursor.execute("create database IF NOT EXISTS Power_Prediction")

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host="localhost", db="Power_Prediction", user="root", pw="82276300"))

con = engine.connect()

df = pd.read_csv("label_power_data.csv")

df.to_sql(con=con, name='Historical_Power_Data',
                if_exists='replace', index=False)