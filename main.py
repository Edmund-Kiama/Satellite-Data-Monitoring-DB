# the app should be able to
# - have a menu for creating, display, update, delete tables
# - for those CRUD menus, they ask for the tree tables

# for creating new values for tables - ask the user for the values

# display just displays the tables, and find by id

# for updating, 
#     - the user picks which table and which value to change,
#     - then prompt user for value
#     - then update the value to db

# for deleting
#     - the user picks which table and which value to delete
#     - update the db

from mydb.models import session, Satellite, SatelliteData, Region
# from sqlalchemy import select
from mydb.session import get_sats, get_reg, get_data, get_sat_ids, get_data_ids, get_reg_ids
from mydb.session import delete_sat, delete_region, delete_data

on_loop = True

# mark: Display Functions

def sat_tb_display():
    sats = get_sats()
    print("")
    print("                             Satellite Table")
    print("-----------------------------------------------------------------------------------------")
    print("| Id    |   Name        | Orbit Type |   Status   |   Description                       ")
    print("-----------------------------------------------------------------------------------------")
    for sat in sats:
        print(f"| {sat.id:<3}   |   {sat.name:<10}  |   {sat.orbit_type:<5}    |   {sat.status:<7}  |   {sat.description:<20}")
    print("-----------------------------------------------------------------------------------------")

def satdata_tb_display():
    data = get_data()
    print("")
    print("                             Satellite Data Table")
    print("-------------------------------------------------------------------------------")
    print("| Id    | Sat Id |       Data Type           |  Data Value   |  Date recorded ")
    print("-------------------------------------------------------------------------------")
    for dat in data:
        print(f"| {dat.id:<3}   |   {dat.sat_id:<3}  |   {dat.data_type:<20}    |   {dat.data_value:<10}  |   {dat.date_recorded:<10}")
    print("------------------------------------------------------------------------------")
    
def region_tb_display():
    regions = get_reg()
    print("")
    print("                             Region Table")
    print("------------------------------------------------------------------------")
    print("| Id    | Sat Id |        Name               |  Latitude  |  Longitude ")
    print("------------------------------------------------------------------------")
    for reg in regions:
        print(f"| {reg.id:<3}   |   {reg.sat_id:<3}  |   {reg.name:<20}    |   {reg.latitude:<7}  |   {reg.longitude:<7}")
    print("------------------------------------------------------------------------")


def display_table():
    print("")
    print("Choose Table to Display")
    print("-----------------------")
    print("1. Satellites table")
    print("2. Satellites Data table")
    print("3. Regions table")
    print("")

    while True:
        user = input("Which table is to be displayed: ")
        if user in ["1", "2", "3"]:
            break
        else:
            print(f"{user} is Invalid Input. Choose in (1, 2, 3)")
    
    if user == "1":
        sat_tb_display()
    elif user == "2":
        satdata_tb_display()
    else:
        region_tb_display()

def create_table():
    pass
def update_table():
    pass

# mark: Delete Functions
def handle_sat_delete():
    sat_tb_display()
    sat_ids = get_sat_ids()

    print("")
    print(f"Choose which satellite to delete according to its Id: {sat_ids}")
    print("")

    while True:
        user = int(input("Choose Id: "))
        if user in sat_ids:
            break
        else:
            print(f"No satellite with Id of {user}")
    
    delete_sat(user)
    print("")
    print("###")
    print(f"Satellite of Id {user} has been deleted successfully!!")
    print("###")

def handle_region_delete():
    region_tb_display()
    reg_ids = get_reg_ids()

    print("")
    print(f"Choose which region to delete according to its Id: {reg_ids}")
    print("")

    while True:
        user = int(input("Choose Id: "))
        if user in reg_ids:
            break
        else:
            print(f"No Region with Id of {user}")
    
    delete_region(user)
    print("")
    print("###")
    print(f"Region of Id {user} has been deleted successfully!!")
    print("###")

def handle_data_delete():
    satdata_tb_display()
    data_ids = get_data_ids()

    print("")
    print(f"Choose which Data Type to delete according to its Id: {data_ids}")
    print("")

    while True:
        user = int(input("Choose Id: "))
        if user in data_ids:
            break
        else:
            print(f"No Data Type with Id of {user}")
    
    delete_data(user)
    print("")
    print("###")
    print(f"Data Type of Id {user} has been deleted successfully!!")
    print("###")

def delete_table():
    print("")
    print("Choose Table to Delete")
    print("-----------------------")
    print("1. Satellites table")
    print("2. Satellites Data table")
    print("3. Regions table")
    print("")

    while True:
        user = input("Which table is to be deleted: ")
        if user in ["1", "2", "3"]:
            break
        else:
            print(f"{user} is Invalid Input. Choose in (1, 2, 3)")
    
    if user == "1":
        handle_sat_delete()
    elif user == "2":
        handle_data_delete()
    else:
        handle_region_delete()

def exit_menu():
    global on_loop
    on_loop = False

def menu():
    print("")
    print("##################################")
    print("     SATELLITE MONITORING SYSTEM")
    print("")
    print("Choose your Options")
    print("-------------------")
    print("1. Display tables")
    print("2. Create new table value")
    print("3. Update table value")
    print("4. Delete table value")
    print("5. Exit")
    print("")
    print("##################################")

    while True:
        user = input("Your option [1, 2, 3, 4, 5]: ")
        if user in ["1", "2", "3", "4", "5"]:
            break;
        else:
            print("f{user} is Invalid! Choose in (1, 2, 3, 4, 5).")

    return user

def main():
    while on_loop:
        user = menu()
        if user == "1":
            display_table()
        elif user == "2":
            create_table()
        elif user == "3":
            update_table()
        elif user == "4":
            delete_table()
        else:
            exit_menu()
         
    pass

if __name__ == "__main__":
    main()