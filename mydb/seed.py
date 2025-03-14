from mydb.models import session, Satellite, SatelliteData, Region
from sqlalchemy import select
from datetime import date


session.query(Satellite).delete()
session.query(Region).delete()
session.query(SatelliteData).delete()
session.commit()

# mark: CREATE
# sat
landsat = Satellite(
    name = "Landsat-9",
    orbit_type = "LEO",
    status = "active",
    description = "NASA's Earth observation satellite"
)
geos = Satellite(
    name = "GOES-16",
    orbit_type = "GEO",
    status = "active",
    description = "NOAA's weather satellite"
)
sentinel = Satellite(
    name = "Sentinel-2",
    orbit_type = "LEO",
    status = "active",
    description = "ESA's Earth observation satellite for land monitoring"
)
himawari = Satellite(
    name = "Himawari-8",
    orbit_type = "GEO",
    status = "active",
    description = "Japan's weather satellite for Asia-Pacific region"
)
terra = Satellite(
    name = "Terra",
    orbit_type = "LEO",
    status = "active",
    description = "NASA's satellite for global climate and environmental research"
)
aqua = Satellite(
    name = "Aqua",
    orbit_type = "LEO",
    status = "active",
    description = "NASA's Earth observation satellite for studying water cycles"
)
cosmo_sky = Satellite(
    name = "COSMO-SkyMed",
    orbit_type = "LEO",
    status = "active",
    description = "Italian radar satellite for Earth observation and disaster monitoring"
)
insat_3d = Satellite(
    name = "INSAT-3D",
    orbit_type = "GEO",
    status = "active",
    description = "India's weather and environmental monitoring satellite"
)


def add_sat(sat_name, sat_orbit_type, sat_status, sat_description):
    instance = Satellite(
        name = sat_name,
        orbit_type = sat_orbit_type,
        status = sat_status,
        description = sat_description
    )
    session.add(instance)
    session.commit()     

session.add_all([landsat, geos, sentinel, himawari, terra, aqua, cosmo_sky, insat_3d])
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
    latitude = 25.00,
    longitude = -90.00,
)
great_barrier_reef = Region(
    sat_id = 3,  
    name = "Great Barrier Reef",
    latitude = -18.2871,
    longitude = 147.6992,
)
himalayas = Region(
    sat_id = 3,  
    name = "Himalayas",
    latitude = 27.9881,
    longitude = 86.9250,
)
philippine_sea = Region(
    sat_id = 4,  
    name = "Philippine Sea",
    latitude = 15.0,
    longitude = 130.0,
)
antarctica = Region(
    sat_id = 5,
    name = "Antarctica",
    latitude = -75.2500,
    longitude = -0.0714,
)
greenland = Region(
    sat_id = 6,  
    name = "Greenland Ice Sheet",
    latitude = 71.7069,
    longitude = -42.6043,
)
andes_mountains = Region(
    sat_id = 7,
    name = "Andes Mountains",
    latitude = -32.6532,
    longitude = -70.0115,
)
indian_ocean = Region(
    sat_id = 8,
    name = "Indian Ocean",
    latitude = -10.0,
    longitude = 80.0,
)
hurricane_zone = Region(
    sat_id = 8,
    name = "Hurricane Formation Zone",
    latitude = 12.5,
    longitude = -60.0,
)

def add_region(sat_idx, reg_name, reg_latitude, reg_longitude):
    instance = Region(
        sat_id = sat_idx,
        name = reg_name,
        latitude = reg_latitude,
        longitude = reg_longitude
    )
    session.add(instance)
    session.commit() 

session.add_all([amazon, sahara, east_coast, mexico_gulf, great_barrier_reef, himalayas, philippine_sea, antarctica, greenland, andes_mountains, indian_ocean, hurricane_zone])
session.commit()

#sat data
surface_temp = SatelliteData(
    sat_id = 1,
    data_type = "Surface Temperature",
    data_value = "32°c",
    date_recorded = date(2024, 12, 27),
)
vegetation_index = SatelliteData(
    sat_id = 1,
    data_type = "NDVI(Veg Index)",
    data_value = "0.75",
    date_recorded = date(2025, 3, 9),
)
cloud_cover = SatelliteData(
    sat_id = 2,
    data_type = "Cloud COver",
    data_value = "65%",
    date_recorded = date(2025, 2, 10),
)
wind_speed = SatelliteData(
    sat_id = 2,
    data_type = "Wind Speed",
    data_value = "120 km/h",
    date_recorded = date(2025, 3, 6),
)
ocean_temp = SatelliteData(
    sat_id = 3,  
    data_type = "Sea Surface Temperature",
    data_value = "28°C",
    date_recorded = date(2025, 1, 15),
)
air_quality = SatelliteData(
    sat_id = 3,  
    data_type = "Air Quality Index",
    data_value = "AQI 42 (Good)",
    date_recorded = date(2025, 2, 5),
)
hurricane_intensity = SatelliteData(
    sat_id = 4,  
    data_type = "Hurricane Intensity",
    data_value = "Category 4",
    date_recorded = date(2025, 3, 8),
)
ozone_levels = SatelliteData(
    sat_id = 5,  
    data_type = "Ozone Concentration",
    data_value = "290 DU",
    date_recorded = date(2025, 3, 10),
)
sea_level_rise = SatelliteData(
    sat_id = 6,  
    data_type = "Sea Level Rise",
    data_value = "3.2 mm/year",
    date_recorded = date(2025, 1, 20),
)
polar_ice_extent = SatelliteData(
    sat_id = 6,  
    data_type = "Polar Ice Extent",
    data_value = "12.5 million km²",
    date_recorded = date(2025, 2, 18),
)
earthquake_detection = SatelliteData(
    sat_id=7,  
    data_type="Ground Displacement",
    data_value="5.3 cm shift",
    date_recorded=date(2025, 3, 5),
)
solar_radiation = SatelliteData(
    sat_id = 8,  
    data_type = "Solar Radiation",
    data_value = "1361 W/m²",
    date_recorded = date(2025, 2, 25),
)
precipitation_rate = SatelliteData(
    sat_id = 8,  
    data_type = "Precipitation Rate",
    data_value = "15 mm/hr",
    date_recorded = date(2025, 3, 12),
)

def add_data(sat_idx, type_data, value_data, date):
    instance = SatelliteData(
        sat_id = sat_idx,
        data_type = type_data,
        data_value = value_data,
        date_recorded = date
    )
    session.add(instance)
    session.commit() 

session.add_all([surface_temp, vegetation_index, cloud_cover, wind_speed, ocean_temp, air_quality, hurricane_intensity, ozone_levels, sea_level_rise, polar_ice_extent, earthquake_detection, solar_radiation, precipitation_rate])
session.commit()




#mark: READ
# read satellites
def get_sats():
    stmt = select(Satellite)
    sat_result = session.execute(stmt).scalars()
    return list(sat_result)

def get_sat_ids():
    sat_objs = get_sats()
    return [sat.id for sat in sat_objs]

def get_active_sat():
    sat_objs = get_sats()
    return [sat for sat in sat_objs if sat.status == "active"]

# read region
def get_reg():
    stmt = select(Region)
    region_result = session.execute(stmt).scalars()
    return list(region_result)

def get_reg_ids():
    reg_objs = get_reg()
    return [reg.id for reg in reg_objs]
# landsat_regions = [reg for reg in reg_objs if reg.sat_id == 1]
# geos_regions = [reg for reg in reg_objs if reg.sat_id == 2]

#read sat data
def get_data():
    stmt = select(SatelliteData)
    data_result = session.execute(stmt).scalars()
    return list(data_result)

def get_data_type():
    data_objs = get_data()
    return [data.data_type for data in data_objs]

def get_data_ids():
    data_objs = get_data()
    return [data.id for data in data_objs]
# landsat_data = [data for data in data_objs if data.sat_id == 1]
# geos_data = [data for data in data_objs if data.sat_id == 2]




# mark UPDATE

# info: update satellite
# stmt = select(Satellite).where(Satellite.id == 1 )
# sat1 = session.scalars(stmt).first()
# sat1.name = "Not Landsat-9"
# session.commit()

def update_sat(sat_id, variable, new_value):
    stmt = select(Satellite).where(Satellite.id == sat_id )
    sat = session.scalars(stmt).first()
    if sat:
        setattr(sat, variable, new_value)
        # fix: sat.update(variable, new_value)
        session.commit()
    else:
        print(f"There is no Satellite of Id {sat_id}")


# info: update region
# stmt = select(Region).where(Region.id == 1 )
# region1 = session.scalars(stmt).first()
# region1.name = "Not Amazon"
# session.commit()

def update_region(reg_id, variable, new_value):
    stmt = select(Region).where(Region.id == reg_id )
    reg = session.scalars(stmt).first()
    if reg:
        setattr(reg, variable, new_value)
        session.commit()
    else:
        print(f"There is no Region of Id {reg_id}")

# info: update data
# stmt = select(SatelliteData).where(SatelliteData.id == 1 )
# data1 = session.scalars(stmt).first()
# data1.name = "Not Surface Temperature"
# session.commit()

def update_data(data_id, variable, new_value):
    stmt = select(SatelliteData).where(SatelliteData.id == data_id )
    data = session.scalars(stmt).first()
    if data:
        setattr(data, variable, new_value)
        session.commit()
    else:
        print(f"There is no Satellite Data of Id {data_id}")




# mark: DELETE
# info: delete satellite
# session.delete(landsat)
# session.delete(geos)
# session.commit()

# def delete_landsat():
#     session.delete(landsat)
#     session.commit()

# def delete_geos():
#     session.delete(geos)
#     session.commit()

def delete_sat(user_id):
    stmt = select(Satellite).where(Satellite.id == user_id)
    sat_result = session.execute(stmt).scalars().first()
    session.delete(sat_result)
    session.commit()

# info: delete region
#session.delete(amazon)
#session.delete(sahara)
#session.delete(east_coast)
#session.delete(mexico_gulf)
#session.commit()

def delete_region(user_id):
    stmt = select(Region).where(Region.id == user_id)
    region_result = session.execute(stmt).scalars().first()
    session.delete(region_result)
    session.commit()


# info: delete data
#session.delete(surface_temp)
#session.delete(vegetation_index)
#session.delete(cloud_cover)
#session.delete(wind_speed)
#session.commit()

def delete_data(user_id):
    stmt = select(SatelliteData).where(SatelliteData.id == user_id)
    data_result = session.execute(stmt).scalars().first()
    session.delete(data_result)
    session.commit()
