from flask import render_template, redirect, request, session, redirect, url_for, escape
from app import app, models, db
from .forms import TravelerForm, TravelForm
from .models import *
# Access the models file to use SQL functions

@app.route('/')
@app.route('/index')
def index():
    username = ''
    form = TravelerForm()
    if 'username' in session:
        username = escape(session['username'])
        # if form.validate_on_submit():
        #     username = form.name.data
        #     insert_traveler(username)
        return redirect('/travelers')
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session['username'] = request.form.get("username")
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# @app.route('/create_traveler', methods=['GET', 'POST'])
# def create_traveler():
#     form = TravelerForm()
#     if form.validate_on_submit():
#         # Get data from the form
#         # Send data from form to Database
#         name = form.name.data
#         email = form.email.data
#         insert_traveler(name, email)
#         return redirect('/travelers')
#     return render_template('traveler.html', form=form)

@app.route('/travelers')
def display_traveler():
    #Retreive data from database to display
    # travelers = retrieve_travelers()
    travels = retrieve_travels()
    username = escape(session['username'])
    return render_template('home.html',
                             travels=travels, name=username)

@app.route('/create_travel/<value>', methods=['GET', 'POST'])
def create_travel(value):
    # Get data from the form
    # Send data from form to Database
    form = TravelForm(obj=value)
    username = escape(session['username'])
    if form.validate_on_submit():
        trip_name = form.trip_name.data
        destination = form.destination.data
        friend = form.friend.data
        insert_travels(trip_name, destination, friend, username)
        return redirect('/travelers')
    return render_template('travel.html', form=form, name=username)
