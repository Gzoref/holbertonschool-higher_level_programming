#!/usr/bin/python3
'''
Lists all states with a name starting with N
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

        conn = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
                if row[1].startswith('N'):
                        print(row)
        cur.close()
        conn.close()
