from tkinter import *
from tkinter import messagebox

from subprocess import call

import mysql.connector

from database import *

def toLogin():
    print("Logged out!")
    main_screen.destroy()
    
def toRoomInfo(roomNumber):
    main_screen.withdraw()
    # call(["python", "room_information.py"])
    main_screen.deiconify()
    

global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("300x400") # set the configuration of GUI window 
main_screen.title("Room Information") # set the title of GUI window

# create a Form label 
Label(text="Angeli's Hotel Reservation System", bg="blue", width="300", height="1", font=("Calibri", 13)).pack()
Label(text="Room Information", bg="blue", width="300", height="1", font=("Calibri", 13)).pack() 
Label(text="").pack() 

# Create an Exit Button
Button(text="Back", height="2", width="30", command=toLogin).pack()
Label(text="").pack()
 
Label(text="1st Floor").pack() 
# Show Room Informations Button 
button11 = Button(text="Room 11", height="2", width="15", command=toRoomInfo(11)).pack() 
button12 = Button(text="Room 12", height="2", width="15", command=toRoomInfo(12)).pack()
button13 = Button(text="Room 13", height="2", width="15", command=toRoomInfo(13)).pack()
button14 = Button(text="Room 14", height="2", width="15", command=toRoomInfo(14)).pack()
button15 = Button(text="Room 15", height="2", width="15", command=toRoomInfo(15)).pack()
 


Label(text="2nd Floor").pack() 
button21 = Button(text="Room 21", height="2", width="15", command=toRoomInfo(21)).pack() 
button22 = Button(text="Room 22", height="2", width="15", command=toRoomInfo(22)).pack()
button23 = Button(text="Room 23", height="2", width="15", command=toRoomInfo(23)).pack()
button24 = Button(text="Room 24", height="2", width="15", command=toRoomInfo(24)).pack()
button25 = Button(text="Room 25", height="2", width="15", command=toRoomInfo(25)).pack()



main_screen.mainloop() # start the GUI
 
# main_account_screen() # call the main_account_screen() function