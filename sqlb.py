# insert command
# import sqlite3 library
import sqlite3
with sqlite3.connect("new.db") as connection:

    # create the connection object
    
    # get a cursor object
    cursor = connection.cursor()
    
    # insert data
    cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

# commit the changes
connection.commit()

# close the db connection
connection.close()