
from mydb.seed import get_sats, get_data, get_reg, get_sat_ids ,get_data_ids, get_reg_ids
from mydb.seed import delete_sat, delete_region, delete_data
from mydb.seed import add_sat, add_region, add_data
from mydb.seed import update_data, update_region, update_sat
from datetime import datetime

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Satellite Monitoring System")
root.geometry("1600x800")


def back_buttons(my_command=None):
    if my_command:
        button_frame = tk.Frame(root)
        button_frame.pack(padx=10, pady=10)

        back_btn = tk.Button(button_frame, text="Back to Main Menu", command=main_menu)
        back_btn.pack(side="right", padx=30, pady=30)

        back_btn = tk.Button(button_frame, text="Back", command=my_command)
        back_btn.pack( side="left", padx=10, pady=10)
    else:
        back_btn = tk.Button(root, text="Back to Main Menu", command=main_menu)
        back_btn.pack(padx=30, pady=30)

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def display_satellite_table():
    clear_screen()
    
    sats = get_sats()

    tree = ttk.Treeview(root, columns=("Id", "Name", "Orbit Type", "Status", "Description"), show="headings")
    
    tree.heading("Id", text="Satellite Id")
    tree.heading("Name", text="Satellite Name")
    tree.heading("Orbit Type", text="Orbit Type")
    tree.heading("Status", text="Status")
    tree.heading("Description", text="Description")

    for sat in sats:
        tree.insert("", tk.END, values=(sat.id, sat.name, sat.orbit_type, sat.status, sat.description))

    tree.pack(expand=True, fill="both", padx=10, pady=10)

def display_region_table():
    clear_screen()
    
    regions = get_reg()

    tree = ttk.Treeview(root, columns=("Id", "Sat Id", "Name", "Latitude", "Longitude"), show="headings")
    
    tree.heading("Id", text="Id")
    tree.heading("Sat Id", text="Satellite Id")
    tree.heading("Name", text="Name")
    tree.heading("Latitude", text="Latitude")
    tree.heading("Longitude", text="Longitude")

    for reg in regions:
        tree.insert("", tk.END, values=(reg.id, reg.sat_id, reg.name, reg.latitude, reg.longitude))

    tree.pack(expand=True, fill="both", padx=20, pady=20)

def display_data_table():
    clear_screen()
    
    data = get_data()

    tree = ttk.Treeview(root, columns=("Id", "Sat Id", "Data Type", "Data Value", "Date Recorded"), show="headings")
    
    tree.heading("Id", text="Id")
    tree.heading("Sat Id", text="Satellite Id")
    tree.heading("Data Type", text="Data Type")
    tree.heading("Data Value", text="Data Value")
    tree.heading("Date Recorded", text="Date Recorded")

    for dat in data:
        tree.insert("", tk.END, values=(dat.id, dat.sat_id, dat.data_type, dat.data_value, dat.date_recorded))

    tree.pack(expand=True, fill="both", padx=10, pady=10)




# MARK: DISPLAY TABLES

def sat_table():
    display_satellite_table()

    btn2 = tk.Button(root, text="Add new satellite", command=handle_add_sat)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Update satellite value", command=handle_update_sat)
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Delete satellite", command=del_sat)
    btn4.pack(pady=5)

    back_buttons()

    
def data_table():
    display_data_table()

    btn2 = tk.Button(root, text="Add new satellite data", command=handle_add_data)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Update satellite data value", command=handle_update_data)
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Delete satellite data", command=del_data)
    btn4.pack(pady=5)

    back_buttons()


def reg_table():
    display_region_table()

    btn2 = tk.Button(root, text="Add new region", command=handle_add_reg)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Update region value", command=handle_update_reg)
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Delete region", command=del_reg)
    btn4.pack(pady=5)

    back_buttons()


def display_table():
    clear_screen()

    label = tk.Label(root, text="Choose Table", font=("Arial", 14, "bold"))
    label.pack(padx=10, pady=10)

    btn1 = tk.Button(root, text="Satellite Table", command=sat_table)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Satellite Data Table", command=data_table)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Region Table", command=reg_table)
    btn3.pack(pady=5)




# MARK: CREATE TABLES VARIABLES 

def handle_add_sat():
    display_satellite_table()

    form_label = tk.Label(root, text="Satellite Form", font=("Arial", 14))
    form_label.pack(padx=10, pady=10)

    name_label = tk.Label(root, text="Satellite Name:")
    name_label.pack(padx=5, pady=5)
    entry_name = tk.Entry(root)
    entry_name.pack()

    orbit_label = tk.Label(root, text="Orbit Type: [MEO, LEO, GEO]")
    orbit_label.pack(padx=5, pady=5)
    entry_orbit = tk.Entry(root)
    entry_orbit.pack()

    status_label = tk.Label(root, text="Status: [active, inactive]")
    status_label.pack(padx=5, pady=5)
    entry_status = tk.Entry(root)
    entry_status.pack()

    des_label = tk.Label(root, text="Description:")
    des_label.pack(padx=5, pady=5)
    entry_desc = tk.Entry(root)
    entry_desc.pack()



    def add_sat_details():
        name = entry_name.get().capitalize().strip()
        orbit_type = entry_orbit.get().upper().strip()
        status = entry_status.get().lower().strip()
        description = entry_desc.get().capitalize().strip()

        if name and orbit_type and status and description:
            if orbit_type in ['MEO', 'LEO', 'GEO'] and status in ['active', 'inactive']:
                add_sat(name, orbit_type, status, description)
                messagebox.showinfo("Adding Info","New Satellite has been added.")
                sat_table()

            elif orbit_type not in ['MEO', 'LEO', 'GEO'] :
                messagebox.showerror("ValueError", "Orbit type is not in [MEO, LEO, GEO]")
            
            else:
                messagebox.showerror("ValueError", "Status is not in [active, inactive]")

        else:
            messagebox.showinfo("Info","Please fill the whole form")

    add_btn = tk.Button(root, text="Add", command=add_sat_details)
    add_btn.pack(padx=10, pady=10)

    back_buttons(sat_table)


def handle_add_data():
    display_data_table()

    form_label = tk.Label(root, text="Satellite Data Form", font=("Arial", 14))
    form_label.pack(padx=10, pady=10)

    sat_ids = get_sat_ids()
    sat_id_label = tk.Label(root, text=f"Satellite Id {sat_ids}:")
    sat_id_label.pack(padx=5, pady=5)
    entry_sat_id = tk.Entry(root)
    entry_sat_id.pack()

    type_label = tk.Label(root, text="Data Type: ")
    type_label.pack(padx=5, pady=5)
    entry_type = tk.Entry(root)
    entry_type.pack()

    value_label = tk.Label(root, text="Data Value: ")
    value_label.pack(padx=5, pady=5)
    entry_value = tk.Entry(root)
    entry_value.pack()

    date_label = tk.Label(root, text="Date Recorded: [YYYY-MM-DD] ")
    date_label.pack(padx=5, pady=5)
    entry_date = tk.Entry(root)
    entry_date.pack()

    def add_data_details():
        sat_id = entry_sat_id.get().strip()
        data_type = entry_type.get().strip().capitalize()
        data_value = entry_value.get().strip()
        date_rec = entry_date.get().strip()
        date_recorded = False

        if sat_id and data_type and data_value and date_rec:
            try:
                date_recorded = datetime.strptime(date_rec,  "%Y-%m-%d").date()
            except:
                messagebox.showerror("Invalid Date", "Please add a valid date: eg 2025-10-06")    
            
            if date_recorded:
                try:
                    sat_id = int(sat_id)
                    if sat_id in sat_ids:
                        add_data(sat_id, data_type, data_value, date_recorded)
                        messagebox.showinfo("Adding Info","New Satellite Data has been added.")
                        data_table()
                    else:
                        messagebox.showerror("ValueError", "Satellite Id does not exist!")
                except:
                    if not isinstance(sat_id,int):
                        messagebox.showerror("ValueError", "Satellite Id is not an Integer")
                    elif not date_recorded:
                        messagebox.showerror("Invalid Date", "Please add a valid date: eg 2025-10-06") 
                    else:
                        messagebox.showerror("ValueError", "Unexpected Error")
        else:
            messagebox.showinfo("Info","Please fill the whole form")

    add_btn = tk.Button(root, text="Add", command=add_data_details)
    add_btn.pack(padx=10, pady=10)

    back_buttons(data_table)


def handle_add_reg():
    display_region_table()


    form_label = tk.Label(root, text="Region Form", font=("Arial", 14))
    form_label.pack(padx=10, pady=10)

    sat_ids = get_sat_ids()
    sat_id_label = tk.Label(root, text=f"Satellite Id {sat_ids}:")
    sat_id_label.pack(padx=5, pady=5)
    entry_sat_id = tk.Entry(root)
    entry_sat_id.pack()

    name_label = tk.Label(root, text="Region Name: ")
    name_label.pack(padx=5, pady=5)
    entry_name = tk.Entry(root)
    entry_name.pack()

    lat_label = tk.Label(root, text="Latitude: ")
    lat_label.pack(padx=5, pady=5)
    entry_lat = tk.Entry(root)
    entry_lat.pack()

    long_label = tk.Label(root, text="Longitude: ")
    long_label.pack(padx=5, pady=5)
    entry_long = tk.Entry(root)
    entry_long.pack()

    def add_reg_details():
        sat_id = entry_sat_id.get().strip()
        name = entry_name.get().strip().capitalize()
        latitude = entry_lat.get().strip()
        longitude = entry_long.get().strip()

        if sat_id and name and latitude and longitude:
            try:
                sat_id = int(sat_id)
                latitude = float(latitude)
                longitude = float(longitude)

                if sat_id in sat_ids:
                    add_region(int(sat_id), name, float(latitude), float(longitude))
                    messagebox.showinfo("Adding Info","New Region has been added.")
                    reg_table()
                else:
                    messagebox.showerror("404", "Satellite Id does not exist")

            except:
                if not isinstance(sat_id, int):
                    messagebox.showerror("Value Error", "Satellite Id is not an Integer")
                elif not isinstance(latitude, float):
                    messagebox.showerror("Value Error", "Latitude is not a Float")
                else:
                    messagebox.showerror("Value Error", "Longitude is not a Float")

        else:
            messagebox.showinfo("Info","Please fill the whole form")

    add_btn = tk.Button(root, text="Add", command=add_reg_details)
    add_btn.pack(padx=10, pady=10)

    back_buttons(reg_table)




# MARK: UPDATE TABLES VARIABLES 

def verify_sat(column, var):

    if column == "orbit_type":
        if var in ['LEO', 'MEO', 'GEO']:
            return True
        else:
            messagebox.showerror("ValueError", f"{var} should either be MEO, LEO or GEO")
    
    elif column == "status":
        if var in ['active', 'inactive']:
            return True
        else:
            messagebox.showerror("ValueError", f"{var} should either be active or inactive")

    else:
        return True

def handle_update_sat():
    display_satellite_table()

    sat_ids = get_sat_ids()

    id_label = tk.Label(root, text=f"Select Satellite Id to update {sat_ids}:")
    id_label.pack(padx=5, pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack()

    column_label = tk.Label(root, text="Enter Column Name [name, orbit_type, status, description]:")
    column_label.pack(padx=5, pady=5)
    entry_column = tk.Entry(root)
    entry_column.pack()

    var_label = tk.Label(root, text="Enter your Edit: ")
    var_label.pack(padx=5, pady=5)
    entry_var = tk.Entry(root)
    entry_var.pack()
        
    def edit_sat():
        sat_id = entry_id.get().strip()
        column = entry_column.get().strip().lower()
        var = entry_var.get().strip()

        try:
            sat_id = int(sat_id)

            if sat_id and column and var:

                if column in ['name', 'orbit_type', 'status', 'description'] and sat_id in sat_ids:

                    if verify_sat(column, var):
                        update_sat(sat_id, column, var)
                        messagebox.showinfo("Editing Info",f"Satellite of ID {sat_id} has been edited")
                        sat_table()

                elif sat_id not in sat_ids:
                    messagebox.showerror("404 Not Found", "Satellite Id does not exist!")
                else:
                    messagebox.showerror("404 Not Found", "Column is not found")

            else:
                messagebox.showinfo("Edit","Please fill the whole form")

        except:
            messagebox.showerror("ValueError", "Satellite Id is not an Integer!")

    btn = tk.Button(root, text="Edit", command=edit_sat)
    btn.pack(padx=5, pady=5)

    back_buttons(sat_table)

def verify_data(column, var):
    data_ids = get_data_ids()

    if column == "sat_id":
        try:
            var = int(var)
            if var in data_ids:
                return True
            else:
                messagebox.showerror("404 Not Found", "No sat_id found")
        except:
            messagebox.showinfo("Invalid Edit",f"{var} should be an Integer")
    else: 
        return True

def handle_update_data():
    display_data_table()

    data_ids = get_data_ids()

    id_label = tk.Label(root, text=f"Select Satellite Data Id to update {data_ids}:")
    id_label.pack(padx=5, pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack()

    column_label = tk.Label(root, text="Enter Column Name [sat_id, data_type, data_value, date_recorded]:")
    column_label.pack(padx=5, pady=5)
    entry_column = tk.Entry(root)
    entry_column.pack()

    var_label = tk.Label(root, text="Enter your Edit: ")
    var_label.pack(padx=5, pady=5)
    entry_var = tk.Entry(root)
    entry_var.pack()
        
    def edit_data():
        data_id = entry_id.get().strip()
        column = entry_column.get().strip().lower()
        var = entry_var.get().strip()

        try:
            data_id = int(data_id)

            if data_id and column and var:

                if column in ['sat_id', 'data_type', 'data_value', 'date_recorded'] and data_id in data_ids:

                    if verify_data(column, var):
                        update_data(data_id, column, var)
                        messagebox.showinfo("Editing Info",f"Satellite Data of Id {data_id} has been edited")
                        data_table()

                elif data_id not in data_ids:
                    messagebox.showerror("404 Not Found", "Satellite Data Id is not found!")
                else:
                    messagebox.showerror("404 Not Found", "Column not found!")

            else:
                messagebox.showinfo("Edit","Please fill the whole form")

        except:
            messagebox.showerror("ValueError", "Satellite Data Id is not an Integer")

    btn = tk.Button(root, text="Edit", command=edit_data)
    btn.pack(padx=5, pady=5)

    back_buttons(data_table)


def verify_reg(column, var):
    sat_ids = get_sat_ids()

    if column == "sat_id":
        try:
            var = int(var)
            if var in sat_ids:
                return True
            else:
                messagebox.showerror("404 Not Found", "No sat_id found")
        except:
            messagebox.showinfo("Invalid Edit",f"{var} should be an Integer")
    
    elif column == "latitude":
        try:
            var = float(var)
            return True
        except:
            messagebox.showinfo("Invalid Edit",f"{var} should be an Float")

    elif column == "latitude":
        try:
            var = float(var)
            return True
        except:
            messagebox.showinfo("Invalid Edit",f"{var} should be an Float")
    
    else:
        return True

def handle_update_reg():
    display_region_table()

    reg_ids = get_reg_ids()

    id_label = tk.Label(root, text=f"Select Region Id to update {reg_ids}:")
    id_label.pack(padx=5, pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack()

    column_label = tk.Label(root, text="Enter Column Name [sat_id, name, latitude, longitude]:")
    column_label.pack(padx=5, pady=5)
    entry_column = tk.Entry(root)
    entry_column.pack()

    var_label = tk.Label(root, text="Enter your Edit: ")
    var_label.pack(padx=5, pady=5)
    entry_var = tk.Entry(root)
    entry_var.pack()
        
    def edit_reg():
        reg_id = entry_id.get().strip()
        column = entry_column.get().strip().lower()
        var = entry_var.get().strip()

        try:
            reg_id = int(reg_id)

            if reg_id and column and var:

                if column in ['sat_id', 'name', 'latitude', 'longitude'] and reg_id in reg_ids:

                    if verify_reg(column,var):
                        update_region(reg_id, column, var)
                        messagebox.showinfo("Editing Info",f"Region of ID {reg_id} has been edited")
                        reg_table()

                elif reg_id not in reg_ids:
                    messagebox.showerror("404 Not Found", "Region Id is not found!")
                else:
                    messagebox.showerror("404 Not Found", "Column not found!")

            else:
                messagebox.showinfo("Edit","Please fill the whole form")
        
        except:
            messagebox.showerror("ValueError", "Region Id is not an Integer")

    btn = tk.Button(root, text="Edit", command=edit_reg)
    btn.pack(padx=5, pady=5)

    back_buttons(reg_table)




# MARK: DELETE TABLES

def del_sat():
    display_satellite_table()

    sat_ids = get_sat_ids()

    label = tk.Label(root, text=f"Enter Satellite ID to delete {sat_ids}:")
    label.pack(padx=5, pady=5)
    entry = tk.Entry(root)
    entry.pack()

    def deleting_sat():
        val = entry.get().strip()

        if val:
            try:
                val = int(val)

                if val in sat_ids:
                    delete_sat(val)
                    messagebox.showinfo("Delete Info",f"Deleted Satellite of Id: {val}")
                    sat_table()
                else:
                     messagebox.showerror("404 Not Found", "Satellite Id not found!")

            except:
                messagebox.showerror("ValueError", "Satellite Id is not an Integer")
        else:
            messagebox.showerror("Empty Value Given", "Please give a Satellite Id")
        
    btn = tk.Button(root, text="Delete", command=deleting_sat)
    btn.pack(padx=5, pady=5)

    back_buttons(sat_table)


def del_data():
    display_data_table()

    data_ids = get_data_ids()

    label = tk.Label(root, text=f"Enter Satellite Data ID to delete {data_ids}:")
    label.pack(padx=5, pady=5)
    entry = tk.Entry(root)
    entry.pack()

    def deleting_data():
        val = entry.get().strip()

        if val:
            try:
                val = int(val)

                if val in data_ids:
                    delete_data(val)
                    messagebox.showinfo("Delete Info",f"Deleted Satellite Data of Id: {val}")
                    data_table()
                else:
                    messagebox.showerror("404 Not Found", "Satellite Data not found!")

            except:
                messagebox.showerror("ValueError", "Satellite  Data Id is not an Integer")
        else:
            messagebox.showerror("Empty Value Given", "Please give a Satellite Data Id")
        
    btn = tk.Button(root, text="Delete", command=deleting_data)
    btn.pack(padx=5, pady=5)

    back_buttons(data_table)


def del_reg():
    display_region_table()

    reg_ids = get_reg_ids()

    label = tk.Label(root, text=f"Enter Region ID to delete {reg_ids}:")
    label.pack(padx=5, pady=5)
    entry = tk.Entry(root)
    entry.pack()

    def deleting_reg():
        val = entry.get().strip()
        if val:
            try:
                val = int(val)

                if val in reg_ids:
                    delete_region(val)
                    messagebox.showinfo("Delete Info",f"Deleted Region of Id: {val}")
                    reg_table()
                else:
                    messagebox.showerror("404 Not Found", "Region Id not found!")
            
            except:
                messagebox.showerror("ValueError", "Region Id is not an Integer")
        else:
            messagebox.showerror("Empty Value Given", "Please give a Region Id")
        
    btn = tk.Button(root, text="Delete", command=deleting_reg)
    btn.pack(padx=5, pady=5)

    back_buttons(reg_table)




def main_menu():
    clear_screen()

    label = tk.Label(root, text="Satellite Monitoring System DataBase", font=("Arial", 14, "bold"))
    label.pack(padx=10, pady=10)

    display_table()

    btn5 = tk.Button(root, text="Exit", command=exit)
    btn5.pack(padx=20, pady=20)


def main():
    main_menu()
    root.mainloop()




if __name__ == "__main__":
    main()
