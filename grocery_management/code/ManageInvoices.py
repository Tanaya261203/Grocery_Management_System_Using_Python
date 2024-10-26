import tkinter
import os
from tkinter import *
from tkinter import messagebox
import tempfile

# ----- WINDOW CREATION -----------
window = tkinter.Tk()
window.title("Manage Invoices.")
window.geometry('930x750+0+0')
window.configure(bg="white")

# -------- MAIN FRAME ------------------
Main_frame = tkinter.Frame(window, bd=5, relief=GROOVE, bg="white")
Main_frame.place(x=0, y=0, width=930, height=700)


# ------------- Search Button Function --------------
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


# -------------- Search Frame -------------
search_frame = tkinter.LabelFrame(Main_frame, text="SEARCH BY BILL NUMBER", font=("Time New Roman", 10, "bold"),
                                  bg="white", fg="orange")
search_frame.place(x=0, y=10, width=430, height=450)

# ------------- Bill Search input ----------------
lbl_bill = tkinter.Label(search_frame, text="BILL NUMBER:", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="black")
lbl_bill.grid(row=2, column=1)
bill_entry = tkinter.Entry(search_frame, bg="white", fg="black", font=("Times New Roman", 11, "bold"), width=35)
bill_entry.grid(row=3, column=1)

# ------------ Search Button ------------------
btn_search = tkinter.Button(search_frame, text="SEARCH", font=("Times New Roman", 12), bg="red", fg="white", command=find_bill)
btn_search.grid(row=3, column=5, padx=10)



# # ----------- DISCAILMER -------------------
# lbl_dis=tkinter.Label(search_frame, tex)


# --------------- Bill Area Frame -------------------
Rightframe = LabelFrame(Main_frame, text="Bill Area", font=("Time New Roman", 18, "bold"), bg="white", fg="red")
Rightframe.place(x=440, y=0, width=480, height=650)
scroll_y = Scrollbar(Rightframe, orient=VERTICAL)
textarea = tkinter.Text(Rightframe, yscrollcommand=scroll_y.set, bg="white", fg="blue",
                        font=("Time New Roman", 12, "bold"))
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)

window.mainloop()
