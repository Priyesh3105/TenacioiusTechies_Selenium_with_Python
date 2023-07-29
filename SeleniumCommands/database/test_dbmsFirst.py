import cx-Oracle

import os
os.environ['PATH'] ='E:\\app\OracleHomeUser\\instantclient_18_3'

# Establish connection to the database

con=cx-Oracle.connect("hr","hr","localhost/pdborcl")

cur = con.cursor()

cur.execute("insert into student values(102,'JOHN')")

cur.close()
con.commit()
con.close()

print("completed!!!")