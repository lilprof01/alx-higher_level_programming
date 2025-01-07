#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create a new database engine using the provided command-line arguments
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create a new session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a new session object
    session = Session()

    # Query all City objects from the database and order them by ID
    for city in session.query(City).order_by(City.id):
        # Print the City ID, name, and the name of its associated State object
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
