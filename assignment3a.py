import sqlite3
from random import randint

#create a new database called newnum.db if it doesn't already exist

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE if exists random_numbers")
    c.execute("""CREATE TABLE random_numbers
              (rnum INT)
              """)
    
    for i in range(0, 100):
        
        #choose a random int from 0 to 100
        new_num = randint(0,100)
        
        #insert it into the db
        c.execute("INSERT INTO random_numbers VALUES (?)", (new_num,))