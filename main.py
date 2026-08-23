import sqlite3
import tkinter.messagebox
from tkinter import ttk


# function to get, compile, and post data to console and database
def enter_data():
    accepted = accept_var.get()

    # If user has accepted the terms
    if accepted == 'Accepted':
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        email = email_entry.get()

        # If all fields are filled out, then continue
        if firstname and lastname and email:
            # User Info
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Personal Data
            registration_status = reg_status_var.get()
            numofdegrees = numofdegrees_spinbox.get()
            numofkids = numofkids_spinbox.get()

            # Address
            address = f'{address_entry.get()} {city_entry.get()}, {state_entry.get()} {zip_entry.get()}'

            # Print to console. (not necessary, but helpful)
            print('First Name: ', firstname, ' Last Name: ', lastname, ' Email: ', email)
            print('Title: ', title, ' Age: ', age, ' Nationality: ', nationality)
            print('Address: ', address)
            print('# Kids: ', numofkids, '# of Degrees: ', numofdegrees)
            print('Registration Status: ', registration_status)
            print('------------------------------------------')

            # Database Connection and table configuration
            conn = sqlite3.connect('data.db')
            table_create_query = '''
                CREATE TABLE IF NOT EXISTS persona_data (
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    email TEXT NOT NULL,
                    title TEXT,
                    age INT NOT NULL,
                    nationality TEXT NOT NULL,
                    address TEXT NOT NULL,
                    registration_status TEXT NOT NULL,
                    num_degrees INT NOT NULL,
                    num_kids INT NOT NULL)'''
            conn.execute(table_create_query)

            data_insert_query = '''
                INSERT INTO persona_data (firstname, lastname, email, title, age, nationality, address, registration_status, num_degrees, num_kids)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, email, title, age, nationality, address, registration_status, numofdegrees, numofkids)
            cursor = conn.cursor()

            # Execute data insert, and commit changes then close connection to database.
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            conn.close()

        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name and email are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")


# Main window
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
email_label = tkinter.Label(user_info_frame, text='Email')
first_name_label.grid(row=0, column=0)
last_name_label.grid(row=0, column=1)
email_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
email_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
email_entry.grid(row=1, column=2)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=2, column=0)
title_combobox.grid(row=3, column=0)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=1)
age_spinbox.grid(row=3, column=1)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame,
                                    values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania",
                                            "South America"])
nationality_label.grid(row=2, column=2)
nationality_combobox.grid(row=3, column=2)

# Add all children components to the parent // "binding"
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Getting the address fields
address_frame = tkinter.LabelFrame(frame, text="Address")
address_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

address_label = tkinter.Label(address_frame, text="Street")
address_entry = tkinter.Entry(address_frame)
address_label.grid(row=1, column=0)
address_entry.grid(row=2, column=0)

city_label = tkinter.Label(address_frame, text="City")
city_entry = tkinter.Entry(address_frame)
city_label.grid(row=1, column=1)
city_entry.grid(row=2, column=1)

state_label = tkinter.Label(address_frame, text='State')
state_entry = tkinter.Entry(address_frame)
state_label.grid(row=1, column=2)
state_entry.grid(row=2, column=2)

zip_label = tkinter.Label(address_frame, text='Zip Code')
zip_entry = tkinter.Entry(address_frame)
zip_label.grid(row=1, column=3)
zip_entry.grid(row=2, column=3)

# Saving Private Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numoofdegrees_label = tkinter.Label(courses_frame, text="# Degrees")
numofdegrees_spinbox = tkinter.Spinbox(courses_frame, from_=0.0, to=99.0)
numoofdegrees_label.grid(row=0, column=1)
numofdegrees_spinbox.grid(row=1, column=1)

numofkids_label = tkinter.Label(courses_frame, text="# Kids")
numofkids_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=99.0)
numofkids_label.grid(row=0, column=2)
numofkids_spinbox.grid(row=1, column=2)

graduated_label = tkinter.Label(courses_frame, text="Graduation Status")
grad_status_var = tkinter.StringVar(value="Not Graduated")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Graduated",
                                       variable=reg_status_var, onvalue="Graduated", offvalue="Not Graduated")
graduated_label.grid(row=0, column=3)
registered_check.grid(row=1, column=3)

# Add all children components to the parent // "binding"
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

# Start tkinter window
window.mainloop()
