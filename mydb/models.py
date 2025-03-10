from sqlalchemy.ext.declarative import declarative_base #type: ignore
from sqlalchemy.orm import relationship, sessionmaker #type: ignore
from sqlalchemy import Column, String, Integer, ForeignKey, Float, create_engine, Date #type: ignore
from datetime import date

Base = declarative_base()

class Satellite(Base):
    
    __tablename__ = "satellites"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    _orbit_type = Column("orbit_type", String, nullable=False) # info: LEO,MEO,GEO
    _status = Column("status", String, nullable=False) # info: active, inactive
    description = Column(String, nullable=False)

    regions = relationship("Region", back_populates="satellite", cascade="all, delete-orphan")
    satellite_data = relationship("SatelliteData", back_populates="satellite",cascade="all, delete-orphan")

    def __repr__(self):
        return f"Satellite(id: {self.id}, name: {self.name}, orbit_type: {self.orbit_type}, status: {self.status}, description: {self.description})"
       
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status) -> None:
        if status in ["active", "inactive"]:
            self._status = status
        else:
            raise ValueError(f"{status} is Invalid! 'active' or 'inactive' allowed only") 
    
    @property
    def orbit_type(self):
        return self._orbit_type
    @orbit_type.setter
    def orbit_type(self, orbit_type) -> None:
        if orbit_type in ["LEO", "MEO", "GEO"]:
            self._orbit_type = orbit_type
        else:
            raise ValueError(f"{orbit_type} is Invalid! 'MEO', 'LEO', 'GEO' allowed only")
        
class SatelliteData(Base):

    __tablename__ = "satellite_data"

    id = Column(Integer, primary_key=True)
    sat_id = Column(Integer, ForeignKey("satellites.id"), nullable=False)
    _data_type = Column("data_type", String, nullable=False)
    data_value = Column(String, nullable=False)
    date_recorded = Column(String, default=date.today()) # fix : Ignore --> Date instead of String
   
    satellite = relationship("Satellite", back_populates="satellite_data")

    def __repr__(self):
        return f"SatelliteData(id: {self.id},sat_id: {self.sat_id}, data_type: {self.data_type}, data_value: {self.data_value}, date_recorded: {self.date_recorded})"

    #note: This property is just here to fill project requirements
    @property
    def data_type(self):
        return self._data_type
    @data_type.setter
    def data_type(self, data_type):
        if isinstance(data_type, str):
            self._data_type = data_type
        else:
            raise ValueError(f"{data_type} is not an string")

class Region(Base):

    __tablename__ = "regions"

    id = Column(Integer, primary_key=True)
    sat_id = Column(Integer, ForeignKey("satellites.id"), nullable=False)
    name = Column(String, nullable=False)
    _latitude = Column("latitude", Float)
    _longitude = Column("longitude", Float)
    
    satellite = relationship("Satellite", back_populates="regions")

    def __repr__(self):
        return f"Region(id: {self.id}, sat_id: {self.sat_id}, name: {self.name}, latitude: {self.latitude}, longitude: {self.longitude})"
    
    @property
    def latitude(self):
        return self._latitude
    @latitude.setter
    def latitude(self, latitude):
        if isinstance(latitude, float):
            self._latitude = latitude
        else:
            raise ValueError(f"{latitude} is not a float")
    
    @property
    def longitude(self):
        return self._longitude
    @longitude.setter
    def longitude(self, longitude):
        if isinstance(longitude, float):
            self._longitude = longitude
        else:
            raise ValueError(f"{longitude} is not a float")
    

engine = create_engine("sqlite:///monitoring.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()