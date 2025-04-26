from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Email Address', validators= [validators.DataRequired(),
    ])

    password = PasswordField('Password', validators= [validators.DataRequired(),

    ])
    submit = SubmitField('Login')
    pass

class RegisterForm(FlaskForm):
    email = EmailField(label="Email Address",
                       validators=[validators.DataRequired()],
                       description="You need to signup with an email"
                       )

    password = PasswordField(label="Create Your Password",
                             validators=[
                                 validators.DataRequired(),
                             ])

    confirm = PasswordField(label="Confirm Your Password",
                            validators=[
                                validators.DataRequired(),
                                validators.EqualTo("password")
                            ]
                            )

    submit = SubmitField('Register')
    pass


