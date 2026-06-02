import pymysql
import pandas as pd

def db_connection():
    connection=pymysql.connect(
    host='localhost',
    user='root',
    password='RRRR',
    database='Uber_Eats_db')
    return connection

def run_query(query):
    connection=db_connection()

    df=pd.read_sql(query,connection)

    connection.close()
    return df