#!/usr/bin/python3
"""Defines a script that list all state objects from
   the database hbtn_0e_6_usa using SQLAlchemy module
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the db for the states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{str(state.id)}: {str(state.name)}")
