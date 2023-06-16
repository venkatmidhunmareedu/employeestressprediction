from flask_wtf import Flaskform
from wtforms import StringField

class RegistrationFrom(Flaskform):
    username = StringField('Username')