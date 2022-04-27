from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import humanize

from subprocess import call

import mysql.connector

from database import *

def toLogin():
    print("Logged out!")
    main_screen.destroy()
    
def closeInfo():
    roomSelected.destroy()

    
def room_selectInfo(detailsArray):
    global roomSelected
    roomSelected = Toplevel(main_screen)
    roomSelected.title("Room Information")
    roomSelected.geometry("300x600")
    
    roomNum = "Room " + str(detailsArray[0][1])
    Label(roomSelected, text="Room Information", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
    Label(roomSelected, text=roomNum, bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
    
    Button(roomSelected, text="Close", height="2", width="30", command=closeInfo).pack()
    Label(text="").pack()    

    Label(roomSelected, text="").pack()
    roomType = "Room Type:\t" + detailsArray[0][6]
    Label(roomSelected, text=roomType, anchor='w').pack(fill='both')
    Label(roomSelected, text="").pack()
    
    location = "Location:\t" + humanize.ordinal(detailsArray[0][4]) + " Floor"
    Label(roomSelected, text=location, anchor='w').pack(fill='both')
    Label(roomSelected, text="").pack()
    
    roomStatus = "Status:\t\t" + "Not Occupied"
    Label(roomSelected, text=roomStatus, anchor='w').pack(fill='both')
    Label(roomSelected, text="").pack()
    
    Label(roomSelected, text="Name\tMarco the Phoenix", anchor='w').pack(fill='both')
    Label(roomSelected, text="").pack()
    
    Label(roomSelected, text="").pack()
    Label(roomSelected, text="Name\tMarco the Phoenix", anchor='w').pack(fill='both')
    Label(roomSelected, text="").pack()
    
    Label(roomSelected, text="").pack()
    Label(roomSelected, text="Name\tMarco the Phoenix", anchor='w').pack(fill='both')
    Label(roomSelected, text="").pack()
    
    Label(roomSelected, text="").pack()
    Label(roomSelected, text="Name\tMarco the Phoenixs", anchor='w').pack(fill='both')
    Label(roomSelected, text="").pack()
 
#SQL FOR ROOMS

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
    
    query = "SELECT * FROM roominformation WHERE roomFloor = '" + floorSelected.get() + "'"
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
        login_screen.destroy()
        
def roomChanged(index, value, op):
    detailsArray = []
    counter=0
    print ("Room changed to " + roomSelected.get())
    
    query = "SELECT * FROM roominformation i JOIN room_type t ON i.roomType = t.roomId WHERE i.roomNum = '" + roomSelected.get() + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    if(len(result) > 0):
        print(result)
        room_selectInfo(result)
    else:
        print("No descriptions available")
        messagebox.showwarning("Warning", "No descriptions available")

########################### START OF THE PROGRAM ################################

global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("500x300") # set the configuration of GUI window 
main_screen.title("Room Information") # set the title of GUI window

# create a Form label 
Label(text="Angeli's Hotel Reservation System", bg="blue", width="300", height="1", font=("Calibri", 20)).pack()
Label(text="Room Information", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
Label(text="").pack() 

# Create an Exit Button
Button(text="Back", height="2", width="30", command=toLogin).pack()
Label(text="").pack()    


floorSelected = StringVar()
roomSelected = StringVar()

floorSelected.trace('w',floorChanged)
roomSelected.trace('w',roomChanged)
             
floorChoice = []
floorChoice = getFloorsAvailable()
print(floorChoice)
Label(text="Floor").pack() 
selectFloor = ttk.Combobox(height="10", textvar=floorSelected, width="30")
selectFloor.config(value = floorChoice)
selectFloor.pack()
Label(text="").pack() 

roomChoice = []
Label(text="Room").pack() 
selectRoom = ttk.Combobox(height="10", textvar=roomSelected, width="30")
selectRoom.config(value = [])
selectRoom.pack()
# selectRoom.bind("<<ComboboxSelected>>", roomChanged)

Label(text="").pack() 





main_screen.mainloop() # start the GUI
 
# main_account_screen() # call the main_account_screen() function