#!/usr/bin/python3
"""Script that lists all states"""

from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host='localhost', port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM states\
                   INNER JOIN cities ON states.id = cities.state_id\
                   WHERE states.name = %s\
                   ORDER BY cities.id ASC", [argv[4]])

    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()
