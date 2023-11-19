#!/usr/bin/python3
"""This module defines a class State that inherits from
   Base and link the table states using SQLAlchemy
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class link the MySQL table 'states.'
    It inherits from Base = declarative_Base using SQLAlchemy
    """
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
