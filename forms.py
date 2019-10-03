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

