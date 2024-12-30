#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server  provided credentials
    connection = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    # Create a cursor object
    cur = connection.cursor()

    # Execute querry to join citiesand state tables
    cur.execute("""SELECT * FROM cities INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")

    # Fetch and display results
    print(", ".join([city[2] for city in cur.fetchall()
                     if city[4] == argv[4]]))
