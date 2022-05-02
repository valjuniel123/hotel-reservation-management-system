from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

from datetime import datetime

import humanize

from subprocess import call
from random import randint

import mysql.connector

from database import *


def toLogin():
    print("Logged out!")
    main_screen.destroy()
    
def checkOutPrompt():
    query = "SELECT * FROM roomreservation WHERE roomNum = '" + roomNum.get() + "' AND guestKey = '" + guestKey.get() + "' AND status = 1"
    cursor.execute(query)
    result = cursor.fetchall()
    if(len(result) > 0):
        #Are you sure you want to check out?
        if messagebox.askyesno("Check Out", "Are you sure you want to check out?"):
            query2 = "UPDATE roomreservation SET status = 0 WHERE roomNum = '" + roomNum.get() + "' AND guestKey = '" + guestKey.get() + "' AND status = 1"
            cursor.execute(query2)
            con.commit()
            messageBox.showinfo("Check Out", "Checked out! \nThank you for using Angeli's Hotel Reservation System!")
    else:
        messagebox.showwarning("Warning", "No reservation found!")
    
    
    

global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("400x500") # set the configuration of GUI window 
main_screen.title("Room Reservation") # set the title of GUI window

# create a Form label 
Label(text="Angeli's Hotel Reservation System", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
Label(text="Checkout", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
Label(text="").pack() 

roomNum = StringVar()
guestKey = StringVar()


Label(text="Room Number * ").pack()
roomNum_entry = Entry(width="30", textvariable=roomNum)
roomNum_entry.pack()

Label(text="").pack()
Label(text="Guest Key * ").pack()
guestKey_entry = Entry(width="30", textvariable=guestKey, show= '*')
guestKey_entry.pack()

Label(text="").pack()
Button(text="Checkout", height="2", width="30", command=checkOutPrompt).pack()

# Create an Exit Button
Button(text="Back", height="2", width="30", command=toLogin).pack()
Label(text="").pack() 
Label(text="").pack() 




Label(text="").pack() 

main_screen.mainloop()