import sqlite3

def show_all():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")

    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    print("The record has been inserted.")
    conn.commit()
    conn.close()

def delete_one(id):
    id = str(id)
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    print("The record has been deleted.")
    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    print("The records has been inserted.")
    conn.commit()
    conn.close()
