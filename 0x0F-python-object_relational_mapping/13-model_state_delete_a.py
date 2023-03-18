#!/usr/bin/python3
'''Delete all State objects with name containing `a`
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    [user, passwd, db_name] = argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%')).delete(
        synchronize_session='fetch')
    session.commit()
