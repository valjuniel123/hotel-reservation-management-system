from tkinter import *
from tkinter import messagebox

from subprocess import call

import mysql.connector

from database import *

def toLogin():
    print("Logged out!")
    main_screen.destroy()
    
def toRoomInformation():
    main_screen.withdraw()
    call(["python", "room_information.py"])
    main_screen.deiconify()
    
def toRoomReservation():
    main_screen.withdraw()
    call(["python", "room_reservation.py"])
    main_screen.deiconify()
    


global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("300x250") # set the configuration of GUI window 
main_screen.title("Main Menu") # set the title of GUI window

# create a Form label 
Label(text="Angeli's Hotel Reservation System", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 
 
# create Room Information Button 
Button(text="Room Information", height="2", width="30", command=toRoomInformation).pack() 

# create a Reservation button
Button(text="For Reservation", height="2", width="30", command=toRoomReservation).pack()
Label(text="").pack()

# Create an Exit Button
Button(text="Logout", height="2", width="30", command=toLogin).pack()



main_screen.mainloop() # start the GUI
 
# main_account_screen() # call the main_account_screen() function