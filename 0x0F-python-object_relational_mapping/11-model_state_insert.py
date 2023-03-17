#!/usr/bin/python3
'''Add a State object `Louisiana` to a database table
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

    session.add(State(name='Louisiana'))
    session.commit()

    for state in session.query(State).filter(State.name == 'Louisiana'):
        print(state.id)
