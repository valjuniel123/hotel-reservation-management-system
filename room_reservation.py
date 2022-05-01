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
    
   
def getFloorsAvailable():
    counter = 0
    floorArray = []
    converter = ""
    
    query = "SELECT roomFloor FROM roominformation GROUP BY roomFloor ORDER BY roomFloor ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        converter = humanize.ordinal(row[0]) + " Floor"
        floorArray.insert(counter, converter)
        counter+=1
    return floorArray

def floorChanged(index, value, op):
    roomChoice = []
    counter=0
    print ("combobox changed to " + floorSelected.get())
    
    query = "SELECT * FROM roominformation WHERE roomFloor = '" + floorSelected.get() + "' AND NOT EXISTS (SELECT * FROM roomreservation WHERE roomreservation.roomNum = roominformation.roomNum AND STATUS = 1)"
    cursor.execute(query)
    result = cursor.fetchall()
    if(len(result) > 0):
        for row in result:
            print(row[0])
            roomChoice.insert(counter, row[1])
            counter+=1
        selectRoom.config(value=roomChoice)
            
    else:
        print("No rooms available")
        messagebox.showwarning("Warning", "No rooms available")
        
def reserve():
    #Declare variables
    roomReserve = roomSelected.get()
    nameReserve = name.get()
    contactReserve = contact.get()
    checkInReserve = datetime.strptime(checkIn.get(), '%m/%d/%y').strftime('%Y-%m-%d')
    checkOutReserve =  datetime.strptime(checkOut.get(), '%m/%d/%y').strftime('%Y-%m-%d')
    guestKey = random_with_N_digits(6)
    
    
     
    #Query Statement
    query = "INSERT INTO roomreservation(id, roomNum, name, contact, checkIn, checkOut, status, guestKey) VALUES ('0', '" + str(roomReserve) + "', '" + nameReserve + "', '" + str(contactReserve) + "', '" + checkInReserve + "', '" + checkOutReserve + "', '1', '" + str(guestKey) + "')"
    cursor.execute(query)
    con.commit()
    
    print("Reservation successful")
    messagebox.showinfo("Success", "Reservation successful")
    messagebox.showinfo("Guest Key", "Your guest key is: " + str(guestKey))
    main_screen.destroy()
        


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("400x500") # set the configuration of GUI window 
main_screen.title("Room Reservation") # set the title of GUI window

# create a Form label 
Label(text="Angeli's Hotel Reservation System", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
Label(text="Room Reservation", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
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

#################################### START OF PYTHON #############################
floorSelected = StringVar()
roomSelected = StringVar()

#On Click Handler
floorSelected.trace('w',floorChanged)
             
floorChoice = []
floorChoice = getFloorsAvailable()
print(floorChoice)
Label(text="Floor").pack() 
selectFloor = ttk.Combobox(height="10", textvar=floorSelected, width="30")
selectFloor.config(value = floorChoice)
selectFloor.pack()

roomChoice = []
Label(text="Room").pack() 
selectRoom = ttk.Combobox(height="10", textvar=roomSelected, width="30")
selectRoom.config(value = [])
selectRoom.pack()

Label(text="Name:").pack()
enteredName = Entry(main_screen, width="30", textvariable=name).pack()

Label(text="Contact:").pack()
enteredContact = Entry(main_screen, width="30", textvariable=contact).pack()

Label(text="Check In:").pack()
enteredCheckIn = DateEntry(main_screen, width="30", selectmode='day', textvariable=checkIn).pack()

Label(text="Check Out:").pack()
enteredCheckOut = DateEntry(main_screen, width="30", selectmode='day', textvariable=checkOut).pack()

Button(text="Reserve", height="2", width="30", command=reserve).pack()

main_screen.mainloop() # start the GUI
 
# main_account_screen() # call the main_account_screen() function