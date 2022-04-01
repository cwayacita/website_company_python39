from django.apps import AppConfig


class FormConfig(AppConfig):
    name = 'form'


# import sqlite3
# import pandas as pd
#
# db = sqlite3.connect(r'C:\Users\cjulemont\PycharmProjects\Django_project\mysite\db.sqlite3.db')
# table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", db)
# table.to_csv('tasks' + '.csv', index_label='index')
# def to_csv():
#     db = sqlite3.connect(r'C:\Users\cjulemont\PycharmProjects\Django_project\mysite\db.sqlite3')
#     cursor = db.cursor()
#     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     tables = cursor.fetchall()
#     for table_name in tables:
#         table_name = table_name[0]
#         table = pd.read_sql_query("SELECT * from %s" % table_name, db)
#         table.to_csv(table_name + '.csv', index_label='index')
#     cursor.close()
#     db.close()
#
#
# con = sqlite3.connect(r'C:\Users\cjulemont\PycharmProjects\Django_project\mysite\db.sqlite3.db')
# cursor = con.cursor()
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())