#!/usr/bin/python3
"""Defines a module or script that list all State object that
   contains the letter `a` from the database hbtn_0e_6_usa
   using SQLAlchemy module
"""

from model_state import Base, State
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
        # fetch list of states that contains letter `a` in its name
        states = session.query(State).order_by(State.id).filter(
            State.name.like("%a%"))

        for state in states:
            print("{}: {}".format(str(state.id), str(state.name)))
