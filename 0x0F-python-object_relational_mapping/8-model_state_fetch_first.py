#!/usr/bin/python3
"""
This script prints the first state object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create database  engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create a new session object  which handle database connections
    session_maker = sessionmaker(bind=engine)

    # Create a new session object
    session = session_maker()

    # Query the State table for first state
    state = session.query(State).order_by(State.id).first()

    # Print the State object's id and name, or nothing if state is not found
    print("Nothing" if state is None else f"{state.id}: {state.name}")
