#!/usr/bin/python3

import MySQLdb
from sys import argv

try:
    conn = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

except MySQLdb.Error as e:
    print(e)
