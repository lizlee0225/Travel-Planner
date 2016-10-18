from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        company = form.company.data
        email = form.email.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        phone = form.phone.data
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        insert_customer(company, email, firstname, lastname, phone, street_address, city, state, country, zip_code)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    #Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    addresses = retrieve_addresses()
    return render_template('home.html',
                            customers=customers, orders=orders, addresses=addresses)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    # Get data from the form
    # Send data from form to Database
    form = OrderForm(obj=value)
    if form.validate_on_submit():
        cust_id = value
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        insert_order(cust_id, name_of_part, manufacturer_of_part)
        return redirect('/customers')
    return render_template('order.html', form=form)

@app.route('/create_address/<value>', methods=['GET', 'POST'])
def create_address(value):
    # Get data from the form
    # Send data from form to Database
    form = AddressForm(obj=value)
    if form.validate_on_submit():
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        insert_address(street_address, city, state, country, zip_code)
        return redirect('/customers')
    return render_template('address.html', form=form)
