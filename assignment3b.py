import sqlite3

connection = sqlite3.connect("newnum.db")
c = connection.cursor()

# Create a user prompt asking for AVG, MAX, MIN, or SUM.  Else exit
choice = ""

valid_choices = ["AVG","MAX","MIN","SUM","EXIT"]

while True:
    choice = str.upper(raw_input("""Choose from the following:
    AVG, MAX, MIN, or SUM.  EXIT to quit --->"""))

    if choice == "EXIT":
        print "EXIT"
        exit()
        
    #create SQL querie from user choice
    elif choice in valid_choices:
        c.execute("SELECT {}(rnum) from random_numbers".format(choice))
        
        get = c.fetchone()
        
        #out result
        print choice + ": {}".format(get[0])

