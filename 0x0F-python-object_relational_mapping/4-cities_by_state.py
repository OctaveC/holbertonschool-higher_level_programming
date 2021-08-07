#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities"
                " JOIN states ON cities.state_id = states.id")

    for row in cur.fetchall():
        print(row)

    cur.close()
    database.close()
