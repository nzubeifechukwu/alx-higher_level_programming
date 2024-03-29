#!/usr/bin/python3
'''Prints a State object whose name is passed as an argument
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
            State.name == argv[4]).first()
    if state is None:
        print('Not found')
    else:
        print(state.id)
