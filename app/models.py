import sqlite3 as sql
import os.path
#defines functions used by views to insert and display info from db

def insert_customer(firstname, lastname, company, email, phone, street_address, city, state, country, zip_code):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO customers (firstname, lastname, company, email, phone) VALUES (?,?,?,?,?)",(company,email,firstname,lastname,phone))
        cust_id = cur.lastrowid
        cur.execute("INSERT INTO addresses (street_address, city, state, country, zip_code, customer_id) VALUES (?,?,?,?,?,?)",(street_address, city, state, country, zip_code, cust_id))
        con.commit()
        con.commit()

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from customers").fetchall()
    return result

def insert_order(cust_id, name_of_part, manufacturer_of_part):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part) VALUES (?,?)",(name_of_part, manufacturer_of_part))
        ord_id = cur.lastrowid
        cur.execute("INSERT INTO order_customer (order_id, customer_id) VALUES (?,?)",(ord_id, cust_id))
        con.commit()

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from orders").fetchall()
    return result

def retrieve_addresses():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from addresses").fetchall()
    return result
