#!/usr/bin/python3
'''Print the first object from a database table
'''


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for obj in session.query(State).filter(State.id == 1):
        if obj is None:
            print('Nothing')
        else:
            print('{}: {}'.format(obj.id, obj.name))
