#!/usr/bin/python3
'''
Take in argyment but make it s safe from MySQL injections.
'''
import MySQLdb
from sys import argv


conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                       user=argv[1], passwd=argv[2], db=argv[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name=%s ORDER BY states.id",
            (argv[4], ))
query_rows = cur.fetchall()
for row in query_rows:
        print(row)
cur.close()
conn.close()
