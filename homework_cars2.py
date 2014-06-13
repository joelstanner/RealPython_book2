"""Add another table to accompany your 'inventory' table called 'orders'. This table should have the following fields: 'make', 'model', and 'order_date'. Make sure to only include makes and models for the cars found in the inventory table. Add 15 records (3 for each car), each with a separate order date (YYYY-MM-DD). Make sure to research how to..."""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    # create a new table and populate
    c.execute("""CREATE TABLE orders
              (make TEXT, model TEXT, order_date TEXT)
              """)
    
    orders = [
        ('Ford', 'Mustang', '1999-05-20'),
        ('Ford', 'Mustang', '2001-08-21'),
        ('Ford', 'Mustang', '2003-09-20'),
        ('Ford', 'Fusion', '2012-12-25'),
        ('Ford', 'Fusion', '2013-10-18'),
        ('Ford', 'Fusion', '2000-12-02'),
        ('Ford', 'Focus', '1982-06-12'),
        ('Ford', 'Focus', '2005-06-12'),
        ('Ford', 'Focus', '2007-03-19'),
        ('Honda', 'Civic', '2008-03-13'),
        ('Honda', 'Civic', '2008-09-29'),
        ('Honda', 'Civic', '2008-07-14'),
        ('Honda', 'Fit', '2002-01-02'),
        ('Honda', 'Fit', '2005-01-22'),
        ('Honda', 'Fit', '2006-08-04')
        ]
    
    c.executemany("INSERT INTO orders VALUES(?,?,?)",orders)
    
    