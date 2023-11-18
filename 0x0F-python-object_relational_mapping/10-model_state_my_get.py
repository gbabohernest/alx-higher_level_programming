#!/usr/bin/python3
"""Defines a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa using SQLAlchemy.
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    state_name = argv[4]
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        searched_query = session.query(State).order_by(State.id).filter_by(name=state_name)
        if searched_query is not None:
            for sq in searched_query:
                print(f"{sq.id}")
                break
        else:
            print("Not found")

