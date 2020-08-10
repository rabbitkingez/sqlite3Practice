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

c.execute("SELECT rowid, * FROM customers LIMIT 2") # 상위에서 2개항까지 조회

# Commit command
conn.commit()


items = c.fetchall()
for item in items:
    print(item)




# Close connection
conn.close()


