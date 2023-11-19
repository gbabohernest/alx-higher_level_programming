#!/usr/bin/python3
"""Defines a module that creates the State "California with
   the City "San Francisco from the db hbtn_0e_100_usa using SQLAlchemy
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        session.add(State(name='California', cities=[City(name='San Francisco')]))
        session.commit()
