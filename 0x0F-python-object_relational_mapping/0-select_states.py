#!/usr/bin/python3
"""
 lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get my SQL connection parameters from the command line
    username, password, database = sys.argv[1:4]

    # Create connection object and cursor
    connection = MySQLdb.connect(user=username, passwd=password, db=database)
    # Create a cursor object
    cursor = connection.cursor()

    # Execute query and fetch results
    cursor.execute("SELECT * FROM states")
    # Fetch the results
    results = cursor.fetchall()

    # print results
    for states in results:
        print(states)

    # Close cursor and the database connection
    cursor.close()
    connection.close()
