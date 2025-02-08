import os
import  tkinter
from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("WELCOME!!, HAVE A NICE DAY!")
window.geometry('550x300')
window.resizable(False, False)
# image_0=Image.open('emplogin.jpg')
# back_end=ImageTk.PhotoImage(image_0)
#lbl= tkinter.Label(window, image=back_end)
#lbl.place(x=0,y=0)



#
def employeelogin():
    window.withdraw()
    os.system("python emp2login.py")
    window.deiconify()

def admin():
    window.withdraw()
    os.system("python admin2login.py")
    window.deiconify()


# Creating widgets
login_button1 = tkinter.Button(window, text="Admin Login", bg='#71955d', fg='white', font=("Airal", 20), command=admin)
login_button2 = tkinter.Button(window, text="Employee Login", bg='FireBrick', fg='white', font=("Airal", 20), command=employeelogin)

# Placing widgets
login_button1.grid(row=3, column=0, padx=50, pady=100)
login_button2.grid(row=3, column=1, pady=100)




window.mainloop()
