import sqlite3 as sql
import os.path
#defines functions used by views to insert and display info from db

def insert_traveler(name, email):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO travelers (name, email) VALUES (?,?)",(name, email))
        con.commit()

def retrieve_travelers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from travelers").fetchall()
    return result

def insert_travels(trip_name, destination):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO travels (trip_name, destination) VALUES (?,?)",(trip_name, destination))
        con.commit()

def retrieve_travels():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from travels").fetchall()
    return result
