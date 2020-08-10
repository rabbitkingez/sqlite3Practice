import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db') # saving on to a file
# conn = sqlite3.connect(':memory:') # saving on memory (temporary)


# Create a cursor
c = conn.cursor()


# Update records
'''
c.execute("""UPDATE customers SET first_name = "Bob"
            WHERE last_name = 'Lee'""") 
'''
c.execute("""UPDATE customers SET first_name = "Jihwan"
            WHERE rowid = 1""") 



# Commit command
conn.commit()



c.execute("SELECT * FROM customers")

items = c.fetchall()
for item in items:
    print(item)




# Close connection
conn.close()


