
from mydb.session import get_sats, get_data, get_reg, get_sat_ids ,get_data_ids, get_reg_ids
from mydb.session import delete_sat, delete_region, delete_data
from mydb.session import add_sat, add_region, add_data
from mydb.session import update_data, update_region, update_sat

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Satellite Monitoring System")
root.geometry("1500x800")


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

    orbit_label = tk.Label(root, text="Orbit Type: ['MEO', 'LEO', 'GEO']")
    orbit_label.pack(padx=5, pady=5)
    entry_orbit = tk.Entry(root)
    entry_orbit.pack()

    status_label = tk.Label(root, text="Status: ['active', 'inactive']")
    status_label.pack(padx=5, pady=5)
    entry_status = tk.Entry(root)
    entry_status.pack()

    des_label = tk.Label(root, text="Description:")
    des_label.pack(padx=5, pady=5)
    entry_desc = tk.Entry(root)
    entry_desc.pack()

    def add_sat_details():
        name = entry_name.get()
        orbit_type = entry_orbit.get()
        status = entry_status.get()
        description = entry_desc.get()

        if name and orbit_type and status and description:
            add_sat(name, orbit_type, status, description)

            messagebox.showinfo("Adding Info","New Satellite has been added.")
            sat_table()
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

    date_label = tk.Label(root, text="Date Recorded: ")
    date_label.pack(padx=5, pady=5)
    entry_date = tk.Entry(root)
    entry_date.pack()

    def add_data_details():
        sat_id = entry_sat_id.get()
        data_type = entry_type.get()
        data_value = entry_value.get()
        date_recorded = entry_date.get()

        if sat_id and data_type and data_value and date_recorded:
            add_data(int(sat_id), data_type, data_value, date_recorded)

            messagebox.showinfo("Adding Info","New Satellite Data has been added.")
            data_table()
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
        sat_id = entry_sat_id.get()
        name = entry_name.get()
        latitude = entry_lat.get()
        longitude = entry_long.get()

        if sat_id and name and latitude and longitude:
            add_region(int(sat_id), name, float(latitude), float(longitude))

            messagebox.showinfo("Adding Info","New Region has been added.")
            reg_table()
        else:
            messagebox.showinfo("Info","Please fill the whole form")

    add_btn = tk.Button(root, text="Add", command=add_reg_details)
    add_btn.pack(padx=10, pady=10)

    back_buttons(reg_table)




# MARK: UPDATE TABLES VARIABLES 

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
        sat_id = entry_id.get()
        column = entry_column.get()
        var = entry_var.get()

        if sat_id and column and var:
            update_sat(int(sat_id), column, var)
            messagebox.showinfo("Editing Info",f"Satellite of ID {sat_id} has been edited")
            sat_table()
        else:
            messagebox.showinfo("Edit","Please fill the whole form")

    btn = tk.Button(root, text="Edit", command=edit_sat)
    btn.pack(padx=5, pady=5)

    back_buttons(sat_table)


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
        data_id = entry_id.get()
        column = entry_column.get()
        var = entry_var.get()

        if data_id and column and var:
            update_data(int(data_id), column, var)
            messagebox.showinfo("Editing Info",f"Satellite Data of Id {data_id} has been edited")
            data_table()
        else:
            messagebox.showinfo("Edit","Please fill the whole form")

    btn = tk.Button(root, text="Edit", command=edit_data)
    btn.pack(padx=5, pady=5)

    back_buttons(data_table)


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
        reg_id = entry_id.get()
        column = entry_column.get()
        var = entry_var.get()

        if reg_id and column and var:
            update_region(int(reg_id), column, var)
            messagebox.showinfo("Editing Info",f"Region of ID {reg_id} has been edited")
            reg_table()
        else:
            messagebox.showinfo("Edit","Please fill the whole form")

    btn = tk.Button(root, text="Edit", command=edit_reg)
    btn.pack(padx=5, pady=5)

    back_buttons(reg_table)




# MARK: DELETE TABLES

def del_sat():
    display_satellite_table()

    user_input = tk.StringVar()
    sat_ids = get_sat_ids()

    label = tk.Label(root, text=f"Enter Satellite ID to delete {sat_ids}:")
    label.pack()

    entry = tk.Entry(root, textvariable=user_input)
    entry.pack(padx=5, pady=5)

    def deleting_sat():
        val = user_input.get()
        delete_sat(val)
        messagebox.showinfo("Delete Info",f"Deleted Satellite of Id: {val}")
        sat_table()
        
    btn = tk.Button(root, text="Delete", command=deleting_sat)
    btn.pack(padx=5, pady=5)

    back_buttons(sat_table)


def del_data():
    display_data_table()

    user_input = tk.StringVar()
    data_ids = get_data_ids()

    label = tk.Label(root, text=f"Enter Satellite Data ID to delete {data_ids}:")
    label.pack()

    entry = tk.Entry(root, textvariable=user_input)
    entry.pack(padx=5, pady=5)

    def deleting_data():
        val = user_input.get()
        delete_data(val)
        messagebox.showinfo("Delete Info",f"Deleted Satellite Data of Id: {val}")
        data_table()
        
    btn = tk.Button(root, text="Delete", command=deleting_data)
    btn.pack(padx=5, pady=5)

    back_buttons(data_table)


def del_reg():
    display_region_table()

    user_input = tk.StringVar()
    reg_ids = get_reg_ids()

    label = tk.Label(root, text=f"Enter Region ID to delete {reg_ids}:")
    label.pack()

    entry = tk.Entry(root, textvariable=user_input)
    entry.pack(padx=5, pady=5)

    def deleting_reg():
        val = user_input.get()
        delete_region(val)
        messagebox.showinfo("Delete Info",f"Deleted Region of Id: {val}")
        reg_table()
        
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
