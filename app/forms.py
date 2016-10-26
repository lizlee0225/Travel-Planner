from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired
import sqlite3 as sql

class TravelerForm(Form):
    name = StringField('username', validators=[DataRequired()])

class TravelForm(Form):
    trip_name = StringField('trip_name', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        results = con.execute("SELECT * FROM travelers").fetchall()
    friend = SelectField(u'friend', choices = [ (str(item[1]), str(item[1])) for item in results])
