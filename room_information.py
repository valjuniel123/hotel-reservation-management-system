from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from subprocess import call

import mysql.connector

from database import *

def toLogin():
    print("Logged out!")
    main_screen.destroy()
    
def toRoomInfo(roomNumber):
    print("Room Number:", roomNumber, " Details")
    # main_screen.withdraw()
    room_selectInfo(roomNumber)
    # main_screen.deiconify()
    
def room_selectInfo(roomNumber):
    
    global roomSelected
    roomSelected = Toplevel(main_screen)
    roomSelected.title("Room Information")
    roomSelected.geometry("300x600")
    
    roomNum = "Room " + str(roomNumber)
    Label(roomSelected, text="Room Information", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
    Label(roomSelected, text=roomNum, bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
 
    
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
    

global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("300x600") # set the configuration of GUI window 
main_screen.title("Room Information") # set the title of GUI window

# create a Form label 
Label(text="Angeli's Hotel Reservation System", bg="blue", width="300", height="1", font=("Calibri", 20)).pack()
Label(text="Room Information", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
Label(text="").pack() 

# Create an Exit Button
Button(text="Back", height="2", width="30", command=toLogin).pack()
Label(text="").pack()
 
#SQL FOR ROOMS
def removeData():
    #Remove values from combobox
    roomChoice.delete(0, END)
    # roomChoice.insert(0, "")
    # selectRoom.set('') # Clear the selection 
    # # selectRoom.delete(0,'end') # clear the selection
    # # l1.config(text=selectRoom.get()+':'+ str(cb1.current())) # value & index


def on_field_change(index, value, op):
    counter=0
    print ("combobox changed to " + floorSelected.get())
    removeData()
    
    query = "SELECT * FROM roominformation WHERE roomFloor = '" + floorSelected.get() + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    if(len(result) > 0):
        for row in result:
            print(row[0])
            roomChoice.insert(counter, row[0])
            counter+=1
        # selectRoom.values = roomChoice
            
    else:
        print("Login failed!")
        messagebox.showwarning("Failed", "Login failed!")
        login_screen.destroy()
    


floorSelected = StringVar()
roomChoice = StringVar()

floorSelected.trace('w',on_field_change)
# roomChoice.trace('w',on_field_change)
             
floorChoice = ['1','2','3']
Label(text="Floor").pack() 
selectFloor = ttk.Combobox(height="10", textvar=floorSelected, width="30", values = floorChoice).pack()
Label(text="").pack() 

roomChoice = [1,2,3,4,5,6,7,8,9,0]
Label(text="Room").pack() 
selectRoom = ttk.Combobox(height="10", textvar=roomChoice, width="30", values = roomChoice).pack()
Label(text="").pack() 
# Show Room Informations Button 
# Label(text="1st Floor").pack() 

# Button(text="Room 11", height="2", width="15", command=lambda:toRoomInfo(11)).pack() 
# Button(text="Room 12", height="2", width="15", command=lambda:toRoomInfo(12)).pack()
# Button(text="Room 13", height="2", width="15", command=lambda:toRoomInfo(13)).pack()
# Button(text="Room 14", height="2", width="15", command=lambda:toRoomInfo(14)).pack()
# Button(text="Room 15", height="2", width="15", command=lambda:toRoomInfo(15)).pack()
 


# Label(text="2nd Floor").pack() 
# Button(text="Room 21", height="2", width="15", command=lambda:toRoomInfo(21)).pack() 
# Button(text="Room 22", height="2", width="15", command=lambda:toRoomInfo(22)).pack()
# Button(text="Room 23", height="2", width="15", command=lambda:toRoomInfo(23)).pack()
# Button(text="Room 24", height="2", width="15", command=lambda:toRoomInfo(24)).pack()
# Button(text="Room 25", height="2", width="15", command=lambda:toRoomInfo(25)).pack()



main_screen.mainloop() # start the GUI
 
# main_account_screen() # call the main_account_screen() function