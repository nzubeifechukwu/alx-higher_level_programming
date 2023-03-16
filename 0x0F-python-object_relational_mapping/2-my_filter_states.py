#!/usr/bin/python3
'''Display all values in states table where name matches the argument'''


import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM states WHERE name="{}" ORDER BY id'.format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
