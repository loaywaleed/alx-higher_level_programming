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

    states = session.query(State).all()
    name_of_state = argv[4]

    flag = 0
    for state in states:
        if name_of_state == state.name:
            flag = 1
            print("{}".format(state.id))

    if flag == 0:
        print("Not found")

    session.close()
