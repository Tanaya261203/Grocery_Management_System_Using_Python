# =========== pacakages imported ============
from tkinter import *
import tkinter
import os
import mysql.connector
from tkinter import messagebox

# ============== Window creation ===============
window = tkinter.Tk()
window.title("Update Products")
window.geometry('650x650')
window.configure(bg='#FFFDD0')
window.resizable(False, False)

# ================ Frame Creation ========================
frame = tkinter.Frame(window, bd=5, relief=GROOVE, bg="white")
frame.place(x=0, y=50, width=530, height=620)


# ========== Function(DATABASE) ==============

# ---------------- Exit ------------
def back():
    window.withdraw()
    os.system('python manageprdts.py')
    window.deiconify()





# -------------- Validation ----------------
def checkid(prdtid_entry):
    if prdtid_entry.isdigit():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")
        return False


def checkname(prdt_entry):
    if prdt_entry.isalnum():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")
        return False


def checkcategory(cat_entry):
    if cat_entry.isalnum():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")
        return False


def checksubcategory(subcat_entry):
    if subcat_entry.isalnum():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")


def checkstock(stock_entry):
    if stock_entry.isdigit():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")


def checkprice(price_entry):
    if price_entry.isdigit():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")


# ===== DATABASE CONNECTION ==========
def update():  # ------Update Record---------
    # ---------- NO NULL VALUE ACCEPTANCE -----------------------

        try:
            # ------------ CONNECTION -------------
            con  = mysql.connector.connect(user='root', password='', host='localhost', port=3306, database='grocerydb')
            cur = con.cursor()
            prdt_id = prdtid_entry.get()
            prdt_name = prdt_entry.get()
            category = cat_entry.get()
            sub_category = subcat_entry.get()
            qty = stock_entry.get()
            price = price_entry.get()
            # -------------- STORE PROCEDURE ---------------
            Update = "UPDATE `manageprdts` SET `prdt_name`='%s',`category`='%s',`sub_category`='%s',`qty`='%s',`price`='%s' WHERE `prdt_id`='%s'" % (
                prdt_name, category, sub_category, qty, price, prdt_id)
            cur.execute(Update)
            con.commit()
            messagebox.showinfo("Info", "Record Updated Sucessfully")
        except:
            messagebox.showinfo('No Data', 'No such data available....')


# ------------- SEARCH BUTTON ----------------------------- 
def search():
    global myresult
    prdt_name = prdtid_entry.get()
    prdtname = prdt_entry.get()
    prdtcat = cat_entry.get()
    prdtsubcat = subcat_entry.get()
    prdtqty = stock_entry.get()
    prdtprice = price_entry.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="grocerydb")
    mycursor = mysqldb.cursor()

    try:
        mycursor.execute("SELECT * FROM manageprdts where prdt_id = '" + prdt_name + "'")
        myresult = mycursor.fetchall()
        for x in myresult:
            prdt_entry.delete(0, END)
            prdt_entry.insert(END, x[1])
            cat_entry.delete(0, END)
            cat_entry.insert(END, x[2])
            subcat_entry.delete(0, END)
            subcat_entry.insert(END, x[3])
            stock_entry.delete(0, END)
            stock_entry.insert(END, x[4])
            price_entry.delete(0, END)
            price_entry.insert(END, x[5])


    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


# ============== INSIDE FRAME ====================

# -------------HEADING--------------------------
label = tkinter.Label(frame, text="UPDATE PRODUCTS", bg='white', fg='black', font=("Times New Roman", 30))
label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)


# ------------PRODUCT ID-------------------
prdt_id = tkinter.Label(frame, text="Product ID:", bg="white", fg='black', font=("Times New Roman", 20))
prdt_id.grid(row=1, column=0)
prdtid_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
prdtid_entry.grid(row=1, column=1, pady=20)
validate_id = window.register(checkid)
prdtid_entry.config(validate="key", validatecommand=(validate_id, "%P"))

# --------------SEARCH BUTTON-------------
search_btn = tkinter.Button(frame, text="Search", bg='#FF3399', fg='white', font=("Times New Roman", 16),
                            command=search)
search_btn.grid(row=1, column=2, pady=20, padx=25)

# ----------------PRODUCT NAME-------------------
prdt_name = tkinter.Label(frame, text="Product Name:", bg="white", fg='black', font=("Times New Roman", 20))
prdt_name.grid(row=2, column=0)
prdt_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
prdt_entry.grid(row=2, column=1, pady=20)
validate_name = window.register(checkname)
prdt_entry.config(validate="key", validatecommand=(validate_name, "%P"))

# ------------CATEGORY---------------------
prdt_cat = tkinter.Label(frame, text="Category:", bg="white", fg='black', font=("Times New Roman", 20))
prdt_cat.grid(row=3, column=0)
cat_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
cat_entry.grid(row=3, column=1, pady=20)
validate_cat = window.register(checkcategory)
cat_entry.config(validate="key", validatecommand=(validate_cat, "%P"))

# -----------------SUBCATEGORIES-----------------
prdt_subcat = tkinter.Label(frame, text="Sub-Category:", bg="white", fg='black', font=("Times New Roman", 20))
prdt_subcat.grid(row=4, column=0)
subcat_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
subcat_entry.grid(row=4, column=1, pady=20)
validate_subcat = window.register(checksubcategory)
subcat_entry.config(validate="key", validatecommand=(validate_subcat, "%P"))

# ------------------STOCK-----------------
prdt_stock = tkinter.Label(frame, text="Stock(QTY):", bg="white", fg='black', font=("Times New Roman", 20))
prdt_stock.grid(row=5, column=0)
stock_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
stock_entry.grid(row=5, column=1, pady=20)
validate_stock = window.register(checkstock)
stock_entry.config(validate="key", validatecommand=(validate_stock, "%P"))

# ------------PRICE-------------------
prdt_price = tkinter.Label(frame, text="Price(INR):", bg="white", fg='black', font=("Times New Roman", 20))
prdt_price.grid(row=6, column=0)
price_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
price_entry.grid(row=6, column=1, pady=20)
validate_price = window.register(checkprice)
price_entry.config(validate="key", validatecommand=(validate_price, "%P"))

# ----------------UPDATE BUTTON---------------------
updt_btn = tkinter.Button(frame, text="Update", bg="#E06B0A", fg='#030303', font=("Times New Roman", 20),
                          command=update)
updt_btn.grid(row=7, column=0, pady=25)

# ------------ CLEAR ---------------
def clear():
    prdtid_entry.delete(0, END)
    prdt_entry.delete(0, END)
    cat_entry.delete(0, END)
    subcat_entry.delete(0, END)
    stock_entry.delete(0, END)
    price_entry.delete(0, END)
# ------------------CLAER BUTTON---------------
clear_btn = tkinter.Button(frame, text="Clear", bg="#E06B0A", fg='#030303', font=("Times New Roman", 20), command=clear)
clear_btn.grid(row=7, column=1, padx=50, pady=25)


# ------------BACK BUTTON----------------
back_btn = tkinter.Button(frame, text="Back", bg="#E06B0A", fg='#030303', font=("Times New Roman", 20), command=back)
back_btn.grid(row=7, column=2, padx=50, pady=25)

frame.pack()
window.mainloop()
