from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, DateField, TimeField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, Length


class register(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=6)]
    )
    mail = StringField("Mail", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo(password)]
    )
    submit = SubmitField("Sign up")


class signin(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=6)]
    )
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8)])
    rememberUserName = BooleanField("Remember Username")
    submit = SubmitField("Sign in")

class CreateTask(FlaskForm):
        task_name=StringField('Task Description',[validators.DataRequired()])
        task_date=DateField('Task Date',[validators.DataRequired()])
        task_time=TimeField('Task Time',[validators.DataRequired()])   
        task_notif=BooleanField('Notify')
        task_save=SubmitField('Save')
        
