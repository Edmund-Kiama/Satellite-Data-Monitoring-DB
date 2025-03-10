
from mydb.session import get_sats, get_reg, get_data, get_sat_ids, get_data_ids, get_reg_ids
from mydb.session import delete_sat, delete_region, delete_data
from mydb.session import add_sat, add_region, add_data
from mydb.session import update_data, update_region, update_sat

on_loop = True


# mark: Display Functions

def sat_tb_display():
    sats = get_sats()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("                             Satellite Table")
    print("------------------------------------------------------------------------------------------")
    print("| Id    |   Name        | Orbit Type |   Status    |   Description                       ")
    print("------------------------------------------------------------------------------------------")
    for sat in sats:
        print(f"| {sat.id:<3}   |   {sat.name:<10}  |   {sat.orbit_type:<5}    |   {sat.status:<8}  |   {sat.description:<20}")
    print("------------------------------------------------------------------------------------------")
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")

def satdata_tb_display():
    data = get_data()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("                             Satellite Data Table")
    print("-------------------------------------------------------------------------------")
    print("| Id    | Sat Id |       Data Type           |  Data Value   |  Date recorded ")
    print("-------------------------------------------------------------------------------")
    for dat in data:
        print(f"| {dat.id:<3}   |   {dat.sat_id:<3}  |   {dat.data_type:<20}    |   {dat.data_value:<10}  |   {dat.date_recorded:<10}")
    print("------------------------------------------------------------------------------")
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    

def region_tb_display():
    regions = get_reg()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("                             Region Table")
    print("------------------------------------------------------------------------")
    print("| Id    | Sat Id |        Name               |  Latitude  |  Longitude ")
    print("------------------------------------------------------------------------")
    for reg in regions:
        print(f"| {reg.id:<3}   |   {reg.sat_id:<3}  |   {reg.name:<20}    |   {reg.latitude:<7}  |   {reg.longitude:<7}")
    print("------------------------------------------------------------------------")
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")


def display_table():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Choose Table to Display")
    print("-----------------------")
    print("1. Satellites table")
    print("2. Satellites Data table")
    print("3. Regions table")
    print("")

    while True:
        user = input("Which table is to be displayed: ")
        print("")
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

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
   



#mark: Create function

def handle_sat_create():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("You chose to add in Satellite table")
    print("Values required are: name, orbit_type,status.description")
    print("")

    name = input("Satellite's name: ")
    print("")
    while True:
        orbit_type = input("Satellite's orbit type ['MEO', 'LEO', 'GEO']: ")
        print("")
        if orbit_type in ["MEO", "LEO", "GEO"]:
            break
        else: 
            raise ValueError("Status can only be 'MEO' or 'LEO' OR 'GEO' .")

    while True:
        status = input("Satellite's status ['active', 'inactive']: ")
        print("")
        if status in ["active", "inactive"]:
            break
        else: 
            raise ValueError("Status can only be 'active' or 'inactive' .")
                
    description = input("Satellite's description: ")
    print("")

    if name and orbit_type and status and description:
        add_sat(name, orbit_type, status, description)
        print("-------------------------------------------")
        print("New Satellite Instance has been added.")
        print("-------------------------------------------")
        print("")
    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")


def handle_satdata_create():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("You chose to add in SatelliteData table")
    print("Values required are: name, orbit_type,status.description")
    print("")

    while True:
        try:
            sat_idx = int(input("Satellite Id that took the data recording: "))
            print("")
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")  
            print("")

    type_data = input("Type of Data: ")
    print("")
    value_data = input("Value of Data: ")
    print("")
    date = input("Date of recording Data [YYYY-MM-DD]: ")
    print("")

    if sat_idx and type_data and value_data and date:
        add_data(sat_idx, type_data, value_data, date)
        print("-------------------------------------------")
        print("New Satellite Data Instance has been added.")
        print("--------------------------------------------")
        print("")
    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")


def handle_region_create():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("You chose to add in Region table")
    print("Values required are: sat_id, name, latitude, longitude")
    print("")

    while True:
        try:
            sat_idx = int(input("Satellite Id for the region: "))
            print("")
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")  
            print("")

    reg_name = input("Name of the region: ")
    print("")

    while True:
        try:
            reg_latitude = float(input("Latitude of the region: "))
            print("")
            break
        except ValueError:
            print("Invalid input! Please enter a Float.")  
            print("")
    
    while True:
        try:
            reg_longitude = float(input("Longitude of the region: "))
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
    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")


def create_table():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Choose from which table to create instances for")
    print("-----------------------")
    print("1. Satellites table")
    print("2. Satellites Data table")
    print("3. Regions table")
    print("")

    while True:
        user = input("Which table do you wanna create instances from: ")
        print("")
        if user in ["1", "2", "3"]:
            break
        else:
            print(f"{user} is Invalid Input. Choose in (1, 2, 3)")
            print("")
    
    if user == "1":
        handle_sat_create()
    elif user == "2":
        handle_satdata_create()
    else:
        handle_region_create()



# mark: Update Function   

def handle_sat_edit():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("You chose to edit in Satellite table")
    print("")
    print("Which satellite do you wanna edit?")
    
    while True:
        try:
            sat_id = int(input("Choose by Id: "))
            break
        except ValueError:
            print("")
            print(f"{sat_id} is not an Integer. Try again")
            print("")

    print("Satellite Columns = ['name','orbit_type','status','description']")
    print("")
    variable = input("Which of its column is to be edited?")
    print("")
    new_value = input("What's the new value: ")
    print("")

    if sat_id and variable and new_value:
        update_sat(sat_id, variable, new_value)
        print("---------------------------------------------")
        print("          Update is successful!")
        print("---------------------------------------------")
        print("")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("")


def handle_reg_edit():
    pass


def handle_data_update():
    pass


def update_table():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Choose Table to Edit")
    print("-----------------------")
    print("1. Satellites table")
    print("2. Satellites Data table")
    print("3. Regions table")
    print("")

    while True:
        user = input("Which table is to be edited: ")
        print("")
        if user in ["1", "2", "3"]:
            break
        else:
            print(f"{user} is Invalid Input. Choose in (1, 2, 3)")
            print("")
    
    if user == "1":
        handle_sat_edit()
    elif user == "2":
        handle_data_edit()
    else:
        handle_region_edit()



# mark: Delete Functions
def handle_sat_delete():
    sat_tb_display()
    sat_ids = get_sat_ids()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print(f"Choose which satellite to delete according to its Id: {sat_ids}")
    print("")

    while True:
        user = int(input("Choose Id: "))
        print("")
        if user in sat_ids:
            break
        else:
            print(f"No satellite with Id of {user}")
            print("")
    
    delete_sat(user)
    print("-----------------------------------------------------------------")
    print(f"     Satellite of Id {user} has been deleted successfully!!")
    print("-----------------------------------------------------------------")
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")


def handle_region_delete():
    region_tb_display()
    reg_ids = get_reg_ids()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print(f"Choose which region to delete according to its Id: {reg_ids}")
    print("")

    while True:
        user = int(input("Choose Id: "))
        print("")
        if user in reg_ids:
            break
        else:
            print(f"No Region with Id of {user}")
    
    delete_region(user)
    print("-----------------------------------------------------------------")
    print(f"     Region of Id {user} has been deleted successfully!!")
    print("-----------------------------------------------------------------")
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")


def handle_data_delete():
    satdata_tb_display()
    data_ids = get_data_ids()

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print(f"Choose which Data Type to delete according to its Id: {data_ids}")
    print("")

    while True:
        user = int(input("Choose Id: "))
        print("")
        if user in data_ids:
            break
        else:
            print(f"No Data Type with Id of {user}")
    
    delete_data(user)
    print("-----------------------------------------------------------------")
    print(f"     Data Type of Id {user} has been deleted successfully!!")
    print("-----------------------------------------------------------------")
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")


def delete_table():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    print("Choose Table to Delete")
    print("-----------------------")
    print("1. Satellites table")
    print("2. Satellites Data table")
    print("3. Regions table")
    print("")

    while True:
        user = input("Which table is to be deleted: ")
        print("")
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
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("                          Exited   from    the     system     ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("")
    



def menu():
    print("")
    print("######################################################################")
    print("               SATELLITE     MONITORING      SYSTEM")
    print("")
    print("Choose your Options")
    print("-------------------")
    print("1. Display tables")
    print("2. Create new table value")
    print("3. Update table value")
    print("4. Delete table value")
    print("5. Exit")
    print("")
    print("######################################################################")
    print("")

    while True:
        user = input("Your option [1, 2, 3, 4, 5]: ")
        print("")
        print("")
        if user in ["1", "2", "3", "4", "5"]:
            break;
        else:
            print("f{user} is Invalid! Choose in (1, 2, 3, 4, 5).")
            print("")

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



if __name__ == "__main__":
    main()