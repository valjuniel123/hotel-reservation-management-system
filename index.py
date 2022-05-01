from tkinter import *
from tkinter import messagebox

from subprocess import call

import mysql.connector

from database import *



def login():
    
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
   
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=verifyLogin).pack()
    
 
def verifyLogin():
    username = username_verify.get()
    password = password_verify.get()
    
    query = "SELECT * FROM `accounts` WHERE userId = %s AND password = %s"
    args = (username, password)
    cursor.execute(query, args)
    result = cursor.fetchall()
    if(len(result) == 0):
        print("Login successful!")
        messagebox.showinfo("Success", "Login successful!")
        main_screen.withdraw()
        login_screen.destroy()
        call(["python", "main_menu.py"])
        main_screen.deiconify()
    else:
        print("Login failed!")
        messagebox.showwarning("Failed", "Login failed!")
        login_screen.destroy()
      
def outroom():
    main_screen.withdraw()
    print("Checking Out")
    call(["python", "checkout.py"])
    main_screen.deiconify()
    
def checkRoom():
    main_screen.withdraw()
    print("Checking Rooms")
    call(["python", "roomsAvailable.py"])
    main_screen.deiconify()
        
 
        
global main_screen
main_screen = Tk()   # create a GUI window 
main_screen.geometry("500x250") # set the configuration of GUI window 
main_screen.title("Account Login") # set the title of GUI window

# create a Form label 
Label(text="Choose Login, Reserve of Checkout", bg="blue", width="300", height="2", font=("Calibri", 20)).pack() 
Label(text="").pack() 
 
# create Login Button 
Button(text="Login", height="2", width="30", command=login).pack() 
Label(text="").pack()
 
# create a Reservation button
Button(text="Check Rooms Available", height="2", width="30", command=checkRoom).pack()

# create a Checkout button
Button(text="Check Out", height="2", width="30", command=outroom).pack()




main_screen.mainloop() # start the GUI
 
# main_account_screen() # call the main_account_screen() function
