# =========== packages imported ============
from tkinter import *
import tkinter
import os
from tkinter import messagebox
import mysql.connector

# ============= WINDOW CREATION ================
window = tkinter.Tk()
window.title("Add Employee ")
window.geometry('700x800')
window.configure(bg="white")

# ================ Frame Creation ========================
frame = tkinter.Frame(window, bd=5, relief=GROOVE, bg="white")
frame.place(x=0, y=50, width=600, height=620)


# ============== Function ================================

# ------------- BACK FUNCTION ------------------
def back():
    window.withdraw()
    os.system('python manageemp.py')
    window.deiconify()



# ------------------- VALIDATION -------------------------
def checkid(empid_entry):
    if empid_entry.isdigit():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")


def checkname(emp_entry):
    if emp_entry.isalnum():
        return True
    else:
        messagebox.showwarning("Invalid", "Not allowed" + emp_entry[-1])


def checkpassword(pass_entry):
    if len(pass_entry) <= 10:
        return True
    else:
        messagebox.showwarning("Invalid", "Length try to exceed")


def checkcontact(cont_entry):
    if len(cont_entry) <= 10:
        return True
    else:
        messagebox.showwarning("Invalid", "Length try to exceed")


def checkaadharnumber(aadh_entry):
    if len(aadh_entry) <= 12:
        return True
    else:
        messagebox.showwarning("Invalid", "Length try to exceed")


def checkun(un_entry):
    if un_entry.isalnum():
        return True
    else:
        messagebox.showwarning("Invalid", "Not allowed" + un_entry[-1])


def checkaddress(address_entry):
    if address_entry.isalnum():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed" + address_entry[-1])

# =============== Database Connection ======================
def add():
    # ---------- NO NULL VALUE ACCEPTANCE -----------------------
    if empid_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter id')
    elif emp_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter name')
    elif cont_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter contact number')
    elif address_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter address')
    elif aadh_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter  aadharch number')
    elif un_entry.get() == '':
        messagebox.showinfo('Error', 'Please provide user name')
    elif pass_entry.get() == '':
        messagebox.showinfo('Error', 'Please provide password')
    else:
        try:
            # ----------- CONNECTION ---------------
            connection = mysql.connector.connect(host="localhost", port=3306, user="root", password="", database="grocerydb")
            c = connection.cursor()
            ID = empid_entry.get()
            name = emp_entry.get()
            contact_no = cont_entry.get()
            address = address_entry.get()
            aadhar_no = aadh_entry.get()
            user = un_entry.get()
            password = pass_entry.get()
            # ----------------------- MAIN QUERY --------------------------------------
            insert_query = "INSERT INTO `manageemp`(`ID`, `name`, `contact_no`, `address`, `aadhar_no`, `user`, `password`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            vals = (ID, name, contact_no, address, aadhar_no, user, password)
            c.execute(insert_query, vals)
            connection.commit()
            messagebox.showinfo("", "Record Added Successfully")
        except:
            messagebox.showwarning("Error", "Database Connection not Possible")


# ============ Widgets Creation and placing ===============

# ------------ HEADING -------------------
label = tkinter.Label(frame, text="ADD  EMPLOYEE  DETAILS", bg='white', fg='black', font=("Time New Roman", 30))
label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

# ----------------- EMPLOYEE ID -----------
emp_id = tkinter.Label(frame, text="Employee ID:", bg="white", fg='black', font=("Times New Roman", 20))
emp_id.grid(row=1, column=0)
empid_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
empid_entry.grid(row=1, column=1, pady=20)
validate_id = window.register(checkid)
empid_entry.config(validate='key', validatecommand=(validate_id, "%P"))

# ----------------- EMPLOYEE NAME -----------
emp_name = tkinter.Label(frame, text="Employe Name:", bg="white", fg='black', font=("Times New Roman", 20))
emp_name.grid(row=2, column=0)
emp_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
emp_entry.grid(row=2, column=1, pady=20)
validate_name = window.register(checkname)
emp_entry.config(validate="key", validatecommand=(validate_name, "%P"))

# ---------------- EMPLOYEE CONTACT -----------------
emp_cont = tkinter.Label(frame, text="Contact Number:", bg="white", fg='black', font=("Times New Roman", 20))
emp_cont.grid(row=3, column=0)
cont_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
cont_entry.grid(row=3, column=1, pady=20)
validate_contact = window.register(checkcontact)
cont_entry.config(validate="key", validatecommand=(validate_contact, "%P"))

# ------------ ADDRESS -------------------
address = tkinter.Label(frame, text="Address:", bg="white", fg='black', font=("Times New Roman", 20))
address.grid(row=4, column=0)
address_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
address_entry.grid(row=4, column=1, pady=20)
validate_address = window.register(checkaddress)
address_entry.config(validate="key", validatecommand=(validate_address, "%P"))

# ------------------ AADHAR NUMBER ----------------
aadh_lbl = tkinter.Label(frame, text="Aadhar Card Number:", bg="white", fg='black', font=("Times New Roman", 20))
aadh_lbl.grid(row=5, column=0)
aadh_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
aadh_entry.grid(row=5, column=1, pady=20)
validate_aadhar = window.register(checkaadharnumber)
aadh_entry.config(validate="key", validatecommand=(validate_aadhar, "%P"))

# -------------- HEADING ---------------
label1 = tkinter.Label(frame, text="* Provide UserName & Password for Employee*", bg='white', fg='red',
                       font=("Cambria, bold", 15))
label1.grid(row=6, column=0)

# --------------- USERNAME --------------------
un_lbl = tkinter.Label(frame, text="Username:", bg="white", fg='black', font=("Times New Roman", 20))
un_lbl.grid(row=7, column=0)
un_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
un_entry.grid(row=7, column=1, pady=20)
validate_un = window.register(checkun)
un_entry.config(validate="key", validatecommand=(validate_un, "%P"))

# -------------- PASSWORD --------------------
pass_lbl = tkinter.Label(frame, text="Password:", bg="white", fg='black', font=("Times New Roman", 20))
pass_lbl.grid(row=8, column=0)
pass_entry = tkinter.Entry(frame, show="*", font=("Times New Roman", 16))
pass_entry.grid(row=8, column=1, pady=20)
validate_pass = window.register(checkpassword)
pass_entry.config(validate="key", validatecommand=(validate_pass, "%P"))

# ------------------- ADD BUTTON ------------------
add_btn = tkinter.Button(frame, text="Add", bg="#623FA7", fg='#030303', font=("Times New Roman", 20), command=add)
add_btn.grid(row=9, column=0, padx=5, pady=5)


# ---------------- CLEAR FUNCTION -------------------------
def clear():
    empid_entry.delete(0, END)
    emp_entry.delete(0, END)
    cont_entry.delete(0, END)
    address_entry.delete(0, END)
    aadh_entry.delete(0, END)
    un_entry.delete(0, END)
    pass_entry.delete(0, END)

# ----------------- CLEAR BUTTON ----------------------
clear_btn = tkinter.Button(frame, text="Clear", bg="#623FA7", fg='#030303', font=("Times New Roman", 20), command=clear)
clear_btn.grid(row=9, column=1, padx=5, pady=5)


# -------------- EXIT BUTTON ----------------------
back_btn = tkinter.Button(frame, text="Back", bg="#623FA7", fg='#030303', font=("Times New Roman", 20), command=back)
back_btn.grid(row=9, column=2, padx=5, pady=5)

frame.pack()
window.mainloop()
