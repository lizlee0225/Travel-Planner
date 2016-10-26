from flask import render_template, redirect, request, session, redirect, url_for, escape
import sqlite3 as sql
import os.path
#defines functions used by views to insert and display info from db

def verify(username):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        results = cur.execute("SELECT * FROM travelers").fetchall()
        print(results)
        for entry in results:
            if username == entry[1]:
                return True
        return False

def sign_up(username):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO travelers (traveler_name) VALUES (?)",(username,))
        con.commit()

def insert_travels(trip_name, destination, friend, value):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        # cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO travels (trip_name, destination, friend, traveler_name) VALUES (?,?,?,?)",(trip_name, destination, friend, value))
        travel_id = cur.lastrowid
        cur.execute("INSERT INTO names (travel_id, friend, traveler_name) VALUES (?,?,?)", (travel_id, friend, value))
        con.commit()
        # newcur.execute("INSERT INTO name_travel (name, travel_id) VALUES (?,?)",(value, cur.lastrowid))

def delete_travels(value):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        # cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("DELETE FROM travels where travel_id=" + value + "")
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

def retrieve_travels2():
    # SQL statement to query database goes here
    username = escape(session['username'])
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("select * from travels where friend = ?",(username,)).fetchall()
    return result
