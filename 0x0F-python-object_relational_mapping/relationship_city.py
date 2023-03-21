#!/usr/bin/python3
'''This model_city module defines a City class that inherits fro a Base class
'''


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    '''City class inherits from Base class
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
