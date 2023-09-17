#!/usr/bin/python3
"""city class module"""

from sqlalchemy import String, Column, Integer, ForeignKey
from model_state import Base


class City(Base):
    """City class that models a table
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
