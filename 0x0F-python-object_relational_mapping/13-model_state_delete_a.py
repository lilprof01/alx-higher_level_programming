#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter "a"
from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to MySQL database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Create session maker to manage database interactions
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Query all State objects with a name containing "a"
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each State object from the database
    [session.delete(state) for state in states]

    # Commit changes to the database
    session.commit()
