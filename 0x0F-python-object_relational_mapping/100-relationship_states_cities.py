#!/usr/bin/python3
'''Creates a state California with a city San Francisco from a given database
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


if __name__ == '__main__':
    [user, passwd, db_name] = argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    california.cities = [City(name='San Francisco')]

    session.add(california)
    session.commit()
