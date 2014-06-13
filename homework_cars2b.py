"""Finally output the cars make and model on one line, the quantity on another line, and then the order_dates on subsequent lines below that."""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    c.execute("""SELECT cars.Make, cars.Model, cars.Quanity, orders.order_date
              FROM cars INNER JOIN orders ON cars.Model = orders.model""")
    
    rows = c.fetchall()
    
    for r in rows:
        print "Make - Model: \t" + r[0] +" - " + r[1]
        print "Quantity: \t" + str(r[2])
        print "Dates ordered: \t" + r[3]
        print