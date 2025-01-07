#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to MySQL server with provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Create session object
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Query the database for the State object with id=2
    state = session.query(State).filter_by(id=2).first()

    # Modify the State object's name
    state.name = "New Mexico"

    # Commit the changes to the database
    session.commit()
