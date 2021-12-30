#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

cities_db = []

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

    cur = conn.cursor()
    cur.execute("\
            SELECT cities.name\
            FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = '{}'\
            ".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        cities_db.append(row)

    for count in range(len(cities_db)):
        for index in cities_db[count]:
            print(index, end="")
        if count != len(cities_db) - 1:
            print(', ', end="")
    print()

    cur.close()
    conn.close()
