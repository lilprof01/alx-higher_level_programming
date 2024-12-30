#!/usr/bin/python3
"""
This script prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine object to connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Create session maker object to interact with the database
    session_maker = sessionmaker(bind=engine)

    # Create session object to execute database queries
    session = session_maker()

    # Query the database for the state with the provided name
    for state in session.query(State):
        if (state.name == argv[4]):
            # If found, print its ID and exit the loop
            print(state.id)
            break
    else:
        # If not found, print an error message
        print("Not found")
