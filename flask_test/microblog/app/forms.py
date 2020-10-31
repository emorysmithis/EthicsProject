from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    choice_A = BooleanField('Choice A') 
    choice_B = BooleanField('Choice B') 
    submit = SubmitField('Submit Answer')
    nextq = SubmitField('Next Question') 
