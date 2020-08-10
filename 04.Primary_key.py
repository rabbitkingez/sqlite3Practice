import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db') # saving on to a file
# conn = sqlite3.connect(':memory:') # saving on memory (temporary)


# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT rowid, * FROM customers") # rowid로 조회 가능

items = c.fetchall()
for item in items:
    print(item)
# Commit command
conn.commit()

# Close connection
conn.close()


