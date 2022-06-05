from wtforms import StringField,Form
from wtforms.fields.html5 import EmailField, TelField # can be accessed under the wtforms.fields.html5 namespace

class LoginForm(Form):
    name = StringField('Name:', id='name')
    phone = TelField('Phone Number:', id='phone')
    email = EmailField('Email:', id='email')
    job = StringField('Job Title:', id='job')
