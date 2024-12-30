#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server with provided credentials
    connection = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    # Create cursor object
    cur = connection.cursor()

    # Execute SQL query to get all cities with corresponding state names
    cur.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities JOIN states ON cities.state_id = states.id
                    ORDER BY cities.id ASC""")

    # Fetch all results and print them using a list comprehension
    [print(city) for city in cur.fetchall()]
