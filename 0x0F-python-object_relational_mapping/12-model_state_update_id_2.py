#!/usr/bin/python3
'''Change the name of a State object in a database table
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

[user, passwd, db_name] = argv[1:4]

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.id == 2):
        state.name = 'New Mexico'

    session.commit()
