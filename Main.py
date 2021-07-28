# import libraries
from tkinter import *
import pyperclip
import random
import string

# initialize window
root = Tk()
root.geometry('400x400')
root.config(background='light blue')
root.resizable(0,0)
root.title('Password generator')

Label(root,text='Password Generator Application',font='arial 15 bold').pack(pady=10)
Label(root,text='SmartProgrammer',font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root,text='Password length', font='arial 10 bold').pack(pady=5)
pass_len=IntVar()
length_box=Spinbox(root,from_ = 8, to_=32, textvariable=pass_len,width=20).pack(pady=5)

# Writing main function to generate password
pass_str= StringVar()

def password_generate():
    password = ''
    for x in range(0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)+ random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password=password+random.choice(string.ascii_lowercase+string.ascii_uppercase + string.punctuation + string.digits)
    pass_str.set(password)
# Adding Button
Button(root,text= 'Generate Password', font= 'arial 10 bold',command=password_generate).pack(pady=5)
entry=Entry(root,textvariable=pass_str,font= 'arial 10 bold', width=21)
entry.pack()

# Add copy to clip board function
def copy_password():
    pyperclip.copy(pass_str.get())
Button(root,text= 'Copy to Clipboard ', command= copy_password).pack(pady=10)
 # Adding a clear entry field button
def Clear_entry():
    entry.delete(0,END)
Button(root,text= 'Clear', command= Clear_entry).pack(pady=10)
root.mainloop()