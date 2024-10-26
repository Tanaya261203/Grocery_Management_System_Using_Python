# ----- IMPORTED PACKAGES -------------
import tkinter
from tkinter import *
from tkinter import ttk
import random
import os
from tkinter import messagebox
import tempfile

# ----- WINDOW CREATION -----------
window = tkinter.Tk()
window.title("Billing Page")
window.geometry('1530x800+0+0')
window.configure(bg="white")

# ----------- BILLING LABEL -------------
lbl_title = tkinter.Label(window, text="Billing Area", font=("Time New Roman", 35, "bold"), bg="white", fg="black")
lbl_title.place(x=0, y=0, width=1530, height=50)

# -------- MAIN FRAME ------------------
Main_frame = tkinter.Frame(window, bd=5, relief=GROOVE, bg="white")
Main_frame.place(x=0, y=50, width=1530, height=620)

# -------- Customer DETAILS FRAME --------------
Cust_frame = tkinter.LabelFrame(Main_frame, text="Customer", font=("Time New Roman", 16, "bold"), bg="white",
                                fg="red")
Cust_frame.place(x=10, y=5, width=350, height=140)

# -------- VARIABLES ------------
c_name = StringVar()
c_email = StringVar()
c_mobileno = StringVar()

# -------- MOBILE NUMBER --------------
lbl_mobile = tkinter.Label(Cust_frame, text="Mobile no:", font=("Time New Roman", 12, "bold"),
                           bg="white", fg="black")
lbl_mobile.grid(row=0, column=0, sticky=W, padx=5, pady=2)
mobile_entry = tkinter.Entry(Cust_frame, font=("Time New Roman", 12, "bold"), textvariable=c_mobileno, bg="white",
                             fg="black")
mobile_entry.grid(row=0, column=1)

# ------------ CUSTOMER NAME --------------
lbl_name = tkinter.Label(Cust_frame, text="Customer Name:", font=("Time New Roman", 12, "bold"), bg="white", fg="black")
lbl_name.grid(row=1, column=0, sticky=W, padx=5, pady=2)
name_entry = tkinter.Entry(Cust_frame, font=("Time New Roman", 12, "bold"), textvariable=c_name, bg="white", fg="black")
name_entry.grid(row=1, column=1)

# ------- EMAIL-ID ----------
lbl_email = tkinter.Label(Cust_frame, text="Email Id:", font=("Time New Roman", 12, "bold"), bg="white", fg="black")
lbl_email.grid(row=2, column=0, sticky=W, padx=5, pady=2)
email_entry = tkinter.Entry(Cust_frame, font=("Time New Roman", 12, "bold"), textvariable=c_email, bg="white",
                            fg="black")
email_entry.grid(row=2, column=1)

# -------------- Product Frame -------------
Prdt_frame = tkinter.LabelFrame(Main_frame, text="Product", font=("Time New Roman", 16, "bold"), bg="white", fg="red")
Prdt_frame.place(x=0, y=180, width=750, height=140)

# -------------- list for category --------------
Category = ["Select Option", "Biscuits", "Grains", "Diary Products", "Cereals"]

# ========== LIST FOR SUB-CATEGORY ================
# ------ BISCUITS --------
SubCatBiscuits = ["Parle", "Britania", "SunFeast", "Bisk Fram", "Cadbury", "Oreo"]

# ------  GRAINS ----------
SubCatGrains = ["Rice", "Wheat", "Jowar", "Bajri"]

# ---------- Diary Product ----------------
SubCatDiaryPrdts = ["Milk", "Bread", "Butter", "Cheese", "Yogurt", "Ghe", "Ice-cream"]

# ------------ CEREALS ------------------------
SubCatCereals = ["Chowali", "Chole", "Frozen Matar", "White Peas", "Matki", "Moong", "Chana Dal", "Soyabeans"]


# ------------- FUNCTION -----------
def category(event=""):
    if Combo_Category.get() == "Biscuits":
        Combo_SubCategory.config(values=SubCatBiscuits)
        Combo_SubCategory.current(0)
    elif Combo_Category.get() == "Grains":
        Combo_SubCategory.config(values=SubCatGrains)
        Combo_SubCategory.current(0)
    elif Combo_Category.get() == "Diary Products":
        Combo_SubCategory.config(values=SubCatDiaryPrdts)
        Combo_SubCategory.current(0)
    elif Combo_Category.get() == "Cereals":
        Combo_SubCategory.config(values=SubCatCereals)
        Combo_SubCategory.current(0)


# ------------- PRODUCT FRAME ------------------
lbl_category = tkinter.Label(Prdt_frame, text="Select Category:", font=("Time New Roman", 12, "bold"), bg="white",
                             fg="black")
lbl_category.grid(row=0, column=0, sticky=W, padx=5, pady=2)

# ------ VARIABLES -------------
prdtname = StringVar()
qty = IntVar()
price = IntVar()

# ------------ CATEGORY ------------
Combo_Category = ttk.Combobox(Prdt_frame, font=("airal", 9, "bold"), width=24, state="readonly", values=Category)
Combo_Category.current(0)
Combo_Category.grid(row=0, column=1)
Combo_Category.bind("<<ComboboxSelected>>", category)

# ----------- SUB-CATEGORY -----------------
lbl_subcategory = tkinter.Label(Prdt_frame, text="Sub-Category:", font=("Time New Roman", 12, "bold"), bg="white",
                                fg="black")
lbl_subcategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)
Combo_SubCategory = ttk.Combobox(Prdt_frame, font=("airal", 9, "bold"), width=24, state="readonly")
Combo_SubCategory.grid(row=1, column=1)

# --------- PRODUCT NAME ----------------
lbl_prdtname = tkinter.Label(Prdt_frame, text="Product Name:", font=("Time New Roman", 12, "bold"), bg="white",
                             fg="black")
lbl_prdtname.grid(row=2, column=0, sticky=W, padx=5, pady=2)
Entry_prdt = tkinter.Entry(Prdt_frame, font=("airal", 9, "bold"), bg="white", fg="black", textvariable=prdtname,
                           width=28)
Entry_prdt.grid(row=2, column=1)

# --------- QTY --------------
lbl_qty = tkinter.Label(Prdt_frame, text="Select Qty:", font=("Time New Roman", 12, "bold"), bg="white", fg="black")
lbl_qty.grid(row=0, column=2, sticky=W, padx=5, pady=2)
qty_entry = tkinter.Entry(Prdt_frame, font=("Time New Roman", 9, "bold"), bg="white", fg="black", textvariable=qty,
                          width=25)
qty_entry.grid(row=0, column=3)

# ---------- PRICE -------------
lbl_price = tkinter.Label(Prdt_frame, text="Price Qty:", font=("Time New Roman", 12, "bold"), bg="white", fg="black")
lbl_price.grid(row=1, column=2, sticky=W, padx=5, pady=2)
price_entry = tkinter.Entry(Prdt_frame, font=("Time New Roman", 9, "bold"), bg="white", fg="black", textvariable=price)
price_entry.grid(row=1, column=3)

# ============ Bill Counter Frame ======================
Bill_frame = tkinter.LabelFrame(Main_frame, text="Bill Counter", font=("Time New Roman", 16, "bold"), bg="white",
                                fg="red")
Bill_frame.place(x=0, y=350, width=870, height=240)

# ---------- VARIABLE ---------------
subtotal = StringVar()
tax = StringVar()
total = StringVar()

# ----- SUB-TOTAL -----------------
lbl_subtotal = tkinter.Label(Bill_frame, text="Sub-Total:", font=("Time New Roman", 12, "bold"), bg="white",
                             fg="black")
lbl_subtotal.grid(row=0, column=0, sticky=W, padx=2, pady=2)
subtotal_entry = tkinter.Entry(Bill_frame, font=("Time New Roman", 12, "bold"), bg="white", fg="black",
                               textvariable=subtotal)
subtotal_entry.grid(row=0, column=1)

# ----------- TAX ----------
lbl_tax = tkinter.Label(Bill_frame, text="Gov Tax:", font=("Time New Roman", 12, "bold"), bg="white", fg="black")
lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)
tax_entry = tkinter.Entry(Bill_frame, font=("Time New Roman", 12, "bold"), bg="white", fg="black", textvariable=tax)
tax_entry.grid(row=1, column=1)

# ------------- TOTAL ----------------
lbl_total = tkinter.Label(Bill_frame, text="Total:", font=("Time New Roman", 12, "bold"), bg="white", fg="black")
lbl_total.grid(row=2, column=0, sticky=W, padx=5, pady=2)
total_entry = tkinter.Entry(Bill_frame, font=("Time New Roman", 12, "bold"), bg="white", fg="black", textvariable=total)
total_entry.grid(row=2, column=1)

# ================ BUTTTONS =====================
list = []


# ----------- ADD TO CART FUNCTION ----------------------
def AddItem():
    n = price.get()
    m = qty.get() * n
    list.append(m)
    if prdtname.get() == "":
        messagebox.showerror("Error", "Enter the product name")
    else:
        textarea.insert(END, f"\n {prdtname.get()}\t\t{qty.get()}\t\t{m}")
        subtotal.set(str('Rs.%.2f' % (sum(list))))
        Tax = 5
        tax.set(str('Rs.%.2f' % ((((sum(list)) - (price.get())) * Tax) / 100)))
        total.set(str('Rs.%.2f' % (((sum(list)) + ((((sum(list)) - (price.get())) * Tax) / 100)))))


# -------------- Search Function ------------------------
def find_bill():
    found = "no"
    for i in os.listdir("C:\\Users\\admin\\Desktop\\grocery management\\bill/"):
        if i.split('.')[0] == bill_entry.get():
            f1 = open(f'C:\\Users\\admin\\Desktop\\grocery management\\bill/{i}', 'r')
            textarea.delete(1.0, END)
            for d in f1:
                textarea.insert(END, d)
            f1.close()
            found = "yes"
    if found == 'no':
        messagebox.showerror("Error", "Invalid Bill No.")


# ------- Bill Generation Function ------------
def gen_bill():
    if prdtname.get() == "":
        messagebox.showerror("Error", "Please Add to Cart")
    else:
        text = textarea.get(10.0, (10.0 + float(len(list))))
        welcome()
        textarea.insert(END, text)
        textarea.insert(END, "\n**************************************************************************")
        textarea.insert(END, f"\n Sub Total:\t\t{subtotal.get()}")
        textarea.insert(END, f"\n Total Tax:\t\t{tax.get()}")
        textarea.insert(END, f"\n Total Amount :\t\t{total.get()}")
        textarea.insert(END, "\n**************************************************************************")


# -------- Print Function --------------
def iprint():
    q = textarea.get(1.0, "end-1c")
    filename = tempfile.mktemp('.txt')
    open(filename, 'w').write(q)
    os.startfile(filename, "print")


# ------- Clear Function -------------
def clear():
    textarea.delete(1.0, END)
    c_name.set("")
    c_mobileno.set("")
    c_email.set("")
    x = random.randint(1000, 9999)
    bill_no.set(str(x))
    Combo_Category.set("Select Option")
    Combo_SubCategory.set("   ")
    prdtname.set("")
    qty.set(0)
    price.set(0)
    subtotal.set("")
    tax.set("")
    total.set("")
    list = [0]
    welcome()


# -------------- ADD BUTTON ---------------
AddBtn = tkinter.Button(Bill_frame, text="Add to Cart", font=("arial", 14, "bold"), bg="#C70039", fg="white", height=2,
                        command=AddItem)
AddBtn.grid(row=3, column=0, pady=30)

# ----------- GENERATE BUTTON -------------------
genBtn = tkinter.Button(Bill_frame, text="Generate Bill", font=("arial", 14, "bold"), bg="#C70039", fg="white",
                        height=2, command=gen_bill)
genBtn.grid(row=3, column=1)


# ------------- Save Function ----------------
def save_bill():
    op = messagebox.askyesno("Save Bill", "Do you want save the Bill")
    if op > 0:
        bill_data = textarea.get(1.0, END)
        f1 = open('C:\\Users\\admin\\Desktop\\grocery management\\bill/' + str(bill_no.get()) + ".txt", 'w')
        f1.write(bill_data)
        op = messagebox.showinfo("Saved", f"Bill No:{bill_no.get()} Saved Successfully")
        f1.close()


# --------- SAVE BUTTON ------------------------
saveBtn = tkinter.Button(Bill_frame, text="Save Bill", font=("arial", 14, "bold"), bg="#C70039", fg="white", height=2,
                         command=save_bill)
saveBtn.grid(row=3, column=2, padx=20)

# ---------- PRINT BUTTON -------------------------
printBtn = tkinter.Button(Bill_frame, text="Print", font=("arial", 14, "bold"), bg="#C70039", fg="white", height=2,
                          width=8, command=iprint)
printBtn.grid(row=3, column=3, padx=20)

# ------------ CLEAR BUTTON -----------------
ClearBtn = tkinter.Button(Bill_frame, text="Clear", font=("arial", 14, "bold"), bg="#C70039", fg="white", height=2,
                          width=8, command=clear)
ClearBtn.grid(row=3, column=4, padx=20)

# ----------- EXIT BUTTON ---------------
ExitBtn = tkinter.Button(Bill_frame, text="Exit", font=("arial", 14, "bold"), bg="#C70039", fg="white", height=2,
                         width=8)
ExitBtn.grid(row=3, column=5, padx=20)

# ---------- SEARCH FRAME  --------------
search_frame = tkinter.Frame(Main_frame, bd=2, bg="white")
search_frame.place(x=390, y=60, width=450, height=40)

# ====== VARIABLES =================
bill_no = IntVar()
z = random.randint(1000, 9999)
bill_no.set(z)
lblBill = tkinter.Label(search_frame, text="Bill Number:", font=("Time New Roman", 16, "bold"), bg="red", fg="white")
lblBill.grid(row=0, column=0, sticky=W, padx=1)
bill_entry = tkinter.Entry(search_frame, font=("Time New Roman", 16, "bold"), bg="white", fg="black")
bill_entry.grid(row=0, column=1, padx=2, sticky=W)
btnsearch = tkinter.Button(search_frame, text="Search", font=("Time New Roman", 11, "bold"), bg="red", fg="white",
                           command=find_bill)
btnsearch.grid(row=0, column=2, padx=1)

# Bill Area Frame
Rightframe = LabelFrame(Main_frame, text="Bill Area", font=("Time New Roman", 18, "bold"), bg="white", fg="red")
Rightframe.place(x=870, y=0, width=480, height=600)

scroll_y = Scrollbar(Rightframe, orient=VERTICAL)
textarea = tkinter.Text(Rightframe, yscrollcommand=scroll_y.set, bg="white", fg="blue",
                        font=("Time New Roman", 12, "bold"))
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)


# ---------------Function-------------------------------
def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t\t Welcome To Mini Mall\n")
    textarea.insert(END, f"\n BILL NUMBER:{bill_no.get()}")
    textarea.insert(END, f"\n CUSTOMER NAME:{c_name.get()}")
    textarea.insert(END, f"\n Email:{c_email.get()}")
    textarea.insert(END, f"\n Contact Number:{c_mobileno.get()}")
    textarea.insert(END, "\n**************************************************************************")
    textarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
    textarea.insert(END, "\n**************************************************************************")


welcome()
# def additem()


window.mainloop()
