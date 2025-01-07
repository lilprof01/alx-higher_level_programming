#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Create SQLAlchemy engine to connect to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory for the engine
    Session = sessionmaker(bind=engine)

    # Create a new session
    session = Session()

    # Query all City and State objects and join them
    # by their state_id and order by City.id
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        # Print the state name, city id and city name
        print("{}: ({}) {}".format(state.name, city.id, city.name))
