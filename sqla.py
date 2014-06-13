# create a SQLite3 database and table

# import the SQLite3 library
import sqlite3

# create a new database if one doesn't already exist
conn = sqlite3.connect("new.db")
conn2 = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()
cursor2 = conn2.cursor()

# create a table
# cursor.execute("CREATE TABLE population (city TEXT, state TEXT, population INT)")
cursor2.execute("CREATE TABLE cars (Make TEXT, Model TEXT, Quanity INT)")

# close the database connection
conn.close()
conn2.close()