
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



# MARK: DISPLAY TABLES

def sat_table():
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

    back_buttons(display_table)

def data_table():
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

    back_buttons(display_table)

def reg_table():
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
    
    back_buttons(display_table)

def display_table():
    clear_screen()

    label = tk.Label(root, text="Choose Table to display ", font=("Arial", 14, "bold"))
    label.pack(padx=10, pady=10)

    btn1 = tk.Button(root, text="Satellite Table", command=sat_table)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Satellite Data Table", command=data_table)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Region Table", command=reg_table)
    btn3.pack(pady=5)

    back_buttons()



# MARK: CREATE TABLES

# def create_table():
#     messagebox.showinfo("Create", "Creating a new table value...")



# MARK: UPDATE TABLES

# def update_table():
#     messagebox.showinfo("Update", "Updating a table value...")



# MARK: DELETE TABLES

def del_sat():
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
        delete_table()
        
    btn = tk.Button(root, text="Delete", command=deleting_sat)
    btn.pack(padx=5, pady=5)

    back_buttons(delete_table)

def del_data():
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
        delete_table()
        
    btn = tk.Button(root, text="Delete", command=deleting_data)
    btn.pack(padx=5, pady=5)

    back_buttons(delete_table)

def del_reg():
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
        delete_table()
        
    btn = tk.Button(root, text="Delete", command=deleting_reg)
    btn.pack(padx=5, pady=5)

    back_buttons(delete_table)

def delete_table():
    clear_screen()

    label = tk.Label(root, text="Choose Table to delete ", font=("Arial", 14, "bold"))
    label.pack(padx=10, pady=10)

    btn1 = tk.Button(root, text="Satellite Table", command=del_sat)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Satellite Data Table", command=del_data)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Region Table", command=del_reg)
    btn3.pack(pady=5)

    back_buttons()



def main_menu():
    clear_screen()

    label = tk.Label(root, text="Satellite Monitoring System", font=("Arial", 14, "bold"))
    label.pack(padx=10, pady=10)

    btn1 = tk.Button(root, text="Display Tables", command=display_table)
    btn1.pack(pady=5)

    # btn2 = tk.Button(root, text="Create New Table Value", command=create_table)
    # btn2.pack(pady=5)

    # btn3 = tk.Button(root, text="Update Table Value", command=update_table)
    # btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Delete Table Value", command=delete_table)
    btn4.pack(pady=5)

    btn5 = tk.Button(root, text="Exit", command=exit)
    btn5.pack(pady=5)



def main():
    main_menu()
    root.mainloop()

if __name__ == "__main__":
    main()
