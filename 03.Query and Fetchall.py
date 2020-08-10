import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db') # saving on to a file
# conn = sqlite3.connect(':memory:') # saving on memory (temporary)


# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")
#c.fetchone() # 1개만 조회
# print(c.fetchone()[1]) # index로 원하는 항목만 지정 출력 가능
print(c.fetchone())
#c.fetchmany(3) # 3개까지 조회

items = c.fetchall() # 전체 조회

for item in items:
    print(item)


# Commit command
conn.commit()

# Close connection
conn.close()


