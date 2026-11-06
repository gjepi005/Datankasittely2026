from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Example: table for JSONPlaceholder "users"
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(JSON, nullable=True)
    phone = Column(String, nullable=False)
    website = Column(String, nullable=False)
    company = Column(JSON, nullable=True)

class Protected_Data(Base):
    __tablename__ = "protected_Data"

    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    website = Column(String, nullable=False)