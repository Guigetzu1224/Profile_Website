'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = TextField('Name',
                           validators=[DataRequired(), Length(min=2, max=30)])
    email = TextField('Email',
                        validators=[DataRequired(), Email()])
    message = TextField('message',validators=[DataRequired()])
    subject = TextField('subject',validators=[DataRequired(), Length(min=10, max=9999)])
    submit = SubmitField('Sign Up')

'''
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo
class ContactForm(Form):
  name = TextField("Name", validators= [DataRequired('Please enter your name')])
  email = TextField("Email", validators = [DataRequired('Please enter your e-mail') , Email('Invalid Email Address')])
  subject = TextField("Subject", validators= [DataRequired('Please enter a subject')])
  message = TextAreaField("Message", validators=  [DataRequired('A message is required')])
  submit = SubmitField("Send")