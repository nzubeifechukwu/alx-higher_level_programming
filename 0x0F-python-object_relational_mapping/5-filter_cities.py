#!/usr/bin/python3
'''Takes the name of a state as an argument and lists all cities in the state
'''


import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute('SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id=states.id\
        WHERE states.name=%s ORDER BY cities.id', (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        if row != rows[len(rows) - 1]:
            print(*row, end=', ')
        else:
            print(*row)
    cur.close()
    conn.close()
