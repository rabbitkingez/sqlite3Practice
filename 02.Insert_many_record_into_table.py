import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db') # saving on to a file
# conn = sqlite3.connect(':memory:') # saving on memory (temporary)


# Create a cursor
c = conn.cursor()

'''
# create a Table (최소 생성 시 1번만 처리하면 됨)
c.execute("""CREATE TABLE customers(
        first_name text,
        last_name text,
        email text
)""")
'''

# sqlite3 supporting datatypes : NULL, INTEGER, REAL, TEXT, BLOB(image,...)

# Make list to multi-insert
many_customers = [
    ('we','brwon','wes@grwo.com'),
    ('stf','use','djkls@gda.com'),
    ]


#Insert data in database
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)



# Commit command
conn.commit()

# Close connection
conn.close()


