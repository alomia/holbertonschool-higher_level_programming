#!/usr/bin/python3

import Py
import MySQLdb
from sys import argv

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC;")
        query = cur.fetchall()

        for i in query:
                print(i)

        cur.close()
        consult.close()

