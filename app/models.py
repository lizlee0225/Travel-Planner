from flask import render_template, redirect, request, session, redirect, url_for, escape
import sqlite3 as sql
import os.path
#defines functions used by views to insert and display info from db

# def insert_traveler(name):
#     # SQL statement to insert into database goes here
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         cur.execute("PRAGMA foreign_keys = ON")
#         cur.execute("INSERT INTO travelers (name) VALUES (?)",(name))
#         con.commit()

# def retrieve_travelers():
#     # SQL statement to query database goes here
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         cur.execute("PRAGMA foreign_keys = ON")
#         result = cur.execute("select * from travelers").fetchall()
#     return result

def insert_travels(trip_name, destination, friend, value):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        # cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO travels (trip_name, destination, friend, traveler_name) VALUES (?,?,?,?)",(trip_name, destination, friend, value))
        con.commit()
        # newcur.execute("INSERT INTO name_travel (name, travel_id) VALUES (?,?)",(value, cur.lastrowid))

def retrieve_travels():
    # SQL statement to query database goes here
    username = escape(session['username'])
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from travels where traveler_name = ?",(username,)).fetchall()
    return result
