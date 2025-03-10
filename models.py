from sqlalchemy.ext.declarative import declarative_base #type: ignore
from sqlalchemy.orm import relationship, sessionmaker #type: ignore
from sqlalchemy import Column, String, Integer, ForeignKey, Float, create_engine, Date #type: ignore
from datetime import date

Base = declarative_base()

class Satellite(Base):
    
    __tablename__ = 'satellites'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    orbit_type = Column(String, nullable=False) # info: LEO,MEO,GEO
    status = Column(String, nullable=False) # info: active, inactive
    description = Column(String, nullable=False)

    # note: relationship --> region & sat data
    regions = relationship('Region', back_populates='satellite', cascade='all, delete-orphan')
    satellite_data = relationship('SatelliteData', back_populates='satellite',cascade='all, delete-orphan')
    

class SatelliteData(Base):

    __tablename__ = 'satellite_data'

    id = Column(Integer, primary_key=True)
    data_type = Column(String, nullable=False)
    data_value = Column(Integer, nullable=False)
    date_recorded = Column(Date, default=date.today) # note: 2025-03-10
    sat_id = Column(Integer, ForeignKey('satellites.id'), nullable=False)
   
    satellite = relationship('Satellite', back_populates='satellite_data')
    

class Region(Base):

    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    sat_id = Column(Integer, ForeignKey('satellites.id'), nullable=False)
    
    satellite = relationship('Satellite', back_populates='regions')
    

# note: Creates the engine
engine = create_engine('sqlite:///monitoring.db')
Base.metadata.create_all(engine)

# note: Create session instance
Session = sessionmaker(bind=engine)
session = Session()