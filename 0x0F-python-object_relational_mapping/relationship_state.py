#!/usr/bin/python3
'''This script defines a State class and an instance Base = declarative_base()
State class inherits from Base, links to the MySQL table states and has class
attributes `id` that represents a column of an auto-generated, unique integer,
can’t be null and is a primary key, and another class attribute name that
represents a column of a string with maximum 128 characters and can’t be null
'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''State class inherits from Base class
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
