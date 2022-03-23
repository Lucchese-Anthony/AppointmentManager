#!/usr/bin/python 

# https://www.tutorialspoint.com/sqlite/sqlite_python.htm

# inserting correct date:
# https://stackoverflow.com/questions/46312391/insert-date-value-in-sql-table

import sqlite3
import pynput
import time

class hostQueue:

    def beginConnection():
        conn = sqlite3.connect('appointments.db')
        print("Opened database successfully")
        while(True):
            time.sleep(20)
            cursor = conn.execute("SELECT id, name, address, salary from COMPANY")


for row in cursor:
    print(f"ID = {row[0]}")
    print(f"NAME = {row[1]}")
    print(f"ADDRESS = {row[2]}")
    print(f"SALARY = {row[3]}\n")

print("Operation done successfully")
conn.close()



