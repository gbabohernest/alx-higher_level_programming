#!/usr/bin/python3
"""Defines a script that prints the first State
   object from the database hbtn_0e_6_usa
   using SQLAlchemy module
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

    first_state = session.query(State).order_by(State.id).where(State.id == 1)

    for fs in first_state:
        print(f"{str(fs.id)}: {str(fs.name)}")
