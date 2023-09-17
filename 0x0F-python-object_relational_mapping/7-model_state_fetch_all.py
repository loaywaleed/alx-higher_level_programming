#!/usr/bin/python3
"""Script that lists all state objects"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base
from sys import argv

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)

    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
