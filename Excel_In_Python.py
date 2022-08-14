import pandas as pd
import pymysql
import sqlite3
import cryptography

pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

df = pd.read_excel("D:\Chaitanya Kulkarni\Python iNeuron Class\data fsds -20220813T092523Z-001\data fsds\Attribute "
                   "DataSet.xlsx")

conn = sqlite3.connect('mydatabase')

engine = create_engine('mysql://localhost:Password@localhost/mydatabase')

df.to_sql('Exceldata', con=engine, if_exists='append', index=False)