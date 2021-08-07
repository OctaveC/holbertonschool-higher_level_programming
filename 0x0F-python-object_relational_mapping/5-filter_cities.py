#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name FROM cities"
                " JOIN states ON cities.state_id = states.id"
                " WHERE states.name LIKE %s", (sys.argv[4],))

    full_string = ""
    for row in cur.fetchall():
        full_string += row[0] + ", "

    print(full_string[:-2])

    cur.close()
    database.close()
