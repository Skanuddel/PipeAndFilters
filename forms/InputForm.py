from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField

CHOICES = ["Double", "Halve", "Multiply with -1", "Square Root"]

class InputForm(FlaskForm):

    input = StringField('Input:', [validators.InputRequired()])

    filter1 = SelectField("Filter 1:", choices=CHOICES, default="Double")

    filter2 = SelectField("Filter 2:", choices=CHOICES, default="Double")

    filter3 = SelectField("Filter 3:", choices=CHOICES, default="Double")