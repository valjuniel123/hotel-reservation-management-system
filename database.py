# import required modules
import mysql.connector

# create connection object
con = mysql.connector.connect(
host="localhost", user="root",
password="", database="hreservation_system")

# create cursor object
cursor = con.cursor()

if(con.is_connected()):
    print("Connected to MySQL database...")
else:
    print("Connection failed...")

# closing cursor connection
cursor.close()

# closing connection object
con.close()
