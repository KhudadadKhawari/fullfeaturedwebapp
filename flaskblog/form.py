from flask_wtf import FlaskForm
from flask_wtf.file import FileField, file_allowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User

class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(),])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data ).first()
        if user:
            raise ValueError('username already exist please choose another username')
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data ).first()
        if user:
            raise ValueError('E-mail already Exist, please choose another email')

class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[file_allowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:

            user = User.query.filter_by(username = username.data ).first()
            if user:
                raise ValueError('username already exist please choose another username')
    def validate_email(self, email):
        if email.data != current_user.email:

            user = User.query.filter_by(email = email.data ).first()
            if user:
                raise ValueError('E-mail already Exist, please choose another email')

class PostForm(FlaskForm):

    title = StringField('title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data ).first()
        if user is None:
            raise ValueError('E-mail not found, Please create an account first.')
            
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired(),])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')