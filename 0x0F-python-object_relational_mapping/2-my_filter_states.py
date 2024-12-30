#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server with provided credentials
    db = MySQLdb.connect(user=argv[1], port=3306, host="localhost",
                         passwd=argv[2], db=argv[3])

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query to get all states with the provided state name
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))

    # Fetch all states
    states = cur.fetchall()

    # Display results
    for state in states:
        if state[1] == argv[4]:
            print(state)

    # Close cursor and database connection
    cur.close()
    db.close()
