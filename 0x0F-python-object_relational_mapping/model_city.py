#!/usr/bin/python3
"""city class module"""

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __table__ = 'cities'
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
