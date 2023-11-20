#!/usr/bin/python3
"""Defines a script that lists all City objects
from the database hbtn_0e_101_usa using SQLAlchemy
"""

from relationship_state import Base
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
        result_set = session.query(City).order_by(City.id).all()
        for city in result_set:
            if city.state:
                state_name = city.state.name
                print(f"{city.id}: {city.name} -> {state_name}")
            else:
                pass
