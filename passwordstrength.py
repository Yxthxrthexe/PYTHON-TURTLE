import string
import getpass
from tkinter import *

def checkPass():
    password = password_entry.get()
    length = len(password)
    
    if 5 < length < 10:
        if any(char in string.ascii_uppercase for char in password):
            if any(char.isdigit() for char in password):
                if '@' in password or '_' in password:
                    result_label.config(text="Your Password is decent!!")
                else:
                    result_label.config(text="Password must contain '@' or '_'")
            else:
                result_label.config(text="Password must contain a numeric value")
        else:
            result_label.config(text="Password must contain Camel Case")
    elif length > 9:
        result_label.config(text="Hurray, Password is Strong!!")
    else:
        result_label.config(text="Password must have letters from 6 up to 14")

root = Tk()
root.title("Password Strength Checker")
root.geometry('350x300')

password_label = Label(root, text="Enter your Password:")
password_label.pack(pady=10)

password_entry = Entry(root, show='*')
password_entry.pack(pady=5)

check_button = Button(root, text="Check Password", command=checkPass)
check_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
