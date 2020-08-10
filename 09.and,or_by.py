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

'''
c.execute("""UPDATE customers SET first_name = "Jihwan"
            WHERE rowid = 1""") 
'''

# Delete records
'''
c.execute("DELETE FROM customers WHERE rowid = 5")
'''

c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%.com' AND rowid = 3") # A AND B OR C : A와 B가 동시에 참이거나 C가 참인 data 검색

# Commit command
conn.commit()


items = c.fetchall()
for item in items:
    print(item)




# Close connection
conn.close()


