import pandas as pd
import sqlite3

# df = pd.read_csv('sample.csv')
# df = pd.read_json('sample.json',encoding = "utf-8")
# df = pd.read_excel('sample.xlsx')

df = pd.read_sql_query('select * from sample', sqlite3.connect('sample.db'))
print(df)

