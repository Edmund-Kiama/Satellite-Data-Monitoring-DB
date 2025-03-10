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

    regions = relationship('Region', back_populates='satellite', cascade='all, delete-orphan')
    satellite_data = relationship('SatelliteData', back_populates='satellite',cascade='all, delete-orphan')

    def __repr__(self):
        return f"Satellite(id: {self.id}, name: {self.name}, orbit_type: {self.orbit_type}, status: {self.status}, description: {self.description})"
    

class SatelliteData(Base):

    __tablename__ = 'satellite_data'

    id = Column(Integer, primary_key=True)
    sat_id = Column(Integer, ForeignKey('satellites.id'), nullable=False)
    data_type = Column(String, nullable=False)
    data_value = Column(Integer, nullable=False)
    date_recorded = Column(Date, default=date.today) # note: date(2025,03,10)
   
    satellite = relationship('Satellite', back_populates='satellite_data')

    def __repr__(self):
        return f"SatelliteData(id: {self.id},sat_id: {self.sat_id}, data_type: {self.data_type}, data_value: {self.data_value}, date_recorded: {self.date_recorded})"
    

class Region(Base):

    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    sat_id = Column(Integer, ForeignKey('satellites.id'), nullable=False)
    name = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    
    satellite = relationship('Satellite', back_populates='regions')

    def __repr__(self):
        return f"Region(id: {self.id}, sat_id: {self.sat_id}, name: {self.name}, latitude: {self.latitude}, longitude: {self.longitude})"
    

engine = create_engine('sqlite:///monitoring.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()