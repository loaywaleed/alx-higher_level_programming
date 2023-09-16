#!/usr/bin/python3
"""Script that lists all states"""

from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host='localhost', port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
