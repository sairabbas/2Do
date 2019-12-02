from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField, IntegerField,  TextAreaField, DateField, TimeField, validators, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Length, ValidationError
from app.models import User, Todo
from wtforms.fields.html5 import EmailField
class signin(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=10)]
    )
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign in")

class register(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=10)]
    )
    email = EmailField('Email address', validators=[DataRequired(), validators.Length(min=6, max=35)])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField("Sign up")


     # To check username and email existed  or not.
     # return: If the username or email is taken, the fucntion will notice.
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')



class createTask(FlaskForm):
    description = StringField("description", validators=[DataRequired(), Length(min=4)])
    content = TextAreaField('content')
    deadline = DateTimeField("deadline", validators= [DataRequired()])
    status = BooleanField("status", default=False)
    submit = SubmitField('save')


class createList(FlaskForm):
    name = StringField("name",validators=[DataRequired()])
    submit = SubmitField('save')

class contactForm(FlaskForm): 
    name=  StringField("Name", validators=[DataRequired(), Length(min=4)])
    email = EmailField('Email address', validators=[DataRequired(), validators.Length(min=6, max=35)])
    subject= StringField("Subject")
    message = TextAreaField('message', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('send')

class shareForm(FlaskForm): 
    subject= StringField("Subject")
    message = TextAreaField('message', validators=[Length(min=4)])
    nameSender=  StringField("NameSender", validators=[DataRequired(), Length(min=4)])
    nameReceiver=  StringField("NameReceiver", validators=[DataRequired(), Length(min=4)])
    emailReceiver = EmailField(' emailReceiver', validators=[DataRequired(), validators.Length(min=6, max=35)])
    submit = SubmitField('send')