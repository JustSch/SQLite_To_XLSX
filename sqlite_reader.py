import sqlite3
from openpyxl import Workbook

wb=Workbook()
ws=wb.active
ws.title = "Worksheet Title"

SQL_QUERY="select * from table"

conn = sqlite3.connect('database.db')
c=conn.cursor()

c.execute(SQL_QUERY)

row=c.fetchall()

column_list = []
for column_name in c.description:
    column_list.append(column_name[0])
ws.append(column_list)

for result in row:
    ws.append(list(result))

wb.save("Workbook Title.xlsx")
