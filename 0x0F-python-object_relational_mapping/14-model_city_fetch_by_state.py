#!/usr/bin/python3
'''Prints all City objects from a given database table
'''


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    [user, passwd, db_name] = argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for obj in session.query(State.name, City.id, City.name).join(
            City).order_by(City.id).all():
        print('{}: ({}) {}'.format(obj[0], obj[1], obj[2]))
