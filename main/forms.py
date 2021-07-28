from secrets import choice
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from flask_login import current_user
from wtforms import MultipleFileField
from wtforms import StringField,PasswordField,TextAreaField, SelectField,SubmitField, BooleanField, TextField,FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Regexp
from main.models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired(),Length(min=2,max=50)])
    lastname = StringField('lastname', validators=[DataRequired(),Length(min=2,max=50)])
    address = StringField('address', validators=[DataRequired(),Length(min=2,max=50)])
    city = StringField('city', validators=[DataRequired(),Length(min=2,max=50)])
    country = StringField('country', validators=[DataRequired(),Length(min=2,max=50)])
    zip_code = StringField('zip_code', validators=[DataRequired(),Length(min=2,max=50)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    type= SelectField('Type',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Regexp('[A-Za-z0-9@#$%^&+=]{8,}',message='Password not valid, example : Password123!')])
    picture = FileField('Image', validators=[ FileRequired(),FileAllowed(['jpg','png','jpeg'])])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    termsConditions = BooleanField('Accept Terms and Conditions')
    submit = SubmitField('Sign Up')
    
    def validate_email(self,email):
        email_user = User.query.filter_by(email= email.data).first()
        if email_user:
            raise ValidationError('That email is taken, please use a different one!')


class editUser(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired(),Length(min=2,max=50)])
    lastname = StringField('lastname', validators=[DataRequired(),Length(min=2,max=50)])
    address = StringField('address', validators=[DataRequired(),Length(min=2,max=50)])
    city = StringField('city', validators=[DataRequired(),Length(min=2,max=50)])
    country = StringField('country', validators=[DataRequired(),Length(min=2,max=50)])
    zip_code = StringField('zip_code', validators=[DataRequired(),Length(min=2,max=50)])
    picture = FileField('Image', validators=[ FileAllowed(['jpg','png','jpeg'])])
    premium = BooleanField('Premium')
    submit = SubmitField('Sign Up')
    
    def validate_email(self,email):
        email_user = User.query.filter_by(email= email.data).first()
        if email_user:
            raise ValidationError('That email is taken, please use a different one!')


class editProfile(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired(),Length(min=2,max=50)])
    lastname = StringField('lastname', validators=[DataRequired(),Length(min=2,max=50)])
    address = StringField('Address', validators=[DataRequired(),Length(min=2,max=50)])
    city = StringField('City', validators=[DataRequired(),Length(min=2,max=50)])
    country = StringField('Country', validators=[DataRequired(),Length(min=2,max=50)])
    picture = FileField('Image', validators=[ FileAllowed(['jpg','png','jpeg'])])
    zip_code = StringField('Zip Code', validators=[DataRequired(),Length(min=2,max=50)])
    submit = SubmitField('Save')



class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')



class addPost(FlaskForm):
    title = StringField('Post title',validators=[DataRequired()])
    text = TextAreaField(render_kw={"rows":3, "cols": 4}) 
    picture = FileField('Image', validators=[ FileAllowed(['jpg','png','jpeg'])])
    type = SelectField('Type',validators=[DataRequired()], choices=["I'm looking for a new owner!","I've an amazing owner!"])
    category = SelectField('Category',validators=[DataRequired()], choices=["Dog","Cat"])
    location = StringField('Location',validators=[DataRequired()])
    submit = SubmitField('Submit')
    back = SubmitField('Back')

class editPost(FlaskForm):
    title = StringField('Post title',validators=[DataRequired()])
    text = TextAreaField(render_kw={"rows":3, "cols": 4}) 
    picture = FileField('Image', validators=[ FileAllowed(['jpg','png','jpeg'])])
    type = SelectField('Type',validators=[DataRequired()], choices=["I'm looking for a new owner!","I've an amazing owner!"])
    category = SelectField('Category',validators=[DataRequired()], choices=["Dog","Cat"])
    location = StringField('Location',validators=[DataRequired()])
    submit = SubmitField('Submit')
    back = SubmitField('Back')

class filterPosts(FlaskForm):
    title = StringField('Post title')
    type = SelectField('Type', choices=["---","I'm looking for a new owner!","I've an amazing owner!"])
    category = SelectField('Category', choices=["---","Dog","Cat"])
    location = StringField('Location')
    submit = SubmitField('Search')
    




class SendEmail(FlaskForm):
    recipient = StringField('Recipient',validators=[DataRequired()])
    description = TextAreaField('Body',render_kw={"rows":10, "cols": 11})
    submit = SubmitField('Send')

class EditProfile(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired(),Length(min=2,max=20)])
    lastname = StringField('lastname', validators=[DataRequired(),Length(min=2,max=20)])
    address = StringField('Address', validators=[DataRequired(),Length(min=2,max=20)])
    city = StringField('City', validators=[DataRequired(),Length(min=2,max=20)])
    country = StringField('Country', validators=[DataRequired(),Length(min=2,max=20)])
    zip_code = StringField('Zip_code', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    Password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Save')
       
    def validate_email(self,email):
        if email.data != current_user.email:
            email_user = User.query.filter_by(email= email.data).first()
            if email_user:
                raise ValidationError('That email is taken, please use a different one!')  



class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')
        
    def validate_email(self,email):
        email_user = User.query.filter_by(email= email.data).first()
        if email_user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPassword(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired(),Regexp('[A-Za-z0-9@#$%^&+=]{8,}',message='Password not valid, example : Password123!')])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Reset Password')

class ConfirmEmail(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Confirm Email')
        
    def validate_email(self,email):
        email_user = User.query.filter_by(email= email.data).first()
        if email_user is None:
            raise ValidationError('There is no account with that email. You must register first.')
