import cx-Oracle

import os
os.environ['PATH'] ='E:\\app\OracleHomeUser\\instantclient_18_3'

# Establish connection to the database

con=cx-Oracle.connect("hr","hr","localhost/pdborcl")
print("connected!!!")

con.close()