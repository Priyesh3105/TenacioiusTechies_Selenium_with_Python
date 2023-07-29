import cx-Oracle

import os
os.environ['PATH'] ='E:\\app\OracleHomeUser\\instantclient_18_3'

# Establish connection to the database

con=cx-Oracle.connect("hr","hr","localhost/pdborcl")

cur = con.cursor()

query1="insert into student values(102,'JOHN')"
cur.execute(query1)
query2="update student set sname='XYZ' where sid=102"
cur.execute(query2)
query3="delete student where sid=102"
cur.execute(query3)

cur.close()
con.commit()
con.close()

print("completed!!!")