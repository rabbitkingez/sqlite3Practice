import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db') # saving on to a file
# conn = sqlite3.connect(':memory:') # saving on memory (temporary)


# Create a cursor
c = conn.cursor()

# Query the database
# c.execute("SELECT * FROM customers WHERE last_name = 'Lee'") # database 내 last_name이 Lee인 것만 선택
c.execute("SELECT * FROM customers WHERE email LIKE '%.com'") # database 내 이메일 주소가 .com을 포함하고 있다면 선택
 


items = c.fetchall()
for item in items:
    print(item)




# Commit command
conn.commit()

# Close connection
conn.close()


