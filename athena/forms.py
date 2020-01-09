from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirmed Password', validators=[DataRequired(), Length(min=8, max=20),
                                                                       EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SearchForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    idea1 = StringField('Idea 1 (enter a topic of your interest)', validators=[DataRequired(), Length(min=2, max=100)])
    idea2 = StringField('Idea 2 (enter a topic of your interest)', validators=[DataRequired(), Length(min=2, max=100)])
    idea3 = StringField('Idea 3 (enter a topic of your interest)', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Analyze & Send Report')
