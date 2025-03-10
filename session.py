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
    name = "Amazon Rainforest",
    latitude = -3.4653,
    longitude = -62.2159,
    sat_id = 1
)
sahara = Region(
    name = "Sahara Desert",
    latitude = 23.4162,
    longitude = 25.6628,
    sat_id = 1
)
east_coast = Region(
    name = "East Coast(US)",
    latitude = 35.2271,
    longitude = -80.8431,
    sat_id = 2
)
mexico_gulf = Region(
    name = "Gulf of Mexico",
    latitude = 25.0,
    longitude = -90.0,
    sat_id = 2
)

session.add_all([amazon, sahara, east_coast, mexico_gulf])
session.commit()

#sat data
surface_temp = SatelliteData(
    data_type = 'Surface Temperature',
    data_value = '32°c',
    date_recorded = date(2024, 12, 27),
    sat_id = '1'
)
vegetation_index = SatelliteData(
    data_type = 'NDVI(Veg Index)',
    data_value = '0.75',
    date_recorded = date(2025, 3, 9),
    sat_id = '1'
)
cloud_cover = SatelliteData(
    data_type = 'Cloud COver',
    data_value = '65%',
    date_recorded = date(2025, 2, 10),
    sat_id = '2'
)
wind_speed = SatelliteData(
    data_type = 'Wind Speed',
    data_value = '120 km/h',
    date_recorded = date(2025, 3, 6),
    sat_id = '1'
)

session.add_all([surface_temp, vegetation_index, cloud_cover, wind_speed])
session.commit()

#read

#update

#delete