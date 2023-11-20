#!/usr/bin/python3
"""Defines a script that lists all State objects and
corresponding City objects, contained in the db hbtn_0e_101_usa
using SQLAlchemy module
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
        result_set = session.query(State).order_by(State.id).all()

        for state in result_set:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")

        # result_set = session.query(State, City).order_by(
        #     State.id, City.id).filter(State.id
        #                               == City.state_id).all()
        # curr_state_id = None
        # for state, city in result_set:
        #     if state.id != curr_state_id:
        #         print(f"{state.id}: {state.name}")
        #         curr_state_id = state.id
        #
        #     print("\t{}: {}".format(city.id, city.name))
