# =========== pacakages imported ============
from tkinter import *
import tkinter
from tkinter import ttk
import os
from tkinter import messagebox
import mysql.connector

# ========== WINDOW CREATION ================
window = tkinter.Tk()
window.title("Add Products")
window.geometry('700x600')
window.configure(bg="white")

# ================ Frame Creation ========================
frame = tkinter.Frame(window, bd=5, relief=GROOVE, bg="white")
frame.place(x=0, y=50, width=600, height=620)


# =========== LIST CREATION ===============
Category = ["Select Option", "Biscuits", "Grains", "Diary Products", "Cereals"]
# ------ BISCUITS -----
SubCatBiscuits = ["Parle", "Britania", "SunFeast", "Bisk Fram", "Cadbury", "Oreo"]
# ------  GRAINS ---
SubCatGrains = ["Rice", "Wheat", "Jowar", "Bajri"]
# ---------- Diary Product ----------------
SubCatDiaryPrdts = ["Milk", "Bread", "Butter", "Cheese", "Yogurt", "Ghe", "Ice-cream"]
SubCatCereals = ["Chowali", "Chole", "Frozen Matar", "White Peas", "Matki", "Moong", "Chana Dal", "Soyabeans"]

# ----------- FUNCTION TO DISPLAY LIST -------------
def category(event=""):
    if cat_combox.get()=="Biscuits":
        subcat_combobox.config(values=SubCatBiscuits)
        subcat_combobox.current(0)
    elif cat_combox.get() == "Grains":
        subcat_combobox.config(values=SubCatGrains)
        subcat_combobox.current(0)
    elif cat_combox.get() == "Diary Products":
        subcat_combobox.config(values=SubCatDiaryPrdts)
        subcat_combobox.current(0)
    elif cat_combox.get() == "Cereals":
        subcat_combobox.config(values=SubCatCereals)
        subcat_combobox.current(0)


# ============ Function ===================

# ------------- BACK FUNCTION -------------------
def back():
    window.withdraw()
    os.system('python manageprdts.py')
    window.deiconify()


# ------------ CLEAR ---------------
def clear():
    prdtid_entry.delete(0, END)
    prdt_entry.delete(0, END)
    cat_combox.delete(0, END)
    subcat_combobox.delete(0, END)
    stock_entry.delete(0, END)
    price_entry.delete(0, END)


# ------------------- VALIDATION -------------------------
def checkid(prdtid_entry):
    if prdtid_entry.isdigit():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")


def checkname(prdt_entry):
    if prdt_entry.isalnum():
        return True
    else:
        messagebox.showwarning("Invalid", "Not allowed")


def checkprdtcat(cat_entry):
    if cat_combox.isalnum():
        return True
    else:
        messagebox.showwarning("Invalid", "Not Allowed")


def checksubcat(subcat_entry):
    if subcat_combobox.isalnum():
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
        messagebox.showwarning("Invalid", "Not allowed")


# ============= Database Connection ====================
def add():
    # ---------- NO NULL VALUE ACCEPTANCE -----------------------
    if prdtid_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter id')
    elif prdt_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter product name')
    elif cat_combox.get() == '':
        messagebox.showinfo('Error', 'Please enter category')
    elif subcat_combobox.get() == '':
        messagebox.showinfo('Error', 'Please enter subactegory')
    elif stock_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter stock')
    elif price_entry.get() == '':
        messagebox.showinfo('Error', 'Please enter price')
    else:
        try:
            connection = mysql.connector.connect(host="localhost", port=3306, user="root", password="",
                                                 database="grocerydb")
            c = connection.cursor()
            ID = prdtid_entry.get()
            name = prdt_entry.get()
            categroy = cat_combox.get()
            subcat = subcat_combobox.get()
            stock = stock_entry.get()
            price = price_entry.get()

            insert_query = "INSERT INTO `manageprdts`(`prdt_id`, `prdt_name`, `category`, `sub_category`, `qty`, `price`) VALUES (%s, %s, %s, %s, %s, %s)"
            vals = (ID, name, categroy, subcat, stock, price)
            c.execute(insert_query, vals)
            connection.commit()
            messagebox.showinfo("", "Record Added Successfully")
        except:
            messagebox.showinfo("", "Database connection not possible")


# ============= WIDGETS CREATION ================

# -------------- HEADING -----------------------
label = tkinter.Label(frame, text="ADD PRODUCTS", bg='white', fg='black', font=("Times New Roman", 30))
label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

# ---------------- PRODUCT ID ------------------
prdt_id = tkinter.Label(frame, text="Product ID:", bg="white", fg='black', font=("Times New Roman", 20))
prdt_id.grid(row=1, column=0)
prdtid_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
prdtid_entry.grid(row=1, column=1, pady=20)
validate_prtid = window.register(checkid)
prdtid_entry.config(validate="key", validatecommand=(validate_prtid, "%P"))

# -------------- PRODUCT NAME --------------
prdt_name = tkinter.Label(frame, text="Product Name:", bg="white", fg='black', font=("Times New Roman", 20))
prdt_name.grid(row=2, column=0)
prdt_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
prdt_entry.grid(row=2, column=1, pady=20)
validate_prdtname = window.register(checkname)
prdt_entry.config(validate="key", validatecommand=(validate_prdtname, "%P"))

# ---------------- CATEGORY --------------
prdt_cat = tkinter.Label(frame, text="Category:", bg="white", fg='black', font=("Times New Roman", 20))
prdt_cat.grid(row=3, column=0)
cat_combox = ttk.Combobox(frame, font=("Times New Roman", 16), width=24, state="readonly", values=Category)
cat_combox.current(0)
cat_combox.bind("<<ComboboxSelected>>", category)
cat_combox.grid(row=3, column=1, pady=20)
validate_cat = window.register(checkprdtcat)
cat_combox.config(validate="key", validatecommand=(validate_cat, "%P"))

# -------------- SUBCATEGORY --------------------
prdt_subcat = tkinter.Label(frame, text="Sub-Category:", bg="white", fg='black', font=("Times New Roman", 20))
prdt_subcat.grid(row=4, column=0)
subcat_combobox = ttk.Combobox(frame, font=("Times New Roman", 16), width=24, state="readonly")
subcat_combobox.grid(row=4, column=1, pady=20)
validate_subcat = window.register(checksubcat)
subcat_combobox.config(validate="key", validatecommand=(validate_subcat, "%P"))

# ------------- STOCK ----------------
prdt_stock = tkinter.Label(frame, text="Stock(QTY):", bg="white", fg='black', font=("Times New Roman", 20))
prdt_stock.grid(row=5, column=0)
stock_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
stock_entry.grid(row=5, column=1, pady=20)
validate_stock = window.register(checkstock)
stock_entry.config(validate="key", validatecommand=(validate_stock, "%P"))

# ------------- PRICE -----------------
prdt_price = tkinter.Label(frame, text="Price(INR):", bg="white", fg='black', font=("Times New Roman", 20))
prdt_price.grid(row=6, column=0)
price_entry = tkinter.Entry(frame, font=("Times New Roman", 16))
price_entry.grid(row=6, column=1, pady=20)
validate_price = window.register(checkprice)
price_entry.config(validate="key", validatecommand=(validate_price, "%P"))

# ------------- ADD BUTTON --------------------------
add_btn = tkinter.Button(frame, text="Add", bg="#623FA7", fg='#030303', font=("Times New Roman", 20), command=add)
add_btn.grid(row=7, column=0, pady=25)

# ------------ CLEAR BUTTON -------------------
clear_btn = tkinter.Button(frame, text="Clear", bg="#623FA7", fg='#030303', font=("Times New Roman", 20), command=clear)
clear_btn.grid(row=7, column=1, padx=50, pady=25)

# -------------- BACK BUTTON -------------------
back_btn = tkinter.Button(frame, text="Back", bg="#623FA7", fg='#030303', font=("Times New Roman", 20), command=back)
back_btn.grid(row=7, column=2, padx=50, pady=25)

frame.pack()
window.mainloop()
