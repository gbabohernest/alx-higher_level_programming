#!/usr/bin/python3
"""Defines a script that prints all objects form the
   database hbtn_0e_14_usa using SQLAlchemy module
"""

from model_state import Base, State
from model_city import City
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
        result_set = session.query(City, State).filter(
            City.state_id == State.id).all()
        for city, state in result_set:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
