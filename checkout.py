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
    

global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("400x500") # set the configuration of GUI window 
main_screen.title("Room Reservation") # set the title of GUI window

# create a Form label 
Label(text="Angeli's Hotel Reservation System", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
Label(text="Checkout", bg="blue", width="300", height="1", font=("Calibri", 20)).pack() 
Label(text="").pack() 
 
# Create an Exit Button
Button(text="Back", height="2", width="30", command=toLogin).pack()
Label(text="").pack() 
Label(text="").pack() 




Label(text="").pack() 

main_screen.mainloop()