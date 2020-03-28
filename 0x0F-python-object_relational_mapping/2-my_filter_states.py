#!/usr/bin/python3
'''
Takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
        conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                               user=argv[1], passwd=argv[2], db=argv[3])
        cur = conn.cursor()
        cur.execute("SELECT * FROM states\
                     WHERE name='{}' ORDER BY states.id ASC"
                    .format(argv[4]))
        query_rows = cur.fetchall()
        for row in query_rows:
                print(row)
        cur.close()
        conn.close()
