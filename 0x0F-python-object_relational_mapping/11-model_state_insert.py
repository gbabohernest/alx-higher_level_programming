#!/usr/bin/python3
"""Defines a module that creates a new start object and
   adds it to the database hbtn_0e_6_usa and prints the new
   state object id after creation using SQLAlchemy module
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
        session.add(State(name='Louisiana'))
        session.commit()
        new_state_id = session.query(State).order_by(State.id.desc()).first()

        if new_state_id is not None:
            print(f"{new_state_id.id}")
