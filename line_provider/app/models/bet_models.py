# import enum
#
# from database import Base
# from sqlalchemy import Column, Integer, Enum, ForeignKey, DECIMAL
# from sqlalchemy.orm import relationship

#
# class BetState(enum.Enum):
#     ACTIVE = 'active'
#     WIN = 'win'
#     LOSE = 'lose'
#
#
# class Bet(Base):
#     __tablename__ = "bets"
#
#     id = Column(Integer, primary_key=True, index=True)
#
#     event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
#     status = Column(Enum("active", "win", 'lose', name="BetState"), default="active", nullable=False)
#     bet_sum = Column(DECIMAL(scale=2), nullable=False)
#
#     event = relationship("Event", backref="bets")
