from flask import render_template, redirect, request
from app import app, models, db
from .forms import TravelerForm, TravelForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_traveler')

@app.route('/create_traveler', methods=['GET', 'POST'])
def create_traveler():
    form = TravelerForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name = form.name.data
        email = form.email.data
        insert_traveler(name, email)
        return redirect('/travelers')
    return render_template('traveler.html', form=form)

@app.route('/travelers')
def display_traveler():
    #Retreive data from database to display
    travelers = retrieve_travelers()
    travels = retrieve_travels()
    return render_template('home.html',
                            travelers=travelers, travels=travels)

@app.route('/create_travel/<value>', methods=['GET', 'POST'])
def create_travel(value):
    # Get data from the form
    # Send data from form to Database
    form = TravelForm(obj=value)
    if form.validate_on_submit():
        traveler_name = value
        trip_name = form.trip_name.data
        destination = form.destination.data
        insert_travels(trip_name, destination)
        return redirect('/travelers')
    return render_template('travel.html', form=form)
