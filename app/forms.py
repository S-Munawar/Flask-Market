from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check): # This function is used to check if the username already exists in the database or not.
        user = User.query.filter_by(username=username_to_check.data).first() # Acessing input(username_to_check.data) from the user and checking if it already exists in the database or not.
        if user:
            raise ValidationError('Username already exists! Please try a different username.')

    def validate_email_address(self, email_address_to_check): # This function is used to check if the email address already exists in the database or not.
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first() # Acessing input(username_to_check.data) from the user and checking if it already exists in the database or not.
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address.')

    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()]) # Creating a StringField with a label 'Username' and validators is used to take the input from the user and validate it, which is first initiated in register_page() & then displayed using HTML.
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password:' , validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm): # This class is used to create a form for the user to login.
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Yes')

class SellForm(FlaskForm):
    submit = SubmitField(label='Sell Item')

class AddItems(FlaskForm):
    name = StringField(label='Name:', validators=[DataRequired()])
    price = StringField(label='Price:', validators=[DataRequired()])
    barcode = StringField(label='Barcode:', validators=[DataRequired()])
    description = StringField(label='Description:', validators=[DataRequired()])
    submit = SubmitField(label='Add Item')