from doctest import master
from tkinter import *
import os
import mysql.connector
from tkinter import ttk

from PIL import ImageTk, Image

import mysql.connector
from mysql.connector import cursor


class Window:
    def __init__(self, master):
        subframe = Frame(master)
        # ======LABEL FRAME=========
        Button_frame = LabelFrame(subframe, text="WELCOME OWNER!!!", font=("Time New Roman", 16, "bold"),
                                  bg="white",
                                  fg="red")
        Button_frame.place(x=10, y=5, width=1330, height=1330)

        emp_id = Label(subframe, text="Employee ID",bg='white', fg='black', font=("Constantia", 18))
        emp_id.grid(row=1, column=3, pady=40, padx=40)
        empid_entry = Entry(subframe, font=("Comic Sans MS", 15))
        empid_entry.grid(row=1, column=4, pady=3)
        srch_btn = Button(subframe, text="Search", bg='#0A9286', fg='black', font=("Times New Roman", 12), command=search)
        srch_btn.grid(row=1, column=6, padx=10, pady=5)
        labl = Label(subframe, text="Choose Option!!!", bg='white', fg='#BA1F5D', font=("Constantia", 18))
        labl.grid(row=3, column=4, pady=20)
        add_btn = Button(subframe, text="Add Employee Details", bg='#396B26', fg='white', font=("Times New Roman", 15),
                         command=add)
        add_btn.grid(row=4, column=4, pady=25)
        update_btn = Button(subframe, text="Update Employee Details", bg='#085F62', fg='white',
                            font=("Times New Roman", 15), command=update)
        update_btn.grid(row=5, column=4, pady=5)
        delete_btn = Button(subframe, text="Delete Employee Details", bg='#1C257B', fg='white',
                            font=("Times New Roman", 15))
        delete_btn.grid(row=6, column=4, pady=25)
        Exit_btn = Button(subframe, text=" LOGOUT", bg='#F6E4E2', fg='Red', font=("Times New Roman", 12),
                          command=exit)
        Exit_btn.grid(row=7, column=4)
        subframe.pack(expand=True, fill=BOTH, side=LEFT)

        subframe2 = Frame(master, background="red")

        scroll_y = Scrollbar(subframe2, orient=VERTICAL)
        emp_record = ttk.Treeview(subframe2, height=20,
                                  columns=("id", "name", "contact", "add", "aadhar", "username", "password"),
                                  yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        emp_record.heading("id", text="Employee ID")
        emp_record.heading("name", text="Employee Name")
        emp_record.heading("contact", text="Contact Number")
        emp_record.heading("add", text="Address")
        emp_record.heading("aadhar", text="Aadhar Card Number")
        emp_record.heading("username", text="Username")
        emp_record.heading("password", text="Password")
        emp_record['show'] = 'headings'
        emp_record.column("id", width=70)
        emp_record.column("name", width=70)
        emp_record.column("contact", width=70)
        emp_record.column("add", width=100)
        emp_record.column("aadhar", width=80)
        emp_record.column("username", width=70)
        emp_record.column("password", width=70)

        emp_record.pack(fill=BOTH, expand=1)
        i = 0
        for ro in conn:
            emp_record.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
            i = i + 1

        subframe2.pack(expand=True, fill=BOTH, side=LEFT)


connect = mysql.connector.connect(host="localhost", user="root", password="", port=3306, database="grocerydb")
conn = connect.cursor()
conn.execute("SELECT * FROM `manageemp`")


def exit():
    os.system('python admin.py')
    master.destroy()


def add():
    os.system('python addemp.py')
    master.destroy()


def update():
    os.system('python updateprdts.py')
    master.destroy()

def search():
    query = "SELECT * FROM `manageemp` WHERE ID=%s"

    cursor.excute(query)
    row = cursor.fetchall()




root = Tk()
root.geometry('1300x1200')
root.title("Manage Employee")
window = Window(root)
root.mainloop()
