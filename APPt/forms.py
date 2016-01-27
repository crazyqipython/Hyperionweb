
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField("What's is your name?", validators = [Required()])
	password = PasswordField('enter your password')
	submit = SubmitField('sumbit')