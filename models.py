from sqlalchemy.ext.declarative import declarative_base #type: ignore
from sqlalchemy.orm import relationship, sessionmaker #type: ignore
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, create_engine #type: ignore

Base = declarative_base()

class Satellite(Base):
    pass

class Satellite_data(Base):
    pass

class Region(Base):
    pass

# note: Creates the engine
engine = create_engine('sqlite:///monitoring.db')
Base.metadata.create_all(engine)

# note: Create session instance
Session = sessionmaker(bind=engine)
session = Session()