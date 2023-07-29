import cx-Oracle

import os
os.environ['PATH'] ='E:\\app\OracleHomeUser\\instantclient_18_3'

# Establish connection to the database

con=cx-Oracle.connect("hr","hr","localhost/pdborcl")

cur = con.cursor()

query1="select * From employees"

cur.execute(query1)

for cols in cur:
    print(cols[0]," ",cols[1]," ",cols[2])

cur.close()
con.commit()
con.close()

print("completed!!!")