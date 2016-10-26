from flask import render_template, redirect, request, session, redirect, url_for, escape
from app import app, models, db
from .forms import TravelerForm, TravelForm
from .models import *
# Access the models file to use SQL functions

@app.route('/')
@app.route('/index')
def index():
    username = ''
    if 'username' in session:
        username = escape(session['username'])
        return redirect('/travelers')
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=TravelerForm
    if request.method=='POST':
        username = request.form.get("username")
        if verify(username):
            session['username'] = request.form.get("username")
            return redirect('/travelers')
        else:
            return render_template('not_authorized.html')

@app.route('/signup_click', methods=['GET', 'POST'])
def signup_click():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form=TravelerForm
    if request.method=='POST':
        username = request.form.get("username")
        if verify(username):
            return render_template('alreadyregistered.html')
        else:
            sign_up(username)
            session['username'] = request.form.get("username")
            return redirect('/travelers')

@app.route('/delete_travel/<value>', methods=['GET', 'POST'])
def delete_travel(value):
    form = TravelForm(obj=value)
    delete_travels(value)
    return redirect('/travelers')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/travelers')
def display_traveler():
    #Retreive data from database to display
    travels = retrieve_travels()
    travels2 = retrieve_travels2()
    username = escape(session['username'])
    return render_template('home.html',
                             travels=travels, travels2=travels2, name=username)

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
