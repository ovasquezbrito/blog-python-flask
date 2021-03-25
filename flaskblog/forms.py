from flask_wtf import FlaskForm
from validate_email import validate_email
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField 
from wtforms.validators import (DataRequired, Length, EqualTo, Email, ValidationError)
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        [
            DataRequired(message='Ingrese un nombre de usuario'), 
            Length(min="2", max="20")
        ]
    )
    email = TextField(
        'Email',
         [
             DataRequired(message='Ingrese un correo'), 
             validate_email
        ]
    )
    password = PasswordField(
        'Password',
        [
            DataRequired(message='Ingrese una contraseña')
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password', 
        [
            DataRequired(message='Debe confrmar contraseña'), 
            EqualTo('password')
        ]
    )

    submit = SubmitField('Registrate')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is token. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That username is token. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), validate_email])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Recordar Contraseña')
    
    submit = SubmitField('Iniciar sesión')

