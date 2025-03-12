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

def add_sat(sat_name, sat_orbit_type, sat_status, sat_description):
    instance = Satellite(
        name = sat_name,
        orbit_type = sat_orbit_type,
        status = sat_status,
        description = sat_description
    )
    session.add(instance)
    session.commit()     

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
    latitude = 25.00,
    longitude = -90.00,
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

session.add_all([amazon, sahara, east_coast, mexico_gulf])
session.commit()

#sat data
surface_temp = SatelliteData(
    sat_id = 1,
    data_type = "Surface Temperature",
    data_value = "32°c",
    date_recorded = f"{date(2024, 12, 27)}",
)
vegetation_index = SatelliteData(
    sat_id = 1,
    data_type = "NDVI(Veg Index)",
    data_value = "0.75",
    date_recorded = f"{date(2025, 3, 9)}",
)
cloud_cover = SatelliteData(
    sat_id = 2,
    data_type = "Cloud COver",
    data_value = "65%",
    date_recorded = f"{date(2025, 2, 10)}",
)
wind_speed = SatelliteData(
    sat_id = 2,
    data_type = "Wind Speed",
    data_value = "120 km/h",
    date_recorded = f"{date(2025, 3, 6)}",
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

session.add_all([surface_temp, vegetation_index, cloud_cover, wind_speed])
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
