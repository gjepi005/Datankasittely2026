from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "Players"
    id = Column(Integer, primary_key=True)
    serial = Column(Integer, nullable=False)
    player_name = Column(String, nullable=False)
    club = Column(String, nullable=False)
    position = Column(String, nullable=False)
    goals = Column(Integer, nullable=False)
    right_foot = Column(Integer, nullable=False)
    left_foot = Column(Integer, nullable=False)
    headers = Column(Integer, nullable=False)
    others = Column(Integer,nullable=False)
    inside_area = Column(Integer,nullable=False)

class Player_Stats(Base):
    __tablename__ = "Player_Stats"

    serial = Column(Integer, primary_key=True)
    goals = Column(Integer, nullable=False)
    right_foot = Column(Integer, nullable=False)
    left_foot = Column(Integer, nullable=False)
    headers = Column(Integer, nullable=False)
    others = Column(Integer,nullable=False)
    inside_area = Column(Integer,nullable=False)
