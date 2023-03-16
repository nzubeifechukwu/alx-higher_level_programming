#!/usr/bin/python3
# Lists all states from a country database

import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()

