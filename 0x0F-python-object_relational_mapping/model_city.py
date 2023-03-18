#!/usr/bin/python3
'''This model_city module defines a City class that inherits fro a Base class
'''


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''City class inherits from Base class
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
