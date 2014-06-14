"""
   Using the COUNT() function, calculate the total number of orders for each make and model.
   Output the cars make and model on one line, the quantity on another line, and then the order
   count on the next line. The latter is a bit difficult, but please try it first before
   looking at the code. Remember: Google-it-first!
"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    #get distinct model types from orders table
    c.execute("SELECT DISTINCT model FROM orders")
    
    #make a list
    models = c.fetchall()
    
    #loop over each model of car
    for car in models:
        c.execute("""SELECT cars.Make, cars.Model, cars.Quanity, orders.order_date
              FROM cars INNER JOIN orders ON cars.Model AND orders.model = ?""", car)
        c.fetchall()
        print car[0], car[1]
        print car[2]
        
    