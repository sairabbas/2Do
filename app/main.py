from flask import render_template, redirect, url_for, flash, redirect, request
from app import app, db
from app.form import register, signin, CreateTask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.form import register
from app.models import User

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

# register page
@app.route("/register", methods=["GET", "POST"])
def signUp():
    form = register()
    # if form.validate_on_submit():
    #     flash('Successfully to create account')
    return render_template("register.html", form=form, title="Sign Up")

# sign in page
@app.route("/signin", methods=["GET", "POST"])
def signIn():
    form = signin()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        print(user)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        #flash('Login requested for user {}, remember me={}' .format((form.username.data, str(form.remember_me.data))))
        return render_template(redirect(home()))
    return render_template("signin.html", form=form, title="Sign In")

# create task
@app.route('/tasks', methods=('GET', 'POST'))
def tasks():
    title = 'Tasks'
    form = CreateTask()
    if form.validate_on_submit():
        return redirect('/home')
    else:
        return "Username or Password is invalid. Please try again"
    return render_template('tasks.html', form=form, title=title)


if __name__ == '__main__':
    app.run(debug=True)
