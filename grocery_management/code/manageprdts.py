from tkinter import *
import os
import mysql.connector
from tkinter import ttk
from tkinter import messagebox


class Window:
    def __init__(self, master):
        subframe = Frame(master)
        # ======LABEL FRAME=========
        def delete():
            selected_item = prdt_record.selection()[0]
            connect = mysql.connector.connect(host="localhost", user="root", password="", port=3306,
                                              database="grocerydb")
            conn = connect.cursor()
            query = "DELETE FROM `manageprdts` WHERE `prdt_id`=%s"
            rs = conn.execute(query, selected_item)
            if (rs.rowcount == 1):
                prdt_record.delete(selected_item)



        Button_frame = LabelFrame(subframe, text="WELCOME OWNER!!!", font=("Time New Roman", 16, "bold"),
                                          bg="white",
                                          fg="red")
        Button_frame.place(x=10, y=5, width=1330, height=1330)
        prodt_id = Label(subframe, text="Product ID",bg='white', fg='black', font=("Constantia", 18))
        prodt_id.grid(row=1, column=3, pady=40, padx=40)
        prtid_entry = Entry(subframe, font=("Comic Sans MS", 15))
        prtid_entry.grid(row=1, column=4, pady=3)
        srch_btn = Button(subframe, text="Search", fg='black', font=("Times New Roman", 12))
        srch_btn.grid(row=1, column=6, padx=10, pady=5)
        labl = Label(subframe, text="Choose Option!!!",bg='white', fg='#BA1F5D', font=("Constantia", 18))
        labl.grid(row=3, column=4, pady=20)
        add_btn = Button(subframe, text="Add Products", bg='#396B26', fg='white', font=("Times New Roman", 15),
                         command=add)
        add_btn.grid(row=4, column=4, pady=25)
        update_btn = Button(subframe, text="Update Products", bg='#085F62', fg='white', font=("Times New Roman", 15),
                            command=update)
        update_btn.grid(row=5, column=4, pady=5)
        delete_btn = Button(subframe, text="Delete Products", bg='#1C257B', fg='white', font=("Times New Roman", 15), command=delete)
        delete_btn.grid(row=6, column=4, pady=25)
        Exit_btn = Button(subframe, text=" <-- Exit", bg='#F6E4E2', fg='Red', font=("Times New Roman", 12),
                          command=exit)
        Exit_btn.grid(row=6, column=6, pady=25)
        subframe.pack(expand=True, fill=BOTH, side=LEFT)



        subframe2 = Frame(master, background="red")
        scroll_y = Scrollbar(subframe2, orient=VERTICAL)
        prdt_record = ttk.Treeview(subframe2, height=20,
                                   columns=("Product Id", "Product name", "Category", "Sub-category", "QTY", "Price"),
                                   yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        prdt_record.heading("Product Id", text="Product ID")
        prdt_record.heading("Product name", text="Product  Name")
        prdt_record.heading("Category", text="Category")
        prdt_record.heading("Sub-category", text="Sub-category")
        prdt_record.heading("QTY", text="QTY")
        prdt_record.heading("Price", text="Price")

        prdt_record['show'] = 'headings'
        prdt_record.column("Product Id", width=70)
        prdt_record.column("Product name", width=70)
        prdt_record.column("Category", width=70)
        prdt_record.column("Sub-category", width=100)
        prdt_record.column("QTY", width=50)
        prdt_record.column("Price", width=70)

        prdt_record.pack(fill=BOTH, expand=1)
        i = 0
        for ro in conn:
            prdt_record.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
            i = i + 1

        subframe2.pack(expand=True, fill=BOTH, side=LEFT)




connect = mysql.connector.connect(host="localhost", user="root", password="", port=3306, database="grocerydb")
conn = connect.cursor()
conn.execute("SELECT * FROM `manageprdts`")



def exit():
    os.system('python admin.py')
    master.destroy()


def add():
    os.system('python addprdts.py')
    master.destroy()


def update():
    os.system('python updateprdts.py')
    master.destroy()


root = Tk()
root.geometry('1300x1200')
root.title("Manage Products")
window = Window(root)
root.mainloop()
