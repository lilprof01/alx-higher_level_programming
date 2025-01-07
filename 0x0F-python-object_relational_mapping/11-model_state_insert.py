#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a database connection using the provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Create a session object to interact with the database
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # Create a new State object and add it to the session
    louisiana = State(name="Louisiana")
    session.add(louisiana)

    # Commit the changes to the database
    session.commit()

    # Print the ID of the newly created State object
    print(louisiana.id)
