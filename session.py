from models import session, Satellite, SatelliteData, Region
from sqlalchemy import select
from datetime import date

# CREATE
# sat
landsat = Satellite(
    id = 1,
    name = "Landsat-9",
    orbit_type = "LEO",
    status = "active",
    description = "NASA's Earth observation satellite"
)
geos = Satellite(
    id = 2,
    name = "GOES-16",
    orbit_type = "GEO",
    status = "active",
    description = "NOAA's weather satellite"
)

session.add_all([landsat,geos])
session.commit()

#region
amazon = Region(
    sat_id = 1,
    name = "Amazon Rainforest",
    latitude = -3.4653,
    longitude = -62.2159,
)
sahara = Region(
    sat_id = 1,
    name = "Sahara Desert",
    latitude = 23.4162,
    longitude = 25.6628,
)
east_coast = Region(
    sat_id = 2,
    name = "East Coast(US)",
    latitude = 35.2271,
    longitude = -80.8431,
)
mexico_gulf = Region(
    sat_id = 2,
    name = "Gulf of Mexico",
    latitude = 25.0,
    longitude = -90.0,
)

session.add_all([amazon, sahara, east_coast, mexico_gulf])
session.commit()

#sat data
surface_temp = SatelliteData(
    sat_id = 1,
    data_type = 'Surface Temperature',
    data_value = '32°c',
    date_recorded = date(2024, 12, 27),
)
vegetation_index = SatelliteData(
    sat_id = 1,
    data_type = 'NDVI(Veg Index)',
    data_value = '0.75',
    date_recorded = date(2025, 3, 9),
)
cloud_cover = SatelliteData(
    sat_id = 2,
    data_type = 'Cloud COver',
    data_value = '65%',
    date_recorded = date(2025, 2, 10),
)
wind_speed = SatelliteData(
    sat_id = 1,
    data_type = 'Wind Speed',
    data_value = '120 km/h',
    date_recorded = date(2025, 3, 6),
)

session.add_all([surface_temp, vegetation_index, cloud_cover, wind_speed])
session.commit()

#READ
# read satellites
stmt = select(Satellite)
sat_result = session.execute(stmt).scalars()

sat_objs = list(sat_result)
sat_names = [sat.name for sat in sat_objs]
active_sats = [sat for sat in sat_objs if sat.status == 'active']

# read region
stmt = select(Region)
region_result = session.execute(stmt).scalars()

reg_objs = list(region_result)
reg_names = [reg.name for reg in reg_objs]
landsat_regions = [reg for reg in reg_objs if reg.sat_id == 1]
geos_regions = [reg for reg in reg_objs if reg.sat_id == 2]

#read sat data
stmt = select(SatelliteData)
data_result = session.execute(stmt).scalars()

data_objs = list(data_result)
data_types = [data.data_type for data in data_objs]
landsat_data = [data for data in data_objs if data.sat_id == 1]
geos_data = [data for data in data_objs if data.sat_id == 2]

# note: UPDATE
# info: update satellite
# stmt = select(Satellite).where(Satellite.id == 1 )
# sat1 = session.scalars(stmt).first()
# sat1.name = "Not Landsat-9"
# session.commit()
# update region
# update data

#delete