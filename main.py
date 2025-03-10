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
from mydb.session import get_sats, get_reg, get_data, delete_sat_tb

on_loop = True

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


    pass
def create_table():
    pass
def update_table():
    pass
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
        delete_sat_tb()
    # elif user == "2":
    #     satdata_tb_display()
    # else:
    #     region_tb_display()

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
    print("1. Display table")
    print("2. Create table")
    print("3. Update table")
    print("4. Delete table")
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