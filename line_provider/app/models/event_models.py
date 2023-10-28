import enum

from database import Base
from sqlalchemy import Column, Integer, Enum, DECIMAL, DateTime


class EventState(enum.Enum):
    NEW = 'new'
    FIRST_WIN = 'first_win'
    SECOND_WIN = 'second_win'


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    coefficient = Column(DECIMAL(precision=5, scale=2), nullable=False)
    deadline = Column(DateTime, nullable=False)
    status = Column(Enum("new", "first_win", 'second_win', name="EventState"), default="new", nullable=False)
