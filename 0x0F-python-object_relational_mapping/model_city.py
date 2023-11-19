#!/usr/bin/python3
"""This module defines a class City that inherits from
   Base and link the table cities using SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Defines a class that inherts from Base
    and link the MQSQL table cities using SQLAlchemy
    """
    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer,
                      ForeignKey(State.id), nullable=False)
