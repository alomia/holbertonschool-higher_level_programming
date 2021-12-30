#!/usr/bin/python3
"""
takes an argument and displays all values in the hbtn_0e_0_usa
state table whose name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

    cur = conn.cursor()
    cur.execute(
            "SELECT *\
            FROM states\
            WHERE BINARY name = '{}'\
            ORDER BY states.id".format(argv[4])
        )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
