import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    # insert multiple items with a tuple
    cars = [
        ('Ford', 'Mustang', 20),
        ('Ford', 'Fusion', 3),
        ('Ford', 'Focus', 42),
        ('Honda', 'Civic', 16),
        ('Honda', 'Fit', 22)
        ]
    
    # insert data into table
    c.executemany("INSERT INTO cars VALUES(?,?,?)", cars)
    
    # update the data on 2 rows
    c.execute("UPDATE cars SET Quanity = 73 WHERE Model = 'Fusion'")
    c.execute("UPDATE cars SET Quanity = 45 WHERE Model = 'Civic'")
    
    # output all three records from the table
    c.execute("SELECT * FROM cars")
    
    rows = c.fetchall()
    
    for r in rows:
        print r[0], r[1], r[2]
        
    # output only Fords
    print "\nFords:\n"
    
    c.execute("SELECT * FROM cars WHERE Make = 'Ford'")
    
    fords = c.fetchall()
    
    for r in fords:
        print r[0], r[1], r[2]
    
    