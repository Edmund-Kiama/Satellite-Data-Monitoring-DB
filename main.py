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
from sqlalchemy import select

on_loop = True

def display_table():
    pass
def create_table():
    pass
def update_table():
    pass
def delete_table():
    pass
def exit_menu():
    global on_loop
    on_loop = False

def menu():
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
            print("f{user} is Invalid! Choose either 1, 2, 3, 4, 5.")

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