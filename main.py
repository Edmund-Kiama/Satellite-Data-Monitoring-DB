
from mydb.seed import get_sats, get_reg, get_data, get_sat_ids, get_data_ids, get_reg_ids
from mydb.seed import delete_sat, delete_region, delete_data
from mydb.seed import add_sat, add_region, add_data
from mydb.seed import update_data, update_region, update_sat
from datetime import datetime, date

on_loop = True

# fix: find object by attribute

def display_satellite():
    sats = get_sats()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("                             Satellite Table")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("| Id    |         Name            | Orbit Type |   Status    |   Description                       ")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    for sat in sats:
        print(f"| {sat.id:<3}   |   {sat.name:<20}  |   {sat.orbit_type:<5}    |   {sat.status:<8}  |   {sat.description:<20}")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("")

def display_data():
    data = get_data()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("                             Satellite Data Table")
    print("-----------------------------------------------------------------------------------------------------")
    print("| Id    | Sat Id |             Data Type               |        Data Value       |  Date recorded ")
    print("------------------------------------------------------------------------------------------------------")
    for dat in data:
        print(f"| {dat.id:<3}   |   {dat.sat_id:<3}  |   {dat.data_type:<30}    |   {dat.data_value:<20}  |   {dat.date_recorded.strftime('%Y-%m-%d'):<10}")
    print("------------------------------------------------------------------------------------------------------")
    print("")

def display_region():
    regions = get_reg()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("                             Region Table")
    print("---------------------------------------------------------------------------------------------------")
    print("| Id    | Sat Id |              Name                   |      Latitude      |  Longitude ")
    print("---------------------------------------------------------------------------------------------------")
    for reg in regions:
        print(f"| {reg.id:<3}   |   {reg.sat_id:<3}  |   {reg.name:<30}    |   {reg.latitude:<15}  |   {reg.longitude:<15}")
    print("---------------------------------------------------------------------------------------------------")
    print("")


# mark: Display Functions

def sat_tb_display():
    display_satellite()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Choose you desired CRUD operation")
    print("-----------------------")
    print("1. Add new satellite")
    print("2. Update satellite value")
    print("3. Delete satellite")
    print("4. Back")
    print("")

    while True:
        user = input("Choose: ")
        print("")
        if user in ["1", "2", "3", "4"]:
            break
        else:
            print(f"{user} is Invalid Input. Choose in (1, 2, 3, 4)")
            print("")
    
    if user == "1":
        handle_sat_create()
    elif user == "2":
        handle_sat_edit()
    elif user =="3":
        handle_sat_delete()
    else:
        pass
    
def satdata_tb_display():
    display_data()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Choose you desired CRUD operation")
    print("-----------------------")
    print("1. Add new satellite data")
    print("2. Update satellite data value")
    print("3. Delete satellite data")
    print("4. Back")
    print("")

    while True:
        user = input("Choose: ")
        print("")
        if user in ["1", "2", "3", "4"]:
            break
        else:
            print(f"{user} is Invalid Input. Choose in (1, 2, 3, 4)")
            print("")
    
    if user == "1":
        handle_satdata_create()
    elif user == "2":
        handle_data_edit()
    elif user == "3":
        handle_data_delete()
    else:
        pass


def region_tb_display():
    display_region()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Choose you desired CRUD operation")
    print("-----------------------")
    print("1. Add new region")
    print("2. Update region value")
    print("3. Delete region")
    print("4. Back")
    print("")

    while True:
        user = input("Choose: ")
        print("")
        if user in ["1", "2", "3", "4"]:
            break
        else:
            print(f"{user} is Invalid Input. Choose in (1, 2, 3, 4)")
            print("")
    
    if user == "1":
        handle_region_create()
    elif user == "2":
        handle_region_edit()
    elif user == "3":
        handle_region_delete()
    else:
        pass
   




#mark: Create function

def handle_sat_create():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Satellite table")
    print("Values required are: name, orbit_type,status.description")
    print("")

    name = input("Satellite's name: ").strip()
    print("")
    while True:
        orbit_type = input("Satellite's orbit type ['MEO', 'LEO', 'GEO']: ").upper().strip()
        print("")
        if orbit_type in ["MEO", "LEO", "GEO"]:
            break
        else: 
            print("Status can only be 'MEO' or 'LEO' or 'GEO' .")

    while True:
        status = input("Satellite's status ['active', 'inactive']: ").lower().strip()
        print("")
        if status in ["active", "inactive"]:
            break
        else: 
            print("Status can only be 'active' or 'inactive'.")
                
    description = input("Satellite's description: ").strip()
    print("")

    if name and orbit_type and status and description:
        add_sat(name, orbit_type, status, description)
        print("-------------------------------------------")
        print("New Satellite Instance has been added.")
        print("-------------------------------------------")
        print("")


def handle_satdata_create():
    sat_ids = get_sat_ids()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Satellite Data table")
    print("Values required are: sat_id, name, orbit_type,status.description")
    print("")

    while True:
        try:
            sat_idx = int(input(f"Satellite Id that took the data recording:{sat_ids} ").strip())
            print("")
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")  
            print("")

    type_data = input("Type of Data: ").strip()
    print("")
    value_data = input("Value of Data: ").strip()
    print("")

    while True:
        user_date = input("Date of recording Data [YYYY-MM-DD]: ").strip()
        print("")
        try:
            date = datetime.strptime(user_date,  "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid Date! Please enter valid date e.g 2025-10-06.")  
            print("")


    if sat_idx and type_data and value_data and date:
        add_data(sat_idx, type_data, value_data, date)
        print("-------------------------------------------")
        print("New Satellite Data Instance has been added.")
        print("--------------------------------------------")
        print("")


def handle_region_create():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Region table")
    print("Values required are: sat_id, name, latitude, longitude")
    print("")

    while True:
        try:
            sat_idx = int(input("Satellite Id for the region: ").strip())
            print("")
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")  
            print("")

    reg_name = input("Name of the region: ").strip()
    print("")

    while True:
        try:
            reg_latitude = float(input("Latitude of the region: ").strip())
            print("")
            break
        except ValueError:
            print("Invalid input! Please enter a Float.")  
            print("")
    
    while True:
        try:
            reg_longitude = float(input("Longitude of the region: ").strip())
            print("")
            break
        except ValueError:
            print("Invalid input! Please enter a Float.")  
            print("")

    if sat_idx and reg_name and reg_latitude and reg_longitude:
        add_region(sat_idx, reg_name, reg_latitude, reg_longitude)
        print("-------------------------------------------")
        print("New Satellite Data Instance has been added.")
        print("--------------------------------------------")
        print("")




# mark: Update Function   

def handle_sat_edit():
    sat_ids = get_sat_ids()
    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("You chose to edit in Satellite table")
    print("")
    print("Which satellite do you wanna edit? ")
    print("")
    
    while True:
        try:
            sat_id = int(input(f"Choose by Id: {sat_ids}").strip())
            print("")

            if sat_id in sat_ids:
                break
            else:
                print(f"{sat_id} is not part of {sat_ids}")
                print("")
        except ValueError:
            print("The value you provided is not an Integer. Try again")
            print("")

    print("Satellite Columns = ['name','orbit_type','status','description']")
    print("")
    while True:
        variable = input("Which of its column is to be edited? ").strip().lower()
        print("")
        if variable in ['name','orbit_type','status','description']:
            break
        else:
            print("Please pick among ['name','orbit_type','status','description']")
            print("")
    while True:
        try:
            if variable == "orbit_type" :
                new_value = input("What's the new value: ").strip().upper()
                print("")
                if new_value in ["LEO", "MEO", "GEO"]:
                    break
                else:
                    print(f'{new_value} is not in ["LEO", "MEO", "GEO"]')
                    print("")
            elif variable == "status":
                new_value = input("What's the new value: ").strip()
                print("")
                if new_value in ["active", "inactive"]:
                    break
                else:
                    print(f'{new_value} is not in ["active", "inactive"]')
                    print("")
            elif (variable == "name" or variable == "description") :
                new_value = input("What's the new value: ").strip()
                print("")
                break
        except ValueError:
            print("Try again")
            print("")

    if sat_id and variable and new_value:
        update_sat(sat_id, variable, new_value)
        print("---------------------------------------------")
        print("          Update is successful!")
        print("---------------------------------------------")
        print("")


def handle_region_edit():
    reg_ids = get_reg_ids()
    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("You chose to edit in Region table")
    print("")
    print("Which region do you wanna edit? ")
    print("")
    
    while True:
        try:
            reg_id = int(input(f"Choose by Id:{reg_ids} ").strip())
            print("")

            if reg_id in reg_ids:
                break
            else:
                print(f"{reg_id} is not part of {reg_ids}")
                print("")
        except ValueError:
            print("The value you provided is not an Integer. Try again")
            print("")

    print("Region Columns = ['sat_id', 'name','latitude','longitude']")
    print("")

    while True:
        variable = input("Which of its column is to be edited? ").strip().lower()
        print("")
        if variable in ['sat_id', 'name','latitude','longitude']:
            break
        else:
            print("Please pick among ['sat_id', 'name','latitude','longitude']")
            print("")

    while True:
        try:
            if variable in ["latitude", "longitude"]:
                new_value = float(input("What's the new value: ").strip())
                print("")
                break
        except ValueError:
            print("The value you provided is not a float")
            print("")

        try:
            if variable == "sat_id":
                new_value = int(input("What's the new value: ").strip())
                print("")
                break
        except ValueError:
            print("The value you provided is not a integer")
            print("")

        try:
            if variable == "name" :
                new_value = input("What's the new value: ").strip()
                print("")   
                break
        except ValueError: 
            print(f"{new_value} is Invalid! Try again!")
            print("")

    if reg_id and variable and new_value:
        update_region(reg_id, variable, new_value)
        print("---------------------------------------------")
        print("          Update is successful!")
        print("---------------------------------------------")
        print("")


def handle_data_edit():
    data_ids = get_data_ids()
    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("You chose to edit in Satellite Data table")
    print("")
    
    print("Which data do you wanna edit? ")
    print("")
    
    while True:
        try:
            data_id = int(input(f"Choose by Id: {data_ids} ").strip())
            print("")

            if data_id in data_ids:
                break
            else:
                print(f"{data_id} is not part of  {data_ids}")
                print("")

        except ValueError:
            print("The value you provided is not an Integer. Try again")
            print("")

    print("Satellite Data Columns = ['sat_id', 'data_type', 'data_value', 'date_recorded']")
    print("")

    while True:
        variable = input("Which of its column is to be edited? ").strip().lower()
        print("")
        if variable in ['sat_id', 'data_type', 'data_value', 'date_recorded']:
                break
        else:
            print("Please pick among  ['sat_id', 'data_type', 'data_value', 'date_recorded']")
            print("")

    while True:
        if variable in ["data_type", "data_value"]:
            try:
                new_value = input("What's the new value: ").strip()
                print("")
                break
            except ValueError:
                print(f'{new_value} is not in ["data_type", "data_value", "date_recorded"]')
                print("")
        elif variable == "sat_id":
            try:
                new_value = int(input("What's the new satellite id: ").strip())
                print("")
                break
            except ValueError:
                print("The value you provided is not an Integer")
                print("")
        else:
            try:
                date_value = int(input("What's the new date: ").strip())
                print("")
                new_value = datetime.strptime(date_value,  "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid Date! Please enter valid date e.g 2025-10-06.")  
                print("")

    if data_id and variable and new_value:
        update_data(data_id, variable, new_value)
        print("---------------------------------------------")
        print("          Update is successful!")
        print("---------------------------------------------")
        print("")




# mark: Delete Functions
def handle_sat_delete():
    sat_ids = get_sat_ids()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Choose which satellite to delete according to its Id: ")
    print("")

    while True:
        try:
            user = int(input(f"Choose Id: {sat_ids} ").strip())
            print("")

            if user in sat_ids:
                break
            else:
                print(f"No satellite with Id of {user}")
                print("")


        except ValueError:
            print("The value you provided is not an Integer")
            print("")

    delete_sat(user)
    print("-----------------------------------------------------------------")
    print(f"     Satellite of Id {user} has been deleted successfully!!")
    print("-----------------------------------------------------------------")
    print("")


def handle_region_delete():
    reg_ids = get_reg_ids()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print(f"Choose which region to delete according to its Id: {reg_ids}")
    print("")

    while True:
        try:
            user = int(input("Choose Id: ").strip())
            print("")
            
            if user in reg_ids:
                break
            else:
                print(f"No Region with Id of {user}")  

        except ValueError:
            print("The value you provided is not an Integer")
            print("")
                
    delete_region(user)
    print("-----------------------------------------------------------------")
    print(f"     Region of Id {user} has been deleted successfully!!")
    print("-----------------------------------------------------------------")
    print("")


def handle_data_delete():
    data_ids = get_data_ids()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print(f"Choose which Data Type to delete according to its Id: {data_ids}")
    print("")

    while True:
        try:
            user = int(input("Choose Id: ").strip())
            print("")
            if user in data_ids:
                break
            else:
                print(f"No Data Type with Id of {user}")   

        except ValueError:
            print("The value you provided is not an Integer")
            print("")

    delete_data(user)
    print("-----------------------------------------------------------------")
    print(f"     Data Type of Id {user} has been deleted successfully!!")
    print("-----------------------------------------------------------------")
    print("")




def exit_menu():
    global on_loop
    on_loop = False
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("                          Exited   from    the     system     ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    

def menu():
    print("")
    print("######################################################################")
    print("               SATELLITE     MONITORING      SYSTEM")
    print("")
    print("Choose your Table")
    print("-------------------")
    print("1. Satellite Table")
    print("2. Satellite Data Table")
    print("3. Region Table")
    print("4. Exit")
    print("")
    print("######################################################################")
    print("")

    while True:
        user = input("Your option [1, 2, 3, 4]: "). strip()
        print("")
        if user in ["1", "2", "3", "4"]:
            break;
        else:
            print(f"{user} is Invalid! Choose in (1, 2, 3, 4).")
            print("")

    return user




def main():
    while on_loop:
        user = menu()
        if user == "1":
            sat_tb_display()
        elif user == "2":
            satdata_tb_display()
        elif user =="3":
            region_tb_display()
        else:
            exit_menu()




if __name__ == "__main__":
    main()