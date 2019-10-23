from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField, IntegerField, TextAreaField, DateField, TimeField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, Length, ValidationError
from app.models import User, Todo
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
    email = StringField("Email", validators=[DataRequired()])
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
    deadline_date = DateField("deadline", validators=[DataRequired()])
    deadline_time = TimeField("time", validators=[DataRequired()])
    status = BooleanField("status", default=False)
    submit = SubmitField('save')


