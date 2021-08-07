#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table hbtn_0e_0_usa
where name matches the argument
"""
import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3])

    cur = database.cursor()
    cur.execute("SELECT id, name FROM states WHERE name = %s"
                "ORDER by id ASC", (sys.argv[4],))

    for row in cur.fetchall():
        print(row)

    cur.close()
    database.close()
