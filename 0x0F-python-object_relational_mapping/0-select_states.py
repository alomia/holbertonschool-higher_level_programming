#!/usr/bin/python3
"""list all states in database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(
                host="localhost",
                port="3306",
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
