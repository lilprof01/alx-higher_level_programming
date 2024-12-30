#!/usr/bin/python3

""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve arguments
    mysql_username, mysql_password, database_name = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # Create cursor object
    cursor = db.cursor()

    # Define SQL query
    query = """
        SELECT *
        FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY states.id
    """

    # Execute SQL query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
