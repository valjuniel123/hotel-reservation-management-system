from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from subprocess import call

# from room_information import toRoomInfo

import mysql.connector

from database import *

def toLogin():
    print("Logged out!")
    main_screen.destroy()
    
   
# def reserve():
     


global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("300x500") # set the configuration of GUI window 
main_screen.title("Room Number 1") # set the title of GUI window

# create a Form label 
Label(text="Angeli's Hotel Reservation System", bg="blue", width="300", height="1", font=("Calibri", 13)).pack() 
Label(text="Room Reservation", bg="blue", width="300", height="1", font=("Calibri", 13)).pack() 
Label(text="").pack() 
 
# Create an Exit Button
Button(text="Back", height="2", width="30", command=toLogin).pack()

Label(text="").pack() 

#Create reservation Form
global roomNumber, name, contact, checkIn, checkOut
roomNumber = StringVar()
name = StringVar()
contact = StringVar()
checkIn = StringVar()
checkOut = StringVar()

Label(text="Room Number:").pack()
enteredRoomNumber = Entry(main_screen, width="30", textvariable=roomNumber).pack()

Label(text="Name:").pack()
enteredName = Entry(main_screen, width="30", textvariable=name).pack()

Label(text="Contact:").pack()
enteredContact = Entry(main_screen, width="30", textvariable=contact).pack()

Label(text="Check In:").pack()
enteredCheckIn = DateEntry(main_screen, width="30", selectmode='day', textvariable=checkIn).pack()

Label(text="Check Out:").pack()
enteredCheckOut = DateEntry(main_screen, width="30", selectmode='day', textvariable=checkOut).pack()

Button(text="Reserve", height="2", width="30").pack()

main_screen.mainloop() # start the GUI
 
# main_account_screen() # call the main_account_screen() function