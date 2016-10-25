from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class TravelerForm(Form):
    name = StringField('username', validators=[DataRequired()])

class TravelForm(Form):
    trip_name = StringField('trip_name', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend = StringField('friend', validators=[DataRequired()])
