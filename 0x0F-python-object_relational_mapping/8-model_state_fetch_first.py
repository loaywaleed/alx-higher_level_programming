#!/usr/bin/python3
"""Prints first state object"""

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3],
                                   pool_pre_ping=True))
    session = Session(engine)

    Base.metadata.create_all(engine)
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
