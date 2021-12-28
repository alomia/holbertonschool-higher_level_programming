#!/usr/bin/python3

import MySQLdb
from sys import argv

conn = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    passwd=argv[2],
    db="hbtn_0e_0_usa"
    )

cur = conn.cursor()
cur.execute("SELECT * FROM states")

rows = cur.fetchall()

for row in rows:
    print(row)
