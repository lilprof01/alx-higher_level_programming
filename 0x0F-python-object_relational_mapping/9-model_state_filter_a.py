#!/usr/bin/python3
"""
This script lists all State objects that contain the
letter a from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine object to connect to the MySQL database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Create a sessionmaker object to create sessions
    session_maker = sessionmaker(bind=engine)

    # Create a session object
    session = session_maker()

    # Query the database for all State objects and
    # print the ones that contain the letter a
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}") if 'a' in state.name else ""
