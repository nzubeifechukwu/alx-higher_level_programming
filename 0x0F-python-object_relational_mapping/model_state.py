#!/usr/bin/python3
'''This script defines a State class and an instance Base = declarative_base()
State class inherits from Base, links to the MySQL table states and has class
attributes `id` that represents a column of an auto-generated, unique integer,
can’t be null and is a primary key, and another class attribute name that
represents a column of a string with maximum 128 characters and can’t be null
'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Sequence
# from sys import argv

Base = declarative_base()


class State(Base):
    '''State class inherits from Base class
    '''
    __tablename__ = 'states'
    seq = Sequence('state_id_seq')
    id = Column(Integer, seq, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    # engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
    #    '.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Base.metadata.create_all(engine)
